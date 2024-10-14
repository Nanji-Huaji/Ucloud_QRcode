import pyzbar.pyzbar as pyzbar
from PIL import Image
import numpy as np
import datetime
from datetime import timedelta

'''
现在遇到的问题: 尽管qrcode_generator函数返回的是一个img对象, 
但是如果将这个img对象传入scan_qr_code函数, 会报错.
从而现在只能通过将img对象保存为文件, 然后再读取文件的方式来解决这个问题.

Current problem: Although the qrcode_generator function returns an img object,
if this img object is passed to the scan_qr_code function, an error will occur.
Therefore, the problem can only be solved by saving the img object as a file and then reading the file.
'''


def scan_qr_code(image)->str:
    """
    Scan a QR code image and return the decoded data.

    Args:
        image (PIL.Image.Image): The image containing the QR code.

    Returns:
        str: The decoded data from the QR code.
    """
    decoded_objects = pyzbar.decode(image)
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

def get_qrcode_data_from_img(img):
    """
    Get the QR code data from the image object.

    Args:
        img (PIL.Image.Image): The image object containing the QR code.

    Returns:
        str: The decoded data from the QR code.
    """
    return scan_qr_code(img)
   
def qrcode_valid(image)->bool:
    '''
    Check whether the QRcode is in the valid time.

    Args:
        image (PIL.Image.Image): The image containing the QR code.
    
    Returns:
        bool: Whether the QRcode is in the valid time.
    '''
    data = scan_qr_code(image)
    if data:
        data = data.split('&')
        createTime = data[2].split('=')[1]
        createTime = datetime.strptime(createTime, '%Y-%m-%dT%H:%M:%S.%f')
        now = datetime.now()
        if now - createTime <= timedelta(minutes=5):
            return True
    