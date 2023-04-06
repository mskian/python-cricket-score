import random
import requests
from bs4 import BeautifulSoup as bs
from flask import Flask, escape, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
cors = CORS(app, resources={
            r"/score/*": {"origins": [r'^https://.+sanweb.info$']}})

user_agent_list = [
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/111.0',
    # 'Mozilla/5.0 (Linux; Android 13) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36',
    # 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36',
    # 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    # 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.3 Safari/605.1.15',
    # 'Mozilla/5.0 (Linux; Android 13) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile DuckDuckGo/5 Safari/537.36',
    # 'Mozilla/5.0 (Linux; Android 13; Pixel 6a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36',
    # 'Mozilla/5.0 (Android 10; Mobile; rv:102.0) Gecko/102.0 Firefox/102.0'
]
get_random_agent = random.choice(user_agent_list)

headers = {
    'User-Agent': get_random_agent
}


@app.route('/')
def hello():
    return jsonify({'Code': 200, 'message': 'Python - Free Cricket Score API - JSON'})


@app.route('/score', methods=['GET'])
def score():
    get_id = request.args.get('id')
    id = escape(get_id)
    if id:
        r = requests.get(
            'https://www.cricbuzz.com/live-cricket-scores/' + id, headers=headers)
        soup = bs(r.content, 'html.parser')

        mobile_data = requests.get(
            'https://m.cricbuzz.com/live-cricket-scores/' + id, headers=headers)
        mobileview = bs(mobile_data.content, 'html.parser')
        update = mobileview.find("div", attrs={"class": "cbz-ui-status"}).text.strip() if mobileview.find("div", attrs={
            "class": "cbz-ui-status"}) else 'Live Score Data Updating Re-check After Few mins or Innings break'

        live_score = soup.find(
            "span", attrs={"class": "cb-font-20 text-bold"}).text.strip() if soup.find("span", attrs={"class": "cb-font-20 text-bold"}) else 'Data Not Found'
        title = soup.find(
            "h1", attrs={"class": "cb-nav-hdr cb-font-18 line-ht24"}).text.strip().replace(", Commentary", "") if soup.find("h1", attrs={"class": "cb-nav-hdr cb-font-18 line-ht24"}) else 'Data Not Found'
        run_rate = soup.find_all(
            "span", attrs={"class": "cb-font-12 cb-text-gray"})[0].text.strip().replace("CRR:\u00a0", "") if soup.find_all("span", attrs={"class": "cb-font-12 cb-text-gray"}) else 'Data Not Found'
        batter_one = soup.find_all(
            "div", attrs={"class": "cb-col cb-col-50"})[1].text.strip() if soup.find_all("div", attrs={"class": "cb-col cb-col-50"}) else 'Data Not Found'
        batter_two = soup.find_all(
            "div", attrs={"class": "cb-col cb-col-50"})[2].text.strip() if soup.find_all("div", attrs={"class": "cb-col cb-col-50"}) else 'Data Not Found'
        batter_one_run = soup.find_all(
            "div", attrs={"class": "cb-col cb-col-10 ab text-right"})[0].text.strip() if soup.find_all("div", attrs={"class": "cb-col cb-col-10 ab text-right"}) else 'Data Not Found'
        batter_two_run = soup.find_all(
            "div", attrs={"class": "cb-col cb-col-10 ab text-right"})[2].text.strip() if soup.find_all("div", attrs={"class": "cb-col cb-col-10 ab text-right"}) else 'Data Not Found'
        batter_one_ball = soup.find_all(
            "div", attrs={"class": "cb-col cb-col-10 ab text-right"})[1].text.strip() if soup.find_all("div", attrs={"class": "cb-col cb-col-10 ab text-right"}) else 'Data Not Found'
        batter_two_ball = soup.find_all(
            "div", attrs={"class": "cb-col cb-col-10 ab text-right"})[3].text.strip() if soup.find_all("div", attrs={"class": "cb-col cb-col-10 ab text-right"}) else 'Data Not Found'
        batter_one_sr = soup.find_all(
            "div", attrs={"class": "cb-col cb-col-14 ab text-right"})[0].text.strip() if soup.find_all("div", attrs={"class": "cb-col cb-col-14 ab text-right"}) else 'Data Not Found'
        batter_two_sr = soup.find_all(
            "div", attrs={"class": "cb-col cb-col-14 ab text-right"})[1].text.strip() if soup.find_all("div", attrs={"class": "cb-col cb-col-14 ab text-right"}) else 'Data Not Found'
        bowler_one = soup.find_all(
            "div", attrs={"class": "cb-col cb-col-50"})[4].text.strip() if soup.find_all("div", attrs={"class": "cb-col cb-col-50"}) else 'Data Not Found'
        bowler_two = soup.find_all(
            "div", attrs={"class": "cb-col cb-col-50"})[5].text.strip() if soup.find_all("div", attrs={"class": "cb-col cb-col-50"}) else 'Data Not Found'
        bowler_one_over = soup.find_all(
            "div", attrs={"class": "cb-col cb-col-10 text-right"})[4].text.strip() if soup.find_all("div", attrs={"class": "cb-col cb-col-10 text-right"}) else 'Data Not Found'
        bowler_two_over = soup.find_all(
            "div", attrs={"class": "cb-col cb-col-10 text-right"})[6].text.strip() if soup.find_all("div", attrs={"class": "cb-col cb-col-10 text-right"}) else 'Data Not Found'
        bowler_one_run = soup.find_all(
            "div", attrs={"class": "cb-col cb-col-10 text-right"})[5].text.strip() if soup.find_all("div", attrs={"class": "cb-col cb-col-10 text-right"}) else 'Data Not Found'
        bowler_two_run = soup.find_all(
            "div", attrs={"class": "cb-col cb-col-10 text-right"})[7].text.strip() if soup.find_all("div", attrs={"class": "cb-col cb-col-10 text-right"}) else 'Data Not Found'
        bowler_one_eco = soup.find_all(
            "div", attrs={"class": "cb-col cb-col-14 text-right"})[2].text.strip() if soup.find_all("div", attrs={"class": "cb-col cb-col-10 ab text-right"}) else 'Data Not Found'
        bowler_two_eco = soup.find_all(
            "div", attrs={"class": "cb-col cb-col-14 text-right"})[3].text.strip() if soup.find_all("div", attrs={"class": "cb-col cb-col-10 ab text-right"}) else 'Data Not Found'
        bowler_one_wicket = soup.find_all(
            "div", attrs={"class": "cb-col cb-col-8 text-right"})[5].text.strip() if soup.find_all("div", attrs={"class": "cb-col cb-col-8 text-right"}) else 'Data Not Found'
        bowler_two_wicket = soup.find_all(
            "div", attrs={"class": "cb-col cb-col-8 text-right"})[7].text.strip() if soup.find_all("div", attrs={"class": "cb-col cb-col-8 text-right"}) else 'Data Not Found'
        return jsonify({
            'title': title,
            'update': update,
            'livescore': live_score,
            'runrate': run_rate,
            'batterone': batter_one,
            'batsmanonerun': batter_one_run,
            'batsmanoneball': batter_one_ball,
            'batsmanonesr': batter_one_sr,
            'battertwo': batter_two,
            'batsmantworun': batter_two_run,
            'batsmantwoball': batter_two_ball,
            'batsmantwosr': batter_two_sr,
            'bowlerone': bowler_one,
            "bowleroneover": bowler_one_over,
            "bowleronerun": bowler_one_run,
            "bowleronewickers": bowler_one_wicket,
            "bowleroneeconomy": bowler_one_eco,
            'bowlertwo': bowler_two,
            "bowlertwoover": bowler_two_over,
            "bowlertworun": bowler_two_run,
            "bowlertwowickers": bowler_two_wicket,
            "bowlertwoeconomy": bowler_two_eco

        })
    else:
        return jsonify({
            'title': 'Data not Found',
            'update': 'Data not Found',
            'livescore': 'Data not Found',
            'runrate': 'Data not Found',
            'batterone': 'Data not Found',
            'batsmanonerun': 'Data not Found',
            'batsmanoneball': 'Data not Found',
            'batsmanonesr': 'Data not Found',
            'battertwo': 'Data not Found',
            'batsmantworun': 'Data not Found',
            'batsmantwoball': 'Data not Found',
            'batsmantwosr': 'Data not Found',
            'bowlerone': 'Data not Found',
            "bowleroneover": 'Data not Found',
            "bowleronerun": 'Data not Found',
            "bowleronewickers": 'Data not Found',
            "bowleroneeconomy": 'Data not Found',
            'bowlertwo': 'Data not Found',
            "bowlertwoover": 'Data not Found',
            "bowlertworun": 'Data not Found',
            "bowlertwowickers": 'Data not Found',
            "bowlertwoeconomy": 'Data not Found',

        })


@app.errorhandler(404)
def invalid_route(e):
    return jsonify({
        'title': 'Data not Found',
        'update': 'Data not Found',
        'livescore': 'Data not Found',
        'runrate': 'Data not Found',
        'batterone': 'Data not Found',
        'batsmanonerun': 'Data not Found',
        'batsmanoneball': 'Data not Found',
        'batsmanonesr': 'Data not Found',
        'battertwo': 'Data not Found',
        'batsmantworun': 'Data not Found',
        'batsmantwoball': 'Data not Found',
        'batsmantwosr': 'Data not Found',
        'bowlerone': 'Data not Found',
        "bowleroneover": 'Data not Found',
        "bowleronerun": 'Data not Found',
        "bowleronewickers": 'Data not Found',
        "bowleroneeconomy": 'Data not Found',
        'bowlertwo': 'Data not Found',
        "bowlertwoover": 'Data not Found',
        "bowlertworun": 'Data not Found',
        "bowlertwowickers": 'Data not Found',
        "bowlertwoeconomy": 'Data not Found',

    })


@app.errorhandler(500)
def invalid_route(e):
    return jsonify({
        'title': 'Data not Found',
        'update': 'Data not Found',
        'livescore': 'Data not Found',
        'runrate': 'Data not Found',
        'batterone': 'Data not Found',
        'batsmanonerun': 'Data not Found',
        'batsmanoneball': 'Data not Found',
        'batsmanonesr': 'Data not Found',
        'battertwo': 'Data not Found',
        'batsmantworun': 'Data not Found',
        'batsmantwoball': 'Data not Found',
        'batsmantwosr': 'Data not Found',
        'bowlerone': 'Data not Found',
        "bowleroneover": 'Data not Found',
        "bowleronerun": 'Data not Found',
        "bowleronewickers": 'Data not Found',
        "bowleroneeconomy": 'Data not Found',
        'bowlertwo': 'Data not Found',
        "bowlertwoover": 'Data not Found',
        "bowlertworun": 'Data not Found',
        "bowlertwowickers": 'Data not Found',
        "bowlertwoeconomy": 'Data not Found',

    })


if __name__ == '__main__':
    app.run()
    # app.run(
    #    host="0.0.0.0",
    #    port=int("5000")
    # )
