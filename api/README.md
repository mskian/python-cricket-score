# Python Cricket API

Free Cricket API - Scrape the data using `BeautifulSoup` and export a output via JSON using Flask is a micro web framework  

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fmskian%2Fpython-cricket-score%2Ftree%2Fmain%2Fapi&demo-title=Cricket%20%2B%20API&demo-image=https://assets.vercel.com/image/upload/v1669994156/random/flask.png)

## Requirements 📑

- Python 3
- Required Modules
- Virtual Environment for Running Flask server

## Setup and Development

```sh
## install python env
sudo apt install python3-venv

## Clone the Repo
git clone https://github.com/mskian/python-cricket-score.git
cd python-cricket-score
cd api

## Activate Virtual Env
source venv/bin/activate

## install Modules
pip install -r requirements.txt

## verify
python -m flask --version

## start the dev server 
flask --app app.py --debug run --host=0.0.0.0 --port=5000
```

- Edit and Modify on `index.py`

## Usage

- API Home Page

```sh
http://127.0.0.1:5001/
```

- Get Live Score

```sh
# Copy the 5 digit code from cricbuzz Current Live Match URL 
http://127.0.0.1:5001/score?id=<Match ID>
```
