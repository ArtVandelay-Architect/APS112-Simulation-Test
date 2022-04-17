import pandas as pd
from onfleet import Onfleet
import googlemaps
from datetime import datetime
import subprocess
import threading
import time
#APS112FTW

def cleanString(st):
    q = False
    for i in range(len(st)):
        if (st == "("):
            q = True
        if (st == ")"):
            q = False
            st[i] = " "
        if (q):
            st[i] = " "
    return (st.lower()).strip()

def getTime(st): #String of form xxhr xxmin
    hrs = 0
    mins = 0
    s = st.split(" ")
    if (len(s) == 2):
        for h in s[0]:
            if (ord(h)<58):
                hrs*=10
                hrs+=int(h)
        for h in s[1]:
            if (ord(h)<58):
                mins*=10
                mins+=int(h)
    else:
        for h in s[0]:
            if (ord(h)<58):
                mins*=10
                mins+=int(h)       
    return hrs*3600 + mins * 60

def startOpti():
    subprocess.call([r"F:\Programs\APS112\ahk.bat"])

startIndex = 5793#7364

ap = Onfleet(api_key = "111c0076f298f8a90adfe86c5e33571c")
gmaps = googlemaps.Client(key='AIzaSyCrQIO8NlrMYuNgLoIm_XhjIOtXX1jKMUM')

taskC = 0 #task count
totals = []
tlist = []
with open("total.txt","r") as file:
    for line in file.readlines():
        line = line.split(",")
        totals.append(tuple(line))

df = pd.read_excel("./Orders.xlsx")
df.head(3)
raw = df[['ID','Add','Zip','Mat','Date']]
odate = raw['Date'][startIndex]


print("\nProcessing date: ",odate,"-----------------")

for i in range(startIndex,len(raw)):

    date = raw['Date'][i]
    
    
    if ((date != odate) or (taskC == 160)):
        print("Uploading finished, Optimising...")
        odate = date
        taskC = 0
        
        while True:
            try:
                opt = threading.Thread(target = startOpti)
                opt.start()
                t1 = input('optimal time1: ')
                t1 = getTime(t1)
                break
            except:
                opt.join()
                subprocess.call([r"F:\Programs\APS112\ahkreset.bat"])
        

        
        t2 = getTime(input('optimal time2: '))
        t3 = getTime(input('optimal time3: '))
        t4 = getTime(input('optimal time4: '))
        opt.join()
        if (t4 == t3):
            t4 = getTime(input('Retry: optimal time4: '))
        
        totals.append((t1,t2,t3,t4))

        with open("total.txt","a") as file:
            file.write("\n%d,%d,%d,%d"%(t1,t2,t3,t4))

        time.sleep(30)
        print("Calculation complete, deleting")
        
        for t in tlist:
            ap.tasks.deleteOne(id=t)

            
        tlist = []

        print("Resetting the system")
        subprocess.call([r"F:\Programs\APS112\ahkreset.bat"])
        
        print("\nProcessing date: ",date,"-----------------")
        
    print("Uploading ",i, ";",taskC)
    
    location = raw['Add'][i] + ', ' + raw['Zip'][i] + ', Canada'
    location = cleanString(location)
    if not ("799 islington" in location):
        dest = {"address":{"unparsed":location},"notes":str(raw['ID'][i])}
        bdy = {'destination':dest,
                'recipients':[{'name':'John Smith','phone':'17058062120',"notes":str(raw['ID'][i])}],                
                'serviceTime':5}
        try:
            t = ap.tasks.create(body=bdy)
        except:
            print("Process failed, ID:",str(raw['ID'][i]))
            continue
        tlist.append(t['id'])

    taskC += 1
        
#'autoAssign':{'mode':'load','maxAssignedTaskCount':40},



