# Using convolutional neural network to diagnose malaria
![quito](https://user-images.githubusercontent.com/115309980/232593816-2ff4a6ae-942c-45fa-a891-99bd010d033c.jpg)

## Background on Malaria

Malaria is a parasitic disease that is spread by infected mosquitoes. It is a major public health issue, particularly in developing countries with warm and humid climates, where transmission is more common. According to the World Health Organization (WHO), in 2020, there were an estimated 241 million cases of malaria worldwide, with approximately 627,000 deaths, the majority of which were young children in sub-Saharan Africa. Looking at the barchart below, we can see that out all the regions in the world, Africa carries the largest malaria burden. In addition, this burden has only increased in the last few years:

![download](https://user-images.githubusercontent.com/115309980/232602525-651f5985-c6c2-491e-bbbd-997ddf4c78b6.png)

In addition to its devastating human toll, malaria also has significant economic and social impacts, particularly in affected countries. The disease has been estimated to cost the African continent over US$12 billion per year in lost productivity, treatment costs, and other expenses. This is especially concerning given that Malaria funding through global and prive efforts has decreased over the last few years.

In the United States, malaria was once a significant public health problem in the southern states, but its incidence has declined substantially since the 1940s, due to the use of effective control measures such as mosquito eradication programs and insecticides. However, in recent years, there have been slight increased in the number of cases of malaria in the United States (see bar chart below). Most of these cases come from individuals contracting malaria while abroad in countries where malaria is endemic:

![download-1](https://user-images.githubusercontent.com/115309980/232603263-4d23b500-109a-4a9c-8343-06ab0b28541e.png)



## Diagnosing Malaria with CNN

For my capstone project, I wanted to create a convolutinal neural network that could help diagnose a blood sample smear as postitive or negative for Malaria. My hope is that this model could help the WHO and CDC with malaria diagnosis given rising malaria cases and reduced global funding. 

The model was built using Python 3 and the TensorFlow and Keras libraries.

## My Data

The dataset used in this project is the Malaria Cell Images Dataset from Tensorflow. The dataset contains 27,558 blood cell images with equal instances of parasitized and uninfected cells.

The images are provided in PNG format and are divided into two subdirectories: Parasitized and Uninfected. The Parasitized directory contains images of blood cells infected with malaria, while the Uninfected directory contains images of normal blood cells. Below are some example of the parasitized and uninfected blood cell images in the dataset:

![download-2](https://user-images.githubusercontent.com/115309980/232607619-9acb3814-c89f-41bc-bc1a-2768858f37ee.png)

When performing EDA on the large set of images, I first noticed that all of the PNG images were different sizes, so they would need to be resized to be all the same dementions. I decided to resize all images to be 128X128. I also tried resizing all images to 224X224 but my comdel performed worse. See below for a plot showing the distribution of image sizes:

![download-3](https://user-images.githubusercontent.com/115309980/232609968-79a1fff4-9b91-424c-a30c-b2d3e440eb5a.png)

In addition to resizing all images, I also looked at the average pixel density for the parasitized cells (label 1) and uninfected cells (label 0). I did this to ensure that the there is a difference is pixel value between the two groups to esnure that my mmodels will be able to tell the difference between the two groups of images. Looking at the histogram below, there does seem to be a distinct difference in pixel value between the two sets of images:

![download-4](https://user-images.githubusercontent.com/115309980/232612178-739f0e2d-b3be-440a-96ae-25b3016ea061.png)

The last EDA I performed on my model was to check for images that met the following criteria:  dark images, light images, low information images, exact duplicate images, near duplicate images, and blurry images. I did this by using a python library called ImageLab and I wanted to check for these images to ensure that all images were of good quality. When I checked my image, only one set of images came back with a problem:

<img width="585" alt="Screenshot 2023-04-17 at 5 18 17 PM" src="https://user-images.githubusercontent.com/115309980/232612920-d1b0185f-093c-4c21-ab33-6501c6cda80c.png">

These two images came back as near duplicates. However, the images are not the same, so I did not discard any of my images. 

## Models

## Choosing My Model

## Conclusions

## Next steps
