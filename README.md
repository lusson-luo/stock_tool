## 股票告警分析工具

### 需求

每次想看股票的时候都要拿出手机，或者打开股票软件，这个过程一般都比较长，很容易打断连贯的代码思路，并且股票软件都有太多广告信息，诱惑信息，让人忍不住去点，浪费很长时间，同时也杂多的信息，容易让人陷入FOLO的心态，活生生成了韭菜。第二个需要一个告警通知，某某股票到了我设定的告警值，我可以加仓或者斩仓了。

功能

1. 查看实时自选股票价格
2. 股票阀值告警

#### 实时自选股票价格

终端输入指定命令：stock

终端显示自选股票信息

```
name      - now      - max_today      - min_today
中兴       - 32.14    - 33.41         32
```

命令后可接参数`income`，如`stock income`，则可以打印出设置的买入价格和目前收益。

```
name      - now      - max_today      - min_today   - buy_price   - income
中兴       - 32.14    - 33.41         32              28.40         1200
```

#### 阀值告警

调用mac系统通知，右上角

![image-20190402175537291](stock_notify.png)

### 使用方法

- 需要本地安装python3，pip3（一般安装python会自动安装）
- mac 系统。

#### 设置查看实时股票

下载文件后，终端进入对应文件夹，执行`python3 show_stock.py`，看它是否打印

> name      - now      - max_today      - min_today
> 中兴通讯    30.260    31.000         30.100
> 上证50    2920.5151    2933.4463         2903.2682

接着修改自己的自选代码，在`show_stock.py`中stockNos和stockNames的数组中添加股票code和股票名称。

接着新建一个命令`stock`关联`python3 show_stock.py`。输入`vim ~/bash_profile`，添加这一行`alias stock='python3 /$path/stock/show_stock.py`，`$path`是文件的绝对路径。添加后输入`:wq`来保存配置的命令。执行`source ~/bash_profile`将新保存的环境变量加载到系统中。接着在终端输入`stock`查看结果。

#### 定时告警

先下载`pync`系统通知包

```
pip3 install pync
```

接着终端进入代码文件夹，执行

```
python3 stock_alarm.py 
```

如下显示

![image-20190412220908534](stock_notify.png)

终端输入`crontab -e`设置定时任务，输入`*/3 9-12,13-15 * * 1-5 /usr/local/bin/python3 /$path/stock/stock_alarm.py`，定时周期为3分钟一次，在周一到周五9-12，13-15点时执行。

注意python3路径是本机安装的python3的绝对路径，不知道自己python3路径的可以通过`which python3`来查看路径。