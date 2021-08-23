# weiboSpiderWatcher
使用 [/dataabc/weiboSpider](https://github.com/dataabc/weiboSpider) 获取到最新微博了，但是我还需要通知到我，这里是涉及到的工具。

## 环境
安装 weibo_spider
```shell
pip3 install weibo-spider
```

## 快速使用本项目
```shell
git@github.com:Bpazy/weiboSpiderWatcher.git
cd weiboSpiderWatcher
python3 -m weibo_spider
# 配置监听用户
# vim config.json

# 配置监听用户和钉钉机器人，参考 watcher.config.json.sample
# vim watcher.config.json
python3 notifyLatestWeibo.py
```

## 监听 weiboSpider 数据库文件变化
也可以使用 inotifywait 监听文件变化来自动触发，比如:
```shell
inotifywait -mrq -e modify,delete,create,attrib /home/ziyuan/weibo_spider/weibo/weibo_user/weibo_uid.txt | while read file 
do 
    python3 notifyLatestWeibo.py
done
```
