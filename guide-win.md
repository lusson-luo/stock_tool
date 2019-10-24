### 使用教程

系统环境需求

- python3，pip3（一般安装python会自动安装）

安装python3和pip3还请自行百度，十分简单。调用`python3 --version`和`pip3 --version`测试是否安装好。

#### 设置查看实时股票

下载文件后，cmd进入文件夹，执行`show_stock_repeat.py`，看它是否打印

> name      - now      - max_today      - min_today
> 中兴通讯    30.260    31.000         30.100
> 上证50    2920.5151    2933.4463         2903.2682

如果成功，说明环境和代码是没有问题的。在`show_stock_repeat.py`中stockNos和stockNames的数组中添加自选股票code和股票名称。

**配置快捷命令**



#### 设置定时告警

打开文件夹，cmd执行stock_alarm_win.py即可，5秒一次拉取股票信息,到达设置目标即会弹框提醒，提醒完后该线程退出，其他提醒作废。
