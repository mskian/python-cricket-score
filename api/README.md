# Python Cricket API

Free Cricket API - Scrape the data using `BeautifulSoup` and export a output via JSON using Flask micro web framework  

You can Free Deploy it on `Vercel` and `deta.space`  

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fmskian%2Fpython-cricket-score%2Ftree%2Fmain%2Fapi)  

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

## Create Virtual Env
python3 -m venv venv

## Activate Virtual Env
source venv/bin/activate

## install Modules
pip install -r requirements.txt

## verify
python -m flask --version

## start the dev server 
flask --app index.py --debug run --host=0.0.0.0 --port=5000
```

## Exit from Virtual Env

```sh
deactivate
```

- Edit and Modification in `index.py` and `main.py`  

- `index.py` - for Vercel Hosting
- `main.py` - for `deta.space` Hosting  

- Deploy on Deta  

```sh
## insatall CLI and Login Account
## https://deta.space/docs/en/basics/cli

## Space Config
space new

## Push the site
space push
```

## Usage

- API Home Page

```sh
http://127.0.0.1:5000/
```

- Get Live Score

```sh
# Copy the 5 digit code from cricbuzz Current Live Match URL 
http://127.0.0.1:5000/score?id=<Match ID>
```

## LICENSE

MIT
