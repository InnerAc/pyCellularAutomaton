#coding:utf-8
#InnerAc
import numpy as np
import cv2
import time

colorw = (255,255,255)
colorb = (0,0,0)
colorg = (0,255,0)
image = 1

# 画白色格子,左上角坐标
def drawCell(x0,y0,b,color):
	rect_start = (x0*b,y0*b) 
	x1 = x0*b+b
	y1 = y0*b+b
	rect_end = (x1,y1)
	cv2.rectangle(image, rect_start, rect_end, color, -1)

# 初始化画布
def init(cmap,b):
	global image
	height = len(cmap)
	width = cmap.size / height
	height *= b
	width *= b
	# print height,width
	image = np.zeros((height,width), np.uint8)
	# drawTwo(cmap,b)

# 画变化图像
def drawTwo(cmap,b):
	global image
	height = len(cmap)
	width = cmap.size / height
	image = np.zeros((height*b,width*b,3))
	for i in range(height):
		for j in range(width):
			if cmap[i][j] == 1:
				# print 'white',i,j
				drawCell(j,i,b,colorg)
			else:
				# print 'black',i,j
				drawCell(j,i,b,colorb)
	win_name = "元胞自动机"
	cv2.namedWindow("元胞自动机",cv2.CV_WINDOW_AUTOSIZE)	
	cv2.imshow(win_name, image)
	# time.sleep(1)
	cv2.waitKey(100)
	
if __name__ == '__main__':
	a = np.zeros((15,10),np.uint8)
	# a[1][5] = 1
	a[14][9] = 1
	print a
	init(a,10)
	drawTwo(a,10)