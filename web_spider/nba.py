from bs4 import BeautifulSoup
import pandas as pd
import requests as re
url = 'https://www.ptt.cc/bbs/NBA/index.html' 
r = re.get(url)
# print(r) #200=ok
soup = BeautifulSoup(r.text, 'html.parser')

title = soup.find_all(class_ = 'title')
author = soup.find_all(class_ = 'author')
date = soup.find_all(class_ = 'date') #

titles = []
authors = []
dates = []

for t, a, d in zip(title, author, date):
    titles.append(t.text)
    authors.append(a.text)
    dates.append(d.text)
dict = {
    '標題':titles,
    '作者':authors,
    '日期':dates
}
df = pd.DataFrame(dict)
print(df.head(5))

df.to_csv('nba.csv', encoding = 'utf_8_sig')