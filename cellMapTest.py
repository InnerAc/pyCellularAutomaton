#coding:utf-8
#InnerAc
import numpy as np
import mapShowTest
import random

rand = lambda : 1 if random.randint(0,100) > 98 else 0

if __name__ == '__main__':
	height = 100
	width = 100
	b = 10
	cmap = np.zeros((height,width),np.uint8)
	for i in range(height):
		for j in range(width):
			cmap[i][j] = rand()
	mapShowTest.init(cmap,b)
	for x in range(100):
		print x
		cmap2 = np.zeros((height,width),np.uint8)
		for i in range(height):
			for j in range(width):
				tmp = 0;
				for k in range(i-1,i+2):
					for l in range(j-1,j+2):
						if(k >= 0 and l >= 0 and k < height and l < width):
							tmp += cmap[k][l]
				tmp -= cmap[i][j]
				if(tmp < 2 or tmp > 4):
					cmap2[i][j] = 0
				elif(tmp == 3):
					cmap2[i][j] = 1
				else:
					cmap2[i][j] = cmap[i][j]
		if not bool((cmap - cmap2).any()):
			print u'收敛'
			break;
		cmap = cmap2
		# print cmap
		mapShowTest.drawTwo(cmap,b)
	# print cmap
	