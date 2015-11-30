import numpy as np
import mapShowTest
import random

rand = lambda : random.randint(0,1)

if __name__ == '__main__':
	height = 8
	wight = 8
	cmap = np.zeros((height,wight),np.uint8)
	for i in range(height):
		for j in range(wight):
			cmap[i][j] = rand()
	# print cmap
	mapShowTest.init(cmap,100)
	for x in range(100):
		print x
		cmap2 = np.zeros((height,wight),np.uint8)
		for i in range(height):
			for j in range(wight):
				tmp = 0;
				for k in range(i-1,i+2):
					for l in range(j-1,j+2):
						if(k >= 0 and l >= 0 and k < height and l < wight):
							tmp += cmap[k][l]
				tmp -= cmap[i][j]
				if(tmp < 2 or tmp > 4):
					cmap2[i][j] = 0
				elif(tmp == 3):
					cmap2[i][j] = 1
				else:
					cmap2[i][j] = cmap[i][j]
		cmap = cmap2
		mapShowTest.drawTwo(cmap,100)
	print cmap
	