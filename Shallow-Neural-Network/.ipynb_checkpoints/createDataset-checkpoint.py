import cv2
for i in range (1,41):
    image = cv2.imread("..\\tarining_images\\"+str(i)+".png")
    image = cv2.resize(image,(64,64))
    cv2.imwrite('1\\'+str(i)+'.png',image)

image1=[]
for i in range(0,40):
    image_path_1 = "0\\"+str(i+1)+".png"
    image = cv2.imread(image_path_1)
    image=cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image1.append(image)

import h5py
with h5py.File("train_stairsvnonstairs.h5", "w") as hf:
    train_set_x = hf.create_dataset("train_set_x", data=train_images)
    train_set_y = hf.create_dataset("train_set_y", data=train_labels)