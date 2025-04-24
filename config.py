import configargparse


class Parser:
    args = None

    @classmethod
    def parser(cls):
        cls.parser = configargparse.ArgumentParser(
            description="这是一个自定义url收集程序",
        )
        cls.parser.add_argument(
            '-o', '--output',
            env_var='OUTPUT',
            help='输出文件路径,默认default.txt',
            default='default.txt'
        )
        cls.parser.add_argument(
            '-k', '--keyword',
            help='输入想要查询的关键字',
            default='关键字'
        )
        cls.parser.add_argument(
            "-n", "--number",
            help="想要收集的资源数量",
            default="10"
        )
        cls.parser.add_argument(
            "-v", "--version",
            action="version",
            version="%(prog)s 1.0"
        )
        cls.parser.add_argument(
            "-e", "--env", choices=["baidu", "bing"], help="选择搜索引擎，默认百度搜索"
        )

        cls.args = cls.parser.parse_args()

    @classmethod
    def get_parser(cls):
        return cls.parser

    @classmethod
    def get_args(cls):
        return cls.args
