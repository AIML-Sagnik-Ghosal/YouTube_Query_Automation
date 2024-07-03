from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import os
import datetime as dt
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)
topic=input()
driver.get("https://www.youtube.com/results?search_query="+topic.replace(' ','+'))
bs=driver.find_elements(By.TAG_NAME,"ytd-video-renderer")
d=pd.DataFrame(columns=['Query No','Query','Video No','Title','Views','Channel',
                        'Length','Upload Date','Video Link','Channel Link'])
i=0
if os.path.exists('Video.csv'):
    df=pd.read_csv("Video.csv")
    qn=df['Query No'][len(df)-1]
    vn=df['Video No'][len(df)-1]
else:
    qn=0
    vn=0
delay=15
for b in bs:
    try:
        myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CSS_SELECTOR, "badge-shape div")))
        time=b.find_element(By.CSS_SELECTOR, "badge-shape div").get_attribute('innerHTML')
        if len(time)<=10:
            d.loc[i, 'Query']=topic
            d.loc[i, 'Query No'] = qn+1
            d.loc[i,'Video No']=vn+i+1
            c=b.find_element(By.ID,"meta")
            l=c.text.split('\n')
            d.loc[i,'Title']=l[0].split('|')[0].split('-')[0].split('.')[0].strip()
            d.loc[i,'Views']=l[1].split(' ')[0]
            d.loc[i,'Upload Date']=l[2].split(' ')[0]+' '+l[2].split(' ')[1]
            d.loc[i,'Length']=time
            d.loc[i,'Video Link']=b.find_element(By.CSS_SELECTOR,"a#thumbnail").get_attribute('href')
            d.loc[i,'Channel Link']=b.find_element(By.CSS_SELECTOR, "a#channel-thumbnail").get_attribute('href')
            d.loc[i,'Channel']=b.find_element(By.CSS_SELECTOR, "div#channel-info").text
            i+=1
    except Exception as e:
        print("An error occured, please restart ")
print(d)
if os.path.exists('Video.csv'):
    d.to_csv('Video.csv',mode='a',index=False,header=False)
else:
    d.to_csv('Video.csv', index=False)

bs=driver.find_elements(By.TAG_NAME,"ytd-playlist-renderer")
d=pd.DataFrame(columns=['Query No','Query','Playlist No','Title','No of Videos','Views','Channel',
                        'Total Length','Avg Length','Last Upload Date','Playlist Link','Channel Link'])
i=0
if os.path.exists('Playlist.csv'):
    df=pd.read_csv("Playlist.csv")
    qn=df['Query No'][len(df)-1]
    vn=df['Playlist No'][len(df)-1]
else:
    qn=0
    vn=0
for b in bs:
    try:
        data=[]
        l=b.find_element(By.CSS_SELECTOR,"yt-formatted-string#view-more a")
        d.loc[i,'Playlist Link']=l.get_attribute('href')
        service = Service(executable_path="chromedriver.exe")
        driver1 = webdriver.Chrome(service=service)
        driver1.get(l.get_attribute('href'))
        bs = driver1.find_elements(By.CSS_SELECTOR, "badge-shape div")
        n=len(bs)
        plt = 0
        for b in bs:
            time = b.get_attribute('innerHTML').split(':')
            unit = [3600, 60, 1]
            tt = sum([l * u for l, u in list(zip(reversed(list(map(int, time))), reversed(unit)))])
            plt += tt
        bs = driver1.find_elements(By.CSS_SELECTOR, "div.metadata-wrapper yt-formatted-string")
        for b in bs:
            a = b.get_attribute('innerHTML')
            if len(a) > 0:
                if a[0] != '<':
                    data.append(a)
                elif a[1] == 'a':
                    data.append(b.find_element(By.TAG_NAME, 'a').get_attribute('href'))
                    data.append(b.find_element(By.TAG_NAME, 'a').get_attribute('innerHTML'))
                elif a[1] == 's':
                    data.append([i.get_attribute('innerHTML') for i in b.find_elements(By.TAG_NAME, 'span')])
        if not os.path.exists('play.html'):
            with open('play.html', 'w', encoding="utf-8") as f:
                f.write(driver.page_source)
        driver1.quit()
        d.loc[i,'Total Length']=str(dt.timedelta(seconds=plt))
        d.loc[i, 'Avg Length']=str(dt.timedelta(seconds=plt//n))
        d.loc[i,'Title']=data[0]
        d.loc[i, 'Channel Link'] = data[1]
        d.loc[i, 'Channel'] = data[2]
        d.loc[i, 'No of Videos'] = data[3][0]
        d.loc[i, 'Views'] = data[4].split(' ')[0]
        d.loc[i, 'Last Upload Date'] = data[5][1]
        d.loc[i, 'Query']=topic
        d.loc[i, 'Query No'] = qn+1
        d.loc[i,'Playlist No']=int(vn+i+1)
        i+=1
    except Exception as e:
        print("An error occured, please restart ")
print(d)
if os.path.exists('Playlist.csv'):
    d.to_csv('Playlist.csv',mode='a',index=False,header=False)
else:
    d.to_csv('Playlist.csv', index=False)
driver.quit()