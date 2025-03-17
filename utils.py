import pyzbar.pyzbar as pyzbar
from PIL import Image
import numpy as np
from datetime import datetime, timedelta
import qrcode


def qrcode_data_generator(id: str, siteId: str, createTime: str, classLessonId: str) -> str:
    """
    Generate the data string for the QR code.

    Returns:
        str: The data string for the QR code.
    """
    qrcode_data = f"checkwork|id={id}&siteId={siteId}&createTime={createTime}&classLessonId={classLessonId}"
    return qrcode_data


def create_time_generator() -> str:
    """
    Generates a timestamp string with the current date and time,
    where the seconds are rounded to the nearest multiple of 5.
    If the rounding results in 60 seconds, the minute is incremented by 1
    and the seconds are set to 0.

    Returns:
        str: The formatted timestamp string in the format '%Y-%m-%dT%H:%M:%S.%f'
                truncated to milliseconds.
    """
    now = datetime.now()
    # 调整秒数为最接近的5的倍数
    rounded_seconds = round(now.second / 5) * 5
    if rounded_seconds == 60:
        now += timedelta(minutes=1)
        rounded_seconds = 0
    rounded_time = now.replace(second=rounded_seconds, microsecond=0)
    formatted_time = rounded_time.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3]
    return formatted_time


def qrcode_generator(id: str, siteId: str, classLessonId: str):
    global current_qrcode_file
    """
    Generates a QR code image file based on the provided identifiers and returns the filename.
    Args:
        id (str): The unique identifier for the QR code.
        siteId (str): The site identifier.
        classLessonId (str): The class lesson identifier.
    Returns:
        str: The filename of the generated QR code image.
    """
    # 生成时间戳
    createTime = create_time_generator()
    # 生成数据字符串
    qrcode_data = qrcode_data_generator(id, siteId, createTime, classLessonId)
    # 生成QR码
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(qrcode_data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    return img


def scan_qr_code(image) -> dict:
    """
    Scan a QR code image and return the decoded data.

    Args:
        image (PIL.Image.Image): The image containing the QR code.

    Returns:
        dict: The decoded data from the QR code in a dictionary format.
    """
    decoded_objects = pyzbar.decode(image)
    if decoded_objects:
        data = decoded_objects[0].data.decode("utf-8")
        if data.startswith("checkwork|"):
            data_dict = {}
            params = data.split("|")[1].split("&")
            for param in params:
                key, value = param.split("=")
                data_dict[key] = value
            return data_dict
    return None


def qrcode_valid(image) -> bool:
    """
    Check whether the QRcode is in the valid time.

    Args:
        image (PIL.Image.Image): The image containing the QR code.

    Returns:
        bool: Whether the QRcode is in the valid time.
    """
    data = scan_qr_code(image)
    if data:
        createTime = data["createTime"]
        createTime = datetime.strptime(createTime, "%Y-%m-%dT%H:%M:%S.%f")
        now = datetime.now()
        if now - createTime <= timedelta(seconds=5):
            return True
    return False


if __name__ == "__main__":
    image = Image.open("qrcode_123456_2024-10-13T12-02-35.000.png")
    print(scan_qr_code(image))
    print(qrcode_valid(image))
