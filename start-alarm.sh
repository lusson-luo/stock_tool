if ! [ `command -v python3` ];then echo '未安装 python3 , 请手动安装python3'; exit 1;fi
if ! [ `command -v pip3` ];then echo '未安装pip3 , 请手动安装'; exit 1;fi
sudo pip3 install pync
work_path=$(cd `dirname $0`; pwd)
cp ${work_path}/stock_data.json.example ${work_path}/stock_data.json
echo "*/3 9-12,13-15 * * 1-5 /usr/local/bin/python3 ${work_path}/stock/stock_alarm.py" >> cron
crontab cron
rm -f cron