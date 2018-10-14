import requests

url = "http://a4c5f33bde894d07baca02412573e7ec47e5b01cd43d4c69.game.ichunqiu.com/?value[]=ea"

al = ['abcdefghijklmnopqrstuvwxyz']

s = requests.session()

r = s.get(url)
print r.content

#for i in range(20):
    #url = "http://a4c5f33bde894d07baca02412573e7ec47e5b01cd43d4c69.game.ichunqiu.com/?value[]=" + r.content[0:2]
    #r = s.get(url)
    #print r.content