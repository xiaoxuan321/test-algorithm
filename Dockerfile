# 使用Python 3.9官方基础镜像
FROM python:3.9

# 创建工作目录
WORKDIR /app

# 确保所需目录存在
RUN mkdir -p /app/data

# 复制当前目录下的所有文件到容器的/app 目录
COPY . /app/data

# 安装所需依赖
RUN apt-get update && apt-get install -y gzip \
    && pip install pm4py pandas

# 解压文件
RUN gzip -d /app/data/BPIC12.xes.gz
RUN gzip -d /app/data/BPIC13_cp.xes.gz
RUN gzip -d /app/data/BPIC13_i.xes.gz
RUN gzip -d /app/data/BPIC14_f.xes.gz
RUN gzip -d /app/data/BPIC15_1f.xes.gz
RUN gzip -d /app/data/BPIC15_2f.xes.gz
RUN gzip -d /app/data/BPIC15_3f.xes.gz
RUN gzip -d /app/data/BPIC15_4f.xes.gz
RUN gzip -d /app/data/BPIC15_5f.xes.gz
RUN gzip -d /app/data/BPIC17_f.xes.gz
RUN gzip -d /app/data/RTFMP.xes.gz
RUN gzip -d /app/data/SEPSIS.xes.gz


