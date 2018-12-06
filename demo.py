import gc
import pandas as pd
from tqdm import tqdm_notebook
from retry import retry
from aip import AipImageCensor, AipNlp

class BaiduAntiSpam(object):
    def __init__(self, api):
        """
        :param api: ['15052846', 'SiU9AAGaZn2Zja7d8iSVqce5', 'P6NZ07ROvKTXFnSlDMmH4hf1smOxbfAA']
        """
        self.api = api
        self.client = AipImageCensor(*self.api)

    @retry(tries=3, delay=2)
    def anti_spam(self, text):
        _ = self.client.antiSpam(text)
        _['log_id'] = text
        return _
    
    def get_result(self, file, corpus):
        with open(file, 'a') as f:
            for s in tqdm_notebook(corpus):
                res = self.anti_spam(s)
                f.writelines("%s\n" % res)
