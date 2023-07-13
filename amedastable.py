import requests
import pandas as pd

data = requests.get('https://www.jma.go.jp/bosai/amedas/const/amedastable.json').json()

list_ = []
for key in data.keys():
  list_.append(data[key])

amedas = pd.DataFrame(list_)

amedas['amdno'] = data.keys()

amedas.lat = [x[0] + x[1]/60 for x in amedas.lat]

amedas.lon = [x[0] + x[1]/60 for x in amedas.lon]

amedas.to_csv('amedastable.csv',index=False,encoding='utf-8-sig')
