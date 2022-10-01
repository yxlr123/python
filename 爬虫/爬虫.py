import json
import requests
url="https://cn.bing.com/ttranslatev3?isVertical=1&&IG=ED0206E205E2433A9D478DB419F3CC7F&IID=translator.5028.2"
headers = {
        'user-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36'
        }
word = input("请输入要翻译的内容").strip() #去除首尾的空格


if 'A' <=word[0]<='Z' or 'a'<=word[0]<='z':
    to = 'zh-Hans'
else:
    to = 'en'
formdata={
        'fromLang': 'auto-detect',
        'to':to,
        'text': word
    }

try:
    r = requests.post(url,data=formdata,headers=headers)

    print('r.status_code: ',r.status_code)
    r.raise_for_status()
    r.encoding =r.apparent_encoding
    data=json.loads(r.text)
    result=data[0]['translations'][0]['text']
    print(result)
except Exception as e:
    print("Error", e)

