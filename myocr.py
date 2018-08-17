from aip import AipOcr
APP_ID = '11516632'
API_KEY = 'gAw0HlllOyi9sQcZulvPlmSB'
SECRET_KEY = 'RlseXLG6SGCxXAYCbliTkCZF7KOxRMZA '

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)


""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

image = get_file_content('./zc.png')

""" 调用通用文字识别, 图片参数为本地图片 """
client.basicGeneral(image);

""" 如果有可选参数 """
options = {}
options["language_type"] = "CHN_ENG"
options["detect_direction"] = "true"
options["detect_language"] = "true"
options["probability"] = "true"

""" 带参数调用通用文字识别, 图片参数为本地图片 """
client.basicGeneral(image, options)
