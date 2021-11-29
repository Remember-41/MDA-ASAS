# Strategy1: Back-translation
# 利用双向翻译，将dataset1扩充到datasetByS1
import json
import requests
import os


# 实现翻译函数
# 利用有道词典api，将问题和答案翻译成中文，再翻译回英文以获得datasetByS1（原文是翻译为日语和百度翻译）
def translate(word):
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null'
    # key字典是发送给有道词典服务器的内容
    key = {
        'type': "AUTO",
        'i': word,
        "doctype": "json",
        "version": "2.1",
        "keyform": "fanyi.web",
        "ue": "UTF-8",
        "action": "FY_BY_CLICKBUTTON",
        "typoResult": "true"
    }
    response = requests.post(url, data=key)
    if response.status_code == 200:
        list_trans = response.text
        result = json.loads(list_trans)
        # 出于测试考虑，限制问题和答案控制在两句话
        # if len(result['translateResult'][0]['tgt']) != 1:
        #     return result['translateResult'][0][0]['tgt'] + " " + result['translateResult'][0][1]['tgt']
        # else:
        #     return result['translateResult'][0][0]['tgt']
        try:
            return result['translateResult'][0][0]['tgt'] + " " + result['translateResult'][0][1]['tgt']
        except IndexError:
            return result['translateResult'][0][0]['tgt']

    else:
        print("有道词典调用失败")
        return None


# word = input("Please input your word or sentence:")
# list_trans = translate(word)
# # 将返回的结果加载成json格式
# result = json.loads(list_trans)
# print(result['translateResult'][0][0]['tgt'])

# word = "水被蒸发，留下盐。"
# print(translate(word))

if not os.path.exists("datasetByS1"):
    os.mkdir("datasetByS1")

# 将dataset1的内容双向翻译得到datasetByS1
with open("dataset1/question", 'r') as f1:
    with open("datasetByS1/question", 'w') as f2:
        f2.write(translate(translate(f1.read())))
        f1.close()
        f2.close()
with open("dataset1/reference answer", 'r') as f1:
    with open("datasetByS1/reference answer", 'w') as f2:
        f2.write(translate(translate(f1.read())))
        f1.close()
        f2.close()
with open("dataset1/student answer", 'r') as f1:
    with open("datasetByS1/student answer", 'w') as f2:
        f2.write(translate(translate(f1.read())))
        f1.close()
        f2.close()
