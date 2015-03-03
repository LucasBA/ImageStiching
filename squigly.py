#!/usr/bin/env python
import numpy as np
import cv2
from scipy.misc import imread,imsave
from numpy import zeros
from PIL import Image

img1 = cv2.imread('001.tif',0) #imports the image in true cv grey 
print img1                          #checks for image if 'None' then path is incorect
print img1.shape                    #prints the dimensions of the image 
for i in range(3196):              #iterates through the image 
    if img1[i,15] < 35 and img1[i,15] > 21:#filters out the squigle
	print "Found the something at y=" #filters out the squigle and any fragments
	print i
	if img1[i,25] < 35 and img1[i,25] > 21:
		print "Found the something at y=" 
		print i
		if img1[i,35] < 35 and img1[i,35] > 21:
			print "Found the something at y=" 
			print i
	   		if img1[i,45] < 35 and img1[i,45] > 21:
				print "Found the line at y=" 
				print i
				n1=i
				break
img2 = cv2.imread('002.tif',0) #imports the image in true cv grey 
print img2                          #checks for image if 'None' then path is incorect
print img2.shape                    #prints the dimensions of the image 
for i in range(3196):              #iterates through the image 
    if img2[i,15] < 35 and img2[i,15] > 21:#filters out the squigle
	print "Found the something at y=" #filters out the squigle and any fragments
	print i
	if img2[i,25] < 35 and img2[i,25] > 21:
		print "Found the something at y=" 
		print i
		if img2[i,35] < 35 and img2[i,35] > 21:
			print "Found the something at y=" 
			print i
	   		if img2[i,45] < 35 and img2[i,45] > 21:
				print "Found the line at y=" 
				print i
				n2=i
				break
img3 = cv2.imread('003.tif',0) #imports the image in true cv grey 
print img3                          #checks for image if 'None' then path is incorect
print img3.shape                    #prints the dimensions of the image 
for i in range(3196):              #iterates through the image 
    if img3[i,15] < 35 and img3[i,15] > 21:#filters out the squigle
	print "Found the something at y=" #filters out the squigle and any fragments
	print i
	if img3[i,25] < 35 and img3[i,25] > 21:
		print "Found the something at y=" 
		print i
		if img3[i,35] < 35 and img3[i,35] > 21:
			print "Found the something at y=" 
			print i
	   		if img3[i,45] < 35 and img3[i,45] > 21:
				print "Found the line at y=" 
				print i
				n3=i
				break
    else:
	n3=n2
			
#background = zeros([6917,15985], dtype=np.uint8)
background = zeros([6994,6717], dtype=np.uint8)
print 'ABCNBCBAC', background.shape
yb=(n1-n2)
yyb=3197-yb
yc=yb+n3-n2
yyc=yyb-(n3-n2)

print yb
print yc
print 'Image 1 shape', img1.shape
background[3197:3197*2, 2239*2:2239*3]=img1[:3197, :2339]

background[3197-yb:3197+yyb, 2239:2239*2]=img2[:3197, :2239]

background[3197-yc:3197+yyc, 0:2239]=img3[:3197, :2239]

cv2.imwrite("outz.jpg",background) 
cv2.waitKey(0)
cv2.destroyAllWindows()


