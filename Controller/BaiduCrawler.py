import requests
from bs4 import BeautifulSoup

from Controller.Crawler import SearchEngineCrawler


class BaiduCollector(SearchEngineCrawler):
    def __init__(self, keyword, number):
        super().__init__()
        self._keyword = keyword
        self._result_num = number
        self._init_page = 1
        self._url = f"http://m.baidu.com/ssid=0/from=0/bd_page_type=1/uid=0/baiduid=F0A715FCC08EDFEF3EF12FEDDC2EC810/pu=sz%40224_220%2Cta%40middle____/pu=sz%40224_220%2Cta%40middle___24_74.0/baiduid=31235B9FF0F7A756A7940620CAF109E1/s?ref=www_colorful&lid=12985577237012163036&word={self._keyword}&pn={self._init_page * 10}&rn=10&tn=middle&prest=111081&st=111091&usm=0&sa=pp"
        self.blacklist = [
            'http://baike.baidu.com',
            'http://zhidao.baidu.com',
            'http://baijiahao.baidu.com',
            'http://wk.baidu.com',
            'http://m.sohu.com',
            'http://zhuanlan.zhihu.com',
            'http://mp.weixin.qq.com',
            'http://baijiahao.baidu.com',
            'http://www.zhihu.com',
            'http://m.ximalaya.com',
            'http://finance.sina.cn'

        ]

    def fetch(self):
        print(f"正在从 baidu 采集 {self._keyword} 的URL...")
        with requests.Session() as session:
            self._url = f"http://m.baidu.com/ssid=0/from=0/bd_page_type=1/uid=0/baiduid=F0A715FCC08EDFEF3EF12FEDDC2EC810/pu=sz%40224_220%2Cta%40middle____/pu=sz%40224_220%2Cta%40middle___24_74.0/baiduid=31235B9FF0F7A756A7940620CAF109E1/s?ref=www_colorful&lid=12985577237012163036&word={self._keyword}&pn={self._init_page * 10}&rn=10&tn=middle&prest=111081&st=111091&usm=0&sa=pp"
            self._response = session.request(method=self._method, url=self._url, headers=self._headers, timeout=10)
            self._init_page += 1
            # print(self._response.text)
            # print(self._url)

    def parse(self):
        if self._response is not None:
            print(f"正在从 baidu解析 {self._keyword} 的URL...")
            soup = BeautifulSoup(self._response.text, 'html.parser')
            res = soup.find_all('div', class_="resitem")
            for i in res:
                try:
                    abs_class = i.find('div', class_="abs")
                    siteurl = abs_class.find('span', class_='site').get_text()
                    siteurl = "http://" + siteurl
                    self._results.append(siteurl)
                except:
                    continue
            self._result_set.update(self._results)
            self._result_set -= set(self.blacklist)
            self._results.clear()
        else:
            print("Request Error!Can't find any request resqponse")
