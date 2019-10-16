import autokeras as ak
import os
from os import listdir
from autokeras import ImageClassifier
from autokeras.image.image_supervised import load_image_dataset
from autokeras.utils import pickle_from_file

import csv

import graphviz
from graphviz import Digraph


from keras.preprocessing import image
import numpy as np


def to_pdf(graph, path):
    dot = Digraph(comment='The Round Table')

    for index, node in enumerate(graph.node_list):
        dot.node(str(index), str(node.shape))

    for u in range(graph.n_nodes):
        for v, layer_id in graph.adj_list[u]:
            dot.edge(str(u), str(v), str(graph.layer_list[layer_id]))

    dot.render(path)


def visualize(path):
    cnn_module = pickle_from_file(os.path.join(path, 'module'))
    cnn_module.searcher.path = path
    for item in cnn_module.searcher.history:
        model_id = item['model_id']
        graph = cnn_module.searcher.load_model_by_id(model_id)
        to_pdf(graph, os.path.join(path, str(model_id)))

visualize(directory)

#Variables
directory = "/var/folders/7m/gzvzm41j76g30dmpn0_tg17w0000gn/T/autokeras_168F7H"
directory2 = "/private/var/folders/7m/gzvzm41j76g30dmpn0_tg17w0000gn/T/autokeras_ETBOQD"
train_dir = '/Users/stevengong/Desktop/AutoML/dataset/training_set' # Path to the train directory
test_dir = '/Users/stevengong/Desktop/AutoML/dataset/test_set' # Path to the train directory
train_csv = '/Users/stevengong/Desktop/AutoML/dataset/train.csv'
test_csv = '/Users/stevengong/Desktop/AutoML/dataset/test.csv'
training_times = [
		60 * 60,		# 1 hour i.e. 60*60 seconds
		60 * 60 * 2,	# 2 hours
		60 * 60 * 4,	# 4 hours
		60 * 60 * 8,	# 8 hours
		60 * 60 * 12,	# 12 hours
		60 * 60 * 24,	# 24 hours
	]



#Creating a CSV file for the list of the paths of the images with their classes
#Function has not yet been tested, use at discretion. Inspired from the Autokeras code: https://autokeras.com/start/
def createCSV(class_directory, csv_directory):
    class_dirs = [i for i in os.listdir(path=class_directory) if os.path.isdir(os.path.join(class_directory, i))]
    with open(csv_directory, 'w') as csv_file:
        #Creates 2 columns in the csv file, the filename with the name of the jpg files and the Label i.e. the classes
        fieldnames = ['File Name', 'Label']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        label = 0
        for current_class in class_dirs:
            for image in os.listdir(os.path.join(class_directory, current_class)):
                writer.writerow({'File Name': str(image), 'Label':label})
        label += 1
        csv_file.close()



"""
This was my attempt to create my own functions in order to transform images to nparrays based on the csv file created, because
the load_image_dataset function was not working for me. However, I realized that my error was due to the csv file not being 
properly created. The functions i created do not fully work properly.

def read_csv_file(csv_file_path):
    #Read the csv file and returns two separate list containing file names and their labels.

    #Args:
        #csv_file_path: Path to the CSV file.

    #Returns:
        #file_names: List containing files names.
        #file_label: List containing their respective labels.
    
    file_names = []
    file_labels = []
    with open(csv_file_path, 'r') as files_path:
        path_list = csv.DictReader(files_path)
        fieldnames = path_list.fieldnames
        for path in path_list:
            file_names.append(path[fieldnames[0]])
            file_labels.append(path[fieldnames[1]])
    return file_names, file_labels



#Function to automatically transform images into NumPy arrays
def transformImageToArray(dir_path, csv_file_location):
    #dir_path is the path where the images are located
    #csv_file is the a csv file containing 2 columns, 1 column for the names of the images and 1 column for the class of the image

    x_values = []
    file_names, y_values = read_csv_file(csv_file_location)
    for file_name in file_names:
        if file_name.endswith('.jpg'):
            try:
                file = image.load_img(dir_path + '/' + file_name, target_size=(64,64)) #Target size I did for safety precautions not sure if it is necessary
                file = image.img_to_array(file)
                file = np.expand_dims(file, axis=0)


                x_values.append(file)

            except (IOError, SyntaxError) as e:
                print('Bad file:', filename)
                # os.remove(base_dir+"/"+filename) (Maybe)

    x_values = np.vstack(x_values)
    y_values = np.array(y_values)


    return x_values, y_values



"""

#Fixed the error, the excel file contained the DS_Store file
#Loading the dataset
x_train, y_train = load_image_dataset(csv_file_path=train_csv, images_path=train_dir)
x_test, y_test = load_image_dataset(csv_file_path=test_csv, images_path=test_dir)


x_train = x_train.reshape(x_train.shape + (1,))
x_test = x_test.reshape(x_test.shape + (1,))


clf = ImageClassifier(verbose=True)
#Chose to set the training time to 3600s for testing purposes
clf.fit(x_train, y_train, time_limit=training_times[3])
clf.final_fit(x_train, y_train, x_test, y_test, retrain=True)
#y gives us the accuracy of our structure
y=clf.evaluate(x_test, y_test)
print(y)



#Verfying if the images are corrupt
for filename in listdir(dir_path):
    if filename.endswith('.jpg'):
        try:
            img = image.open(dir_path+"/"+filename) # open the image file
            img.verify() # verify that it is, in fact an image
        except (IOError, SyntaxError) as e:
            print('Bad file:', filename)
            #os.remove(base_dir+"\\"+filename) (Maybe)


