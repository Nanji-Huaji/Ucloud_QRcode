import pyzbar.pyzbar as pyzbar
from PIL import Image
import numpy as np


'''
现在遇到的问题: 尽管qrcode_generator函数返回的是一个img对象, 
但是如果将这个img对象传入scan_qr_code函数, 会报错.
从而现在只能通过将img对象保存为文件, 然后再读取文件的方式来解决这个问题.

Current problem: Although the qrcode_generator function returns an img object,
if this img object is passed to the scan_qr_code function, an error will occur.
Therefore, the problem can only be solved by saving the img object as a file and then reading the file.
'''


def scan_qr_code(image):
    """
    Scan a QR code image and return the decoded data.

    Args:
        image (PIL.Image.Image): The image containing the QR code.

    Returns:
        str: The decoded data from the QR code.
    """
    # 将 PIL.Image 对象转换为 NumPy 数组
    image_np = np.array(image)
    decoded_objects = pyzbar.decode(image_np)
    if decoded_objects:
        return decoded_objects[0].data.decode('utf-8')
    return None

def get_qrcode_data(qrcode_file):
    """
    Open the QR code image file and return the decoded data.

    Args:
        qrcode_file (str): The filename of the QR code image.

    Returns:
        str: The decoded data from the QR code.
    """
    # 打开QR码图片文件
    image = Image.open(qrcode_file)
    return scan_qr_code(image)