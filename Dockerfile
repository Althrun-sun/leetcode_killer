# 使用官方 Python 基础镜像
FROM python:3.9-slim

# 设置工作目录
WORKDIR /app

# 将当前目录的内容复制到容器中的 /app 目录
COPY . /app

# 安装所有依赖项
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# 开放容器的端口，使外部访问成为可能
EXPOSE 80

# 定义环境变量
ENV FLASK_APP=my_flask_app.py

# 当容器启动时，运行以下命令
CMD ["flask", "run", "--host=0.0.0.0", "--port=80"]
