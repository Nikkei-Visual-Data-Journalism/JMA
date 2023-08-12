import pandas as pd

df = pd.read_csv('https://www.data.jma.go.jp/stats/data/mdrr/tem_rct/alltable/mxtemsadext00_rct.csv',
                 encoding='Shift-JIS',
                 dtype={'観測所番号':'str','今日の最高気温起時（時）':'str','今日の最高気温起時（分）':'str','今日の最高気温(℃)':'float'})

amdno = pd.read_csv('https://github.com/Nikkei-Visual-Data-Journalism/JMA/raw/main/amedastable.csv',
                    dtype={'amdno':'str','lat':'float','lon':'float'}).set_index('amdno')

df['lat'] = df['観測所番号'].map(amdno['lat'].to_dict())

df['lon'] = df['観測所番号'].map(amdno['lon'].to_dict())

df['観測所'] = df['観測所番号'].map(amdno['kjName'].to_dict())

df['都道府県'] = df['観測所番号'].map(amdno['pref'].to_dict())

df['時間'] = df['今日の最高気温起時（時）'] + '時' + df['今日の最高気温起時（分）'] + '分'

df = df.rename(columns={'今日の最高気温(℃)':'気温'})

df[['観測所','都道府県','lat','lon','時間','気温']].to_csv('maxtem.csv',index=False,encoding='utf-8-sig')

df[df['今年最高'] == '1'].reset_index(drop=True)[['観測所','lat','lon','時間','気温']].to_csv('yearhigh.csv',index=False,encoding='utf-8-sig')

df[df['気温'] >= 35].reset_index(drop=True)[['観測所','lat','lon','時間','気温']].to_csv('above35.csv',index=False,encoding='utf-8-sig')
