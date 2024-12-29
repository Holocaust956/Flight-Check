# 使用官方 Python 镜像
FROM python:3.9-slim

# 设置工作目录
WORKDIR /fetch

# 安装依赖
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 复制代码到容器中
COPY . .

# 设置默认命令
CMD sleep 60 && python scraper/main.py --dep BJS --arr HGH --date 2024-01-05