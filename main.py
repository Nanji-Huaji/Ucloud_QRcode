import PIL.Image
import streamlit as st
from utils import *
import PIL
import time
import io
import pandas as pd


st.title("云平台二维码生成器")

st.markdown("上传一张当前课程的二维码")

source_qrcode = st.file_uploader("上传二维码")

qrcode_status_text = st.empty()
qrcode_status_placeholder = st.empty()
warning_placeholder = st.empty()
qrcode_placeholder = st.empty()
qrcode_info_describe_text = st.empty()
qrcode_info_placeholder = st.empty()
sign_info_placeholder = st.empty()
sign_id_input_placeholder = st.empty()
sign_passwd_placeholder = st.empty()
sign_bottom_placeholder = st.empty()

if st.button("生成二维码"):
    if source_qrcode is None:
        st.error("请上传二维码")
    else:
        image = PIL.Image.open(source_qrcode)
        data = scan_qr_code(image)
        if data:
            qrcode_placeholder.image(image, caption="原始二维码", use_container_width=True)
            while True:
                if qrcode_valid(image):
                    # 将 data 转换为 DataFrame 并显示为表格
                    data_df = pd.DataFrame(list(data.items()), columns=["键", "值"])
                    qrcode_info_describe_text.markdown("当前二维码")
                    qrcode_info_placeholder.table(data_df)
                    qrcode_createtime = data["createTime"]
                    qrcode_createtime = datetime.strptime(qrcode_createtime, "%Y-%m-%dT%H:%M:%S.%f")
                    time_to_refresh = 5 - (datetime.now() - qrcode_createtime).seconds
                    now_time = datetime.now()
                    qrcode_status_text.markdown(f"# 还有{time_to_refresh}秒刷新")
                    qrcode_status_placeholder.success("二维码有效")
                    warning_placeholder.warning("还有5秒过期")
                else:
                    qrcode_status_placeholder.error("二维码已失效")
                    qrcode_status_text.markdown("# 正在刷新")
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


st.markdown("# 使用说明")
st.markdown("还没补充这个部分:(")
