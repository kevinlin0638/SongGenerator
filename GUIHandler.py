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

        self.btn_output = tk.Button(self.mtk, text='作業輸出').grid(row=1, column=1)


        self.outputfn_txt = tk.Label(self.mtk, text='使用教學 : 請輸入 1 ~ 7(Do ~ Si)  0 為休止符 並輸入拍子數').grid(row=2, column=1, pady=40)

        self.outputfn_txt = tk.Label(self.mtk, text='音符(0~7) : ').grid(row=3, column=0, pady=40)
        self.chord = tk.Entry(self.mtk).grid(row=4, column=0, padx=10)

        self.outputfn_txt = tk.Label(self.mtk, text='拍數 : ').grid(row=3, column=1)
        self.sec = tk.Entry(self.mtk).grid(row=4, column=1, padx=10)

        self.btn_delete = tk.Button(self.mtk, text='刪除一個').grid(row=4, column=2, padx=50, sticky='E')
        self.btn_sumit = tk.Button(self.mtk, text='增加').grid(row=4, column=2, sticky='W')

        self.outputfn_txt = tk.Label(self.mtk, text='當前樂譜 : ').grid(row=5, column=0, pady=60)

        self.btn_output = tk.Button(self.mtk, text='輸出檔案').grid(row=6, column=1)








