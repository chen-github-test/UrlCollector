from Controller.BaiduCrawler import BaiduCollector


class BaiduService(BaiduCollector):
    def __init__(self, keyword, number):
        super().__init__(keyword=keyword, number=number)

    def run(self):
        # 采集数据的数量知道达到目标数量，否则会一直搜集资源
        while self._result_num > len(self._result_set):
            super().fetch()
            super().parse()
        super().handle_data()
