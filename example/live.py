import sys
import time
import requests
from bs4 import BeautifulSoup as bs
from halo import Halo

spinner = Halo(text='Fetching Live Score', color='green', spinner='hamburger')
url_data = "https://www.cricbuzz.com/cricket-match/live-scores/"
recent_data = "https://www.cricbuzz.com/cricket-match/live-scores/recent-matches"

try:

    spinner.start()
    time.sleep(1)
    spinner.stop()
    r = requests.get(url_data)
    soup = bs(r.content, 'html.parser')
    div = soup.find(
        "div", attrs={"ng-show": "active_match_type == 'international-tab'"})

    matches = div.find_all(class_="cb-mtch-lst cb-col cb-col-100 cb-tms-itm")
    for match in matches:
        team_names = match.find("h3").text.strip().replace(",", "")
        status = match.find(
            "div", attrs={"class": "cb-text-live"}).text.strip()
        score = match.find(
            "div", attrs={"style": "display:inline-block; width:140px"}).text.strip()
        team_one = match.find_all(
            "div", attrs={"class": "cb-ovr-flo cb-hmscg-tm-nm"})[0].text.strip()
        team_two = match.find_all(
            "div", attrs={"class": "cb-ovr-flo cb-hmscg-tm-nm"})[1].text.strip()

        print("\n")
        print(">", team_names, "-", status, "\n")
        print("score: ", score, "\n")

except IndexError:
    spinner.stop()
    r = requests.get(recent_data)
    soup = bs(r.content, 'html.parser')
    div = soup.find(
        "div", attrs={"ng-show": "active_match_type == 'international-tab'"})

    matches = div.find_all(class_="cb-mtch-lst cb-col cb-col-100 cb-tms-itm")
    for match in matches:
        team_names = match.find("h3").text.strip().replace(",", "")
        status = match.find(
            "div", attrs={"class": "cb-text-complete"}).text.strip()
        print("\n")
        print(">", team_names, "-", status, "\n")
except AttributeError:
    spinner.stop()
    r = requests.get(recent_data)
    soup = bs(r.content, 'html.parser')
    div = soup.find(
        "div", attrs={"ng-show": "active_match_type == 'international-tab'"})

    matches = div.find_all(class_="cb-mtch-lst cb-col cb-col-100 cb-tms-itm")
    for match in matches:
        team_names = match.find("h3").text.strip().replace(",", "")
        status = match.find(
            "div", attrs={"class": "cb-text-complete"}).text.strip()
        print("\n")
        print(">", team_names, "-", status, "\n")
except requests.ConnectionError as e:
    spinner.stop()
    print("OOPS!! Connection Error")
except requests.Timeout as e:
    spinner.stop()
    print("OOPS!! Timeout Error")
except requests.RequestException as e:
    spinner.stop()
    print("API Error")
except (KeyboardInterrupt, SystemExit):
    spinner.stop()
    print("i am quitting")
