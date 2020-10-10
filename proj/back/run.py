import os
import yaml
import datetime
from flask import Flask


dirname, filename = os.path.split(os.path.abspath(__file__))
print(dirname)
print(filename)


def parseConfig():
    try:
        with open(os.path.join(dirname, 'conf', 'config.yaml')) as fs:
            y = yaml.load(fs.read(), Loader=yaml.FullLoader)
            app_conf = y['project']
            database_conf = y['database']


    except Exception as e:
        print('[ %s ] 没找到配置文件./config.yaml，或打开失败...[%s]' % (datetime.datetime.now(), e))


# create app
app = Flask(__name__)

if __name__ == "__main__":
    app.run()