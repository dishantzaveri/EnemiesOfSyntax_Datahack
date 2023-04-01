

from urllib.request import urlopen, Request
from bs4 import BeautifulSoup, Comment
from selenium.webdriver.common.keys import Keys
import pandas as pd
import numpy as np
import time
import requests
import random
import re
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
keyword = "geeksforgeeks"
# chrome_part = "C:/Program Files/Google/Chrome/Application/chromedriver"
# driver = webdriver.Chrome(chrome_part)
driver.get("https://www.arabam.com/ikinci-el/otomobil?take=50")
header = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"}

# chrome_part = "C:/Program Files/Google/Chrome/Application/chromedriver"
# driver = webdriver.Chrome(chrome_part)
driver.get("https://www.arabam.com/ikinci-el/otomobil?take=50")
header = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"}
liste = []
a = 1
while a <=50:
    sayfamiz = driver.page_source
    # soup = BeautifulSoup(sayfamiz, "lxml") # sayfayı beautifulsoup ile parçaladık
    soup = BeautifulSoup(sayfamiz,  "html.parser") # sayfayı beautifulsoup ile parçaladık
    print(soup)
    s1 = soup.find("table", attrs = {"class":"table listing-table w100 border-grey2"})
    s2 = s1.find_all("tr", attrs = {"class":"listing-list-item pr should-hover bg-white"})
    for i in s2:
        link_sonu = i.a.get('href')
        link_basi = "https://www.arabam.com/"
        link = link_basi+link_sonu
        r1 = requests.get(link, headers = header)
        soup1 = BeautifulSoup(r1.content, "lxml")
        fiyat = soup1.find("span", {"class" : "color-red4 font-semi-big bold fl"})
        if fiyat == None:
            fiyat = soup1.find("span", {"class" : "color-red4 font-semi-big bold fl w66"})
            if fiyat == None:
                fiyat = "None"
        try:
            yer = soup1.find("p", attrs = {"class":"one-line-overflow font-default-minus pt4 color-black2018 bold"}).text
        except:
            yer = "None"
        try:
            ilan_no = soup1.find(text=re.compile("İlan No:"))
            ilan_no = ilan_no.findNext().text
        except:
            ilan_no = "None"
        try:
            ilan_tarihi = soup1.find(text=re.compile("İlan Tarihi:"))
            ilan_tarihi = ilan_tarihi.findNext().text
        except:
            ilan_tarihi = "None"
        try:
            marka = soup1.find(text=re.compile("Marka:"))
            marka = marka.findNext().text
        except:
            marka = "None"
        try:
            seri = soup1.find(text=re.compile("Seri:"))
            seri = seri.findNext().text
        except:
            seri = "None"
        try:
            model = soup1.find(text=re.compile("Model:"))
            model = model.findNext().text
        except:
            model = "None"
        try:
            yıl = soup1.find(text=re.compile("Yıl:"))
            yıl = yıl.findNext().text
        except:
            yıl = "None"
        try:
            yakıt = soup1.find(text=re.compile("Yakıt Tipi:"))
            yakıt = yakıt.findNext().text
        except:
            yakıt = "None"
        try:
            vites = soup1.find(text=re.compile("Vites Tipi:"))
            vites = vites.findNext().text
        except:
            vites = "None"
        try:
            km = soup1.find(text=re.compile("Kilometre:"))
            km = km.findNext().text
        except:
            km = "None"
        try:
            hacim = soup1.find(text=re.compile("Motor Hacmi:"))
            hacim = hacim.findNext().text
        except:
            hacim = "None"
        try:
            guc = soup1.find(text=re.compile("Motor Gücü:"))
            guc = guc.findNext().text
        except:
            guc = "None"
        try:
            kimden = soup1.find(text=re.compile("Kimden:"))
            kimden = kimden.findNext().text
        except:
            kimden = "None"
        try:
            takas = soup1.find(text=re.compile("Takasa Uygun:"))
            takas = takas.findNext().text
        except:
            takas = "None"
        try:
            boya_degisen = soup1.find(text=re.compile("Boya-değişen:"))
            boya_degisen = boya_degisen.findNext().text
        except:
            boya_degisen = "None"
        liste.append([fiyat.text,yer,ilan_no,ilan_tarihi, marka, seri, model, yıl, yakıt, vites, km, hacim, guc, kimden, takas, boya_degisen])
    a = a+ 1
    time.sleep(.5+2*random.random())

df = pd.DataFrame(liste)
df.columns = ["price","city", "announcement_no", "announcement_date", "make", "seri", "model", "year", "fuel", "gear_type", "km", "engine_size","horse_power","from_who","exchange","dye_parts replaced"]

df.to_csv('cars.csv')

df = pd.read_csv("cars.csv")
df

df.drop('Unnamed: 0', axis = 1, inplace = True)
df.drop('Unnamed: 0.1', axis = 1, inplace = True)

df.head(10)

df.info()

"""# Data Preprocessing"""

df["city"]=df["city"].str.split("/", n=1, expand=True )
df["engine_size"]=df["engine_size"].str.split("-", n=1, expand=True)
df["horse_power"]=df["horse_power"].str.split("-", n=1, expand=True)
df["fuel"]=df["fuel"].str.split("&", n=1, expand=True)

df['price']=df.price.str.strip()
df['city']=df.city.str.strip()
df['announcement_date']=df.announcement_date.str.strip()
df['make']=df.make.str.strip()
df['seri']=df.seri.str.strip()
df['model']=df.model.str.strip()
df['fuel']=df.fuel.str.strip()
df['gear_type']=df.gear_type.str.strip()
df['km']=df.km.str.strip()
df['engine_size']=df.engine_size.str.strip()
df['horse_power']=df.horse_power.str.strip()
df['from_who']=df.from_who.str.strip()
df['exchange']=df.exchange.str.strip()
df['dye_parts replaced']=df.exchange.str.strip()

df["price"]=df["price"].str.replace("TL","")
df["km"]=df["km"].str.replace("km","")
df["engine_size"]=df["engine_size"].str.replace("cc","")
df["horse_power"]=df["horse_power"].str.replace("hp","")
df["horse_power"]=df["horse_power"].str.replace("HP","")
df["horse_power"]=df["horse_power"].str.replace("50 HP'ye kadar","")
df["horse_power"]=df["horse_power"].str.replace("50 'ye kadar","")
df["price"]=df["price"].str.replace(".","")
df["km"]=df["km"].str.replace(".","")
df["engine_size"]=df["engine_size"].str.replace("cm3' e kadar","")
df["from_who"]=df["from_who"].str.replace("Yetkili Bayiden","authorized dealer")
df["from_who"]=df["from_who"].str.replace("Sahibinden","owner")
df["from_who"]=df["from_who"].str.replace("Galeriden","gallery")
df["gear_type"]=df["gear_type"].str.replace("Düz","manuel")
df["gear_type"]=df["gear_type"].str.replace("Otomatik","automatic")
df["fuel"]=df["fuel"].str.replace("Dizel","Diesel")
df["fuel"]=df["fuel"].str.replace("Benzin","Fuel")
df["fuel"]=df["fuel"].str.replace("LPG & Benzing","LPG")
df["gear_type"]=df["gear_type"].str.replace("Yarı automatic","semi-automatic")

# Dropping NaN
df = df.replace("None", np.NaN)
df = df.replace("-", np.NaN)
df = df.replace(" ", np.NaN)
df = df.replace("", np.NaN)
df = df.dropna(how = 'any')

# Dropping different type money
patternGBP = "GBP"

GBP = df['price'].str.contains(patternGBP)

df = df[~GBP]

# Converting Type
df['price']=df['price'].astype(int)
df['km']=df['km'].astype(int)
df['engine_size']=df['engine_size'].astype(int)
df['horse_power']=df['horse_power'].astype(int)

# Drop columns
df.drop(columns=["announcement_no"], inplace=True)
df.drop(columns=["announcement_date"], inplace=True)
df.drop(columns=["model"], inplace=True)
df.drop(columns=["seri"], inplace=True)
df.drop(columns=["dye_parts replaced"], inplace=True)

df.set_index('price').sort_values('city')

df.info()

df.to_pickle("last_cars")

df = pd.read_pickle("last_cars")

df2 = df.loc[df['price'] <= 500000,:]
df1 = df2.loc[df['price'] >= 5000,:]

"""# Exploratory Data Analysis"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
import chart_studio.plotly as py
import cufflinks as cf
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt
# %matplotlib inline
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import requests
import json

from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
init_notebook_mode(connected=True)
cf.go_offline()

price_make1 = df.groupby('make')[['make','price']].mean().sort_values(by='price',ascending=True).reset_index()
price_make2 = df1.groupby('make')[['make','price']].mean().sort_values(by='price',ascending=True).reset_index()

fig = px.sunburst(price_make1, path=['price', 'make'], values='price',
                  color='price',
                  color_continuous_scale='RdBu',)
fig.update_layout(title_text="Price and Make",title_x=0.5, font_size=15)
fig.show()

fig = px.sunburst(price_make2, path=['price', 'make'], values='price',
                  color='price',
                  color_continuous_scale='RdBu',)
fig.update_layout(title_text="Price and Make After Drop Price",title_x=0.5, font_size=15)
fig.show()

sns.heatmap(df1.corr(), cmap="seismic", annot=True, vmin=-1, vmax=1);

#Pairplot 
plt.figure(1, figsize=(18, 7))
sns.set(style="whitegrid")
g=sns.pairplot(df1, height=1.2, aspect=1.5)
plt.yticks(rotation=90); 
plt.show()

cities = df.groupby('city')[['city','price']].mean().sort_values(by='city',ascending=True).reset_index()
cities = pd.DataFrame(cities)
cities['city']=cities['city'].str.capitalize()
cities['city']=cities.city.str.strip()
cities

cities.loc[cities['city'] == 'Adiyaman'] = cities.loc[cities['city']
                                                == 'Adiyaman'].replace('Adiyaman', 'Adıyaman')
cities.loc[cities['city'] == 'Afyonkarahi̇sar'] = cities.loc[cities['city']
                                                == 'Afyonkarahi̇sar'].replace('Afyonkarahi̇sar', 'Afyon')
cities.loc[cities['city'] == 'Artvi̇n'] = cities.loc[cities['city']
                                                == 'Artvi̇n'].replace('Artvi̇n', 'Artvin')
cities.loc[cities['city'] == 'Aydin'] = cities.loc[cities['city']
                                                == 'Aydin'].replace('Aydin', 'Aydın')
cities.loc[cities['city'] == 'Ağri'] = cities.loc[cities['city']
                                                == 'Ağri'].replace('Ağri', 'Ağrı')
cities.loc[cities['city'] == 'Balikesi̇r'] = cities.loc[cities['city']
                                                == 'Balikesi̇r'].replace('Balikesi̇r', 'Balıkesir')
cities.loc[cities['city'] == 'Bartin'] = cities.loc[cities['city']
                                                == 'Bartin'].replace('Bartin', 'Bartın')
cities.loc[cities['city'] == 'Bi̇leci̇k'] = cities.loc[cities['city']
                                                == 'Bi̇leci̇k'].replace('Bi̇leci̇k', 'Bilecik')
cities.loc[cities['city'] == 'Bi̇ngöl'] = cities.loc[cities['city']
                                                == 'Bi̇ngöl'].replace('Bi̇ngöl', 'Bingöl')
cities.loc[cities['city'] == 'Bi̇tli̇s'] = cities.loc[cities['city']
                                                == 'Bi̇tli̇s'].replace('Bi̇tli̇s', 'Bitlis')
cities.loc[cities['city'] == 'Deni̇zli̇'] = cities.loc[cities['city']
                                                == 'Deni̇zli̇'].replace('Deni̇zli̇', 'Denizli')
cities.loc[cities['city'] == 'Di̇yarbakir'] = cities.loc[cities['city']
                                                == 'Di̇yarbakir'].replace('Di̇yarbakir', 'Diyarbakır')
cities.loc[cities['city'] == 'Edi̇rne'] = cities.loc[cities['city']
                                                == 'Edi̇rne'].replace('Edi̇rne', 'Edirne')
cities.loc[cities['city'] == 'Elaziğ'] = cities.loc[cities['city']
                                                == 'Elaziğ'].replace('Elaziğ', 'Elazığ')
cities.loc[cities['city'] == 'Erzi̇ncan'] = cities.loc[cities['city']
                                                == 'Erzi̇ncan'].replace('Erzi̇ncan', 'Erzincan')
cities.loc[cities['city'] == 'Eski̇şehi̇r'] = cities.loc[cities['city']
                                                == 'Eski̇şehi̇r'].replace('Eski̇şehi̇r', 'Eskişehir')
cities.loc[cities['city'] == 'Gazi̇antep'] = cities.loc[cities['city']
                                                == 'Gazi̇antep'].replace('Gazi̇antep', 'Gaziantep')
cities.loc[cities['city'] == 'Gi̇resun'] = cities.loc[cities['city']
                                                == 'Gi̇resun'].replace('Gi̇resun', 'Giresun')
cities.loc[cities['city'] == 'Iğdir'] = cities.loc[cities['city']
                                                == 'Iğdir'].replace('Iğdir', 'Iğdır')
cities.loc[cities['city'] == 'Kayseri̇'] = cities.loc[cities['city']
                                                == 'Kayseri̇'].replace('Kayseri̇', 'Kayseri')
cities.loc[cities['city'] == 'Kirikkale'] = cities.loc[cities['city']
                                                == 'Kirikkale'].replace('Kirikkale', 'Kırıkkale')
cities.loc[cities['city'] == 'Kirklareli̇'] = cities.loc[cities['city']
                                                == 'Kirklareli̇'].replace('Kirklareli̇', 'Kırklareli')
cities.loc[cities['city'] == 'Kirşehi̇r'] = cities.loc[cities['city']
                                                == 'Kirşehi̇r'].replace('Kirşehi̇r', 'Kırşehir')
cities.loc[cities['city'] == 'Kocaeli̇'] = cities.loc[cities['city']
                                                == 'Kocaeli̇'].replace('Kocaeli̇', 'Kocaeli')
cities.loc[cities['city'] == 'Ki̇li̇s'] = cities.loc[cities['city']
                                                == 'Ki̇li̇s'].replace('Ki̇li̇s', 'Kilis')
cities.loc[cities['city'] == 'Mani̇sa'] = cities.loc[cities['city']
                                                == 'Mani̇sa'].replace('Mani̇sa', 'Manisa')
cities.loc[cities['city'] == 'Mardi̇n'] = cities.loc[cities['city']
                                                == 'Mardi̇n'].replace('Mardi̇n', 'Mardin')
cities.loc[cities['city'] == 'Mersi̇n'] = cities.loc[cities['city']
                                                == 'Mersi̇n'].replace('Mersi̇n', 'Mersin')
cities.loc[cities['city'] == 'Nevşehi̇r'] = cities.loc[cities['city']
                                                == 'Nevşehi̇r'].replace('Nevşehi̇r', 'Nevşehir')
cities.loc[cities['city'] == 'Ni̇ğde'] = cities.loc[cities['city']
                                                == 'Ni̇ğde'].replace('Ni̇ğde', 'Niğde')
cities.loc[cities['city'] == 'Osmani̇ye'] = cities.loc[cities['city']
                                                == 'Osmani̇ye'].replace('Osmani̇ye', 'Osmaniye')
cities.loc[cities['city'] == 'Ri̇ze'] = cities.loc[cities['city']
                                                == 'Ri̇ze'].replace('Ri̇ze', 'Rize')
cities.loc[cities['city'] == 'Si̇nop'] = cities.loc[cities['city']
                                                == 'Si̇nop'].replace('Si̇nop', 'Sinop')
cities.loc[cities['city'] == 'Si̇vas'] = cities.loc[cities['city']
                                                == 'Si̇vas'].replace('Si̇vas', 'Sivas')
cities.loc[cities['city'] == 'Si̇i̇rt'] = cities.loc[cities['city']
                                                == 'Si̇i̇rt'].replace('Si̇i̇rt', 'Siirt')
cities.loc[cities['city'] == 'Teki̇rdağ'] = cities.loc[cities['city']
                                                == 'Teki̇rdağ'].replace('Teki̇rdağ', 'Tekirdağ')
cities.loc[cities['city'] == 'Çankiri'] = cities.loc[cities['city']
                                                == 'Çankiri'].replace('Çankiri', 'Çankırı')
cities.loc[cities['city'] == 'İzmi̇r'] = cities.loc[cities['city']
                                                == 'İzmi̇r'].replace('İzmi̇r', 'İzmir')
cities.loc[cities['city'] == 'Şanliurfa'] = cities.loc[cities['city']
                                                == 'Şanliurfa'].replace('Şanliurfa', 'Şanlıurfa')
cities.loc[cities['city'] == 'Şirnak'] = cities.loc[cities['city']
                                                == 'Şirnak'].replace('Şirnak', 'Şırnak')
cities.tail(60)

response = requests.get(
    'https://gist.githubusercontent.com/mebaysan/9be56dd1ca5659c0ff7ea5e2b5cf6479/raw/6d7a77d8a2892bd59f401eb87bd82d7f48642a58/turkey-geojson.json')

geojson = response.json()

geojson['features']

geojson['features'][0]

geojson['features'][0]['id']

geojson['features'][0]['properties']['name']

geoDict={}

for i in geojson['features']:
    geoDict[i['properties']['name']]=i['id']

geoDict

cities['city']=cities.city.str.strip()

cities['GeoID'] = cities['city'].apply(lambda x: geoDict[x])

cities.head(1)

fig = px.choropleth(cities,  # hangi veri seti
                    geojson=geojson,  # hangi geojson dosyası
                    locations='city',  # featureidkey ile belirtilen özelliğe denk gelen değişken
                    # locations değişkeni ile geojson'daki hangi özelliği bağlayacağız
                    featureidkey='properties.name',
                    color='price',  # hangi Değişkene göre renk paleti
                    color_continuous_scale="Viridis",  # hangi renk paleti
                    # renklendirme için min ve max değerler aralığı
                    #range_color=(df['price'].mean(),
                    #             df['price'].mean()),
                    # map başlangıç lat & lon
                    center={'lat': 38.7200, 'lon': 34.0000},
                    custom_data=[cities['city'],
                                        cities['price']]  # figure'e göndereceğimiz ekstra veriler
                    )
fig.update_geos(fitbounds="locations",  # harita sınırları
                visible=False  # sınırların gözüküp gözükmemesi
                )
fig.update_layout(title="Cities Car's price",  # figure başlığı
                  title_x=0.5  # Title'ın x eksenindeki pozisyonu
                  )

#  gönderdiğimiz customdata'nın ilk elemanı
hovertemp = '<i>Şehir Adı:</i> %{customdata[0]}<br>'
hovertemp += '<i>Şehir Statüsü:</i> %{customdata[1]}<br>'
# figure üzerine gelince oluşturduğum stringi göster
fig.update_traces(hovertemplate=hovertemp)
fig.show()

fig = px.choropleth_mapbox(cities,  # hangi veri seti
                           geojson=geojson,  # hangi geojson dosyası
                           locations='GeoID',  # geojson dosyasında id'e denk gelen, veri setindeki hangi değişken
                           color='price',  # hangi Değişkene göre renk paleti
                           color_continuous_scale="Viridis",  # hangi renk paleti
                           # renklendirme için min ve max değerler aralığı
                           # map başlangıç lat & lon
                           center={'lat': 38.7200, 'lon': 34.0000},
                           # labellar değişecek mi
                           mapbox_style="carto-positron",  # mapbox stil
                           zoom=4.7,  # yakınlık
                           opacity=0.5,  # opacity
                           custom_data=[cities['city'],
                                        cities['price']]  # figure'e göndereceğimiz ekstra veriler
                           )
fig.update_layout(title="Cities Car's price",  # figure başlığı
                  title_x=0.5  # Title'ın x eksenindeki pozisyonu
                  )
#  gönderdiğimiz customdata'nın ilk elemanı
hovertemp = '<i>Şehir Adı:</i> %{customdata[0]}<br>'
hovertemp += '<i>Car price :</i> %{customdata[1]}<br>'
# figure üzerine gelince oluşturduğum stringi göster
fig.update_traces(hovertemplate=hovertemp)
fig.show()

fig = px.box(df1, x="make", y="engine_size", color="make")
fig.update_layout(title_text="Make and Engine Size",
                  title_x = 0.5, font_size=15)
fig.show()

fig = px.box(df1, x="from_who", y="price", color="from_who")
fig.update_layout(title_text="Cars from",
                    font_size=15)
fig.show()

fig = px.sunburst(df1, path=['gear_type', 'make'], values='price',
                  color='price', hover_data=['price'],
                  color_continuous_scale='RdBu')
                  #color_continuous_midpoint=np.average(df['transmission'], weights=df['transmission']))
fig.update_layout(title_text="Transmission type", title_x = 0.5,
                  font_size=15)
fig.show()

cars_2018 = df1.loc[df1['year'] >= 2018,:]
fig = px.sunburst(cars_2018, path=['gear_type', 'make'], values='price',
                  color='price', hover_data=['price'],
                  color_continuous_scale='RdBu')
                  #color_continuous_midpoint=np.average(df['transmission'], weights=df['transmission']))
fig.update_layout(title_text="Transmission type after 2018",title_x = 0.5,
                  font_size=15)
fig.show()

x = df['price']

fig = go.Figure()
fig.add_trace(go.Histogram(histfunc="count", y=y, x=x, name="price"))
fig.update_layout(title_text="Price",
                  title_x = 0.5, font_size=15)
fig.show()

x = df1['price']

fig = go.Figure()
fig.add_trace(go.Histogram(histfunc="count", y=y, x=x, name="price"))
fig.update_layout(title_text="Price",
                  title_x = 0.5, font_size=15)
fig.show()

"""# Modelling"""

import statsmodels.api as sm
import patsy
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.linear_model import Lasso
from pandas import Series, DataFrame
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from pandas import DataFrame,Series

y, X = patsy.dmatrices('price ~ year + km + engine_size + horse_power', data=df1, return_type="dataframe")

model = sm.OLS(y, X)

fit = model.fit()

print(fit.summary())

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.linear_model import Lasso
from pandas import Series, DataFrame
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score

cars = df1.select_dtypes(exclude=['object']).copy()
lm = LinearRegression()
x, y = cars.drop('price', axis=1), cars['price']
lm.fit(x, y)
lm.score(x,y)

### Future engineering
cars = df1.select_dtypes(exclude=['object']).copy()
cars['make']= df['make']
cars['brand']= df['make']
cars['gear_type']= df['gear_type']
cars['from_who']= df['from_who']
cars['fuel']= df['fuel']
cars['exchange']= df['exchange']
cars = pd.get_dummies(cars,columns=['brand'])
cars = pd.get_dummies(cars,columns=['gear_type'])
cars = pd.get_dummies(cars,columns=['from_who'])
cars = pd.get_dummies(cars,columns=['fuel'])
cars = pd.get_dummies(cars,columns=['exchange'])
cars['log_price']=np.log(cars.price)

### Future engineering
data = [cars]
for dataset in data:
    dataset['km'] = dataset['km'].astype(int)
    dataset.loc[dataset['km'] <= 1000, 'km'] = 0
    dataset.loc[(dataset['km'] > 1000) & (dataset['km'] <= 10000), 'km'] = 1
    dataset.loc[(dataset['km'] > 10000) & (dataset['km'] <= 20000), 'km'] = 2
    dataset.loc[(dataset['km'] > 20000) & (dataset['km'] <= 30000), 'km'] = 3
    dataset.loc[(dataset['km'] > 30000) & (dataset['km'] <= 40000), 'km'] = 4
    dataset.loc[(dataset['km'] > 40000) & (dataset['km'] <= 50000), 'km'] = 5
    dataset.loc[(dataset['km'] > 50000) & (dataset['km'] <= 60000), 'km'] = 6
    dataset.loc[(dataset['km'] > 60000) & (dataset['km'] <= 70000), 'km'] = 7
    dataset.loc[(dataset['km'] > 70000) & (dataset['km'] <= 80000), 'km'] = 8
    dataset.loc[(dataset['km'] > 80000) & (dataset['km'] <= 90000), 'km'] = 9
    dataset.loc[(dataset['km'] > 90000) & (dataset['km'] <= 100000), 'km'] = 10
    dataset.loc[(dataset['km'] > 100000) & (dataset['km'] <= 110000), 'km'] = 11
    dataset.loc[(dataset['km'] > 110000) & (dataset['km'] <= 120000), 'km'] = 12
    dataset.loc[(dataset['km'] > 120000) & (dataset['km'] <= 130000), 'km'] = 13
    dataset.loc[(dataset['km'] > 130000) & (dataset['km'] <= 140000), 'km'] = 14
    dataset.loc[(dataset['km'] > 140000) & (dataset['km'] <= 150000), 'km'] = 15
    dataset.loc[(dataset['km'] > 150000) & (dataset['km'] <= 160000), 'km'] = 16
    dataset.loc[(dataset['km'] > 160000) & (dataset['km'] <= 170000), 'km'] = 17
    dataset.loc[(dataset['km'] > 170000) & (dataset['km'] <= 180000), 'km'] = 18
    dataset.loc[(dataset['km'] > 180000) & (dataset['km'] <= 190000), 'km'] = 19
    dataset.loc[(dataset['km'] > 190000) & (dataset['km'] <= 200000), 'km'] = 20
    dataset.loc[(dataset['km'] > 200000) & (dataset['km'] <= 210000), 'km'] = 21
    dataset.loc[(dataset['km'] > 210000) & (dataset['km'] <= 220000), 'km'] = 22
    dataset.loc[(dataset['km'] > 220000) & (dataset['km'] <= 230000), 'km'] = 23
    dataset.loc[(dataset['km'] > 230000) & (dataset['km'] <= 240000), 'km'] = 24
    dataset.loc[(dataset['km'] > 240000) & (dataset['km'] <= 250000), 'km'] = 25
    dataset.loc[(dataset['km'] > 250000) & (dataset['km'] <= 260000), 'km'] = 26
    dataset.loc[(dataset['km'] > 260000) & (dataset['km'] <= 270000), 'km'] = 27
    dataset.loc[(dataset['km'] > 270000) & (dataset['km'] <= 280000), 'km'] = 28
    dataset.loc[(dataset['km'] > 280000) & (dataset['km'] <= 290000), 'km'] = 29
    dataset.loc[(dataset['km'] > 290000) & (dataset['km'] <= 300000), 'km'] = 30
    dataset.loc[(dataset['km'] > 300000) & (dataset['km'] <= 310000), 'km'] = 31
    dataset.loc[(dataset['km'] > 310000) & (dataset['km'] <= 320000), 'km'] = 32
    dataset.loc[(dataset['km'] > 320000) & (dataset['km'] <= 330000), 'km'] = 33
    dataset.loc[(dataset['km'] > 330000) & (dataset['km'] <= 340000), 'km'] = 34
    dataset.loc[(dataset['km'] > 340000) & (dataset['km'] <= 350000), 'km'] = 35
    dataset.loc[(dataset['km'] > 350000) & (dataset['km'] <= 360000), 'km'] = 36
    dataset.loc[(dataset['km'] > 360000) & (dataset['km'] <= 370000), 'km'] = 37
    dataset.loc[(dataset['km'] > 370000) & (dataset['km'] <= 380000), 'km'] = 38
    dataset.loc[(dataset['km'] > 380000) & (dataset['km'] <= 390000), 'km'] = 39
    dataset.loc[(dataset['km'] > 390000) & (dataset['km'] <= 400000), 'km'] = 40
    dataset.loc[(dataset['km'] > 400000) & (dataset['km'] <= 410000), 'km'] = 41
    dataset.loc[(dataset['km'] > 410000) & (dataset['km'] <= 420000), 'km'] = 42
    dataset.loc[(dataset['km'] > 420000) & (dataset['km'] <= 430000), 'km'] = 43
    dataset.loc[(dataset['km'] > 430000) & (dataset['km'] <= 440000), 'km'] = 44
    dataset.loc[(dataset['km'] > 440000) & (dataset['km'] <= 450000), 'km'] = 45
    dataset.loc[(dataset['km'] > 450000) & (dataset['km'] <= 460000), 'km'] = 46
    dataset.loc[(dataset['km'] > 460000) & (dataset['km'] <= 470000), 'km'] = 47
    dataset.loc[(dataset['km'] > 470000) & (dataset['km'] <= 480000), 'km'] = 48
    dataset.loc[(dataset['km'] > 480000) & (dataset['km'] <= 490000), 'km'] = 49
    dataset.loc[(dataset['km'] > 490000) & (dataset['km'] <= 500000), 'km'] = 50
    dataset.loc[(dataset['km'] > 500000) & (dataset['km'] <= 510000), 'km'] = 51
    dataset.loc[(dataset['km'] > 510000) & (dataset['km'] <= 520000), 'km'] = 52
    dataset.loc[(dataset['km'] > 520000) & (dataset['km'] <= 530000), 'km'] = 53
    dataset.loc[(dataset['km'] > 530000) & (dataset['km'] <= 540000), 'km'] = 54
    dataset.loc[(dataset['km'] > 540000) & (dataset['km'] <= 550000), 'km'] = 55
    dataset.loc[(dataset['km'] > 550000) & (dataset['km'] <= 560000), 'km'] = 56
    dataset.loc[(dataset['km'] > 560000) & (dataset['km'] <= 570000), 'km'] = 57
    dataset.loc[(dataset['km'] > 570000) & (dataset['km'] <= 580000), 'km'] = 58
    dataset.loc[(dataset['km'] > 580000) & (dataset['km'] <= 590000), 'km'] = 59
    dataset.loc[(dataset['km'] > 590000) & (dataset['km'] <= 600000), 'km'] = 60
    dataset.loc[(dataset['km'] > 600000) & (dataset['km'] <= 610000), 'km'] = 61
    dataset.loc[(dataset['km'] > 610000) & (dataset['km'] <= 620000), 'km'] = 62
    dataset.loc[(dataset['km'] > 620000) & (dataset['km'] <= 630000), 'km'] = 53
    dataset.loc[(dataset['km'] > 630000) & (dataset['km'] <= 640000), 'km'] = 64
    dataset.loc[(dataset['km'] > 640000) & (dataset['km'] <= 650000), 'km'] = 65

### Future engineering
data = [cars]
for dataset in data:
    dataset['engine_size'] = dataset['engine_size'].astype(float)
    dataset.loc[dataset['engine_size'] <= 1000, 'engine_size'] = 1.0
    dataset.loc[(dataset['engine_size'] > 1000) & (dataset['engine_size'] <= 1100), 'engine_size'] = 1.1
    dataset.loc[(dataset['engine_size'] > 1100) & (dataset['engine_size'] <= 1200), 'engine_size'] = 1.2
    dataset.loc[(dataset['engine_size'] > 1200) & (dataset['engine_size'] <= 1300), 'engine_size'] = 1.3
    dataset.loc[(dataset['engine_size'] > 1300) & (dataset['engine_size'] <= 1400), 'engine_size'] = 1.4
    dataset.loc[(dataset['engine_size'] > 1400) & (dataset['engine_size'] <= 1500), 'engine_size'] = 1.5
    dataset.loc[(dataset['engine_size'] > 1500) & (dataset['engine_size'] <= 1600), 'engine_size'] = 1.6
    dataset.loc[(dataset['engine_size'] > 1600) & (dataset['engine_size'] <= 1800), 'engine_size'] = 1.8
    dataset.loc[(dataset['engine_size'] > 1800) & (dataset['engine_size'] <= 2000), 'engine_size'] = 2.0
    dataset.loc[(dataset['engine_size'] > 2000) & (dataset['engine_size'] <= 2100), 'engine_size'] = 2.1
    dataset.loc[(dataset['engine_size'] > 2100) & (dataset['engine_size'] <= 2200), 'engine_size'] = 2.2
    dataset.loc[(dataset['engine_size'] > 2200) & (dataset['engine_size'] <= 2300), 'engine_size'] = 2.3
    dataset.loc[(dataset['engine_size'] > 2300) & (dataset['engine_size'] <= 2400), 'engine_size'] = 2.4
    dataset.loc[(dataset['engine_size'] > 2400) & (dataset['engine_size'] <= 2500), 'engine_size'] = 2.5
    dataset.loc[(dataset['engine_size'] > 2500) & (dataset['engine_size'] <= 2600), 'engine_size'] = 2.6
    dataset.loc[(dataset['engine_size'] > 2600) & (dataset['engine_size'] <= 2700), 'engine_size'] = 2.7
    dataset.loc[(dataset['engine_size'] > 2700) & (dataset['engine_size'] <= 2800), 'engine_size'] = 2.8
    dataset.loc[(dataset['engine_size'] > 2800) & (dataset['engine_size'] <= 2900), 'engine_size'] = 2.9
    dataset.loc[(dataset['engine_size'] > 2900) & (dataset['engine_size'] <= 3000), 'engine_size'] = 3.0
    dataset.loc[(dataset['engine_size'] > 3000) & (dataset['engine_size'] <= 3100), 'engine_size'] = 3.1
    dataset.loc[(dataset['engine_size'] > 3100) & (dataset['engine_size'] <= 3200), 'engine_size'] = 3.2
    dataset.loc[(dataset['engine_size'] > 3200) & (dataset['engine_size'] <= 3300), 'engine_size'] = 3.3
    dataset.loc[(dataset['engine_size'] > 3300) & (dataset['engine_size'] <= 3400), 'engine_size'] = 3.4
    dataset.loc[(dataset['engine_size'] > 3400) & (dataset['engine_size'] <= 3500), 'engine_size'] = 3.5
    dataset.loc[(dataset['engine_size'] > 3500) & (dataset['engine_size'] <= 3600), 'engine_size'] = 3.6
    dataset.loc[(dataset['engine_size'] > 3600) & (dataset['engine_size'] <= 3700), 'engine_size'] = 3.7
    dataset.loc[(dataset['engine_size'] > 3700) & (dataset['engine_size'] <= 3800), 'engine_size'] = 3.8
    dataset.loc[(dataset['engine_size'] > 3800) & (dataset['engine_size'] <= 3900), 'engine_size'] = 3.9
    dataset.loc[(dataset['engine_size'] > 3900) & (dataset['engine_size'] <= 4000), 'engine_size'] = 4.0
    dataset.loc[(dataset['engine_size'] > 4000) & (dataset['engine_size'] <= 4100), 'engine_size'] = 4.1
    dataset.loc[(dataset['engine_size'] > 4100) & (dataset['engine_size'] <= 4200), 'engine_size'] = 4.2
    dataset.loc[(dataset['engine_size'] > 4200) & (dataset['engine_size'] <= 4300), 'engine_size'] = 4.3
    dataset.loc[(dataset['engine_size'] > 4300) & (dataset['engine_size'] <= 4400), 'engine_size'] = 4.4
    dataset.loc[(dataset['engine_size'] > 4400) & (dataset['engine_size'] <= 4500), 'engine_size'] = 4.5
    dataset.loc[(dataset['engine_size'] > 4500) & (dataset['engine_size'] <= 4600), 'engine_size'] = 4.6
    dataset.loc[(dataset['engine_size'] > 4600) & (dataset['engine_size'] <= 4700), 'engine_size'] = 4.7
    dataset.loc[(dataset['engine_size'] > 4700) & (dataset['engine_size'] <= 4800), 'engine_size'] = 4.8
    dataset.loc[(dataset['engine_size'] > 4800) & (dataset['engine_size'] <= 4900), 'engine_size'] = 4.9
    dataset.loc[(dataset['engine_size'] > 4900) & (dataset['engine_size'] <= 5000), 'engine_size'] = 5.0
    dataset.loc[(dataset['engine_size'] > 5000) & (dataset['engine_size'] <= 5100), 'engine_size'] = 5.1
    dataset.loc[(dataset['engine_size'] > 5100) & (dataset['engine_size'] <= 5200), 'engine_size'] = 5.2
    dataset.loc[(dataset['engine_size'] > 5200) & (dataset['engine_size'] <= 5300), 'engine_size'] = 5.3
    dataset.loc[(dataset['engine_size'] > 5300) & (dataset['engine_size'] <= 5400), 'engine_size'] = 5.4
    dataset.loc[(dataset['engine_size'] > 5400) & (dataset['engine_size'] <= 5500), 'engine_size'] = 5.5
    dataset.loc[(dataset['engine_size'] > 5500) & (dataset['engine_size'] <= 5600), 'engine_size'] = 5.6
    dataset.loc[(dataset['engine_size'] > 5600) & (dataset['engine_size'] <= 5700), 'engine_size'] = 5.7

cars

x = cars['price']
y = cars['log_price']

fig = go.Figure()
fig.add_trace(go.Histogram(histfunc="count", y=y, x=x, name="price"))
fig.add_trace(go.Histogram(histfunc="sum", y=y, x=x, name="log_price"))
fig.update_layout(title_text="Price vs. Log.Price",
                  title_x = 0.5, font_size=15)
fig.show()

cars.drop('price', axis = 1, inplace = True)

car = cars.select_dtypes(exclude=['object']).copy()
X, y = car.drop('log_price', axis=1), car['log_price']

model = sm.OLS(y, X)

fit = model.fit()

print(fit.summary())

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from pandas import DataFrame,Series

def linear_regression(x,y):
    
    model = LinearRegression()
    model.fit(x,y)
    predict = model.predict(x)
    mse = np.mean((y-predict)**2)
    
    #result = pd.DataFrame({'Actual':y, 'Predicted':predict})
    #result.plot(kind='line', figsize=(16,10))
    
    print("Model score : ", model.score(x,y))
    print('MSE : ',mse)
    coeff = DataFrame(x.columns)
    
    coeff['Coef est'] = Series(model.coef_)
    print(coeff.sort_values(by='Coef est',ascending=False))

x, y = car.drop('log_price', axis=1), car['log_price']
linear_regression(x,y)

reg = LinearRegression()
reg.fit(X,y)
coeff_df = pd.DataFrame(regressor.coef_, X.columns, columns=['Coefficient'])  
coeff_df.sort_values("Coefficient",ascending=False)

y_pred = lr.predict(X)
df3 = pd.DataFrame({'Name':cars.make,'Actual': y, 'Predicted': (y_pred)})
df3["Difference"] = df3["Actual"]-df3["Predicted"]
df3

#Split data into train, test and validation (%60 - %20)

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2, random_state=10)

X_train, X_val, y_train, y_val = train_test_split(X,y, test_size=.25, random_state=10)

lr = LinearRegression()
lr.fit(X_train,y_train)
pred = lr.predict(X_val)
mse = np.mean((pred-y_val)**2)

print(lr.score(X_test,y_test))
print(mse)

# Comparing 4 model
Xs, ys = car.drop('log_price', axis=1), car['log_price']

X, X_test, y, y_test = train_test_split(Xs,ys,test_size=0.2, random_state=10)

X_train, X_val, y_train, y_val = train_test_split(X,y, test_size=.25, random_state=10)


lm = LinearRegression()

#Feature scaling for train, val, and test so that we can run our ridge model on each
scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train.values)
X_val_scaled = scaler.transform(X_val.values)
X_test_scaled = scaler.transform(X_test.values)

lm_reg = Ridge(alpha=0.05, normalize=True)

lm_lasso = Lasso(alpha=0.05, normalize=True)

#Feature transforms for train, val, and test so that we can run our poly model on each
poly = PolynomialFeatures(degree=2) 

Xs_poly = poly.fit_transform(X.values)
X_train_poly = poly.fit_transform(X_train.values)
X_val_poly = poly.transform(X_val.values)
X_test_poly = poly.transform(X_test.values)

lm_poly = LinearRegression()

lm.fit(X_train, y_train)
print(f'Linear Regression for all data R^2: {lm.score(Xs, ys):.6f}')
print(f'Linear Regression for test data R^2: {lm.score(X_test, y_test):.6f}')
print(f'Linear Regression for validation data R^2: {lm.score(X_val, y_val):.6f}')
print("")

lm_reg.fit(X_train_scaled, y_train)
print(f'Ridge Regression for test data R^2: {lm_reg.score(X_test_scaled, y_test):.6f}')
print(f'Ridge Regression for validation data R^2: {lm_reg.score(X_val_scaled, y_val):.6f}')
print("")


lm_lasso.fit(X_train,y_train)
print(f'Lasso Regression for test data R^2: {lm_lasso.score(X_test, y_test):.6f}')
print(f'Lasso Regression for validation data R^2: {lm_lasso.score(X_val, y_val):.6f}')
print("")

lm_poly.fit(X_train_poly, y_train)
print(f'Degree 2 polynomial regression for test data R^2: {lm_poly.score(X_test_poly, y_test):.6f}')
print(f'Degree 2 polynomial regression for validation data R^2: {lm_poly.score(X_val_poly, y_val):.6f}')

# Run Cross Validation
kf = KFold(n_splits=10, shuffle=True, random_state = 16)
cross_val_score(lm, Xs, ys, cv=kf, scoring='r2')

print('Linear Regression:',round(np.mean(cross_val_score(lm, Xs, ys, cv=kf, scoring='r2')),5))
print('Ridge Regression:',round(np.mean(cross_val_score(lm_reg, Xs, ys, cv=kf, scoring='r2')),5))
print('Lasso Regression:',round(np.mean(cross_val_score(lm_lasso, Xs, ys, cv=kf, scoring='r2')),5))
print('Degree 2 Poly. Regression:',round(np.mean(cross_val_score(lm_poly, Xs, ys, cv=kf, scoring='r2')),5))

# Regression Fit with Log
plt.figure(figsize=(10,6),dpi=150),
lr = LinearRegression()
fit = lr.fit(X,y);
pred = lr.predict(X)
plt.scatter(pred,y)
plt.title("Actual Value (log) vs Predicted Value (log)")
plt.xlabel("Predicted Value (log)")
plt.ylabel("Actual Value (log)")
plt.show()

plt.figure(figsize=(10,6),dpi=150),
lr = LinearRegression()
fit = lr.fit(X,np.exp(y));
pred = lr.predict(X)
sns.regplot(x=pred,y=np.exp(y),data=cars)
plt.title("Actual Value vs Predicted Value")
plt.xlabel("Predicted Value")
plt.ylabel("Actual Value")
plt.show()

