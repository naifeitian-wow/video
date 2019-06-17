url='http://bf2.ahpai.cc/20181203/yik1hiGC/index.m3u8'

if 'www.605-zy.com' in str or '605ziyuan.com/share' in url:
    url = url
else:
    url = 'https://www.ppf8.com/605m3u8.php?url=' + url
print(url)