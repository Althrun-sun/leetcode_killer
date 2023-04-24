FROM python:3.9
WORKDIR /app
COPY . /app
FROM python:3.9
WORKDIR /app
COPY . /app
RUN pip install openai flask hashlib os boto3
EXPOSE 5000

# 当容器启动时，运行以下命令
CMD ["flask", "run", "--host=0.0.0.0"]
