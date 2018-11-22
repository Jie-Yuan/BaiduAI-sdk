import json
import urllib

import requests


import json
import urllib

import requests


class BaiDuNLP(object):
    def __init__(self, api, api_key, secret_key):
        """
        api = 'https://aip.baidubce.com/rpc/2.0/nlp/v1/lexer'
        api_key='MnLk1hDXdIzGSqgudr3190yB'
        secret_key='FXseFlaYU4cFiq1x1NfWAiVEyWRPdGVG'
        """
        self.api = api
        self._get_access_token(api_key, secret_key)
        self.url = self.api + '?charset=UTF-8&access_token=' + self.access_token
        
    def get_api_prediction(self, text):
        # the input is json format
        input_text = json.dumps({'text': text})
        r = requests.post(self.url, data=input_text, headers={'Content-Type': 'application/json'})
        return r.json()

    def _get_access_token(self, api_key, secret_key):
        host = f'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={api_key}&client_secret={secret_key}'
        request = urllib.request.Request(host)
        request.add_header('Content-Type', 'application/json; charset=UTF-8')
        response = urllib.request.urlopen(request)
        content = response.read()
        self.access_token = json.loads(content)['access_token']
        
