import requests, bs4, re, os, threading
from down import download_ch

base = 'https://www.cartoonmad.cc'

def chdir(ds):
    dlist = ds.split(os.path.sep)
    for d in dlist:
        if not os.path.exists(d) and not os.path.isdir(d):
            os.mkdir(d)
        os.chdir(d)

def main():
    print('僅作為個人使用，勿作為商業用途，版權由包括但不限於原作者與受到原作者合法授權者擁有')
    while True:
        print('輸入作品目錄URL:', end='')
        url = input()
        try:
            if re.match(r'https://www\.cartoonmad\.com/comic/[0-9]+\.html', url).group(0):
                break
        except:
            print('無效的網址')
            continue
    res = requests.get(url)
    res.encoding = 'big5'
    bs = bs4.BeautifulSoup(res.text, 'html.parser')
    chs = bs.select('#info a[href^="/comic/"]')
    bname = bs.select('td[style="font-size:12pt;color:#000066"] a[href^="/comic/"]')[0].text
    chdir(bname)
    chdir('imgs')
    print('標題: %s' % bname)
    print('編號 對應名稱')
    ch_list = []
    for ch in chs:
        ch_list.append([ch.text, ch.attrs['href']])
    for i in range(len(ch_list)):
        print(str(i).ljust(5) + ch_list[i][0])
    print('輸入上列編號選擇下載話數(ex:1-2 5-8 10 將會下載編號1, 2, 5, 6, 7, 8, 10的章節)')
    choose_chs = input()
    tmp = re.findall(r'[0-9]+\-?[0-9]*', choose_chs)
    choose_block_list = []
    for block in tmp:
        try:
            block = block.split('-')
            for i in range(len(block)):
                block[i] = int(block[i])
                if block[i] > len(ch_list) or block[i] < 0:
                    raise Exception('out of range')
            if len(block) >= 2:
                if block[1] < block[0]:
                    block[0], block[1] = block[1], block[0]
                choose_block_list.append([block[0], block[1]])
            else:
                choose_block_list.append([block[0], block[0]])
        except:
            continue
    threads = []
    for area in choose_block_list:
        block = ch_list[area[0]:area[1]+1]
        for ch in block:
            chdir(ch[0])
            os.chdir('..')
            threads.append(threading.Thread(target=download_ch, args=(base + ch[1], ch[0])))
    print('多執行緒正在暴走中')
    for thread in threads:
        thread.start()
main()
