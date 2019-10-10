import autokeras as ak
import os
from os import listdir
from PIL import Image
from autokeras import ImageClassifier
from autokeras.image.image_supervised import load_image_dataset
import csv

from keras.preprocessing import image
import numpy as np

training_times = [
		60 * 60,		# 1 hour i.e. 60*60 seconds
		60 * 60 * 2,	# 2 hours
		60 * 60 * 4,	# 4 hours
		60 * 60 * 8,	# 8 hours
		60 * 60 * 12,	# 12 hours
		60 * 60 * 24,	# 24 hours
	]

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
train_dir = '/Users/stevengong/Desktop/AutoML/dataset/training_set'
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

def read_csv_file(csv_file_path):
    """Read the csv file and returns two separate list containing file names and their labels.

    Args:
        csv_file_path: Path to the CSV file.

    Returns:
        file_names: List containing files names.
        file_label: List containing their respective labels.
    """
    file_names = []
    file_labels = []
    with open(csv_file_path, 'r') as files_path:
        path_list = csv.DictReader(files_path)
        fieldnames = path_list.fieldnames
        for path in path_list:
            file_names.append(path[fieldnames[0]])
            file_labels.append(path[fieldnames[1]])
    return file_names, file_labels


train_file_names, y_train = read_csv_file(train_csv)

#Function to automatically transform images into NumPy arrays
def transformImageToArray(dir_path, csv_file_location):
    #dir_path is the path where the images are located
    #csv_file is the a csv file containing 2 columns, 1 column for the names of the images and 1 column for the class of the image

    x_values = []
    file_names, y_values = read_csv_file(csv_file_location)
    for file_name in file_names:
        if file_name.endswith('.jpg'):
            try:
                file = image.load_img(dir_path + '/' + file_name)
                file = image.img_to_array(file)
                file = np.expand_dims(file, axis=0)
                x_values.append(file)

            except (IOError, SyntaxError) as e:
                print('Bad file:', filename)
                # os.remove(base_dir+"\\"+filename) (Maybe)

    return x_values, y_values


train_file_names, y_train = read_csv_file('/Users/stevengong/Desktop/AutoML/dataset/train.csv')

train_csv = '/Users/stevengong/Desktop/AutoML/dataset/train.csv'
train_dir = '/Users/stevengong/Desktop/AutoML/dataset/training_set' # Path to the train directory

x_train, y_train = transformImageToArray(train_dir, train_csv)


#Building the AutoML

x_train = x_train.reshape(x_train.shape + (1,))

x_test = x_test.reshape(x_test.shape + (1,))
clf = ImageClassifier(verbose=True)
clf.fit(x_train, y_train, time_limit=training_times[0])
clf.final_fit(x_train, y_train, x_test, y_test, retrain=True)
#y gives us the accuracy of our structure
y=clf.evaluate(x_test, y_test)
print(y)



#Verfying if the images are corrupt
for filename in listdir(dir_path):
    if filename.endswith('.jpg'):
        try:
            img = Image.open(dir_path+"/"+filename) # open the image file
            img.verify() # verify that it is, in fact an image
        except (IOError, SyntaxError) as e:
            print('Bad file:', filename)
            #os.remove(base_dir+"\\"+filename) (Maybe)
