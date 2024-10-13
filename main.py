import qrcode_generator

if __name__ == '__main__':
    id = '123456'
    siteId = 'site1'
    classLessonId = 'lesson1'
    qrcode_generator.qrcode_generator(id, siteId, classLessonId)
    print(qrcode_generator.qrcode_generator(id, siteId, classLessonId))