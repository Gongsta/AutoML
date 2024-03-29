#importing the autokeras library and renaming to ak (shortened version)
import autokeras as ak

from autokeras.image.image_supervised import load_image_dataset

#x_train, y_train = load_image_dataset(csv_file_path="")

import numpy as np

#mnist is a dataset wof handwritten digits, used for testing a lot
from keras.datasets import mnist
from autokeras import ImageClassifier


(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train = x_train.reshape(x_train.shape + (1,)) # (1,) denotes the channles which is 1 in this case
x_test = x_test.reshape(x_test.shape + (1,)) # (1,) denotes the channles which is 1 in this case

# Instantiate the ImageClassifier class
clf = ImageClassifier(verbose=True, augment=False)
# Fit the train set to the image classifier
clf.fit(x_train, y_train, time_limit=12 * 60 * 60)
clf.final_fit(x_train, y_train, x_test, y_test, retrain=True)
# Summarize the results
y = clf.evaluate(x_test, y_test)
print(y * 100)