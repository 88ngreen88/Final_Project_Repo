# Using convolutional neural networks to diagnose malaria
![quito](https://user-images.githubusercontent.com/115309980/232593816-2ff4a6ae-942c-45fa-a891-99bd010d033c.jpg)

## Overview

For this project I wanted to create a CNN model that will help the World Health Orgization stream line their current malaria detection efforts.

## Background on Malaria

Malaria is a parasitic disease that is spread through the saliva of infected mosquitoes. Once in the body, the malaria parasite infects and untlimatley destroys red blood cells. This disease can cause flu like symptoms in most hosts and potentially death if left untreated, especially in vulnerable populations like children. 

Malaria is a major public health issue, particularly in developing nations with warm and humid climates, where transmission is more common. According to the World Health Organization (WHO), in 2020, there were an estimated 241 million cases of malaria worldwide, with approximately 627,000 deaths, the majority of which were young children in sub-Saharan Africa. Looking at the barchart below, we can see that out all the regions in the world, Africa carries the largest malaria burden. In addition, this burden has only increased in the last few years:

![download-5](https://user-images.githubusercontent.com/115309980/232851698-93ebfde0-35a0-4f60-8145-5b64b434a3df.png)


In addition to its devastating human toll, malaria also has significant economic and social impacts, particularly in affected countries. The disease has been estimated to cost the African continent over US$12 billion per year in lost productivity, treatment costs, and other expenses. This is especially concerning given that Malaria funding through global and prive efforts has decreased over the last few years.

In the United States, malaria was once a significant public health problem in the southern states, but its incidence has declined substantially since the 1940s, due to the use of effective control measures such as mosquito eradication programs and insecticides. However, in recent years, there have been a slight increase in the number of cases of malaria in the United States (see bar chart below). Most of these cases come from individuals contracting malaria while abroad in countries where malaria is endemic:

![download-1](https://user-images.githubusercontent.com/115309980/232851683-25b9b848-2da7-4bee-b481-b5d22849eb0f.png)

## Diagnosing Malaria with CNN

For my capstone project, I wanted to create a convolutinal neural network (CNN) that could help diagnose a blood sample smear as postitive or negative for Malaria. Despite reduced global funding for malaria, the WHO still wants to reduce global malaria incidence by at least 90% by 2030.  My hope is that by launching my CNN through Streamlit, the model could help the WHO by assisting microscopist and field workers in achieving faster and more accurate malaria  diagnoses. In addition, if the WHO are able to use this model to diagnose more patients with Malaria, then this allows the WHO to more accurately and intentionally distribute malaria aid in areas impacted the most by malaria outbreaks.

The model was built using Python 3 and the TensorFlow and Keras libraries.

## My Data

The dataset used in this project is the Malaria Cell Images Dataset from the National Library of Medicine. The dataset contains 27,558 blood cell images with equal instances of parasitized and uninfected cells.

The images are provided in PNG format and are divided into two subdirectories: Parasitized and Uninfected. The Parasitized directory contains images of blood cells infected with malaria at various stages of infections, while the Uninfected directory contains images of normal blood cells. Below are some examples of the parasitized and uninfected blood cell images in the dataset:

![download-2](https://user-images.githubusercontent.com/115309980/232607619-9acb3814-c89f-41bc-bc1a-2768858f37ee.png)

When performing EDA on the large set of images, I first noticed that all of the PNG images were different sizes, so they would need to be resized to be all the same dimentions. I decided to resize all images to be 128X128. I also tried resizing all images to 224X224 but my models performed worse. See below for a plot showing the distribution of image sizes:

![download-3](https://user-images.githubusercontent.com/115309980/232609968-79a1fff4-9b91-424c-a30c-b2d3e440eb5a.png)

After preprocessing my train images, I also looked at the average pixel density for the parasitized cells (label 1) and uninfected cells (label 0). I did this to ensure that there is a difference in pixel value between the two groups to esnure that my models will be able to tell the difference between the two groups of images. Looking at the histogram below, there does seem to be a distinct difference in pixel value between the two sets of images:

![download-4](https://user-images.githubusercontent.com/115309980/232612178-739f0e2d-b3be-440a-96ae-25b3016ea061.png)

The last EDA I performed on my model was to check for images that met the following criteria:  dark images, light images, low information images, exact duplicate images, near duplicate images, and blurry images. I did this by using a python library called ImageLab and I wanted to check for these images to make sure that all the images I was training my model on were of good quality. When I checked my images, only one set of images came back with a problem:

<img width="585" alt="Screenshot 2023-04-17 at 5 18 17 PM" src="https://user-images.githubusercontent.com/115309980/232612920-d1b0185f-093c-4c21-ab33-6501c6cda80c.png">

These two images came back as near duplicates according to ImageLab. However, the images are not the same, so I did not discard any of the images in my data set. 

## Models

For this project, I ran eleven different CNN models. Model details are briefly given below:

<img width="763" alt="Screenshot 2023-04-20 at 4 08 40 PM" src="https://user-images.githubusercontent.com/115309980/233476823-0cf4b0f9-eba7-40f8-8c0d-92e339ea7c64.png">

## Choosing My Model

Out of the 11 different models I ran, three models had an accuracy of around 95%. I ended up choosing Model three as my best model because it had the fewest false negative results. I prioritized having a low number of false negative tests because I do not want a patient thinking that they do not have malaria when they do have malaria. See the chart below for more details on the three best models:

<img width="1439" alt="Screenshot 2023-04-19 at 1 09 15 PM" src="https://user-images.githubusercontent.com/115309980/233149462-5cadadef-4dc9-4146-8787-7ba03af2df84.png">

Looking at the chart above my final model (model 3) has a test accuracy of 96%. Below is the architecture of my final cnn model:

<img width="454" alt="Screenshot 2023-04-19 at 4 44 21 PM" src="https://user-images.githubusercontent.com/115309980/233455452-ba777a29-ae73-4d94-ac61-c7aa2b56f382.png">

## Conclusions

In this project, I built a CNN model that can accurately identify malaria-infected cells in blood samples. The model achieved a test accuracy of 96%, which demonstrates its effectiveness in detecting malaria. In addition, the model was faster and simpler than transfer learning models I looked at like VGG19. By launching this model on Streamlit, workers for the WHO will be able to easily use this model. 

Given that my model is categorizing  blood samples as being infected/uninfected with malaria with 96% accuracy, I would recommend use my Streamlit app.

Next, I would recommend the WHO train field works, local doctors, and microscopist on how to use the Streamlit app.

## Next Steps

1. Continue to run models with the goal of reducing false negatives.

2. Update streamlit app to intake patients information

3. Connect Streamlit website to mongoDB in order to save results in a database to improve the WHO’s malaria surveillance system

## File Tree

├── [Malaria_Data]()

├── cell_images

├── streamlit_images

├── .gitignore

├── Final_Clean_Notebook.ipynb

├── ReadME.md

├── Streamlit.ipynd

├── Streamlit.py

├── cnn_model_3(3).pkl

└── requirements.txt



