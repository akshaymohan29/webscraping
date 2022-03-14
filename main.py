from bs4 import BeautifulSoup
import requests
import lxml
responce=requests.get(url="https://web.archive.org/web/20200518073855/https:"
                          "//www.empireonline.com/movies/features/best-movies-2/")
data=responce.text
# print(data)

soup=BeautifulSoup(data,'lxml')
title=soup.find_all(name="h3", class_="title")

# print(title)

text=[i.getText() for i in title]
# print(len(text))
#movie=text[::-1]#to reverse
#or use
out=[]
for i in range(len(text)-1,-1,-1):
    out.append(text[i])
    print(out)
    with open("text.txt","w") as t :
     for i in out:
      t.write(f"{i}\n")