import time
import os
import requests
from bs4 import BeautifulSoup as bs
from halo import Halo
import yaml
from yaml.loader import SafeLoader

HOME = os.path.expanduser('~')
APP_NAME = 'python-cricket-score'
CONFIG_NAME = 'score'
GENERATE_APP = os.path.join(HOME, APP_NAME)
READ_DATA = os.path.join(HOME, APP_NAME, CONFIG_NAME + '.yaml')

spinner = Halo(text='Fetching Live Score', color='green', spinner='hamburger')

try:

    if not os.path.exists(GENERATE_APP):
        os.mkdir(GENERATE_APP)
        with open(os.path.join(GENERATE_APP, 'score.yaml'), 'w') as f:
            f.write("url: '<Update Current Live Match URL From Cricbuzz>'")
        print("App Directory ", APP_NAME, " Created ")
    else:

        with open(READ_DATA) as f:
            data = yaml.load(f, Loader=SafeLoader)
            url_data = data['url']

        spinner.start()
        time.sleep(2)
        spinner.stop()
        r = requests.get(url_data)
        soup = bs(r.content, 'html.parser')
        update = soup.find("div", attrs={"class": "cb-text-inprogress"}).text.strip(
        ) if soup.find("div", attrs={"class": "cb-text-inprogress"}) else 'Data Not Found'
        tea = soup.find("div", attrs={"class": "cb-text-tea"}).text.strip() if soup.find(
            "div", attrs={"class": "cb-text-tea"}) else 'Data Not Found'
        lunch = soup.find("div", attrs={"class": "cb-text-lunch"}).text.strip(
        ) if soup.find("div", attrs={"class": "cb-text-lunch"}) else 'Data Not Found'
        innings_break = soup.find("div", attrs={"class": "cb-text-innings.break"}).text.strip(
        ) if soup.find("div", attrs={"class": "cb-text-innings.break"}) else 'Data Not Found'
        rain_break = soup.find("div", attrs={"class": "cb-text-rain"}).text.strip(
        ) if soup.find("div", attrs={"class": "cb-text-rain"}) else 'Data Not Found'
        wet_outfield = soup.find("div", attrs={"class": "cb-text-wetoutfield"}).text.strip(
        ) if soup.find("div", attrs={"class": "cb-text-wetoutfield"}) else 'Data Not Found'
        stumps = soup.find("div", attrs={"class": "cb-text-stumps"}).text.strip(
        ) if soup.find("div", attrs={"class": "cb-text-stumps"}) else 'Data Not Found'
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
        if stumps:
            status = stumps[0].text
            print(status)
        elif lunch:
            status = lunch[0].text
            print(status)
        elif tea:
            status = tea[0].text
            print(status)
        elif innings_break:
            status = innings_break[0].text
            print(status)
        elif rain_break:
            status = rain_break[0].text
            print(status)
        elif wet_outfield:
            status = wet_outfield[0].text
            print(status)
        else:
            status = update
            print(status)

except IndexError:
    spinner.stop()
    with open(READ_DATA) as f:
        data = yaml.load(f, Loader=SafeLoader)
        url_data = data['url']
    get_mobile_view = url_data.replace("www", "m")
    r = requests.get(get_mobile_view)
    soup = bs(r.content, 'html.parser')
    update = soup.find("div", attrs={"class": "cbz-ui-status"}).text.strip() if soup.find("div", attrs={
        "class": "cbz-ui-status"}) else 'Live Score Data Updating Re-check After Few mins or Innings break'
    print(update)
except AttributeError:
    spinner.stop()
    with open(READ_DATA) as f:
        data = yaml.load(f, Loader=SafeLoader)
        url_data = data['url']
    get_mobile_view = url_data.replace("www", "m")
    r = requests.get(get_mobile_view)
    soup = bs(r.content, 'html.parser')
    update = soup.find("div", attrs={"class": "cbz-ui-status"}).text.strip() if soup.find("div", attrs={
        "class": "cbz-ui-status"}) else 'Live Score Data Updating Re-check After Few mins or Innings break'
    print(update)
except FileExistsError:
    spinner.stop()
    print("Directory ", APP_NAME, " already exists")
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
