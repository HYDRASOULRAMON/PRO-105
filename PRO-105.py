import os
import cv2

path = r"C:\Users\Ramon Chettiar\OneDrive\Desktop\Whitehat Jr\PROJECTS\PRO-105\Images"

Images = []

for file in os.listdir(path):
    name, extension = os.path.splitext(file)
    if extension.lower() in ['.jpg', '.jpeg', '.png', '.bmp', '.gif']:
        file_name = os.path.join(path, file)
        print(file_name)
        Images.append(file_name)

count = len(Images)

frame = cv2.imread(Images[0])

height, width, channels = frame.shape

size = (width, height)

print(size)


out=cv2.VideoWriter('project.avi',cv2.VideoWriter_fourcc(*'DIVX'), 0.8, size)

for i in range(0, count):
    image = cv2.imread(Images[i])
    if image is not None:
        out.write(image)
    else:
        print(f"Error reading image: {Images[i]}")

out.release()

print("Done")

