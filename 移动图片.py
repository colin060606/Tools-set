import os
import shutil
import cv2
def readhw(w,h,old_path,new_path):
    for parent, dirnames, filenames in os.walk(old_path):
        for filename in filenames:
            if filename[-4:] == '.jpg':
                currentPath = os.path.join(parent, filename)
                img = cv2.imread(currentPath)
                if int(w) == img.shape[0] and int(h) == img.shape[1]:
                    src = os.path.join(old_path, filename)
                    dst = os.path.join(new_path, filename)
                    shutil.move(src,dst)
old = input("输入移动图片文件夹地址:")
new = input("输入目标文件夹地址:")
img_h = input("输入图像高: ")
img_w = input("输入图像宽: ")
readhw(img_w, img_h, old, new)
