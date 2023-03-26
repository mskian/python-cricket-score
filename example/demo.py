from bs4 import BeautifulSoup as bs
import requests

r = requests.get(
    'https://www.cricbuzz.com/live-cricket-scores/50165/vic-vs-wa-final-sheffield-shield-2022-23')
soup = bs(r.content, 'html.parser')
live_score = soup.find("span", attrs={"class": "cb-font-20 text-bold"}).text.strip(
) if soup.find("span", attrs={"class": "cb-font-20 text-bold"}) else 'Data Not Found'
toss = soup.find("div", attrs={"class": "cb-text-inprogress"}).text.strip(
) if soup.find("div", attrs={"class": "cb-text-inprogress"}) else 'Data Not Found'
title = soup.find("h1", attrs={
                  "class": "cb-nav-hdr cb-font-18 line-ht24"}).text.strip().replace(", Commentary", "")
run_rate = soup.find_all("span", attrs={"class": "cb-font-12 cb-text-gray"})[0].text.strip(
) if soup.find_all("span", attrs={"class": "cb-font-12 cb-text-gray"}) else 'Data Not Found'
batter_one = soup.find_all("div", attrs={"class": "cb-col cb-col-50"})[1].text.strip(
) if soup.find_all("div", attrs={"class": "cb-col cb-col-50"}) else 'Data Not Found'
batter_two = soup.find_all("div", attrs={"class": "cb-col cb-col-50"})[2].text.strip(
) if soup.find_all("div", attrs={"class": "cb-col cb-col-50"}) else 'Data Not Found'
bowler_one = soup.find_all("div", attrs={"class": "cb-col cb-col-50"})[4].text.strip(
) if soup.find_all("div", attrs={"class": "cb-col cb-col-50"}) else 'Data Not Found'
bowler_two = soup.find_all("div", attrs={"class": "cb-col cb-col-50"})[5].text.strip(
) if soup.find_all("div", attrs={"class": "cb-col cb-col-50"}) else 'Data Not Found'

print(toss)
print(live_score)
print(title)
print(run_rate)
print(batter_one)
print(batter_two)
print(bowler_one)
print(bowler_two)
