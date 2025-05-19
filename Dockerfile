FROM python:3.9-slim

WORKDIR /app

# 复制项目文件
COPY . .

# 安装系统依赖（pyzbar需要）
RUN apt-get update && \
    apt-get install -y libzbar0 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# 安装Python依赖
RUN pip install --no-cache-dir -r requirements.txt

# 暴露Streamlit默认端口
EXPOSE 8501

# 启动命令
CMD ["streamlit", "run", "app.py", "--server.address", "0.0.0.0"]