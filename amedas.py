import requests
import pandas as pd
from datetime import datetime,timedelta

amedastable = pd.read_csv('https://github.com/Nikkei-Visual-Data-Journalism/JMA/raw/main/amedastable.csv',index_col='amdno')

jst = datetime.today() + timedelta(hours=9)

data = requests.get('https://www.jma.go.jp/bosai/amedas/data/map/'+jst.strftime('%Y%m%d%H') + '0000'+'.json').json()

list_ = []
for amdno in amedastable.index.astype(str):
  list_.append(data[amdno])

amedas = pd.DataFrame(list_)

amedas['amdno'] = amedastable.index

temp = pd.concat([amedastable,amedas.set_index('amdno')['temp']],axis=1).dropna(subset=['temp'])

temp.temp = [x[0] for x in temp.temp]

temp = temp.rename(columns={'kjName':'地名','temp':'気温'})

temp.to_csv('temp.csv',encoding='utf-8-sig')

precipitation1h = pd.concat([amedastable,amedas.set_index('amdno')['precipitation1h']],axis=1).dropna(subset=['precipitation1h'])

precipitation1h.precipitation1h = [x[0] for x in precipitation1h.precipitation1h]

precipitation1h.to_csv('precipitation1h.csv',encoding='utf-8-sig')

precipitation24h = pd.concat([amedastable,amedas.set_index('amdno')['precipitation24h']],axis=1).dropna(subset=['precipitation24h'])

precipitation24h.precipitation24h = [x[0] for x in precipitation24h.precipitation24h]

precipitation24h.to_csv('precipitation24h.csv',encoding='utf-8-sig')
