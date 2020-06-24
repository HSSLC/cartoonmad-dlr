# development by HSSLCreative
# Date: 2020/5/17

import requests, bs4, threading, os

base = 'https://www.cartoonmad.cc/comic/'
h = {'Referer':'https://www.cartoonmad.com/comic/'}
MAX_RETRY = 10

def download_ch(url, cname):
    res = requests.get(url, headers=h)
    res.encoding = 'big5'
    bs = bs4.BeautifulSoup(res.text, features='html.parser')
    pg_list = bs.select('option[value]')
    threads = []
    for i in range(len(pg_list)):
        t = threading.Thread(target=download_pg, args=(base + pg_list[i].attrs['value'], i, cname))
        threads.append(t)
        t.start()
    for i in threads:
        i.join()
        

def download_pg(url, num, cname):
    for i in range(MAX_RETRY):
        try:
            res = requests.get(url, headers=h)
            res.raise_for_status()
            res.encoding = 'big5'
            bs = bs4.BeautifulSoup(res.text, features='html.parser')
            img_src = bs.select('img[src^="https://www.cartoonmad.com/comic/comicpic.asp"]')[0].attrs['src']
            img_res = requests.get(img_src)
            img_res.raise_for_status()
            file = open(os.path.join(cname, '%s.jpg' % num), 'wb')
            for chunk in img_res.iter_content(100000):
                file.write(chunk)
            file.close()
            return
        except:
            print('一個頁面錯誤 重試中...\n', end='')
            continue
    print('已達最大重試次數')
        
