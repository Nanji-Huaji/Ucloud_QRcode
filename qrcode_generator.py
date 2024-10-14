import qrcode
import time
from datetime import datetime, timedelta

current_qrcode_file = None


def qrcode_data_generator(id: str, siteId: str, createTime: str, classLessonId: str)->str:
    '''
    Generate the data string for the QR code.

    Returns:
        str: The data string for the QR code.
    '''
    qrcode_data = f'''
    checkwork|
    id={id}&
    siteId={siteId}&
    createTime={createTime}&
    classLessonId={classLessonId}
    '''
    return qrcode_data

def create_time_generator()->str:
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
    formatted_time = rounded_time.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3]
    return formatted_time

def qrcode_generator(id: str, siteId: str, classLessonId: str)->str:
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
    # return img
    # 生成文件名
    filename = f'qrcode_{id}_{createTime.replace(":", "-")}.png'
    img.save(filename)
    current_qrcode_file = filename
    return filename



    