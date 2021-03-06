## A - White Cells
Time Limit: 2 sec / Memory Limit: 1024 MB

### 問題文
H 行 W 列の白色のマス目があります。
あなたは h 個の行と w 個の列を選び、選んだ行または列に含まれるマス目を全て黒色で塗りつぶします。
白色のマス目はいくつ残るでしょうか。
なお、残る白色のマス目の数は行や列の選び方によらないことが証明できます。

### 制約

* 入力は全て整数である。
* 1 \leq H, W \leq 20
* 1 \leq h \leq H
* 1 \leq w \leq W

### 入力
入力は以下の形式で標準入力から与えられる。

```
H W
h w
```
### 出力
残る白色のマス目の数を出力せよ。

### 入力例 1

```
3 2
2 1
```
### 出力例 1

```
1
```
3 行 2 列の白色のマス目があり、2 行と 1 列を選んで黒色で塗りつぶしたとき、白色のマス目は必ず 1 個だけ残ります。

### 入力例 2

```
5 5
2 3
```
### 出力例 2

```
6
```
### 入力例 3

```
2 4
2 4
```
### 出力例 3

```
0
```
## B - Can you solve this?
Time Limit: 2 sec / Memory Limit: 1024 MB

### 問題文
N 個のソースコードがあり、i 個目のソースコードの特徴は A_{i1}, A_{i2}, ..., A_{iM} の M 個の整数で表されます。
また、整数 B_1, B_2, ..., B_M と 整数 C が与えられます。
A_{i1} B_1 + A_{i2} B_2 + ... + A_{iM} B_M + C > 0 のときに限り、i 個目のソースコードはこの問題に正答するソースコードです。
N 個のソースコードのうち、この問題に正答するソースコードの個数を求めてください。

### 制約

* 入力は全て整数である。
* 1 \leq N, M \leq 20
* -100 \leq A_{ij} \leq 100
* -100 \leq B_i \leq 100
* -100 \leq C \leq 100

### 入力
入力は以下の形式で標準入力から与えられる。

```
N M C
B_1 B_2 ... B_M
A_{11} A_{12} ... A_{1M}
A_{21} A_{22} ... A_{2M}
\vdots
A_{N1} A_{N2} ... A_{NM}
```
### 出力
N 個のソースコードのうち、この問題に正答するソースコードの個数を出力せよ。

### 入力例 1

```
2 3 -10
1 2 3
3 2 1
1 2 2
```
### 出力例 1

```
1
```
以下のように 2 個目のソースコードのみがこの問題に正答します。

### 入力例 2

```
5 2 -4
-2 5
100 41
100 40
-3 0
-6 -2
18 -13
```
### 出力例 2

```
2
```
### 入力例 3

```
3 3 0
100 -100 0
0 100 100
100 100 100
-100 100 100
```
### 出力例 3

```
0
```
全て Wrong Answer です。あなたのソースコードは含めません。

## C - Energy Drink Collector
Time Limit: 2 sec / Memory Limit: 1024 MB

### 問題文
栄養ドリンクにレーティング上昇効果があると聞いた高橋くんは、M 本の栄養ドリンクを買い集めることにしました。
栄養ドリンクが売られている店は N 軒あり、i 軒目の店では 1 本 A_i 円の栄養ドリンクを B_i 本まで買うことができます。
最小で何円あれば M 本の栄養ドリンクを買い集めることができるでしょうか。
なお、与えられる入力では、十分なお金があれば M 本の栄養ドリンクを買い集められることが保証されます。

### 制約

* 入力は全て整数である。
* 1 \leq N, M \leq 10^5
* 1 \leq A_i \leq 10^9
* 1 \leq B_i \leq 10^5
* B_1 + ... + B_N \geq M

### 入力
入力は以下の形式で標準入力から与えられる。

```
N M
A_1 B_1
A_2 B_2
\vdots
A_N B_N
```
### 出力
M 本の栄養ドリンクを買い集めるのに必要な最小の金額を出力せよ。

### 入力例 1

```
2 5
4 9
2 4
```
### 出力例 1

```
12
```
12 円あれば 1 軒目の店で 1 本、2 軒目の店で 4 本の栄養ドリンクを購入し、合計 5 本の栄養ドリンクを買い集めることができます。一方、11 円以下では 5 本の栄養ドリンクを買い集めることができません。

### 入力例 2

```
4 30
6 18
2 5
3 10
7 9
```
### 出力例 2

```
130
```
### 入力例 3

```
1 100000
1000000000 100000
```
### 出力例 3

```
100000000000000
```
出力が 32 ビット整数型におさまらないことがあります。

