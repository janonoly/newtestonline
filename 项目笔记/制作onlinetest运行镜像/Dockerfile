FROM django
MAINTAINER janono

# 定义docker中工作目录
ENV WORK_DIR /work/
# 创建docker内工作目录
RUN mkdir $WORK_DIR
# 定义映射端口

EXPOSE 8000

WORKDIR $WORK_DIR
RUN git clone http://192.168.25.3:7002/janono/onlinetest.git

# 添加启动服务脚本
ADD *.sh ${WORK_DIR}

CMD `which bash` /work/start_all.sh && tail -f /work/logs/server-$(date +%F).log

