from os import name
import re
import requests
import json

# 配置文件
with open('watcher.config.json') as f:
    cfg = json.load(f)
    print(cfg)

txtPath = './weibo/{name}/{uid}.txt'.format(name=cfg['user']['name'], uid=cfg['user']['uid'])
txt = open(txtPath, encoding="utf-8")

latestBlog = ''
time = ''
while True:
    line = txt.readline()
    if "原创微博内容" in line:
        latestBlog = txt.readline()
        txt.readline()
        time = re.match('发布时间：(.+)', txt.readline())[1]
        break
print(time + ': ' + latestBlog)

with open('latest_weibo') as f:
    if latestBlog.strip() == f.readline().strip():
        exit(0)
    f.write(latestBlog)

url = 'https://oapi.dingtalk.com/robot/send?access_token={accessToken}'.format(accessToken=cfg['ding']['accessToken'])
j = {
    "msgtype": "markdown",
    "markdown": {
        "title": latestBlog,
        "text": '微博:\n' + latestBlog + "\n> " + time
    }
}
r = requests.post(url, json=j)
print(r.text)
