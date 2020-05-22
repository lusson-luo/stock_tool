### 使用教程

系统环境需求

- mac 系统。
- 需要安装python3，pip3（一般安装python会自动安装）

#### 设置定时告警

进入项目文件夹，执行

```shell
cp stock_data.json.example stock_data.json
./start-alarm.sh
```

在stock_data.json的alarm_data中添加告警数据。

**或者手动执行一下步骤**

> 手动执行步骤可以方便发现错误发现在哪一步，对于不能执行`./start-alarm.sh`的情况下使用。

下载`pync`系统通知包

```
pip3 install pync
```

接着终端进入代码文件夹，测试

```
python3 stock_alarm.py 
```

如下显示

![image-20190412220908534](stock_notify.png)

**设置系统定时任务**

终端输入`crontab -e`设置定时任务，输入`*/3 9-12,13-15 * * 1-5 /usr/local/bin/python3 /$path/stock/stock_alarm.py`，定时周期为3分钟一次，在周一到周五9-12，13-15点时执行。

注意python3路径是本机安装的python3的绝对路径，不知道自己python3路径的可以通过`which python3`来查看路径。

设置好后，输入`crontab -l`查看定时任务列表.

如果报错`crontab: "/usr/bin/vi" exited with status 1`，意思是系统没有安装vi编辑器，需要把默认编辑器改成vim即可，在`～/.bash_profile`加上`export EDITOR=vim`，重写设置定时任务。

#### 设置查看实时股票

> 不推荐查看实时股票，股票买了放在那里设置告警就可以，没必要实时查看，浪费自己的精力。

下载项目后，终端进入对应文件夹，执行

```
cp stock_data.json.example stock_data.json
python3 show_stock.py
```

看它是否打印

> name      - now      - max_today      - min_today
> 中兴通讯    30.260    31.000         30.100
> 上证50    2920.5151    2933.4463         2903.2682

修改自己的自选股票，在`stock_data.json`中的`show_data`添加股票名和code。

**配置快捷命令**

1. 在环境变量中新建`stock`执行`python3 show_stock.py`。
2. 终端输入`vim ~/bash_profile`，添加`alias stock='python3 /$path/stock/show_stock.py`，`$path`是文件的绝对路径。
3. 输入`:wq`来保存配置的命令。
4. 执行`source ~/bash_profile`将新保存的环境变量加载到系统中。
5. 重新终端输入`stock`查看结果。

这样我就可以在终端中通过命令快捷，方便，不留痕迹的查看股票了。