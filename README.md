# XLS2PLJ
方便的将excel数据表导出为lua、python、json格式。

环境配置：
此工具目前只能在window系统使用，需要安装如下工具才能使用(Need to install the following tools to use):
	
python-3.x.msi(https://www.python.org/downloads/windows/)

pywin32-x-py3.x.exe(https://sourceforge.net/projects/pywin32/files/pywin32/)
office2010及以上

特点：
*支持excel表导出为： lua、python、json  （json格式不支持Vector类型导出）

*表名前缀: "@"为服务器和客户端同时导出；"#"仅客户端导出；"$"仅服务器导出。

*数据列中命令符号:"c"仅客户端导出；"s"仅服务器端导出。详情查看“xlsxs/使用说明.xlsx”

*支持对整表或数据列设置导出到客户端 和 服务器

*excel文件命名规则：随便起名字_导出名.xls   "_"后面的名字为导出文件名，如果无"_"则整个文件不处理。

*对异常报错进行高亮显示

执行格式：
python xlsx2py/xlsx2py.py  excel目录  输出目录  [lua json python]  [client server] 
具体使用方式参考对应.bat文件

配表规范：
查看xlsxs/使用说明.xlsx
