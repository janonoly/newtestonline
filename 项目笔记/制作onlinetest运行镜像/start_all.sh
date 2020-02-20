#!/bin/bash

BASEPATH=$(cd `dirname $0`;pwd)

PY_CMD=/python3/bin/python


# 服务入口文件
#MAIN_APP=${BASEPATH}/go2cloud/manage.py
# 迁移脚本入口文件
SCRIPTS_APP=${BASEPATH}/go2cloud/scripts/migrate_task_schdule.py
# 删除脚本入口文件
DELETE_APP=${BASEPATH}/go2cloud/scripts/delete_transfer_server.py


# 日志目录

LOG_DIR=${BASEPATH}/logs/
[ ! -d ${LOG_DIR} ] && mkdir ${LOG_DIR}

# 启动服务
#nohup ${PY_CMD} -u ${MAIN_APP} runserver 0.0.0.0:80 >> ${LOG_DIR}server-$(date +%F).log 2>&1 &
# 启动脚本迁移调度脚本
echo "---------$0 $(date) excute----------" >> ${LOG_DIR}task-script-$(date +%F).log
nohup ${PY_CMD} -u ${SCRIPTS_APP} >> ${LOG_DIR}script-$(date +%F).log 2>&1 &

# 启动迁移删除脚本
echo "---------$0 $(date) excute----------" >> ${LOG_DIR}delete-script-$(date +%F).log
nohup ${PY_CMD} -u ${DELETE_APP} >> ${LOG_DIR}delete-script-$(date +%F).log 2>&1 &
