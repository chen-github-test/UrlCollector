import os
from abc import ABC, abstractmethod

import requests

from config import Parser


class Crawler(ABC):
    @abstractmethod
    def fetch(self):
        pass

    @abstractmethod
    def parse(self):
        pass

    @abstractmethod
    def handle_data(self):
        pass


class SearchEngineCrawler(Crawler):
    def __init__(self):
        self._keyword = None
        self._result_num = None
        self._result_set = set()
        self._results = list()
        self._response = None
        self._url = f"http://m.baidu.com/ssid=0/from=0/bd_page_type=1/uid=0/baiduid=F0A715FCC08EDFEF3EF12FEDDC2EC810/pu=sz%40224_220%2Cta%40middle____/pu=sz%40224_220%2Cta%40middle___24_74.0/baiduid=31235B9FF0F7A756A7940620CAF109E1/s?ref=www_colorful&lid=12985577237012163036&word={self._keyword}&pn={self._result_num}&rn=10&tn=middle&prest=111081&st=111091&usm=0&sa=pp"
        self._method = "GET"
        self._headers = {
            "Accept": "* / *",
            "Accept-Encoding": "gzip",
            "Accept-Language": "en,zh-CN;q=0.9,zh;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "Connection": "keep - alive",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }

    def fetch(self):
        with requests.Session() as session:
            self._response = session.request(method=self._method, url=self._url, headers=self._headers, timeout=10)
            # print(self._response.text)
            # print(self._url)

    def parse(self):
        pass

    def handle_data(self):
        print("正在做数据处理……")
        # 去重处理
        unique_results = list(self._result_set)
        if os.path.exists(Parser.args.output):
            overwrite = input(f"文件 {Parser.args.output} 已存在，是否覆盖？ (y/n): ").lower()
            if overwrite != 'y':
                print("操作已取消")
                exit()

        with open(Parser.args.output, "w", encoding='utf-8') as file:
            for url in unique_results:
                file.write(url + "\n")
        print("数据处理完毕。")
        print(f"采集结束，共收集到 {len(unique_results)} 个唯一URL")
        print(f"结果已保存到 {Parser.args.output}文件")
