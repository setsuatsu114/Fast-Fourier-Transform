# 高速フーリエ変換を自作してみた(Python)

## 目的

	• 離散フーリエ変換（DFT)をpythonで書くこと
	• FFTとの実行時間の差を計測すること

## 環境

python3.10.8

## 結果

	• 入力数を2の累乗(横軸)ごとに計算時間(縦軸)の差をライブラリを用いた計算結果と比較した図が以下
 	• ライブラリを使うと入力値が増えても計算時間が変動しないことがわかる
  
<img width="362" alt="image" src="https://github.com/setsuatsu114/Fast-Fourier-Transform/assets/118243126/0aaf4f60-4538-416e-ba22-b19f377bedc2">

