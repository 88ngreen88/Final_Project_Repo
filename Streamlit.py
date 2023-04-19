#!/usr/bin/env python
# coding: utf-8

# In[32]:


# make usual imports
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
import altair as alt
import numpy as np
from PIL import Image
import pickle
import numpy as np
from tensorflow.keras.preprocessing.image import ImageDataGenerator


# In[22]:


#images
st.image("streamlit_images/quito.jpg", use_column_width = "always")


# In[23]:


#title
#this is my main page, add github link and information about my project. Tableua graphs?
st.title("Malaria Detection")
st.header("Look at the data below on the global impact of malaria")


# In[24]:


st.write("Below shows the number of cases of malaria in the United States and regions around the world")


# In[25]:


#load data
XLS = pd.ExcelFile("Data/US_Malaria.xlsx")
df_cases = pd.read_excel(XLS, "Data")

#cleaning data
df_cases = df_cases.drop("Unnamed: 0", axis =1)
df_cases = df_cases.drop(df_cases.index[0:4])
df_cases.rename(columns = {"Unnamed: 1":"Year", "Unnamed: 2":"Malaria Cases"}, inplace = True)
df_cases.reset_index(drop=True, inplace = True)

#creating barchart
chart = alt.Chart(df_cases).mark_bar().encode(
    x='Year',
    y='Malaria Cases',
    tooltip=['Year', 'Malaria Cases']
).properties(
    width=600,
    height=400
)

#Showing chart in Streamlit
st.altair_chart(chart, use_container_width=True)


# In[3]:


data = {
    'Year': [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021],
    'African': [104478030, 102278324, 113761255, 125732311, 135095910, 142473526, 160847397, 164222522, 157996344, 168282485, 168364949, 174962186],
    'Eastern Mediterranean': [6369494, 5952130, 5835463, 4946316, 5343572, 5420260, 3683265, 4464691, 5289329, 4492250, 4198608, 4805377],
    'European': [271, 252, 666, 328, 270, 238, 226, 231, 255, 295, 144, None],
    'Americas': [677583, 495221, 471841, 468931, 410975, 479057, 651224, 932341, 930469, 848994, 589418, 524158],
    'South-East Asia': [3085804, 2504444, 2144568, 1681812, 1696800, 1659425, 1477428, 1240255, 752907, 671608, 512084, 558990],
    'Western Pacific': [1792851, 1429780, 1122080, 1372377, 923262, 813712, 954305, 1069932, 1104615, 790987, 1049905, 90273]}

df = pd.DataFrame(data)


# In[4]:


df_melt = pd.melt(df, id_vars=['Year'], var_name='Region', value_name='Population')

# Create a stacked bar chart using Altair
chart = alt.Chart(df_melt).mark_bar().encode(
    x='Year:O',
    y='Population:Q',
    color=alt.Color('Region:N', legend=alt.Legend(title='Region'), scale=alt.Scale(scheme='category20')),
    tooltip=['Year', 'Region', 'Population']
).properties(
    width=600,
    height=400,
    title='Population by Region (2010-2021)'
)

# Display the chart in Streamlit
st.altair_chart(chart, use_container_width=True)


# In[5]:


st.write("Please use the malaria model below to classify blood smear samples")


# In[7]:


st.title("Malaria Classification Model")


# In[8]:


def load_model(file):
    model_file = open(file, "rb")
    loaded_model = joblib.load(model_file)
    model_file.close()
    return loaded_model


# In[10]:


malaria_model = load_model("cnn_model_3(3).pkl")


# In[18]:


#submit button
uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])


# In[23]:


if uploaded_file is not None:
    st.image(uploaded_file, caption='Blood Smear Image', use_column_width=True)


# In[31]:


cat_button = st.button("Categorize the Image")

def predict(uploaded_file):
    # Open and resize the uploaded file
    image = Image.open(uploaded_file)
    image_resized = image.resize((128, 128))
        
    # Convert the resized file to a Numpy array
    image_array = np.array(image_resized)
        
        
    # Create an instance of ImageDataGenerator with desired preprocessing settings
    datagen = ImageDataGenerator(rescale=1./255)
        
    # Apply the data generator to the image array
    image_processed = datagen.flow(np.array([image_array]))
    proba = malaria_model.predict(image_processed)
    pred = (proba > 0.5).astype('int')
        
    if pred == 0:
        return st.write("uninfected with malaria")
    else:
        return st.write("infected with malaria")


if cat_button:
    predict(uploaded_file)


# In[ ]:




