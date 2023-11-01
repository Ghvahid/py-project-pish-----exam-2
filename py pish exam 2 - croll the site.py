import requests
from bs4 import BeautifulSoup
import csv

file = open("VarzeshNews.csv", "w", encoding="UTF-8", newline="")
writer = csv.writer(file)

list_all = []
selected_news_code = 1976282
for i in range(selected_news_code,selected_news_code+1000):
    inner_list = []
    url = f"https://www.varzesh3.com/news/{i}"
    res = requests.get(url).text
    res_b = BeautifulSoup(res , "html.parser")
    print(i)
    all_title = res_b.find("div", class_ = "news-detail-text")
    title = str(all_title.find("h1", class_="headline")).replace('<h1 class="headline">', '').replace("</h1>","")
    inner_list.append(title)
    # print("title : ",title)


    view = int(float(str(all_title.find("div", class_ = "news-info")).split("<span>")[3].replace("| </span>","").replace(" بازدید", "").replace("K",""))*1000)
    inner_list.append(view)
    # print("view : ",view)


    all_tags = str(res_b.find("div", class_ = "tags tags-news").find_all("span")).replace("<span>","").replace("</span>","").replace("[","").replace("]","")
    inner_list.append(all_tags)
    # print("tags for this news: ",all_tags)

    list_all.append(inner_list)


writer.writerow(['title', 'view', 'tags'])
writer.writerows(list_all)
file.close()

# print(list_all)

