#系统ulimit参数检查工具使用
## 1. 工具套件

- UlimitCheck.exe 自行主程序工具
- checkhosts.csv 配置文件

## 2. 配置文件checkhosts.csv解读

|序号|字段名|说明|备注|
| --- | --- | --- | --- |
|1|site|公积金中心名称|如"长春市住房公积金管理中心"|
|2|host|检查主机IP地址|如"192.168.10.100"|
|3|port|主机SSH连接端口|如"22"|
|4|user|SSH登录用户名|如"workflow"|
|5|password|SSH登录用户密码|如"workflow"|
|6|operator|检查运维人员姓名||
|7|description|该主机用途描述|如"BSP DB2核心数据库服务器"|

## 3. 执行方法
将UlimitCheck.exe和checkhosts.csv放在同一目录下，双击执行UlimitCheck.exe程序，执行结束后会生产如下文件:

- log/systeminfo.log 日志文件
- 系统内核参数检查结果.csv检查结果csv文件


# 不能远程远程执行工具场景信息收集方法
```shell script
$echo $(hostname;ulimit -n;ulimit -u;uname)
hb3-aza-k8s-master01 65535 100000 Linux           # 说明第一列为"主机名称",第二列"单进程最大句柄数",第三列"单用户最大进程数",最后一列"系统类型"
```
***[说明]***

- 不同操作系统账号下的单进程最大句柄数和单用户最大进程数可能不同,取决于其配置参数设置用户是所有还是指定用户