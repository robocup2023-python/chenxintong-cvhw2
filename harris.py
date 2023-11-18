import numpy as np
import cv2


# 读取图像
img = cv2.imread('/home/oem/下载/格子.jpg')

# 转化为灰度图像
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


# 设置窗口大小和卷积核大小
window_size = 3
kernel_size = 3


# 计算图像梯度
dx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=kernel_size)
dy = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=kernel_size)


# 计算Harris矩阵的三个分量
Ixx = dx**2
Ixy = dx*dy
Iyy = dy**2


# 对Harris矩阵的三个分量进行高斯滤波
ksize = (window_size, window_size)
sigma = 1.5
Ixx = cv2.GaussianBlur(Ixx, ksize, sigma)
Ixy = cv2.GaussianBlur(Ixy, ksize, sigma)
Iyy = cv2.GaussianBlur(Iyy, ksize, sigma)


# 计算Harris响应函数
k = 0.04
det = Ixx*Iyy - Ixy**2
trace = Ixx + Iyy
R = det - k*trace**2


# 设置阈值并进行非极大值抑制
threshold = 0.05*np.max(R)
R[R < threshold] = 0
R_nms = cv2.dilate(R, np.ones((3, 3), np.uint8))
R_nms[R < R_nms] = 0


# 显示角点
corners = np.argwhere(R_nms > 0)
for corner in corners:
    x, y = corner
    cv2.circle(img, (y, x), 3, (0, 0, 255), 1)


# 显示图像
cv2.imshow('image', img)
cv2.imwrite("/home/oem/catkin_n10/src/parks/scripts/myharris.jpg",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
