import autokeras as ak
import os
from autokeras import ImageClassifier
from autokeras.image.image_supervised import load_image_dataset
import csv

#Creating a CSV file for the list of the paths of the datasets
train_dir = '/Users/stevengong/Desktop/AutoML/dataset/training_set' # Path to the train directory
class_dirs = [i for i in os.listdir(path=train_dir) if os.path.isdir(os.path.join(train_dir, i))]
 with open('/Users/stevengong/Desktop/AutoML/dataset/train.csv', 'w') as train_csv:
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
 with open('/Users/stevengong/Desktop/AutoML/dataset/test.csv', 'w') as test_csv:
    fieldnames = ['File Name', 'Label']
    writer = csv.DictWriter(test_csv, fieldnames=fieldnames)
    writer.writeheader()
    label = 0
    for current_class in class_dirs:
        for image in os.listdir(os.path.join(test_dir, current_class)):
            writer.writerow({'File Name': str(image), 'Label':label})
        label += 1
    test_csv.close()


x_train, y_train = load_image_dataset(csv_file_path=)