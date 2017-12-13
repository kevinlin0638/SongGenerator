### 多媒體作業02 音訊產生器

## GUI
![Alt text](https://i.imgur.com/qw3yEco.jpg)
![Alt text](https://i.imgur.com/wg4HSZA.jpg)

# 功能
* 點擊作業輸出可以直接輸出題目
* Extra Work 點選音符與拍數 可以自行作歌XD
* 可以讀入.txt的譜檔

# txt檔寫譜格式 : 
*音符(0至7 0為休止符),拍數(1至4)
![Alt text](https://i.imgur.com/29ACmId.jpg)

# 製作譜系統:
將使用者輸入的譜存在物件中,完成譜之後點及傳送即可將譜中的音轉成Data，最夠再將Data存入.wav檔 (存檔前記得打上檔名)

# 讀取模式
* 直接在檔名輸入檔案名，即可直接由文字檔案匯入樂譜
* 1 ~ 7 為 Do 至 Si 0 為休止符，也可直接在GUI內使用做譜功能

# 程式流程

def generate_wave(self, chord, sec):
	wave_data = self.amplitude * np.sin(2 * np.pi * self.hzArr[chord][1] / self.sample_rate * np.arange(sec * 0.5 * self.sample_rate)).astype(np.float32)
使用此Function來產生sin波動，每次傳進來一個音高輸出一拍 -> 傳回Sin波 -> 將Sin波存入.wav檔


def kappa(self, chord, sec, low, moder):
    wave_data = self.amplitude * np.sin(
        2 * np.pi * self.hzArr[chord][1] / self.sample_rate * np.arange(sec * 0.5 * self.sample_rate)).astype(
        np.float32)
    cos_wave_data = self.amplitude * np.cos(
        2 * np.pi * moder / self.sample_rate * np.arange(sec * 0.5 * self.sample_rate)).astype(
        np.float32)
    multi = np.multiply(wave_data, cos_wave_data)
使用此段Function來產生sin波與cos波，再將兩段聲音組合，以達到FM效果。



## 製作過程中遇到的困難
* wave的套件因為資料格式問題改了好久
* 不知道為何使用wave套件存聲音一直怪怪的，最後使用spicy
* 摸索了許多次有關FM，找了很久才懂題目的意思

# 學到什麼
* 產生一段音訊的方法
* 如何合成兩段不同頻率的聲音
* 製作 Frequency Modulation，調適頻率