# -*- coding: utf-8 -*-
from app   import app
from app   import mongo
#from app   import base

#from app   import mpcollection
from flask import request, jsonify, url_for,redirect
from flask import render_template,flash, make_response, session
from datetime import datetime
import json 
#import pymongo
import time
import os

from subprocess import check_call

import datetime

#from bson.objectid import ObjectId

def sayl(sst): # local ttts
    os.system("echo " + sst + " | RHVoice-client -s Aleksandr+CLB | aplay -q")



@app.route('/')
def index(): # начальная меню панель 
    
    ff=mongo.db.signals.find({}).limit(50).sort([("seton", -1)])

    # если первй cancel
    d1='none'
    for f in ff:
        if f["type"]=="canceling": 
            break
        if "setto" in f:
            d1=f['setto']

    return render_template('bt4index.html',ttt=d1)
    #return render_template('index.html')


@app.route('/api/off/<tm>')
def apioff(tm): # начальная меню панель
    d1 = datetime.datetime.now() + datetime.timedelta(minutes=int(tm))

    t1 = datetime.datetime.now() 

    print("shutdown +"+tm)
    ##return render_template('btindex.html',ttt=d1)
    # vremay no , + 
    # type 

    mongo.db.signals.insert_one({'type':"shutdown",'seton':t1,'setto':d1 })

    #sayl("Выключение через "+tm+" минут") 
    
    #check_call(["sudo /sbin/shutdown", "+"+tm])
    #check_call(["/bin/sudo","/home/chuser/sites/weboff/app/off.sh"])
    #check_call(["/bin/sudo","/sbin/shutdown +"+tm])
    os.system("/bin/whoami")
    #os.system("/home/chuser/sites/weboff/app/say.sh")
    os.system("/bin/sudo /home/chuser/sites/weboff/app/off.sh +"+tm )
    
    if tm=="0":
        os.system("/bin/sudo /home/chuser/sites/weboff/app/offnow.sh ")
    

    #os.system("sudo /sbin/shu " )
    #os.system("/bin/sudo ","/sbin/shutdown +"+tm)
    
    
    return redirect(url_for('index',ttt=d1))


    #return render_template('bt4index.html',ttt=d1)
        

    #return render_template('gosh.html',ttt=d1)


@app.route('/api/rb')
def apirb():
    t1 = datetime.datetime.now()
    mongo.db.signals.insert_one({'type':"reboot",'seton':t1 })

    os.system("/bin/sudo /home/chuser/sites/weboff/app/rb.sh ")
    
    return render_template('reboot.html',ttt=dq)


@app.route('/api/csh')
def apicsh():
    os.system("/bin/sudo /home/chuser/sites/weboff/app/csh.sh ")
    t1 = datetime.datetime.now()
    mongo.db.signals.insert_one({'type':"canceling",'seton':t1 })
    return render_template('bt4index.html')

@app.route('/log')
def getlog():
    ff=mongo.db.signals.find({}).limit(50).sort([("seton", -1)])
    log=[]
    for f in ff:
        log.append({"type":f["type"],
            'seton':"-" if "seton" not in f else f['seton'],
            'setto':"-" if "setto" not in f else f['setto'] })

    return render_template('log.html',log=log)




# sudo visudo
 
# %group_name ALL=(ALL) NOPASSWD: /sbin/poweroff, /sbin/reboot, /sbin/shutdown 
# user_name ALL=(ALL) NOPASSWD: /sbin/poweroff, /sbin/reboot, /sbin/shutdown

# Дизайн картинки шрифт иконки - стиль 
# нгникс уникорн 
# добавдление в базу выключения время
# еще бы добавить на включение запуск скрипта 
# на питоне и в окружении 






