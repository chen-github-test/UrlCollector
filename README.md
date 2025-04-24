# UrlCollector
url 扫描搜集




<code>
usage: collect.py [-h] [-o OUTPUT] [-k KEYWORD] [-n NUMBER] [-v]

这是一个自定义url收集程序

options:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        输出文件路径,默认default.txt [env var: OUTPUT]
  -k KEYWORD, --keyword KEYWORD
                        输入想要查询的关键字
  -n NUMBER, --number NUMBER
                        想要收集的资源数量
  -v, --version         show program's version number and exit

 In general, command-line values override environment variables which override defaults.

</code>

运行环境：python3.6+
pip install -r requirements # 安装所需要的环境依赖
cd UrlCollector 进入项目

<code> 
使用方法：
python collect.py -k "keyword" -n 10 -o test.txt 
# -k 输入搜索关键字
# -n 收集的信息数量
# -o 输出的文件路径
</code>