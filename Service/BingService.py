from Controller.BingCrawler import BingCrawler


class BingService(BingCrawler):
    def __init__(self, keyword, num):
        super().__init__(keyword=keyword, num=num)

    def run(self):
        # 采集数据的数量知道达到目标数量，否则会一直搜集资源
        while self._result_num > len(self._result_set):
            super().fetch()
            super().parse()
        super().handle_data()
