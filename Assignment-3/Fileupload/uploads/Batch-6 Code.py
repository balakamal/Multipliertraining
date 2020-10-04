import os
import csv
from collections import defaultdict
# Importing libraries
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.utils import to_categorical
from keras.preprocessing import image
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from keras.utils import to_categorical
from tqdm import tqdm
trainingset=input("Enter the type of data you want to classify:")
trainingset=trainingset+'.csv'
train = pd.read_csv('training/'+trainingset)
print("============================\nReading training data\n===============================\n")
# Reading the training images
train_image = []
for i in tqdm(range(train.shape[0])):
    img = image.load_img('datasets/data/training/'+train['filename'][i], target_size=(28,28,3),grayscale=False)
    img = image.img_to_array(img)
    img = img/255
    train_image.append(img)
X = np.array(train_image)
# Creating the target variable
y = train['label'].values
count=len(set(y))
y = to_categorical(y)
# Creating validation set
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, test_size=0.01)
# Define the model structure
model = Sequential()
model.add(Conv2D(32, kernel_size=(3, 3),activation='relu',input_shape=(28,28,3)))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(count+1, activation='softmax'))
# Compile the model
model.compile(loss='categorical_crossentropy',optimizer='Adam',metrics=['accuracy'])
# Training the model
model.fit(X_train, y_train, epochs=10, validation_data=(X_test, y_test))

print("============================\nReading testing data\n===============================\n")

#testingset=input("Enter the filename for testing data:")
test_file = pd.read_csv('testing/'+trainingset)
test_image = []
for i in tqdm(range(test_file.shape[0])):
    img = image.load_img('datasets/data/testing/'+test_file['filename'][i], target_size=(28,28,3),grayscale=False)
    img = image.img_to_array(img)
    img = img/255
    test_image.append(img)
test = np.array(test_image)
prediction = model.predict_classes(test)

sample = pd.read_csv('Sample_Submission.csv')
sample['filename'] = test_file['filename']
sample['label'] = prediction

print(sample)
if(trainingset=='gender.csv'):
    print('\n=====================================\n1. Female\t2. Male\n======================================')
if(trainingset=='vehicle.csv'):
    print('\n=====================================\n1. Bike\t2. Car\t3. Bus\n======================================')
if(trainingset=='combo.csv'):
    print('\n=====================================\n1. Vehicle\t2. Gender\t3. Animal\n======================================')
if(trainingset=='animal.csv'):
    print('\n=====================================\n1. Cat\t2. Dog\n======================================')

#for i in range(test_file.shape[0]):
 #   print(sample['filename'][i]+" belongs to "+ sample['label'][i])

#outputfile=input("Enter the filename for output:")
sample.to_csv('outputs/'+trainingset, header=True, index=False)
print("Output is stored in the outputs folder with filename "+trainingset)


#Finding parameters
i=0
fi=""
a=defaultdict(list)
#fname=input("Enter filename:")
with open('original/'+trainingset,'r') as grades:
    for row in grades:
        for v in row:
            if(v=="\n"):
                a[i].append(fi)
                i=0
                fi=""
            elif(v=="," and "\"" not in fi):
                a[i].append(fi)
                i+=1
                fi=""
            else:
                fi+=v
        fi=""

tp=0
tn=0
fp=0
fn=0
for i in range(len(prediction)):
    if(prediction[i]==int(a[1][i+1])):
        if(int(a[1][i+1])==1):
            tp=tp+1
        else:
            fn=fn+1
    else:
        if(int(a[1][i+1])==1):
            tn=tn+1
        else:
            fp=fp+1
print("\n============================\nConfusion Matrix\n===============================\n\tPositive\tNegative")
print("True\t    "+str(tp)+"\t\t"+str(tn))
print("False\t    "+str(fp)+"\t\t"+str(fn))
pre=(tp)/(tp+fp)
rec=(tp)/(tp+fn)
f1=2*(pre*rec/(pre+rec))
acc=((tp+fn)/(tp+fn+tn+fp))
print("\n\nAccuracy\tPrecision\tRecall\tF1 Score")
print(round(acc*100,2),end="\t\t")
print(round(pre,2),end="\t\t")
print(round(rec,2),end="\t\t")
print(round(f1,2),end="\t\t")

