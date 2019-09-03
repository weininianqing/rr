from urllib import parse,request
import json

url = 'https://fanyi.baidu.com/sug'
kw = input("请输入需要翻译的词语:")
data = {
    'kw' : kw

}
data = parse.urlencode(data).encode()

rsq = request.urlopen(url,data=data)

json_data = rsq.read().decode()

#print(json_data)

json_data = json.loads(json_data)

for i in json_data['data']:
    print(i['k'],"-->",i['v'])
#print(json_data)



