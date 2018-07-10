import json
import urllib

import requests


class BaiDuNLP(object):
    def __init__(self, api_key='MnLk1hDXdIzGSqgudr3190yB', secret_key='FXseFlaYU4cFiq1x1NfWAiVEyWRPdGVG'):
        self._get_access_token(api_key, secret_key)

    def get_api_prediction(self, text, api_url='/v1/lexer'):
        """http://ai.baidu.com/docs#/NLP-API/89828646
        api_url:
            /v1/lexer: 词法分析接口
            /v1/depparser: 依存句法分析接口
        """
        url = f'https://aip.baidubce.com/rpc/2.0/nlp{api_url}?charset=UTF-8&access_token=' + self.access_token
        
        # the input is json format
        input_text = {'text': text} # {'data': text}
        input_text = json.dumps(input_text)
        
        r = requests.post(url, data=input_text, headers={'Content-Type': 'application/json'})
        return r.json()

    def _get_access_token(self, api_key, secret_key):
        host = f'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={api_key}&client_secret={secret_key}'
        request = urllib.request.Request(host)
        request.add_header('Content-Type', 'application/json; charset=UTF-8')
        response = urllib.request.urlopen(request)
        content = response.read()
        self.access_token = json.loads(content)['access_token']
