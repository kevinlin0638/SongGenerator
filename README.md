### 多媒體作業02 音訊產生器

## GUI
![Alt text](https://i.imgur.com/qw3yEco.jpg)
![Alt text](https://i.imgur.com/wg4HSZA.jpg)

# 功能
* 點擊作業輸出可以直接輸出題目
* Extra Work 點選音符與拍數 可以自行作歌XD
* 可以讀入.txt的譜檔
txt檔寫譜格式
音符(0~7 0為休止符),拍數(1~4)
![Alt text](https://i.imgur.com/29ACmId.jpg)

# 程式流程
產生Sin波 -> 將Sin波存入.wav檔


# 製作譜系統:
將使用者輸入的譜存在物件中,完成譜之後點及傳送即可將譜中的音轉成Data，最夠再將Data存入.wav檔

# 讀取模式
* 1 ~ 7 為 Do 至 Si 0 為休止符，也可直接在GUI內使用做譜功能


## 製作過程中遇到的困難
* wave的套件因為資料格式問題改了好久
* 不知道為何使用wave套件存聲音一直怪怪的，最後使用spicy

# 學到什麼
* 產生一段音訊的方法
* 如何合成兩段不同頻率的聲音
* 製作 Frequency Modulation