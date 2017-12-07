import tkinter as tk


class GUIHandler:
    def __init__(self):
        self.mtk = tk.Tk()
        self.mtk.wm_minsize(480, 480)
        self.mtk.resizable(0, 0)
        self.mtk.title('音訊產生器')
        self.ini_widges()

    def ini_widges(self):
        self.filename_inp = tk.Entry(self.mtk).grid(row=1, column=0, padx=10)

        self.outputfn_txt = tk.Label(self.mtk, text='輸出檔名 : ').grid(row=0, column=0)

        self.sample_rate = tk.Entry(self.mtk).grid(row=1, column=2, padx=10)

        self.outputfn_txt = tk.Label(self.mtk, text='取樣率 : ').grid(row=0, column=2)

        #self.sec = tk.Entry(self.mtk).grid(row=3, column=1, padx=10)

        self.outputfn_txt = tk.Label(self.mtk, text='使用教學 : 請輸入 1 ~ 7(Do ~ Si)  0 為休止符 並輸入拍子數').grid(row=2, column=1, pady=40)



