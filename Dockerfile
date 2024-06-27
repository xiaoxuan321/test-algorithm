# 使用Python 3.9官方基础镜像
FROM python:3.9

# 创建工作目录
WORKDIR /app

# 复制当前目录下的所有文件到容器的/app 目录
COPY . /app

# 安装所需依赖
RUN apt-get update && apt-get install -y gzip \
    && pip install pm4py pandas

# 解压文件
RUN gzip -d /app/BPIC12.xes.gz
RUN gzip -d /app/BPIC13_cp.xes.gz
RUN gzip -d /app/BPIC13_i.xes.gz
RUN gzip -d /app/BPIC14_f.xes.gz
RUN gzip -d /app/BPIC15_1f.xes.gz
RUN gzip -d /app/BPIC15_2f.xes.gz
RUN gzip -d /app/BPIC15_3f.xes.gz
RUN gzip -d /app/BPIC15_4f.xes.gz
RUN gzip -d /app/BPIC15_5f.xes.gz
RUN gzip -d /app/BPIC17_f.xes.gz
RUN gzip -d /app/RTFMP.xes.gz
RUN gzip -d /app/SEPSIS.xes.gz


