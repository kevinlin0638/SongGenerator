# -*-coding:utf-8-*-
import Generator as sg
import GUIHandler as guiH
import tkinter as tk

if __name__ == '__main__':
    win = guiH.GUIHandler()
    win = win.mtk

    generator = sg.SoundGenerator(16200, 1)
    # debug
    generator.print_properties()

    g_wave = generator.generate_wave(440, 2)
    print(g_wave)
    generator.play_wave(g_wave)
    generator.save_wave(g_wave)
    win.mainloop()
