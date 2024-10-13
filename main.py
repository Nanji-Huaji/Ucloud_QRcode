from qrcode_scanner import *
from qrcode_generator import *
from PIL import Image

# 生成QR码
id = '123'
siteId = '456'
classLessonId = '789'
qr_code = qrcode_generator(id, siteId, classLessonId)

print(scan_qr_code(qr_code))
print(type(qr_code))
