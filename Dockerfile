# 使用Python 3.9官方基础镜像
FROM python:3.9

# 创建工作目录
WORKDIR /app

# 确保所需目录存在
RUN mkdir -p /app/data

# 复制 gz 文件到工作目录和脚本文件到正确目录
COPY BPIC12.xes.gz /app/data/BPIC12.xes.gz
COPY BPIC13_cp.xes.gz /app/data/BPIC13_cp.xes.gz
COPY BPIC13_i.xes.gz /app/data/BPIC13_i.xes.gz
COPY BPIC14_f.xes.gz /app/data/BPIC14_f.xes.gz
COPY BPIC15_1f.xes.gz /app/data/BPIC15_1f.xes.gz
COPY BPIC15_2f.xes.gz /app/data/BPIC15_2f.xes.gz
COPY BPIC15_3f.xes.gz /app/data/BPIC15_3f.xes.gz
COPY BPIC15_4f.xes.gz /app/data/BPIC15_4f.xes.gz
COPY BPIC15_5f.xes.gz /app/data/BPIC15_5f.xes.gz
COPY BPIC17_f.xes.gz /app/data/BPIC17_f.xes.gz
COPY RTFMP.xes.gz /app/data/RTFMP.xes.gz
COPY SEPSIS.xes.gz /app/data/SEPSIS.xes.gz
COPY algorithm.py /app/algorithm.py

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

# 列出解压后的文件和确认algorithm.py是否存在
RUN ls -la /app && ls -la /app/data

