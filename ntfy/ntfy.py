import json
from dotenv import load_dotenv
import os
import requests

load_dotenv()

URL = os.environ['MATCHURL']
READ = requests.get(URL)
DATA = json.loads(READ.content.decode())

url = os.environ["URL"]
message = "\n\n" + DATA['title'] + "\n\n" + "➡ Current Score: " + DATA['livescore'] + "\n\n" + "➡ Run Rate: " + DATA['runrate'] + "\n\n" + "➡ Current Batsman: " + DATA['batterone'] + " - Runs:" + DATA['batsmanonerun'] + " - Balls: " + DATA['batsmanoneball'] + " - SR: " + DATA['batsmanonesr'] + "\n\n" + "➡ Other Batsman: " + DATA['battertwo'] + " - Runs: " + DATA['batsmantworun'] + " - Balls: " + \
    DATA['batsmantwoball'] + " - SR: " + DATA['batsmantwosr'] + "\n\n" + "➡ Current Bowler: " + DATA['bowlerone'] + " - Overs: " + DATA['bowleroneover'] + " - run: " + DATA['bowleronerun'] + \
    " - Wickets: " + DATA['bowleronewickers'] + "\n\n" + "➡ Other Bowler: " + DATA['bowlertwo'] + " - Overs: " + \
    DATA['bowlertwoover'] + " - run: " + DATA['bowlertworun'] + \
    " - Wickets: " + DATA['bowlertwowickers']

querystring = {"title": "Cricket Score 🔴", "message": message}

headers = {
    "Priority": "high",
    "Icon": os.environ['ICON']
}

response = requests.request("POST", url, headers=headers, params=querystring)

print(response.text)
