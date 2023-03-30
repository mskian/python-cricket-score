import time
import requests
from bs4 import BeautifulSoup as bs
from halo import Halo

# using it for Testing, Development and Github Workflow

spinner = Halo(text='Fetching Live Score', color='green', spinner='hamburger')
url_data = "https://www.cricbuzz.com/live-cricket-scores/60042/aus-vs-ind-3rd-odi-australia-tour-of-india-2023"

try:

    spinner.start()
    time.sleep(2)
    spinner.stop()
    r = requests.get(url_data)
    soup = bs(r.content, 'html.parser')
    update = soup.find(
        "div", attrs={"class": "cb-text-inprogress"}).text.strip()
    live_score = soup.find(
        "span", attrs={"class": "cb-font-20 text-bold"}).text.strip()
    title = soup.find(
        "h1", attrs={"class": "cb-nav-hdr cb-font-18 line-ht24"}).text.strip().replace(", Commentary", "")
    run_rate = soup.find_all(
        "span", attrs={"class": "cb-font-12 cb-text-gray"})[0].text.strip()
    batter_one = soup.find_all(
        "div", attrs={"class": "cb-col cb-col-50"})[1].text.strip()
    batter_two = soup.find_all(
        "div", attrs={"class": "cb-col cb-col-50"})[2].text.strip()
    batter_one_run = soup.find_all(
        "div", attrs={"class": "cb-col cb-col-10 ab text-right"})[0].text.strip()
    batter_two_run = soup.find_all(
        "div", attrs={"class": "cb-col cb-col-10 ab text-right"})[2].text.strip()
    batter_one_ball = soup.find_all(
        "div", attrs={"class": "cb-col cb-col-10 ab text-right"})[1].text.strip()
    batter_two_ball = soup.find_all(
        "div", attrs={"class": "cb-col cb-col-10 ab text-right"})[3].text.strip()
    batter_one_sr = soup.find_all(
        "div", attrs={"class": "cb-col cb-col-14 ab text-right"})[0].text.strip()
    batter_two_sr = soup.find_all(
        "div", attrs={"class": "cb-col cb-col-14 ab text-right"})[1].text.strip()
    bowler_one = soup.find_all(
        "div", attrs={"class": "cb-col cb-col-50"})[4].text.strip()
    bowler_two = soup.find_all(
        "div", attrs={"class": "cb-col cb-col-50"})[5].text.strip()
    bowler_one_over = soup.find_all(
        "div", attrs={"class": "cb-col cb-col-10 text-right"})[4].text.strip()
    bowler_two_over = soup.find_all(
        "div", attrs={"class": "cb-col cb-col-10 text-right"})[6].text.strip()
    bowler_one_run = soup.find_all(
        "div", attrs={"class": "cb-col cb-col-10 text-right"})[5].text.strip()
    bowler_two_run = soup.find_all(
        "div", attrs={"class": "cb-col cb-col-10 text-right"})[7].text.strip()
    bowler_one_eco = soup.find_all(
        "div", attrs={"class": "cb-col cb-col-14 text-right"})[2].text.strip()
    bowler_two_eco = soup.find_all(
        "div", attrs={"class": "cb-col cb-col-14 text-right"})[3].text.strip()
    bowler_one_wicket = soup.find_all(
        "div", attrs={"class": "cb-col cb-col-8 text-right"})[5].text.strip()
    bowler_two_wicket = soup.find_all(
        "div", attrs={"class": "cb-col cb-col-8 text-right"})[7].text.strip()

    print(title)
    print("Current Score:" + live_score)
    print("Run Rate:", run_rate)
    print(
        f"Current Batsman - {batter_one}: {batter_one_run}({batter_one_ball}) - SR: {batter_one_sr}")
    print(
        f"Other Batsman - {batter_two}: {batter_two_run}({batter_two_ball}) - SR: {batter_two_sr}")
    print(
        f"Current Bowler - {bowler_one} - Overs: {bowler_one_over} - Runs: {bowler_one_run} - Wicket: {bowler_one_wicket} - ECO: {bowler_one_eco}")
    print(
        f"other Bowler - {bowler_two} - overs: {bowler_two_over} - Runs: {bowler_two_run} - Wicket: {bowler_two_wicket} ECO: {bowler_two_eco}")
    print("Update: " + update)

except IndexError:
    spinner.stop()
    get_mobile_view = url_data.replace("www", "m")
    r = requests.get(get_mobile_view)
    soup = bs(r.content, 'html.parser')
    update = soup.find("div", attrs={"class": "cbz-ui-status"}).text.strip() if soup.find("div", attrs={
        "class": "cbz-ui-status"}) else 'Live Score Data Updating Re-check After Few mins or Innings break'
    print(update)
except AttributeError:
    spinner.stop()
    get_mobile_view = url_data.replace("www", "m")
    r = requests.get(get_mobile_view)
    soup = bs(r.content, 'html.parser')
    update = soup.find("div", attrs={"class": "cbz-ui-status"}).text.strip() if soup.find("div", attrs={
        "class": "cbz-ui-status"}) else 'Live Score Data Updating Re-check After Few mins or Innings break'
    print(update)
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
