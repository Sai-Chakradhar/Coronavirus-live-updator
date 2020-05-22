from bs4 import BeautifulSoup as bf
import requests
import time
from boltiot import Bolt
import ssl
a = list()
#———————-Algorithum  to compare the values every 10 min—————





def checking1(x,count):
  a.insert(count,x)
  if count == 1:
    print(a)
    if(a[1]-a[0] > 10):
      a.clear()
      return(1)
    else:
      a.clear()
      return(0)
  
    
    
  #—————————getting the value from website————————


def getting_value(): #getting the value from website
  y = ''
  html = requests.get("https://www.worldometers.info/coronavirus/")
  soup = bp(html.text,'html.parser')
  tag = soup("span")
  Effected_people = tag[4].contents[0]
  for i in range(9):
    if i==1 or i==5:
      continue
    y = y + Effected_people[i]
  x = int(y)
  return(x)

#———————Execution starts from here————————————
Effected_people = getting_value()
apikey = input("Enter API Key")
Bolt_id = input("Enter the Bolt_ID")
device = Bolt(apikey,Bolt_id)
for i in range(1000):
  print(device.isOnline())
  response = device.serialBegin(9600)
  x = getting_value()
  z = checking1(x,0)
  response2 = device.serialWrite(x)
  print(response2)
  time.sleep(100)    #time.sleep(100) with delay for execution for 100 sec
  y = getting_value()
  z = checking1(y,1)
  response2 = device.serialWrite(y)
  if(z == 1):
    device.digitalWrite('0','HIGH')
    time.sleep(5)
    device.digitalWrite('0','LOW')
