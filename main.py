import os
import subprocess


def run_streamlit():
    try:
        # 设置工作目录
        os.chdir(os.path.dirname(os.path.abspath(__file__)))

        # 运行 streamlit
        print("正在启动 Streamlit 应用...")
        subprocess.run(["streamlit", "run", "app.py"], check=True)

    except FileNotFoundError:
        print("错误：未找到 main.py 文件")
    except subprocess.CalledProcessError:
        print("错误：Streamlit 运行失败")
    except Exception as e:
        print(f"发生错误：{str(e)}")


if __name__ == "__main__":
    run_streamlit()
