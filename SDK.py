from aip import AipNlp
APP_ID = '11515591'
API_KEY = 'MnLk1hDXdIzGSqgudr3190yB'
SECRET_KEY = 'FXseFlaYU4cFiq1x1NfWAiVEyWRPdGVG '

client = AipNlp(APP_ID, API_KEY, SECRET_KEY)
client.wordSimEmbedding('知道', '了解')
