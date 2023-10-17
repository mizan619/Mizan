#----------------------------------------------------------------------------------------------------------
import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' 
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' 
M = '\x1b[1;91m' 
H = '\x1b[1;92m' 
K = '\x1b[1;93m' 
B = '\x1b[1;94m' 
U = '\x1b[1;95m' 
O = '\x1b[1;96m' 
N = '\x1b[0m'    
A = '\x1b[1;90m' 
BN = '\x1b[1;107m' 
BBL = '\x1b[1;106m' 
BP = '\x1b[1;105m' 
BB = '\x1b[1;104m' 
BK = '\x1b[1;103m' 
BH = '\x1b[1;102m' 
BM = '\x1b[1;101m' 
BA = '\x1b[1;100m' 
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today() 
loop = 0
oks = []
cps = []
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
 prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
 open('.prox.txt','w').write(prox)
except Exception as e:
 print('')
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
    a='Nokia'
    b=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    c=random.randrange(1, 99)
    d='/GoBrowser/'
    e='1.6.0.'
    f=random.randrange(1, 99)
    uaku2=(f'{a}{b}{c}{d}{e}{f}')
    ugen.append(uaku2)
    
def __init__(self):
        self.id = []
        self.ok = []
        self.cp = []
        self.loop = 0
        
logo = ("""\033[1;37m
  🤤       ___|\  /|___🤤
          /                        \         😏    .. 
😏   /   /|(  *  ) (  *  )|\  \🔥
     /   /  |                  |  \   \
   /   /    |          💋   |    \   \
            /         .         \            🔥
    🔥 /       💋            \ 🔥
         |           \ı/           |     🔥
  🔥  |             |     💋    |  🔥      🔥
          \           |           /
            \         |         /      🔥
  🔥       |        |        |
              |        |        |         🔥🤤
              ◢🌸🌸◣🦜◢🌸🌸◣
🌸DABIT SULTAN ,,🌸
🌸DABIT SULTAN  🌸
 ◥🌸,ATIK ATIK,, 🌸◤
   ◥🌸,,ATIK,🌸◤  
    ◥,,বন্ধু,,,◤  
    ❣️
              
        
\x1b[38;5;196m╔═════════════╗  \033[37;1m🦋⃟𝗕𝗢𝗦𝗦✮⃝ ATIK𝄟⃝  \033[38;5;46m╔══════════════════╗
\033[38;5;46m║[🔵]\x1b[38;5;196m𝐀𝐔𝐓𝐇𝐎𝐑   ║  \033[37;1m🦋⃟𝗕𝗢𝗦𝗦✮⃝ ATIK𝄟⃝  \033[38;5;46m║\033[38;5;46mATIK  ║
\033[38;5;46m║[🔵]\x1b[38;5;196m𝐅𝐀𝐂𝐄𝐁𝐎𝐎𝐊 ║  \033[37;1m🦋⃟𝗕𝗢𝗦𝗦✮⃝ ATIK𝄟⃝  \033[38;5;46m║\033[38;5;46mATIK VAI         ║
\033[38;5;46m║[🔵]\x1b[38;5;196m𝐖𝐇𝐀𝐓𝐒𝐀𝐏𝐏 ║  \033[37;1m🦋⃟𝗕𝗢𝗦𝗦✮⃝ ATIK𝄟⃝  \033[38;5;46m║\033[38;5;46m𝟎𝟏608032030       ║
\033[38;5;46m║[🔵]\x1b[38;5;196m𝐆𝐈𝐓𝐇𝐔𝐁   ║  \033[37;1m🦋⃟𝗕𝗢𝗦𝗦✮⃝ ATIK𝄟⃝  \033[38;5;46m║\033[38;5;46mATIKVAI07        ║
\033[38;5;46m║[🔵]\x1b[38;5;196m𝐓𝐄𝐋𝐄𝐆𝐑𝐀𝐌 ║  \033[37;1m🦋⃟𝗕𝗢𝗦𝗦✮⃝ ATIK𝄟⃝  \033[38;5;46m║\033[38;5;46m𝟎𝟏608032030       ║
\033[38;5;46m║[🔵]\x1b[38;5;196m𝐈𝐌𝐎      ║  \033[37;1m🦋⃟𝗕𝗢𝗦𝗦✮⃝ ATIK𝄟⃝  \033[38;5;46m║\033[38;5;46m𝟎𝟏608032030      ║
\033[38;5;46m║[🔵]\x1b[38;5;196m𝐅𝐑𝐎𝐌     ║  \033[37;1m🦋⃟𝗕𝗢𝗦𝗦✮⃝ ATIK𝄟⃝ \033[38;5;46m ║\033[38;5;46m𝐁𝐀𝐍𝐆𝐋𝐀𝐃𝐄𝐒𝐇        ║
\x1b[38;5;196m╚═════════════╝  \033[37;1m🦋⃟𝗕𝗢𝗦𝗦✮⃝ ATIK𝄟⃝  \033[38;5;46m╚══════════════════╝\033[00m\033[1;30m
\033[37;1m▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀""")

logo1 = ("""\033[1;37m
\x1b[38;5;196m╔═════════════╗  \033[37;1m🦋⃟𝗕𝗢𝗦𝗦✮⃝ ATIK𝄟⃝  \033[38;5;46m╔══════════════════╗
\033[38;5;46m║[🔵]\x1b[38;5;196m𝐀𝐔𝐓𝐇𝐎𝐑   ║  \033[37;1m🦋⃟𝗕𝗢𝗦𝗦✮⃝ ATIK𝄟⃝  \033[38;5;46m║\033[38;5;46mATIK  ║
\033[38;5;46m║[🔵]\x1b[38;5;196m𝐅𝐀𝐂𝐄𝐁𝐎𝐎𝐊 ║  \033[37;1m🦋⃟𝗕𝗢𝗦𝗦✮⃝ ATIK𝄟⃝  \033[38;5;46m║\033[38;5;46mATIK║
\033[38;5;46m║[🔵]\x1b[38;5;196m𝐖𝐇𝐀𝐓𝐒𝐀𝐏𝐏 ║  \033[37;1m🦋⃟𝗕𝗢𝗦𝗦✮⃝ ATIK𝄟⃝  \033[38;5;46m║\033[38;5;46m𝟎𝟏608032030║
\033[38;5;46m║[🔵]\x1b[38;5;196m𝐆𝐈𝐓𝐇𝐔𝐁   ║  \033[37;1m🦋⃟𝗕𝗢𝗦𝗦✮⃝ ATIK𝄟⃝  \033[38;5;46m║\033[38;5;46matik-lx   ║
\033[38;5;46m║[🔵]\x1b[38;5;196m𝐓𝐄𝐋𝐄𝐆𝐑𝐀𝐌 ║  \033[37;1m🦋⃟𝗕𝗢𝗦𝗦✮⃝ ATIK𝄟⃝  \033[38;5;46m║\033[38;5;46m𝟎𝟏608032030     ║
\033[38;5;46m║[🔵]\x1b[38;5;196m𝐈𝐌𝐎      ║  \033[37;1m🦋⃟𝗕𝗢𝗦𝗦✮⃝ ATIK𝄟⃝  \033[38;5;46m║\033[38;5;46m𝟎𝟏608032030    ║
\033[38;5;46m║[🔵]\x1b[38;5;196m𝐅𝐑𝐎𝐌     ║  \033[37;1m🦋⃟𝗕𝗢𝗦𝗦✮⃝ ATIK𝄟⃝ \033[38;5;46m ║\033[38;5;46m𝐁𝐀𝐍𝐆
