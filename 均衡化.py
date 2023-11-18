import cv2
import numpy as np
from matplotlib import pyplot as plt
 
'''
equalizeHist—直方图均衡化
函数原型： equalizeHist(src, dst=None)
src：图像矩阵(单通道图像)
dst：默认即可
'''
 
 
def equalizeHist(img):
    """直方图均衡化"""
 
    if img.shape == 1:  # 单通道图--》灰度图
        # 灰度图像直方图均衡化
        # 原始图像像素直方图
        plt.hist(img.ravel(), 256)
        plt.show()
        dst = cv2.equalizeHist(img)
        # 目标图像像素直方图
        plt.figure()
        plt.hist(dst.ravel(), 256)
        plt.show()
 
        cv2.imshow("Histogram Equalization", np.hstack([img, dst]))  # 拼接在一起输出
        cv2.waitKey(0)
    # 彩色图像直方图均衡化,3通道图
    else:
        (b, g, r) = cv2.split(img)
        # 显示原图直方图
        plt.hist(img.ravel(), 256)
        plt.show()
        # 彩色图像均衡化,需要分解通道 对每一个通道均衡化
        bH = cv2.equalizeHist(b)
        gH = cv2.equalizeHist(g)
        rH = cv2.equalizeHist(r)
        # 合并每一个通道
        result = cv2.merge((bH, gH, rH))
        # 均衡化之后的直方图
        plt.hist(result.ravel(), 256)
        plt.show()
        # 均衡化之后的图
        cv2.imshow("src_img and dst_img", np.hstack([img, result]))
        cv2.imwrite("/home/oem/catkin_n10/src/parks/scripts/myeuqlization.jpg",np.hstack([img, result]))
        cv2.waitKey(0)
 
 
if __name__ == '__main__':
    img = cv2.imread('/home/oem/下载/1021_1.jpg')
    equalizeHist(img)