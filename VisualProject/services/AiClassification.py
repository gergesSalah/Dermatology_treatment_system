import cv2
import keras
import numpy as np
import os

def classify(name):
    if name == None or name =="":
        label = "you didn't insert any photo"
        return label
    else:
        classes = ['1. Eczema', '2. Melanoma', '3. Atopic Dermatitis', '4. Basal Cell Carcinoma', '5. Melanocytic Nevi']
        # print(model.score(normal_test, label_test))

        # predict = model.predict(normal_test)
        # print(confusion_matrix(label_test, predict))
        img_name = str(name)#"ISIC_6653456.jpg"
        dir = "D:/myWork/3rd year/smester 2/Visual programming/projects/system/visual project/VisualProject/media/images"
        img_path = os.path.join(dir,img_name)

        img = cv2.imread(img_path,0)
        # img = cv2.imread(IMG, 0)
        # img = image.img_to_array(img)
        img = cv2.resize(img, (100, 100))
        img = img.reshape(1, 100, 100, 1)

        model_path = "D:/myWork/3rd year/smester 2/Visual programming/projects/system/visual project/VisualProject/services/my_model3.h5"
        mm = keras.models.load_model(model_path)
        # print(classes[(np.argmax(mm.predict(img)))])

        # if model.predict([img]) == 0:
        #     print("normal")
        # else:
        #     print("PNEUMONIA")

        # print(model.predict([img]))
        #
        # print(clases[model.predict([img])[0]])
        Accuracy = "96.64%"
        label = str(classes[(np.argmax(mm.predict(img)))])
        label = label[3:]
        # label = "At a rate of " +Accuracy+""", this is :
        
        # """ + str(classes[(np.argmax(mm.predict(img)))])
        # label = "90.64%" + str(classes[(np.argmax(mm.predict(img)))])
        
        return Accuracy,label
        # my_label1.config(text= Accuracy + label,font=32)
        