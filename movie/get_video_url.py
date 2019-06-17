import requests
from fake_useragent import UserAgent
import random
from lxml import etree
import pymysql
import datetime
import re
# Create your views here.
import threading
import time

headers={
        'User-Agent':UserAgent().random
    }

def get_url(href):
    code=requests.get(href,headers=headers).content.decode()
    pattern=re.compile(r'{"flag":"play","encrypt":0,"trysee":0,"points":0,"link":".*?","link_next":".*?","link_pre":".*?","url":"(.*?)",.*?}',re.S)
    url=''
    try:
        url=pattern.findall(code)[0].replace('\\','')
        if 'www.605-zy.com' in url or '605ziyuan.com/share' in url:
            url = url
        else:
            url='https://www.ppf8.com/605m3u8.php?url='+url
    except Exception as e:
        print('获取真实链接失败，原因：',e)
    return url

def get_detail(href):
    code1=requests.get(href,headers=headers).text
    code=etree.HTML(code1)
    list=code.xpath('//div[@class="stui-content__detail"]')[0]
    #类型
    type=list.xpath('./p[1]/a[1]/text()')
    if type:
        type=type[0]
    # 地区
    country=list.xpath('./p[1]/a[2]/text()')
    if country:
        country=country[0]
    else:
        country='未知'
    # 年份
    year=list.xpath('./p[1]/a[3]/text()')
    if year:
        year=year[0]
    else:
        year='未知'
    # # 主演
    pattern=re.compile(r'<p class="data">.*?<span>主演：</span>(.*?)</p>',re.S)
    zhuyan=pattern.findall(code1)
    if zhuyan:
        zhuyan=zhuyan[0]
    # 导演
    director=list.xpath('./p[3]/text()')
    if director:
        director=director[0]
    else:
        director='未知'
    # 剧情
    story=code.xpath('//div[@class="stui-content__desc col-pd clearfix"]/text()')
    if story:
        story=story[0]
        story=story.strip()
        story=story.replace('\n','')

    if list.xpath('./div/a/@href'):
        href='http://5566.feifei6688.cn'+list.xpath('./div/a/@href')[0]

    # print('主演：',zhuyan)

    url=get_url(href)
    return {'type':type,'country':country,'year':year,
            'director':director,'zhuyan':zhuyan,'story':story,'url':url}
def get_movie(page):
    url='http://5566.feifei6688.cn/index.php/vod/show/id/1/page/{}/'.format(page)

    code=requests.get(url,headers=headers).text
    code=etree.HTML(code)
    lists=code.xpath('//li[@class="stui-vodlist__item"]')
    for list in lists:
        title=list.xpath('./a/@title')[0]
        #详情页地址
        href='http://5566.feifei6688.cn'+list.xpath('./a/@href')[0]
        pic=list.xpath('./a/@data-original')[0]
        if pic.startswith('http'):
            pic=pic
        else:
            pic='http://5566.feifei6688.cn'+list.xpath('./a/@data-original')[0]

        # 标题
        print(title)
        data=get_detail(href)
        # 类型
        type=data['type']
        country=data['country']
        year=data['year']
        director=data['director']
        zhuyan=data['zhuyan']
        story=data['story']
        url=data['url']
        time = datetime.datetime.now()

        try:
            cursor.execute('SELECT * FROM movie where title="{}"'.format(title))
            one = cursor.fetchone()
            if one:
                cursor.execute(
                    'update movie set title="{}",pic="{}",type="{}",country="{}",year="{}",director="{}",zhuyan="{}",story="{}",url="{}",time="{}" where title="{}"'.format(
                        title, pic, type, country, year, director, zhuyan, story, url, time,title))
                db.commit()
                print('update movie ok')
            else:
                cursor.execute(
                    'insert into movie(title,pic,type,country,year,director,zhuyan,story,url,time,category_id)VALUES ("{}","{}","{}","{}","{}","{}","{}","{}","{}","{}",1)'.format(title,pic,type,country,year,director,zhuyan,story,url,time))
                db.commit()
        except Exception as e:
            print('存储失败，失败原因：',e)


db = pymysql.connect(host="localhost", user='root', password='123456', db='movie', port=3306)
cursor = db.cursor()


import get_TV
import get_zongyi
import get_cartoon

for i in range(435,0,-1):
    print('now page {}'.format(i))
    get_movie(i)
for i in range(21,0,-1):
    print('now page {}'.format(i))
    get_zongyi.get_movie(i)

for i in range(43,0,-1):
    print('now page {}'.format(i))
    get_cartoon.get_movie(i)

for i in range(220,0,-1):
    print('now page {}'.format(i))
    get_TV.get_movie(i)