import json
import urllib

import requests


import json
import urllib

import requests


class BaiDuNLP(object):
    def __init__(self, api_key='B0cphM43tmxUyR4YcGMvCn1X', secret_key='SjRpd3Fg6aaX9B5KQD796IDHgvFMrURb'):
        self.access_token = None
        self._get_access_token(api_key, secret_key)

    def predict(self, text, api_url):
        """
        api_url = 'https://aip.baidubce.com/rpc/2.0/kg/v1/cognitive/entity_annotation?charset=UTF-8&access_token='
        api = BaiDuNLP()
        api.predict('周杰伦', api_url)
        """
        url = api_url + self.access_token
        
        # the input is json format
        input_text = {'data': text}
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
