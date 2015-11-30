#coding:utf-8
#InnerAc
import numpy as np
import cv2

colorw = (255,255,255)
colorb = (0,0,0)
image = 1

# 画白色格子,左上角坐标
def drawCell(x0,y0,b):
	rect_start = (x0*b,y0*b) 
	x1 = x0*b+b
	y1 = y0*b+b
	rect_end = (x1,y1)
	cv2.rectangle(image, rect_start, rect_end, colorw, -1)

# 初始化画布
def init(cmap,b):
	global image
	height = len(cmap)
	width = cmap.size / height
	height *= b
	width *= b
	print height,width
	image = np.zeros((height,width), np.uint8)
	# drawTwo(cmap,b)

# 画变化图像
def drawTwo(cmap,b):
	global image
	height = len(cmap)
	width = cmap.size / height
	for i in range(height):
		for j in range(width):
			if cmap[i][j] == 1:
				drawCell(i,j,b)
	win_name = "元胞自动机"
	cv2.namedWindow("元胞自动机",cv2.CV_WINDOW_AUTOSIZE)	
	cv2.imshow(win_name, image)
	cv2.waitKey(0)