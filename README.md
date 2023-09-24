
# deep Classfier project

## Deep Learing 
**CNN Image Classifier**

**Project Description:**

This project aims to develop a Convolutional Neural Network (CNN) image classifier to classify images into different categories. CNNs are a type of deep learning algorithm that are well-suited for image classification tasks, as they are able to learn the spatial hierarchies of features in images, such as edges, textures, and shapes.

The project will involve the following steps:

1. **Collecting and preparing a dataset of images.** The dataset should include a variety of images from different categories, such as animals, objects, and scenes. The images should be cleaned and resized to a consistent format.
2. **Designing and training a CNN model.** The CNN model will be designed using a popular deep learning framework likeTensorFlow . The model will be trained on the prepared dataset using a supervised learning approach.
3. **Evaluating the performance of the CNN model.** Once the model has been trained, it will be evaluated on a held-out test set to assess its accuracy.
4. **Deploying the CNN model.** Once the model has been evaluated and found to be performing well, it can be deployed to production so that it can be used to classify new images.

**Potential Applications:**

The CNN image classifier can be used in a variety of applications, such as:

* **Image classification for social media.** The classifier can be used to automatically classify images uploaded to social media platforms, such as Facebook and Instagram. This can help to improve the organization and search functionality of these platforms.
* **Image classification for e-commerce.** The classifier can be used to automatically classify product images on e-commerce websites. This can help users to find the products they are looking for more easily.
* **Image classification for medical imaging.** The classifier can be used to assist doctors in diagnosing diseases by classifying medical images, such as X-rays and MRIs.

**Conclusion:**

CNN image classifiers are a powerful tool for image classification tasks. This project will develop a CNN image classifier and explore its potential applications.

## Workflows

1. update config.yaml
2. update secrets.yaml [ Optional]
3. update params.yaml
4. update the entity
5. update the configuraton manager in src config
6. update the componenets
7. update the pipeline
8. Test run pipeline stage
9. Run tox for testin your package
10. update the dvc.yaml
11. run "dvc repro"for runnin all the stage



STEP 1: Set the env variable | Get it from dagshub -> remote tab -> mlflow tab

MLFLOW_TRACKING_URI=https://dagshub.com/syedsajjadaskari/Deep-Learing.mlflow
MLFLOW_TRACKING_USERNAME=syedsajjadaskari
MLFLOW_TRACKING_PASSWORD=<> \


step 2: install mlflow

step 3: set remote URI

STEP 4: Use context manager of mlflow to start run and then log metrics, params and model

