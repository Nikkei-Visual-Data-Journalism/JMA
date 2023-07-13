import requests
import pandas as pd
from datetime import datetime,timedelta

data = pd.DataFrame(requests.get('https://www.jma.go.jp/bosai/information/data/information.json').json())

heat = data[data.controlTitle == '熱中症警戒アラート'].reset_index(drop=True)

heat.targetDatetime = pd.to_datetime(heat.targetDatetime)

jst = datetime.today() + timedelta(hours=9)

heat = heat[heat.targetDatetime >= jst.strftime('%Y-%m-%d %H:00:00')].reset_index(drop=True)

area = pd.read_csv('https://github.com/Nikkei-Visual-Data-Journalism/JMA/raw/main/area.csv')

area = area[area.office.isin(heat.areaCode.astype(int))].reset_index(drop=True)

geojson = pd.DataFrame(requests.get('https://www.jma.go.jp/bosai/common/const/geojson/class10s.json').json()['features'])

geojson['code'] = [x['code'] for x in geojson['properties']]

geojson = geojson[geojson.code.isin(area.class10.astype(str))].reset_index(drop=True)

geojson.geometry = [str(x).replace("'",'"') for x in geojson.geometry]

geojson.to_csv('heat.csv',index=False,encoding='utf-8-sig')
