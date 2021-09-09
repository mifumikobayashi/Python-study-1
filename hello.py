import datetime
import configparser
import random

random.randint(1,3)

now = datetime.datetime.now()
config_ini = configparser.ConfigParser()

def hello( name ):
    print(name + "さん" )

def nowtime():
    print("{0:%Y年%m月%d日 %H時%M分}".format(now))

def greeting():
    
    config_ini.read('config.ini', encoding='utf-8') #config_ini=設定ファイル
    read_morning = config_ini['morning']
    read_noon = config_ini['noon']
    read_night = config_ini['night']
    random_number = str(random.randint(1,3))

    hour = now.hour
    print(hour)
    if hour < 3 :
        print (read_night[random_number])
    elif hour < 10 :
        print (read_morning[random_number])
    elif hour < 18 :
        print (read_noon[random_number])
    else :
        print (read_night[random_number])

def tukinowamei():
    #配列　0番目から始まる
    watuki = ["睦月（むつき）", "如月（きさらぎ）", "弥生（やよい）", "卯月（うづき）", "皐月（さつき）", "水無月（みなづき）", "文月（ふみづき）", "葉月（はづき）", "長月（ながつき）", "神無月（かんなづき）","霜月（しもつき）", "師走（しわす）"]
    month = now.month
    message = f'{month}月の和名は、『{watuki[month-1]}』といいます'    
    print(message)

def inputname():
    name = input('Enter your name: ')
    return name
 
if __name__ == '__main__':
    name = inputname()
    greeting()
    hello( name )
    nowtime()
    tukinowamei()

