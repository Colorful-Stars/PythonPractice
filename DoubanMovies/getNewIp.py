import requests
import time
from bs4 import BeautifulSoup
import random

def getNewIp(num):

	f = open('host2.txt','a+',encoding=('utf-8'))
	j = 0
	UA_list = [
		        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
		        "Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_2 like Mac OS X) App leWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D257 Safari/9537.53",
		        "Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13",
		        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ;  QIHU 360EE)",
		        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; Maxthon/3.0)",
		        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
		        "Mozilla/5.0 (Macintosh; U; IntelMac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1Safari/534.50",
		        "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0"]
	header = {'User-Agent': random.choice(UA_list)}
	for i in range(1, num + 1):
		url = 'http://www.kuaidaili.com/free/inha/%s/'%(i)
		r = requests.get(url,headers=header,timeout=30)
		soup = BeautifulSoup(r.text, 'html.parser')
		context = soup.find_all('tr')
		# print(context)
		for con in context:
			try:
				demo = BeautifulSoup(str(con),'html.parser')
				ip = demo.find(name='td',attrs={'data-title':'IP'}).get_text()
				port = demo.find(name='td',attrs={'data-title':'PORT'}).get_text()
				Ipport = ip + ':' + port + '\n'
				print(Ipport)
				f.write(Ipport)
				j=j+1
				print('获得%s个IP地址'%(j))
			except:
				print('No Ip!')
		time.sleep(random.uniform(1,2.3))
	f.close()

getNewIp(500)
