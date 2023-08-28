#行列計算
def F_cal(F, e, N, x):
    for k in range(N):
        Fk = []
        for n in range(N):
            ek = math.cos(2*k*n*math.pi/N) - 1j * math.sin(2*k*n*math.pi/N) 
            f = ek * x[n]
            Fk.append(f)
        F.append(sum(Fk))
    return F
    

import numpy as np
import math
import time
N = 1024
n = np.arange(N)
freq = 3
x = np.sin(freq * 2 * np.pi * (n/N))

e = []
F = []
start = time.time()
F = F_cal(F, e, N, x)
dft_time = (time.time() - start)
#print('自作')
print(len(F))

fft = np.fft.fft(x)
#print('ライブラリfft')
print(len(fft))

print('誤差')
print(F-fft)

print('自作タイム')
print(dft_time)
