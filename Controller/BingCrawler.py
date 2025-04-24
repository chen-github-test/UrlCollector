from urllib.parse import quote_plus

from bs4 import BeautifulSoup

from Controller.Crawler import SearchEngineCrawler


class BingCrawler(SearchEngineCrawler):
    def __init__(self, keyword, num):
        super().__init__()
        self._keyword = keyword
        self._result_num = num
        self._headers.update({
                                 "Cookie": "MUID=34912DCE60E169D41ADE3C1264E16879; MUIDB=34912DCE60E169D41ADE3C1264E16879; ANON=A=CE154E05C2E7079D187C2AFBFFFFFFFF; SnrOvr=X=rebateson; SRCHD=AF=NOFORM; SRCHUID=V=2&GUID=1606BD139259476DA66778F75408A479&dmnchg=1; _UR=QS=0&TQS=0&Pn=0; _clck=fm9dsk%7C2%7Cftj%7C0%7C1658; MMCASM=ID=A93589443D7A4AA1BCF06790C3533489; MSPTC=qho5WnGwKZ_NebzTk8L1hLEuJ6OBbhweLZhr1bpGMLM; _tarLang=default=zh-Hans; _TTSS_IN=isADRU=1; _TTSS_OUT=hist=WyJ6aC1IYW5zIl0=; _uetvid=0cfc7cf01aa311efb618d3b2f63a6c9a; _uetmsclkid=_uet6f106229b21b1591e0da05d938f2d7f3; SRCHUSR=DOB=20220709&T=1743486808000&DS=1&POEX=W; BFBUSR=BFBHP=0; _HPVN=CS=eyJQbiI6eyJDbiI6NCwiU3QiOjAsIlFzIjowLCJQcm9kIjoiUCJ9LCJTYyI6eyJDbiI6NCwiU3QiOjAsIlFzIjowLCJQcm9kIjoiSCJ9LCJReiI6eyJDbiI6NCwiU3QiOjAsIlFzIjowLCJQcm9kIjoiVCJ9LCJBcCI6dHJ1ZSwiTXV0ZSI6dHJ1ZSwiTGFkIjoiMjAyNS0wNC0yNFQwMDowMDowMFoiLCJJb3RkIjowLCJHd2IiOjAsIlRucyI6MCwiRGZ0IjpudWxsLCJNdnMiOjAsIkZsdCI6MCwiSW1wIjoxOCwiVG9ibiI6MH0=; _EDGE_S=SID=21B1A7F224FB6CAD22C1B22A25B86DE5; .MSA.Auth=CfDJ8GtUudZcSi1Enm88WwQKtCfSuFINciGb4xQ1Qox4qVqezNLPoyygRkYdwdiyo2UC7Hs74CCrVp8v8ClYcVz4ql6ODHfYmyl8HhDRYTloIvV6z6YKvCZ8IftbiJ4lIlwT455jdHSkfXpxPPTd8evvDoCqT9hM448noKAvorD_atPPl_9GfDGe8Z1e7L4w5yYZMWhAfkPIRAYdRRmIuN3lBrJx_wc6datMs9lMUxv0xtKquQxQq3o3BtJu_ohU4MbYLICENM-4sHv9dqc2W1G6hqPGYpfLB8v0eyPRW--eogyyazWIEbuyAa0jeGoMpC1m1pjWJedBp3Tqw3owq1BKNIbN4kRaVLSDXvJX_aPw8m4ucNtj5FdZqRTHYLLUvaKk6f7oJYNvFSAN8JEU5D7PQLU; SNRHOP=I=&TS=; _U=1IhlufEz82Z2LOcDgippO7RGKZ6rbHcPJdZxiZEW-ANcorVDui0n5NBonzGuZg63Zk1wh-uHC3o_Qp7ELK6OM4fJ4-ll5WjI4eIe2Gx0eT9phKJRo3qih96loleOzDoep5OD-3vS3f9Ilqt70JlzPtLDXEW56t9NvrFBhAWyi3FYhQALwK10E7GH8-tRQ-qCXZrr3oUGMZ1fPGuZZ3J_PoQ; WLS=C=175b239500f6f716&N=Falk; ENSEARCH=BENVER=1; _FP=hta=on; _Rwho=u=d&ts=2025-04-24; USRLOC=HS=1&ELOC=LAT=31.233678817749023|LON=121.30188751220703|N=Jiading%20District%2C%20Shanghai|ELT=2|&CLOC=LAT=31.233678329399062|LON=121.3018909807428|A=733.4464586120832|TS=250424051637|SRC=W&BID=MjUwNDI0MTMxNjM3XzcwZjg2NzA1MjBkZjQ5M2U4MDIyNTRhYTUyYjFlZDNhZTBjNjFlNjc5MTA2MzQyNDUxYWJkZjUyYjQ0MDFiZGY=; _SS=SID=21B1A7F224FB6CAD22C1B22A25B86DE5&R=3861&RB=3861&GB=0&RG=0&RP=3861; BFPRResults=FirstPageUrls=BF9F50DA73FC9EF28D4AD16BC4F81C48%2CF65CB28BA7BBE9893A6D89D9EE790D79%2C66BEA8DD909A3FCAF71FDD23952DD6B2%2C2DF70DD939F8B68115B2AF112745DB1A%2C2624FA06E5C06CFC6831165A22D9CEB4%2C16A5FD0A957885D424656B2DE7C9E582%2CFCCD5DBBDDB92C5E4036D356230368C8%2CDAAAEFC40B3824474990EC9BDEB3F5DC%2C8A85634D5065D24224A891F1FC803D14%2CFE1BDD0788B992EBE91B3AE4D8DDBA75&FPIG=08B7A7CEEEE04A27B0BF14DE528D701C; GC=75WedxtKOejByOfcr5yU4XDWeXA0S4cjQH2p_ENQ-c9TezYp9Zhgk67cB1yj_5BdMWhWLK47MeaNmv18lNbW8g; _RwBf=ilt=19&ihpd=0&ispd=1&rc=3861&rb=3861&gb=2025w17_c&rg=0&pc=3861&mtu=0&rbb=0.0&g=&cid=0&clo=0&v=53&l=2025-04-23T07:00:00.0000000Z&lft=0001-01-01T00:00:00.0000000&aof=0&o=0&p=RewardsAcquisition&c=M4025P&t=2139&s=2023-02-08T04:02:57.7976629+00:00&ts=2025-04-24T05:43:07.4531621+00:00&rwred=0&wls=2&lka=0&lkt=0&TH=&mte=0&dci=0&r=1&wlb=0&ard=0001-01-01T00:00:00.0000000&wle=0&ccp=2&aad=0&rwdbt=1675800182&rwflt=1712884564&mta=0&cpt=0&e=hknJ6NuPuV3p587w7HL8iy4ZlCA0on196K8LoAUBkIn-JWqKQ7QxTIYtFdjf-oLSrhvwWjroU-_2m2DM8F6Bch91zJrBKR6cw5n1eCBoG3k&A=&rwaul2=0; dsc=order=BingPages; SRCHHPGUSR=SRCHLANG=en&PV=19.0.0&BZA=0&DM=0&BRW=XW&BRH=S&CW=1912&CH=214&SCW=1897&SCH=2591&DPR=1.0&UTC=480&EXLTT=31&AV=14&ADV=14&RB=0&MB=0&HV=1745473386&HVE=CfDJ8GtUudZcSi1Enm88WwQKtCeHVKvVUFXnKErtu4SvXVsFLlcxliBTyE2wN3ax9D0IcM1xNq7dN01WnWRpVzi3htXHbvlXx4Tfjk6t7dcXisyCZ5d6k3ThrKCnGqumNvjH-sbdXSvw7mrLxcDyDCI9lE1Wwq2GlT3CM7Oq9WLuzOWUkB3VLIZvO2U9lKRnfXafxw&PRVCW=1912&PRVCH=214&IG=8F968EA350E2442684B55415A3C60235&DMREF=0"})
        self._url = f"https://cn.bing.com/search?q={quote_plus(self._keyword)}&qs=HS&sc=14-0&cvid=84A9D35E5B8048B9ACBA42B34C014EBD&sp=1&lq=0&FPIG=A589135231594C76937DBACF703BDCDD&FPIG=3C7539F7D66847C99875A2A3FD6DDFAC&first=5&FORM=BESBTB&ensearch=1"
        self.blacklist = [
            'https://baike.baidu.com',
            'https://zhidao.baidu.com',
            'https://baijiahao.baidu.com',
            'https://wk.baidu.com',
            'https://m.sohu.com',
            'https://zhuanlan.zhihu.com',
            'https://mp.weixin.qq.com',
            'https://baijiahao.baidu.com',
            'https://www.zhihu.com',
            'https://m.ximalaya.com',
            'https://finance.sina.cn'

        ]
        self.init_page = 1

    def fetch(self):
        self._url = f"https://cn.bing.com/search?q={quote_plus(self._keyword)}&qs=HS&sc=14-0&cvid=84A9D35E5B8048B9ACBA42B34C014EBD&sp=1&lq=0&FPIG=A589135231594C76937DBACF703BDCDD&FPIG=3C7539F7D66847C99875A2A3FD6DDFAC&first={self.init_page}&FORM=BESBTB&ensearch=1"
        super().fetch()
        self.init_page += 10

    def parse(self):
        if self._response is not None:
            print(f"正在从 Bing解析 {self._keyword} 的URL...")
            soup = BeautifulSoup(self._response.text, 'html.parser')
            res = soup.find_all('li', class_="b_algo")
            for i in res:
                try:
                    p_ele = i.find('div', class_="b_attribution")
                    siteurl_p = p_ele.find("cite").get_text()
                    siteurl = siteurl_p.split('›')[0].strip()
                    self._results.append(siteurl)
                except:
                    continue
            self._result_set.update(self._results)
            self._result_set -= set(self.blacklist)
            self._results.clear()
        else:
            print("Request Error!Can't find any request resqponse")
