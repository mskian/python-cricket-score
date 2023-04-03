# nfty Push

Send Live cricket Score Updates via ntfy Push notification  

## Setup

```sh
## install subversion svn
sudo apt install subversion

## svn Checkout
svn export https://github.com/mskian/python-cricket-score/trunk/ntfy

## install packages
python -m pip install --upgrade pip
pip install -r requirements.txt
```

- Env File `.env`

```sh
URL= "<NTFY Push server URL>"
MATCHURL = "<Python Cricket score API>"
ICON = "ICON URL For NTFY"
```

## LICENSE

MIT
