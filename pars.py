import requests
from bs4 import BeautifulSoup
import json
import csv
import random
from time import sleep
headers = {
	'accept' : '*/*',
	"user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.174 YaBrowser/22.1.4.840 Yowser/2.5 Safari/537.36"
}
baza = {}
sex = 'света'

def find_sex(sex): #поиск видео и время видео
	url = 'https://www.xvideos.com/tags/s:rating/'+ str(sex)
	req = requests.get(url)
	src = req.text
	soup = BeautifulSoup(src, 'lxml')
	top = soup.find(class_='mozaique cust-nb-cols').find_all('div')
	top1,views,time = [],[],[]
	for i in top:
		
		if i.get('id') != None: #проверка на пустоту

			top1.append(i.find('a').get('href')) 
			src1 = 'https://www.xvideos.com'+str(i)
			soup1 = BeautifulSoup(src1,'lxml')
			time.append(soup1.find('span',class_='duration').text)
			# views.append(soup1.find("div", {"id": "v-views"}))
			
			if len(top1) >=3:
				break
	return[top1, time]
	
	


def views(x):
	url = str('https://www.xvideos.com'+ str(x)) #принимает номер видео и пределывает в ссылку
	req = requests.get(url) #parsing
	src = req.text
	soup = BeautifulSoup(src, 'lxml')
	views = soup.find('div', id = 'v-views').find(class_='mobile-hide').text #ищет просмотры и выводит в текст
	return[views]

find = find_sex(sex)[0]
time = find_sex(sex)[1]

def vivod(find,time):# вывод
	for i in range(len(find)):
		temp = views(find_sex(find)[0][i])

		print (f'Top{i + 1}')
		print (f'https://www.xvideos.com{find[i]}')
		print (f'Длительность: {time[i]}')
		print (" ".join(reversed(temp)))
def add_pers(id1,name):
	
	with open('baza.json','r') as f:
		baza = json.load(f)
		for i in list(baza.items()):
			if id1 == i:
				print('yes')
			else:
				baza[id1]={}
				baza[id1]['name']=name
				with open("baza.json",'w') as file:
					json.dump(baza,file,indent=4)

def add_firstname(id1,firstname):
	with open('baza.json','r') as f:
		baza = json.load(f)
		for i in baza:
			if id1 == i:
				baza[i]['firstname']= firstname
				with open("baza.json",'w') as file:
					json.dump(baza,file,indent=4)

def add_request(id1,request,time):
	with open('baza.json','r') as f:
		baza = json.load(f)
		for i in baza:
			if id1 == i:
				try:
					len_requests = len(baza[i]['requests'])
					baza[i]['requests'][f'request{len_requests+1}'] = [f'Request : {request}',f'Time : {time}']
					# baza[i] = {'requests':[]}
					# baza[i]['requests']['request'] = [request, time]
					with open("baza.json",'w') as file:
						json.dump(baza,file,indent=4)
					
				except:
					baza[i]['requests'] = {'request1':[f'Request : {request}',f'Time : {time}']}
					# baza[i]['requests1'] = [request, time]
					with open("baza.json",'w') as file:
						json.dump(baza,file,indent=4)

def find_request(id1):
	with open('baza.json','r') as f:
		baza = json.load(f)
		len_requests = len(baza[id1]['requests'])
		for i in range(1,len_requests+1):
			print (baza[id1]['requests'][f'request{i}'])




name = 'valek2'
id1= '41421'
firstname = 'stokozov231'
request ='gay porno'
time = '09.03.2022 24:33'
vivod(find,time)

