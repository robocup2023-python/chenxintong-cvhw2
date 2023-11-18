

import os
import cv2
import numpy as np

def ScharrFilter(img_path='/home/oem/下载/1021_1.jpg'):
    img_src=cv2.imread(img_path)
    img=cv2.resize(src=img_src,dsize=(450,450))
    img_dy=cv2.Scharr(src=img,ddepth=-1,dx=1,dy=0)
    img_dx=cv2.Scharr(src=img,ddepth=-1,dx=0,dy=1)
    img_dx_dy=img_dx+img_dy
    # img_dx_dy=cv2.add(img_dx,img_dy)
    cv2.imshow('img_src',img_src)
    cv2.imwrite("/home/oem/catkin_n10/src/parks/scripts/img_src.jpg",img_src)
    cv2.imshow('img_dx',img_dx)
    cv2.imwrite("/home/oem/catkin_n10/src/parks/scripts/img_dx.jpg",img_dx)   
    cv2.imshow('img_dy',img_dy)
    cv2.imwrite("/home/oem/catkin_n10/src/parks/scripts/img_dy.jpg",img_dy)
    cv2.imshow('img_dx_dy',img_dx_dy)
    cv2.imwrite("/home/oem/catkin_n10/src/parks/scripts/img_dx_dy.jpg",img_dx_dy)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def detectScharrFilter():
    cap=cv2.VideoCapture(0)
    while cap.isOpened():
        OK,frame=cap.read()
        if OK:
            img = cv2.resize(src=frame, dsize=(450, 450))
            img_dy = cv2.Scharr(src=img, ddepth=cv2.CV_64F, dx=1, dy=0)
            img_dx = cv2.Scharr(src=img, ddepth=cv2.CV_64F, dx=0, dy=1)
            img_dx_dy = img_dx + img_dy
            cv2.imshow('object',img_dx_dy)
        else:
            print('为检测到物体')
        if cv2.waitKey(1)&0XFF==27:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    print('Pycharm')
    ScharrFilter()
    # detectScharrFilter()


