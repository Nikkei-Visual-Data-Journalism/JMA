# JMA
# 気象庁｜全国の防災情報

https://www.jma.go.jp/bosai/

## アメダス
|URL|データ|
|-|-|
|[気温](https://www.jma.go.jp/bosai/map.html#5/34.5/137/&elem=temp&contents=amedas&interval=60)|[temp.csv](https://github.com/Nikkei-Visual-Data-Journalism/JMA/raw/main/temp.csv)|
|[1時間降水量](https://www.jma.go.jp/bosai/map.html#5/34.5/137/&elem=precipitation1h&contents=amedas&interval=60)|[precipitation1h.csv](https://github.com/Nikkei-Visual-Data-Journalism/JMA/raw/main/precipitation1h.csv)|
|[24時間降水量](https://www.jma.go.jp/bosai/map.html#5/34.5/137/&elem=precipitation24h&contents=amedas&interval=60)|[precipitation24h.csv](https://github.com/Nikkei-Visual-Data-Journalism/JMA/raw/main/precipitation24h.csv)|

## 熱中症警戒アラート
|URL|データ|
|-|-|
|[今日](https://www.jma.go.jp/bosai/map.html#5/34.5/137/&contents=heat&term=today)|[heat.csv](https://github.com/Nikkei-Visual-Data-Journalism/JMA/raw/main/heat.csv)|

## 雨雲の動き
[降水強度](https://www.jma.go.jp/bosai/nowc/#zoom:5/lat:35.012002/lon:135.000000/colordepth:normal/elements:hrpns&slmcs&slmcs_fcst)<br>
https://www.jma.go.jp/bosai/jmatile/data/nowc/yyyymmddHHMMSS/none/yyyymmddHHMMSS/surf/hrpns/{z}/{x}/{y}.png<br>
yyyymmddHHMMSSは5分単位、UTC(JST-9)表記

## キキクル（危険度分布）

[土砂キキクル](https://www.jma.go.jp/bosai/risk/#elements:land/zoom:5/lat:35.012002/lon:135.000000/colordepth:normal)<br>
https://www.jma.go.jp/bosai/jmatile/data/risk/yyyymmddHHMMSS/immed0/yyyymmddHHMMSS/surf/land/{z}/{x}/{y}.png

[浸水キキクル](https://www.jma.go.jp/bosai/risk/#zoom:5/lat:35.012002/lon:135.000000/colordepth:normal/elements:inund)<br>
https://www.jma.go.jp/bosai/jmatile/data/risk/yyyymmddHHMMSS/immed0/yyyymmddHHMMSS/surf/inund/{z}/{x}/{y}.png

[洪水キキクル](https://www.jma.go.jp/bosai/risk/#zoom:5/lat:35.012002/lon:135.000000/colordepth:normal/elements:flood)<br>
https://www.jma.go.jp/bosai/jmatile/data/risk/yyyymmddHHMMSS/immed0/yyyymmddHHMMSS/surf/flood{z}/{x}/{y}.pbf
