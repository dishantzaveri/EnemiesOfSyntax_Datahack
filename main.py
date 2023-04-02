import numpy as np
import pandas as pd
import streamlit as st
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
import random
from PIL import Image
import numpy as np
from tensorflow.keras.layers import MaxPooling2D

from IPython.display import Image
from keras import optimizers
from keras.models import Sequential, load_model, Model
from keras.layers import Convolution2D, MaxPooling2D, ZeroPadding2D, Activation, Dense, Dropout, Flatten
#import #paddleocr
from keras.preprocessing.image import array_to_img, img_to_array, load_img
from keras.regularizers import l2, l1
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import KFold
import scipy
import scipy.sparse

from scipy.sparse import hstack
import requests
from sklearn.preprocessing import OneHotEncoder
import tensorflow as tf
from tensorflow.keras.layers import Dense, Input,Dropout,Flatten,concatenate
import tensorflow.keras
from tensorflow.keras.models import Model,load_model
from tensorflow.keras.layers import BatchNormalization

from tensorflow.keras import optimizers
from tensorflow.keras.metrics import mean_squared_logarithmic_error
import warnings
from torch.utils.data import DataLoader,TensorDataset,Dataset
warnings.filterwarnings("ignore")
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.tokenize import word_tokenize
import gc
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import tensorflow as tf


def pipeline(df_test):
    def one_hot_encoder(train_data):
        ohe_encoder = OneHotEncoder()
        train_ohe = ohe_encoder.fit_transform(train_data)    
        return train_ohe
    def SMLP(frame,i):    
        input = Input(shape=(frame.shape[1],),sparse=True,dtype='float32')
        output = Dense(i,activation='relu')(input)
        output = BatchNormalization()(output)
        if i==256:                      
            while i!=64:          
                i/=2           
                output = Dense(i,activation='relu')(output)                
        else:                      
            while i!=16:                      
                i/=2
                output = Dense(i,activation='relu')(output)  
        output = Dropout(0.2)(output)
        output = Dense(1)(output)
        model = Model(input,output)
        return model
    def text_encoder(training,type,params):
        '''
        Description -> Encoding different types of input text data according to its requirements using Countvectorizer
                       & Tfidfvectorizer and returning the transformed data as output
        '''
        if(type == "BOW"):
            vectorizer = CountVectorizer(ngram_range = params[0],min_df = params[1],max_df = params[2],max_features = params[3])
        elif(type == "TFIDF"):
            N_GRAMS =params
            vectorizer = vectorizer = TfidfVectorizer(max_features = 100000,
                                     ngram_range = (1, N_GRAMS),
                                     strip_accents = 'unicode',
                                     analyzer = 'word',
                                     token_pattern = r'\w+')
        elif(type=="CNTVECT"):
            vectorizer = CountVectorizer(vocabulary=params, lowercase=False, binary=True)

        train_transform = vectorizer.fit_transform(training)    
        if (type == "BOW"):
            return train_transform, ''
        elif (type == "CNTVECT"):
            return train_transform, ''
        elif (type == "TFIDF"):
            feat_names = vectorizer.get_feature_names_out()
            del vectorizer
            gc.collect()
            return train_transform, feat_names
    ocr_reader = paddleocr.PaddleOCR()
    result = ocr_reader.ocr(image)
    DL_text = ' '.join([word[1][0] for line in result for word in line])
    url = "https://vehicle-rc-information.p.rapidapi.com/"
    payload = {"VehicleNumber": result[0][0][1][0]}
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "0768fbb2bemsh0762c21b0ca177bp17cc16jsn578413086999",
        "X-RapidAPI-Host": "vehicle-rc-information.p.rapidapi.com"
    }
    response = requests.request("POST", url, json=payload, headers=headers)
    print(response.text)
    X_test_name,_ = text_encoder(df_test['Name'], "TFIDF", 2)
    X_test_Text,_ = text_encoder(df_test['text'], "TFIDF", 1)
    s1=one_hot_encoder(np.reshape(df_test['Seats'].values, (-1, 1)))
    o1=one_hot_encoder(np.reshape(df_test['Owner_Type'].values, (-1, 1)))
    t1=one_hot_encoder(np.reshape(df_test['Transmission'].values, (-1, 1)))
    f1=one_hot_encoder(np.reshape(df_test['Fuel_Type'].values, (-1, 1)))
    hotcodedtest = hstack((s1,o1,t1,f1)).tocsr().astype('float32')
    testframe = hstack((X_test_name,X_test_Text,hotcodedtest)).tocsr().astype('float32')
    return np.expm1(model1.predict(testframe)[:, 0])


# import data file csv
df = pd.read_csv('merc.csv')
# set page title
st.set_page_config('Price Prediction App')
col1, col2, col3 = st.columns(3)

with col1:
    st.write(' ')

with col2:
    st.image("logo.jpg")

with col3:
    st.write(' ')
#st.image('logo.jpg')

st.title('Predict M\Car Prices (in Euros)')
social_acc = ['About', 'Kaggle', 'Medium', 'LinkedIn']
social_acc_nav = st.sidebar.selectbox('About', social_acc)
if social_acc_nav == 'About':
    st.sidebar.markdown("<h2 style='text-align: center;'>CAR GPT</h2> ", unsafe_allow_html=True)
    st.sidebar.markdown('''---''')
    # st.sidebar.markdown('''
    # • Data Analytics (Python/SQL/Tableau) \n 
    # • Industrial Robotics (KUKA Robots) \n 
    # • Interned as a Data Engineer''')
    st.sidebar.markdown("[ ML Models](https://drive.google.com/drive/folders/1PxWZxr6TdD6cvp7HcNbnEol4W07YRawj?usp=sharing)")
    st.sidebar.markdown("[ Github Source Code](https://github.com/dishantzaveri/EnemiesOfSyntax_Datahack)")

elif social_acc_nav == 'Kaggle':
    st.sidebar.image('kaggle.jpg')
    st.sidebar.markdown("[Kaggle](https://www.kaggle.com/sarveshtalele)")

elif social_acc_nav == 'Medium':
    st.sidebar.image('medium.jpg')
    st.sidebar.markdown("[Click to read my blogs](https://wyverical.medium.com/)")

elif social_acc_nav == 'LinkedIn':
    st.sidebar.image('linkedin.jpg')
    st.sidebar.markdown("[Visit LinkedIn account](https://www.linkedin.com/in/sarvesh-talele-320356196/)")
menu_list = ['Exploratory Data Analysis', "Predict Price"]
menu = st.radio("Menu", menu_list)

if menu == 'Exploratory Data Analysis':
    st.title('Exploratory Data Analysis of Car Models ')

    if st.checkbox("View data"):
        st.write(df)

    st.video("https://youtu.be/YlBAKiUnp_Q")
    st.markdown('---')
    st.markdown("<h2 style='text-align: center;'> The Deduction Show!</h2>", unsafe_allow_html=True)
    st.markdown('---')
    st.markdown("<h3 style='text-align: left;'> Visualisation and Analysis</h3>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: left;'> A) Model v/s Miles per gallon</h4>", unsafe_allow_html=True)
    st.image('model_mpg.jpg')
    st.markdown("<h4 style='text-align: left;'> Insights </h4>", unsafe_allow_html=True)
    st.markdown('''
    The used car market is a significant and growing industry, with millions of used cars being sold every year. One of the biggest challenges for buyers and sellers is determining the fair market value of a used car, which can vary widely depending on a variety of factors, including make, model, year, mileage, and condition.''')

    st.markdown("<h4 style='text-align: left;'> B) Model v/s Mileage </h4>", unsafe_allow_html=True)
    st.image('model_mileage.jpg')
    st.markdown("<h4 style='text-align: left;'> Insights </h4>", unsafe_allow_html=True)
    st.markdown('''
    1.  According to a study conducted by Carfax, a vehicle with severe damage can lose upto 60 to 70% of it's pre-damaged value, while a vehicle with less scratches and dents loses about 10-25% of it's pre-damage price and a car moderately damaged may lose upto 40-50% of the same price.
    2.   However, when compared to the median value of our data, the Mercedes 
    CLK model has approximately **12.51%** higher miles, and altogether, the CLK model delivers
     **15.67%** mileage to the dataset.
    3.  Subsequently, an overall fuel consumption of CLK model is 3265.30 gallons at 33.6 miles per gallon. 
    4.  Hence, we can deduce that car models with higher mpg value has following applications 
    - Fuel consumption is reduced.
    -  Lower Maintenance Costs
    ''')

    st.markdown("<h4 style='text-align: left;'> C)  Model v/s Price </h4>", unsafe_allow_html=True)
    st.image('model_price.jpg')

    st.markdown("<h4 style='text-align: left;'>D)  Year v/s Price  </h4>", unsafe_allow_html=True)
    st.image('year_price.jpg')

    st.markdown("<h4 style='text-align: left;'> E) Mileage v/s Transmission </h4>", unsafe_allow_html=True)
    st.image('mileage_transmission.jpg')
    st.markdown("<h4 style='text-align: left;'> Insights </h4>", unsafe_allow_html=True)
    st.markdown('''
    1.  Manual Transmission has the most mileage of the three most recent transmission systems when compared 
    to the other transmission systems.
    - Manual transmissions include more gears and a simpler design, resulting in a lighter transmission system.
    - A simpler design decreases the car's annual fuel consumption and, as a result, the cost of maintenance.
    2.   The other category may include the following transmission systems (these are some of the examples 
    of transmission system)
    - **Tiptronic Transmission :**
    A tiptronic is a type of automatic transmission that allows for fully automatic gear shifting or manual
    gear shifting by the driver. Tiptronics use a torque converter rather than a clutch.
    - **Dual Clutch Transmission (DCT) :**
    A dual clutch transmission has two gear shafts with a clutch for each. The dual system allows for 
    faster and smoother gear changes.
    ''')

    st.markdown("<h4 style='text-align: left;'> F) Model v/s Tax </h4>", unsafe_allow_html=True)
    st.image('model_tax.jpg')
    st.markdown("<h4 style='text-align: left;'> Insights </h4>", unsafe_allow_html=True)
    st.markdown(''' **Road Tax Description**: \n
    1. It is a tax that must be paid by anybody who purchases a car. The Road Tax is a 
    state-level tax, meaning that it is imposed at the state level by the governments of several states.
    2. For charging the road tax, each state has its own set of rules and regulations. 
    The amount of tax varies due to the varied percentages charged by different states. 
    According to the Central Motor Vehicles Act, if a vehicle is operated for more than a year, 
    the entire amount of road tax must be paid at once. 
    3. Individuals purchasing a vehicle pay the road tax which is based on the ex-showroom price of the vehicle. 
    The calculation of road tax depends on these following things:\n
    a. Seating capacity of the vehicle \n
    b. Engine capacity of the vehicle \n
    c. Age of the vehicle \n
    d. Weight of the Vehicle \n
    *Note: This is according to Indian Rules and Regulations* \n
    **Analysis** \n
    1. Although the Mercedes C class has more advanced built-in technology, making 
    the C class interface more user-friendly, it has a far higher road tax than the Mercedes A class, by 9.29 percent.\n
    2. When it comes to miles per gallon and price, an A class vehicle would be a better choice than a C class model.\n
''')

    st.markdown("<h4 style='text-align: left;'> G) Fueltype v/s Mileage </h4>", unsafe_allow_html=True)
    st.image('mileage_fuel.jpg')
    st.markdown("<h4 style='text-align: left;'> Insights </h4>", unsafe_allow_html=True)
    st.markdown('''
    1. For long distance travel, diesel engines are recommended. For those who are Hodophile, 
    Mercedes automobile models with Diesel engines have a 79 percent probability of being their first preference. 
    2.  Diesel engines are limited for vehicles that have a high frequency of travel, such as trucks, buses, 
    and off-road vehicles, despite having higher efficiency and lower costs than petroleum. 
    Because of the increased green house gases, 
    diesel engines are limited for vehicles that have a high frequency of travel, such as trucks, buses, and 
    off-road vehicles.

    ''')

    st.markdown("<h2 style='text-align: left;'> Conclusion </h2>", unsafe_allow_html=True)
    st.markdown('''
    The deduction and statistical analysis determined with the full consideration of metrics of Mercedes 
    Model cars using the dataset. 
    The notebook have explored Transmission, Miles/gallon, Mileage and road tax metrics for better 
    comprehension of our dataset.  \n
    1. For those who want to buy a car for travel or daily use, the miles per gallon number should 
    be greater than 30 mpg.\n
    2. Mileage is another element that influences a vehicle's fuel usage. The cost of maintaining a car 
    is determined by its mileage.\n
    3. Manual transmissions have more gears and a simpler design, making them lighter.\n
    4. Diesel engines are restricted for vehicles that travel often, such as
 t  rucks, buses, and off-road vehicles, due to higher greenhouse gas emissions.''')

elif menu == 'Predict Price':

    model_dic = {'a class': 0, 'b class': 1, 'c class': 2, 'cl class': 3, 'cla class': 4, 'clc class': 5, 'clk': 6,
                 'cls class': 7, 'e class': 8, 'g class': 9, 'gl class': 10, 'gla class': 11, 'glb class': 12,
                 'glc class': 13, 'gle class': 14, 'gls class': 15, 'm class': 16, 'r class': 17, 's class': 18,
                 'sl class': 19, 'slk': 20, 'v class': 21, 'x-class': 22}
    transmission_dic = {'automatic': 0, 'manual': 1, 'other': 2, 'semi-auto': 3}
    fuel_dic = {'diesel': 0, 'hybrid': 1, 'other': 2, 'petrol': 3}

    model_list = [
        "SUV", "sedan", "compact"]
    transmission_list = ['automatic', 'manual', 'other', 'semi-auto']
    Owners_list = ['First', 'Second', 'Third', 'Fourth', 'Other']
    fuel_list = ['diesel', 'CNG', 'LPG', 'petrol']

    img1 = st.file_uploader("Add image 1", type=['png','jpeg','jpg'])
    img2 = st.file_uploader("Add image 2", type=['png','jpeg','jpg'])
    img3 = st.file_uploader("Add image 3", type=['png','jpeg','jpg'])
    img4 = st.file_uploader("Add image 4", type=['png','jpeg','jpg'])
    img5 = st.file_uploader("Add image 5", type=['png','jpeg','jpg'])

    year = st.slider("Enter the year", 1970, 2021)

    No_of_Kms = st.slider("Enter the kms driven", 0, 6500000)

    engine_size = st.number_input('Enter Engine Size  (range = 0 - 7)')

    model_choice = st.selectbox(label='What type is your car?', options=model_list)
    #models = model_dic[model_choice]

    transmission_choice = st.selectbox(label=' Select the Transmission type', options=transmission_list)
    transmissions = transmission_dic[transmission_choice]
    Owner_type = st.selectbox(label="What is the ownership type?", options= Owners_list)


    fuel_choice = st.selectbox(label='Select the Fuel type', options=fuel_list)
    #fuels = fuel_dic[fuel_choice]

    data = pd.read_csv('merc.csv')
    data['models'] = data['model'].str.strip()
    df = data.drop('model', axis='columns')

    OH_encoder = OneHotEncoder(sparse=False)
    encode_data = pd.DataFrame(OH_encoder.fit_transform(df[['transmission', 'fuelType']]))

    encode_data.columns = ['Automatic', 'Manual', 'Other', 'Semi-Auto', 'Diesel', 'Hybrid', 'Other', 'Petrol']

    merc_data = pd.concat([df, encode_data], axis=1)
    df1 = merc_data.drop(['transmission', 'fuelType', 'models'], axis='columns')
    df2 = pd.get_dummies(df.models)
    df3 = pd.concat([df1, df2], axis=1)
    X = df3.drop(['price', 'tax', 'mpg', 'mileage'], axis='columns')
    y = df3.price

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

    decision_tree = DecisionTreeRegressor()
    linear_reg = LinearRegression()

    decision_tree.fit(X_train.values, y_train.values)
    linear_reg.fit(X_train.values, y_train.values)

    decision_score = decision_tree.score(X_test.values, y_test.values)
    linear_score = linear_reg.score(X_test.values, y_test.values)
    column_data = X.columns.values


    def predict_price_decision(model, _year, engineSize, transmission, fuel):
        try:
            model_index = model_list.index(model)[0][0]
            transmission_index = transmission_list.index(transmission)[0][0]
            fuel_index = fuel_list.index(fuel)[0][0]
        except ValueError:
            model_index = -1
            fuel_index = -1
            transmission_index = -1

        x = np.zeros(len(column_data))
        x[0] = _year
        x[1] = engineSize
        if transmission_index >= 0:
            x[transmission_index] = 1
        elif fuel_index >= 0:
            x[fuel_index] = 5
        elif model_index >= 0:
            x[model_index] = 9

        return decision_tree.predict([x])[0]

    def predict_price_linear(model, _year, engineSize, transmission, fuel):
        try:
            model_index = model_list.index(model)[0][0]
            transmission_index = transmission_list.index(transmission)[0][0]
            fuel_index = fuel_list.index(fuel)[0][0]
        except ValueError:
            model_index = -1
            fuel_index = -1
            transmission_index = -1

        x = np.zeros(len(column_data))
        x[0] = _year
        x[1] = engineSize
        if transmission_index >= 0:
            x[transmission_index] = 1
        elif fuel_index >= 0:
            x[fuel_index] = 5
        elif model_index >= 0:
            x[model_index] = 9

        return linear_reg.predict([x])[0]


    #alg = ['Sparse Multilayer Perceptron', 'Light Gradient Boosting Trees']
    #select_alg = st.selectbox('Choose Algorithm for Efficient Predict', alg)
    if st.button('Predict'):
        im = Image.open(img1).convert('L').resize((256,256))
        x = img_to_array(im).reshape(2,-1)
        p_model = load_model('idk.h5')
        model2 = load_model('pipe2model.h5')
        model3 = load_model('pipe3model.h5')
        model4 = load_model('pipe4model.h5')
        p2 = model2.predict(x)
        p4=None
        if p2[0][0]<=0.5:
            p3 = model3.predict(x)[0]
            p4 = np.argmax(model4.predict(x), axis=1)[0]
        d = {0:'minor', 1:'moderate', 2:'severe'}
        price = pipeline(img1)
        if p4==None:
            pass
        elif p4==0:
            price-=0.1*price
        elif p4==1:
            price-=0.45*price
        else:
            price-=0.65*price
        


    #    if select_alg == 'Sparse Multilayer Perceptron':
    #        st.write('Accuracy Score', decision_score)
    #        st.subheader(predict_price_decision(models, year, engine_size, transmissions, fuels))
    #        st.markdown("<h5 style='text-align: left;'> Euros </h5>", unsafe_allow_html=True)

    #    elif select_alg == 'Light Gradient Boosting Trees':
    #        st.write('Accuracy Score', linear_score)
    #        predicted_price = st.subheader(predict_price_linear(models, year, engine_size, transmissions, fuels))
    #        st.markdown("<h5 style='text-align: left;'> Euros </h5>", unsafe_allow_html=True)
    #        if predict_price_linear(models, year, engine_size, transmissions, fuels) <= 0:
    #            st.write('Curious about why Linear Regression received Negative value as a Prediction. Here are '
    #                     'some resources which would make you understand mathematics behind Linear Regression better. ')
    #            st.markdown("[Stack Overflow answer](https://stackoverflow.com/questions/63757258/negative-accuracy-in-linear-regression)")
    #            st.markdown("[Quora](https://www.quora.com/What-is-a-negative-regression)")
    #            st.markdown("[Edureka Video on Linear regression ](https://www.youtube.com/watch?v=E5RjzSK0fvY)")
    #            st.write('Hope this helps you!')

    #            st.markdown('---')

    #quotes = ['Focus your attention on what is most important', 'Expect perfection (but accept excellence)',
    #          'Make your own rules',
    #          'Give more than you take', 'Leverage imbalance']
    #quote_choice = random.choice(quotes)
    #st.markdown("<h4 style='text-align: left;'> Quote of the Day </h4>", unsafe_allow_html=True)
    #st.write(quote_choice)
