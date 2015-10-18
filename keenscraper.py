#scrape links on keens update page
import urllib
import webbrowser
import requests
import time
from bs4 import BeautifulSoup
baseurl = 'http://forums.keenswh.com/forums/change-log.326211/'
useurl = 'http://forums.keenswh.com/'
count = 0
old = True

def checker():
  result = requests.get(baseurl)
  c = result.content


  soup = BeautifulSoup(c, 'html.parser')
  samples = soup.find_all("a")
  a = []
  for link in soup.find_all('a'):
    a.append(link.get('href'))
  
  b = []

  for link in xrange(len(a)):
    if 'threads' in str(a[link]):
      b.append(a[link])

  d = []
  z = 0
  y  = 0 
  for i in xrange(len(b)):
    if 'page' not in str(b[i]):
      d.append(b[i])
      y += 1
    else:
      z += 1
  print z
  print y
  #print d[0]
  
#give url for first entry
  url = useurl + str(d[0])

  #print url
  if "104" not in url:
    old = False
    webbrowser.open(url)
    return False
  else:
    print "still on update 104"
    return True
	
    
def main():
  count = 0
  old = True
  while old:
    old = checker()
    
    #print str(count) + " minutes have elapsed"
   # count += 1
    if old:
      time.sleep(300)
    else:
      break
  
if __name__ == "__main__":
  main()