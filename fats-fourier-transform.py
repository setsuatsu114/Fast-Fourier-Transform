#回転因子 W
def W_cal(N, k):
    W = math.cos(2*k*math.pi/N) - 1j * math.sin(2*k*math.pi/N)
    return W

#FFT 再帰関数
def dft(N, x):
    if N != 2:
        even = x[0:len(x):2]
        odd = x[1:len(x):2]
        X = []
        dft_e = dft(int(N/2), even)
        dft_o = dft(int(N/2), odd)
        for k in range(int(N/2)):
            X.append(dft_e[k] + W_cal(N,k) * dft_o[k])  
        for k in range(int(N/2)):
            X.append(dft_e[k] - W_cal(N,k) * dft_o[k])
        return X

    else: 
        dft2 = [0,0]
        dft2[0] = x[0] + x[1]
        dft2[1] = x[0] - x[1]
        return dft2

#送るデータの準備
import math
import numpy as np
import time
N = 1024
index = np.arange(N)
freq = 3
f = np.sin(freq * 2 * np.pi * (index/N))
x = f

#実装
start1 = time.time()
fft_self = dft(N, x)
fft_time = (time.time() - start1)

#print('自作')
#print(fft_self)
print('自作時間')
print(fft_time)

#ライブラリを用いたFFT
start2 = time.time()
fft_x = np.fft.fft(x)
fft_libtime = (time.time() - start2)
#print('ライブラリ使用')
#print(fft_x)
print('ライブラリ使用時の計算時間')
print(fft_libtime)

#比較結果
#print('数値の誤差')
gap = fft_self - fft_x
print(gap)
