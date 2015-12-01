#coding:utf-8
#InnerAc
import numpy as np
import mapShowTest
import random
born = 95
height = 100
width = 100
rate = 10
cmap = 0
# rand = lambda : 1 if random.randint(0,100) > born else 0

def init(m_height,m_width,m_rate,m_born):
	global height,width,rate,born
	height = m_height
	width = m_width
	rate = m_rate
	born = m_born
	
def createFirst():
	global cmap
	global born
	cmap = np.zeros((height,width),np.uint8)
	print born
	for i in range(height):
		for j in range(width):
			cmap[i][j] = 1 if random.randint(0,100) > born else 0
	mapShowTest.init(cmap,rate)
	mapShowTest.drawTwo(cmap,rate)
	print cmap
def caluNext(num):
	global cmap
	for x in range(num):
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
		mapShowTest.drawTwo(cmap,rate)

def start(num):
	createFirst()
	caluNext(num)

if __name__ == '__main__':
	"""
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
	"""
	init(10,10,10,50)
	start(100)