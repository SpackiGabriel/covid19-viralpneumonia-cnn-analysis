# Final Project of LAMIA Bootcamp

## LAMIA

LAMIA, located on the UTFPR campus in Santa Helena, is a research center dedicated to the application of Data Science and Computer Vision in the industry. It develops technology and academic knowledge for the sector, with a team of collaborators spread throughout the country.

![LAMIA logo](/images/lamia.png)

## Bootcamp and Journey

Upon joining the laboratory, it is necessary to go through a training bootcamp and develop a final project that showcases one's skills and contributions. During this process, participants are considered beginners and have a deadline to complete the training. The laboratory covers various areas, and I chose to focus on Machine Learning.

## Chosen Challenge

For my final project, I chose the following challenge:

- To compare three famous convolutional models currently available.
    - The models must classify Covid-19 and Pneumonia from an X-ray image.

The chosen models were:

- ResNet50
- VGG16
- InceptionV3

All available for use in the TensorFlow library.

# Dataset

The training and validation of the models were based on a merge of the following datasets:

- Covid-19 Image Dataset.
    - Available at: https://www.kaggle.com/datasets/pranavraikokte/covid19-image-dataset

- COVIDx CXR-4.
    - Available at: https://www.kaggle.com/datasets/andyczhao/covidx-cxr2

- Chest X-Ray Images (Pneumonia) with new class.
    - Available at: https://www.kaggle.com/datasets/ahmedhaytham/chest-xray-images-pneumonia-with-new-clas

Resulting in 9423 images for training and 2353 images for validation.

# Results

I am pleased to inform you that I have achieved consistent results. However, for a better analysis among the comparisons, simply observing the accuracy and loss numbers of the models would not be sufficient. That's why detailed results have been provided in the testing-models.ipynb file. In it, you can analyze the metrics of each model on the test set. (Note: the test set was compiled with real images available on Google Images and various medical websites.) For an analysis of the metrics of each model on the validation dataset, you can find the graphs in the respective model's file.

These results establish a promising foundation for future enhancements and applications. Therefore, I intend to continue developing my skills in Machine Learning at LAMIA.