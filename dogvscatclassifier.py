import autokeras as ak
import os
from os import listdir
from PIL import Image
from autokeras import ImageClassifier
from autokeras.image.image_supervised import load_image_dataset
import csv

from keras.preprocessing import image
import numpy as np


#Creating a CSV file for the list of the paths of the datasets
train_dir = '/Users/stevengong/Desktop/AutoML/dataset/training_set' # Path to the train directory
class_dirs = [i for i in os.listdir(path=train_dir) if os.path.isdir(os.path.join(train_dir, i))]
with open('/Users/stevengong/Desktop/AutoML/train.csv', 'w') as train_csv:
    #Creates 2 columns in the csv file, the filename with the name of the jpg files and the Label i.e. the classes
    fieldnames = ['File Name', 'Label']
    writer = csv.DictWriter(train_csv, fieldnames=fieldnames)
    writer.writeheader()
    label = 0
    for current_class in class_dirs:
        for image in os.listdir(os.path.join(train_dir, current_class)):
            writer.writerow({'File Name': str(image), 'Label':label})
        label += 1
    train_csv.close()

test_dir = '/Users/stevengong/Desktop/AutoML/dataset/test_set' # Path to the train directory
class_dirs = [i for i in os.listdir(path=train_dir) if os.path.isdir(os.path.join(test_dir, i))]
 with open('/Users/stevengong/Desktop/AutoML/test.csv', 'w') as test_csv:
    fieldnames = ['File Name', 'Label']
    writer = csv.DictWriter(test_csv, fieldnames=fieldnames)
    writer.writeheader()
    label = 0
    for current_class in class_dirs:
        for image in os.listdir(os.path.join(test_dir, current_class)):
            writer.writerow({'File Name': str(image), 'Label':label})
        label += 1
    test_csv.close()


"""
These 2 lines of code does not work for me for some reason...I tried debugging without success

x_train, y_train = load_image_dataset(csv_file_path='/Users/stevengong/Desktop/AutoML/dataset/train.csv', images_path='/Users/stevengong/Desktop/AutoML/dataset/training_set', parallel=True)

x_test, y_test = load_image_dataset(csv_file_path='/Users/stevengong/Desktop/AutoML/dataset/test.csv', images_path='/Users/stevengong/Desktop/AutoML/dataset/test_set')
"""

dir_path = '/Users/stevengong/Desktop/AutoML/dataset/training_set'
for filename in listdir(dir_path):
    if filename.endswith('.jpg'):
        try:
            img = Image.open(dir_path+"/"+filename) # open the image file
            img.verify() # verify that it is, in fact an image
        except (IOError, SyntaxError) as e:
            print('Bad file:', filename)
            #os.remove(base_dir+"\\"+filename) (Maybe)

x_train = []
dir_path = '/Users/stevengong/Desktop/AutoML/dataset/training_set'
for filename in listdir(dir_path):
    if filename.endswith('.jpg'):
        try:
            train_img = image.load_img(dir_path+"/"+filename) # open the image file
            train_img = image.img_to_array(train_img)
            test_image = np.expand_dims(test_image, axis=0)  # this line of code transforms our 3-dimensional array into a 4 dimensional one, axis is 0 since it is in the first position, index = 0

            img.verify() # verify that it is, in fact an image

        except (IOError, SyntaxError) as e:
            print('Bad file:', filename)
            #os.remove(base_dir+"\\"+filename) (Maybe)
