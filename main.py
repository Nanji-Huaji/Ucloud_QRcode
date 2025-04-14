import PIL.Image
import streamlit as st
from utils import *
import PIL
import time
import io
import pandas as pd


st.title("云平台二维码生成器")

st.markdown("上传一张当前课程的二维码")


qrcode_status_placeholder = st.empty()
qrcode_placeholder = st.empty()
qrcode_info_placeholder = st.empty()
source_qrcode = st.file_uploader("上传二维码")
generate_qrcode_botton_placeholder = st.empty()
sign_info_placeholder = st.empty()
sign_id_input_placeholder = st.empty()
sign_passwd_placeholder = st.empty()
sign_botton_placeholder = st.empty()

qrcode_status = qrcode_status_placeholder.info("请上传二维码")
generate_qrcode_botton = generate_qrcode_botton_placeholder.button("生成二维码")
sign_id_input = sign_id_input_placeholder.text_input("请输入学号", placeholder="请输入学号")
sign_passwd = sign_passwd_placeholder.text_input("请输入密码", placeholder="请输入密码", type="password")
sign_botton = sign_botton_placeholder.button("签到")

if generate_qrcode_botton:
    if source_qrcode is None:
        qrcode_status_placeholder.error("请上传二维码")
    else:
        image = PIL.Image.open(source_qrcode)
        data = scan_qr_code(image)
        if data is not None:
            qrcode_placeholder.image(image, caption="原始二维码", use_container_width=True)
            qrcode_info_placeholder.markdown("当前二维码")
            # 成功扫描二维码
            qrcode_status_placeholder.success("已接收二维码")
            while True:
                if qrcode_valid(image):
                    # 将 data 转换为 DataFrame 并显示为表格
                    data_df = pd.DataFrame(list(data.items()), columns=["键", "值"])
                    qrcode_info_placeholder.table(data_df)
                    qrcode_createtime = data["createTime"]
                    qrcode_createtime = datetime.strptime(qrcode_createtime, "%Y-%m-%dT%H:%M:%S.%f")
                    time_to_refresh = 5 - (datetime.now() - qrcode_createtime).seconds
                    now_time = datetime.now()
                    qrcode_status_text = qrcode_status_placeholder.markdown(f"# 还有{time_to_refresh}秒刷新")
                    qrcode_status_placeholder.success(f"二维码有效，还有{time_to_refresh}秒刷新")
                    # 提示用户还有多少时间刷新二维码
                    warning_placeholder = st.empty()
                else:
                    qrcode_status_placeholder.warning("二维码失效，正在刷新")
                    new_qrcode = qrcode_generator(data["id"], data["siteId"], data["classLessonId"])
                    # 将生成的二维码图像保存到字节流中
                    buf = io.BytesIO()
                    new_qrcode.save(buf, format="PNG")
                    buf.seek(0)
                    # 将字节流转换回 PIL.Image 对象
                    new_qrcode_image = PIL.Image.open(buf)
                    # 更新 image 变量以继续循环检查新二维码的有效性
                    image = new_qrcode_image
                    # 重新扫描新的二维码
                    data = scan_qr_code(new_qrcode_image)
                    qrcode_placeholder.image(new_qrcode_image, caption="新二维码", use_container_width=True)
                    # 更新表格内容
                    data_df = pd.DataFrame(list(data.items()), columns=["键", "值"])
                    qrcode_info_placeholder.table(data_df)

                    time.sleep(0.5)
        else:
            qrcode_status_placeholder.error("二维码无效")

if sign_botton:
    if source_qrcode is not None:
        if sign_id_input and sign_passwd:
            pass
        else:
            sign_info_placeholder.error("请输入学号和密码")
    else:
        sign_info_placeholder.error("请先上传二维码")


st.markdown("# 使用说明")
st.markdown("还没补充这个部分:(")
