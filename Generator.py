# -*-coding:utf-8-*-
import numpy as np
import pyaudio
import wave
import scipy.io.wavfile as wwf
import matplotlib.pyplot as pl


class SoundGenerator:
    def __init__(self, sample_rate, amplitude):
        self.sample_rate = sample_rate
        self.amplitude = amplitude

    def print_properties(self):
        print(self.sample_rate, self.amplitude)

    def generate_wave(self, frequency, sec):
        wave_data = self.amplitude * np.sin(2 * np.pi * frequency / self.sample_rate * np.arange(sec * self.sample_rate)).astype(np.float32)
        return wave_data

    def play_wave(self, wave_data):
        # 寫入音檔
        p = pyaudio.PyAudio()
        stream = p.open(format=pyaudio.paFloat32,
                        channels=1,
                        rate=self.sample_rate,
                        output=True)

        # 關閉 Stream
        stream.stop_stream()
        stream.close()

        # 關閉 Pyaudio
        p.terminate()

    def save_wave(self, wave_data):
        # 寫入 Wave 檔案
        wf = wave.open('record.wav', 'wb')
        wf.setnchannels(1)
        wf.setsampwidth(pyaudio.paFloat32)
        wf.setframerate(self.sample_rate*22)
        wf.writeframes(b''.join(wave_data))
        print(self.sample_rate)
        wf.close()

        wwf.write('kappa.wav', self.sample_rate, wave_data)



