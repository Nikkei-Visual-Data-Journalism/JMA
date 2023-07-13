import requests
import pandas as pd

data = requests.get('https://www.jma.go.jp/bosai/common/const/area.json').json()

codes = [x for x in data['class10s']]

list_ = []
for code in codes:
  list_.append(data['class10s'][code])

class10s = pd.DataFrame(list_,index=codes).rename(columns={'parent':'office'}).drop(['children'],axis=1).rename_axis('class10')

codes = [x for x in data['offices']]

offices = pd.DataFrame()
for code in codes:
  offices = pd.concat([offices,pd.DataFrame(data['offices'][code])],ignore_index=True)

dic = pd.Series(codes,index=[data['offices'][x]['name'] for x in data['offices']]).to_dict()

offices['office'] = offices.name.map(dic)

offices = offices.rename(columns={'parent':'center','children':'class10'}).set_index('class10')

area = pd.concat([class10s,offices[['officeName','center']]],axis=1)

area.to_csv('area.csv',encoding='utf-8-sig')
