#!/bin/bash
# 包装脚本：用 JobFinder 自带的 Python 运行 job_skill_review.py（路径无空格，方便定时任务免确认）
exec "$HOME/Library/Application Support/JobFinder/.tools/python/bin/python3" "$(dirname "$0")/job_skill_review.py" "$@"
