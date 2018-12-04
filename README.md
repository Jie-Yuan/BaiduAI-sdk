## 说明书

### nlp
```python
from aip import AipNlp, 
APP_ID = '11515591'
API_KEY = 'MnLk1hDXdIzGSqgudr3190yB'
SECRET_KEY = 'FXseFlaYU4cFiq1x1NfWAiVEyWRPdGVG '
client = AipNlp(APP_ID, API_KEY, SECRET_KEY)
```
```
client.commentTag # 评论观点抽取
client.depParser # 依存句法分析
client.dnnlm # 中文DNN语言模型接口用于输出切词结果并给出每个词在句子中的概率值,判断一句话是否符合语言表达习惯（ppl越小越好）。
client.ecnet # 文本纠错 未开放
client.emotion # 对话情绪识别接口  pessimistic neutral  optimistic
client.keyword # 文章标签
client.lexer # 词法分析
client.lexerCustom
client.sentimentClassify # 情感倾向分析 0:负向，1:中性，2:正向
client.simnet # 短文本相似度
client.topic # 文章分类：首批支持娱乐、体育、科技等26个主流内容类型，为文章聚类、文本内容分析等应用提供基础技术支持

client.wordEmbedding # 词向量
client.wordSimEmbedding # 词义相似度

client.post
client.setConnectionTimeoutInMillis
```


- 内容审核
```
from aip import AipImageCensor
APP_ID = "14910672"
API_KEY = "quiV9tZGK9ojl1CyU1yGPLm7"
SECRET_KEY = "7xglWFskKwu9bwxt98IDHOaeQeu466sT"
client = AipImageCensor(APP_ID, API_KEY, SECRET_KEY)
```
