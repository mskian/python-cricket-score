import os

HOME = os.path.expanduser('~')
APP_NAME = 'python-cricket-score'
CONFIG_NAME = 'score'
GENERATE_APP = os.path.join(HOME, APP_NAME)
READ_DATA = os.path.join(HOME, APP_NAME, CONFIG_NAME + '.yaml')

if not os.path.exists(GENERATE_APP):
    os.mkdir(GENERATE_APP)
    with open(os.path.join(GENERATE_APP, 'score.yaml'), 'w') as f:
        f.write("url: '<Update Current Live Match URL From Cricbuzz>'")
    print("App Directory ", APP_NAME, " Created ")
    print(READ_DATA)
else:
    print("Directory ", APP_NAME, " already exists")
    print(READ_DATA)
