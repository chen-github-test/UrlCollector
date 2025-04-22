from Controller.BaiduCrawler import BaiduCollector


class BaiduService(BaiduCollector):
    def __init__(self, keyword, pn):
        super().__init__(keyword=keyword, pn=pn)
        self._keyword = keyword
        self._result_num = pn // 10
        self._url = f"http://m.baidu.com/ssid=0/from=0/bd_page_type=1/uid=0/baiduid=F0A715FCC08EDFEF3EF12FEDDC2EC810/pu=sz%40224_220%2Cta%40middle____/pu=sz%40224_220%2Cta%40middle___24_74.0/baiduid=31235B9FF0F7A756A7940620CAF109E1/s?ref=www_colorful&lid=12985577237012163036&word={self._keyword}&pn={self._result_num}&rn=10&tn=middle&prest=111081&st=111091&usm=0&sa=pp"

    def run(self):
        super().fetch()
        super().parse()
        super().handle_data()
