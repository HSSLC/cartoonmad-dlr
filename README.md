# cartoonmad-dlr
自動多執行緒批量下載動漫狂的漫畫，可完全掛機運作  
**僅作為個人使用，勿作為商業用途，版權由包括但不限於原作者與受到原作者合法授權者擁有**

## 執行環境
此程式由Python製作，執行需要Python環境  
至於如何安裝Python環境就自己去查囉，裝起來其實不難  
Googleは君のよい友達
## 必要模組
* requests
* BeautifulSoup4

## 使用方法
1. 執行`main.py`
2. 輸入動漫狂中作品的目錄頁面網址，例如`https://www.cartoonmad.com/comic/xxxx.html`
3. 程式會提示編號與章節對應表，照表輸入要下載的章節，範例：  
  <pre>
    編號 對應名稱
    0    第 001 話
    1    第 002 話
    2    第 003 話
    3    第 004 話
    4    第 005 話
    5    第 006 話
    6    第 007 話
    7    第 008 話
    8    第 009 話
    9    第 010 話
    10   第 011 話
    11   第 012 話
  </pre>
  如果輸入`1-2 5-8 10`就會下載`第 002 話`、`第 003 話`、`第 006 話`、`第 007 話`、`第 008 話`、`第 009 話`、`第 011 話`  
  **注意:輸入的數字是章節對應編號，不是話數**  
4. 接下來就可以放著掛機了

## 注意事項/說明
* 歸檔方式  
  下載後的檔案將位於`本程式放置位置`旁的`書名`目錄下  
  `書名`目錄下的目錄結構會照著`章節名稱`歸檔
* 因為這個下載器是多執行緒的，所以有時候會因為**太快**了，高機率跳出`一個頁面錯誤 重試中...`訊息，但不用擔心，這個程式會自動重新下載失敗的頁面
* 關於將圖片下載完後的運用，可參考[kc-generator](https://github.com/HSSLC/kc-generator)來把大量圖片編成一本amazon kindle的mobi格式電子書
