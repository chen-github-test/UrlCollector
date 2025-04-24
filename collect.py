from Service.BaiduService import BaiduService
from Service.BingService import BingService
from config import Parser

if __name__ == '__main__':
    Parser.parser()
    match Parser.args.env.lower():
        case "bing":
            collector = BingService(Parser.args.keyword, int(Parser.args.number))
        case _:

            collector = BaiduService(Parser.args.keyword, int(Parser.args.number))

    collector.run()
