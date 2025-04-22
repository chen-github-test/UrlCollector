from Service.BaiduService import BaiduService
from config import Parser

if __name__ == '__main__':
    Parser.parser()
    baidu = BaiduService(Parser.args.keyword, int(Parser.args.number))
    baidu.run()
