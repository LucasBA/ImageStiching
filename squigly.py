
#!/usr/bin/env python
import numpy as np
import cv2
from scipy.misc import imread,imsave
from numpy import zeros
from PIL import Image
from scipy import ndimage

img7 = cv2.imread('007.tif',0)#imports and rotates images 007-012
img7 = ndimage.rotate(img7, 180)

img8 = cv2.imread('008.tif',0)
img8 = ndimage.rotate(img8, 180)

img9 = cv2.imread('009.tif',0)
img9 = ndimage.rotate(img9, 180)

img10 = cv2.imread('010.tif',0)
img10 = ndimage.rotate(img10, 180)

img11 = cv2.imread('011.tif',0)
img11 = ndimage.rotate(img11, 180)

img12 = cv2.imread('012.tif',0)
img12 = ndimage.rotate(img12, 180)

img1 = cv2.imread('001.tif',0) #imports the image in true cv grey 
print img1                          #checks for image if 'None' then path is incorect
print img1.shape                    #prints the dimensions of the image 
for i in range(3196):              #iterates through the image 
    if img1[i,15] < 35 and img1[i,15] > 10:#filters out the squigle
	print "Found the something at y=" #filters out the squigle and any fragments
	print i
	if img1[i,25] < 35 and img1[i,25] > 10:
		print "Found the something at y=" 
		print i
		if img1[i,35] < 35 and img1[i,35] > 10:
			print "Found the something at y=" 
			print i
	   		if img1[i,45] < 35 and img1[i,45] > 10:
				print "Found the img1 line at y=" 
				print i
				n1=i
				break

img2 = cv2.imread('002.tif',0) #imports the image in true cv grey 
print img2                          #checks for image if 'None' then path is incorect
print img2.shape                    #prints the dimensions of the image 
for i in range(3196):              #iterates through the image 
    if img2[i,15] < 35 and img2[i,15] > 10:#filters out the squigle
	print "Found the something at y=" #filters out the squigle and any fragments
	print i
	if img2[i,25] < 35 and img2[i,25] > 10:
		print "Found the something at y=" 
		print i
		if img2[i,35] < 35 and img2[i,35] > 10:
			print "Found the something at y=" 
			print i
	   		if img2[i,45] < 35 and img2[i,45] > 10:
				print "Found the img2 line at y=" 
				print i
				n2=i
				break
img3 = cv2.imread('003.tif',0) #imports the image in true cv grey 
print img3                          #checks for image if 'None' then path is incorect
print img3.shape                    #prints the dimensions of the image 
for i in range(3196):              #iterates through the image 
    if img3[i,15] < 35 and img3[i,15] > 10:#filters out the squigle
	print "Found the something at y=" #filters out the squigle and any fragments
	print i
	if img3[i,25] < 35 and img3[i,25] > 10:
		print "Found the something at y=" 
		print i
		if img3[i,35] < 35 and img3[i,35] > 10:
			print "Found the something at y=" 
			print i
	   		if img3[i,45] < 35 and img3[i,45] > 10:
				print "Found the img3 line at y=" 
				print i
				n3=i
				break
    else:
	n3=n2
#i is row
img4 = cv2.imread('004.tif',0)
print img4
print img4.shape
i=3000
for i in range(3000,3196):
	if img4[i,15] < 35 and img4[i,15] > 10:#filters out the squigle
            print "Found the something at y=" #filters out the squigle and any fragments
	    print i
	    if img4[i,25] < 35 and img4[i,25] > 10:
		print "Found the something at y=" 
		print i
		if img4[i,35] < 35 and img4[i,35] > 10:
			print "Found the something at y=" 
			print i
	   		if img4[i,45] < 35 and img4[i,45] > 10:
				print "Found the img4 line at y=" 
				print i
				n4=i
				break
img5 = cv2.imread('005.tif',0)
print img5
print img5.shape
i=3000
for i in range(3000,3196):
	if img5[i,15] < 35 and img5[i,15] > 10:#filters out the squigle
            print "Found the something at y=" #filters out the squigle and any fragments
	    print i
	    if img5[i,25] < 35 and img5[i,25] > 10:
		print "Found the something at y=" 
		print i
		if img5[i,35] < 35 and img5[i,35] > 10:
			print "Found the something at y=" 
			print i
	   		if img5[i,45] < 35 and img5[i,45] > 10:
				print "Found the img5 line at y=" 
				print i
				n5=i
				break

img6 = cv2.imread('006.tif',0)
print img6
print img6.shape
i=3000
for i in range(3000,3196):
	if img6[i,15] < 35 and img6[i,15] > 10:#filters out the squigle
            print "Found the something at y=" #filters out the squigle and any fragments
	    print i
	    if img6[i,25] < 35 and img6[i,25] > 10:
		print "Found the something at y=" 
		print i
		if img6[i,35] < 35 and img6[i,35] > 10:
			print "Found the something at y=" 
			print i
	   		if img6[i,45] < 35 and img6[i,45] > 10:
				print "Found the img5 line at y=" 
				print i
				n6=i
				break
    	else:
	    n6=0

for i in range(1000,3196):
	if img7[i,15] < 35 and img7[i,15] > 10:#filters out the squigle
            print "Found the something at y=" #filters out the squigle and any fragments
	    print i
	    if img7[i,25] < 35 and img7[i,25] > 10:
		print "Found the something at y=" 
		print i
		if img7[i,35] < 35 and img7[i,35] > 10:
			print "Found the something at y=" 
			print i
	   		if img7[i,45] < 35 and img7[i,45] > 10:
				print "Found the img5 line at y=" 
				print i
				n7=i
				break


for i in range(2338):              #iterates through the image 
    if img1[15,i] < 28 and img1[15,i] > 10:#filters out the squigle
	print "Found the something at x=" #filters out the squigle and any fragments
	print i
	if img1[25,i] < 35 and img1[25,i] > 10:
		print "Found the something at x=" 
		print i
		if img1[35,i] < 35 and img1[35,i] > 10:
			print "Found the something at x=" 
			print i
	   		if img1[45,i] < 35 and img1[45,i] > 10:
				print "Found the img1 line at x=" 
				print i
				m1=i
				break	
for i in range(2338):              #iterates through the image 
    if img2[15,i] < 28 and img2[15,i] > 10:#filters out the squigle
	print "Found the something at x=" #filters out the squigle and any fragments
	print i
	if img2[25,i] < 35 and img2[25,i] > 10:
		print "Found the something at x=" 
		print i
		if img2[35,i] < 35 and img2[35,i] > 10:
			print "Found the something at x=" 
			print i
	   		if img2[45,i] < 35 and img2[45,i] > 10:
				print "Found the img2 line at x=" 
				print i
				m2=i
				break
for i in range(2338):              #iterates through the image 
    if img3[15,i] < 28 and img3[15,i] > 10:#filters out the squigle
	print "Found the something at x=" #filters out the squigle and any fragments
	print i
	if img3[25,i] < 35 and img3[25,i] > 10:
		print "Found the something at y=" 
		print i
		if img3[35,i] < 35 and img3[35,i] > 10:
			print "Found the something at x=" 
			print i
	   		if img3[45,i] < 35 and img3[45,i] > 10:
				print "Found the img3 line at x=" 
				print i
				m3=i
				break
    else:
        m3=m2	
for i in range(2338):              #iterates through the image 
    if img4[15,i] < 28 and img4[15,i] > 10:#filters out the squigle
	print "Found the something at x=" #filters out the squigle and any fragments
	print i
	if img4[25,i] < 35 and img4[25,i] > 10:
		print "Found the something at x=" 
		print i
		if img4[35,i] < 35 and img4[35,i] > 10:
			print "Found the something at x=" 
			print i
	   		if img4[45,i] < 35 and img4[45,i] > 10:
				print "Found the img4 line at x=" 
				print i
				m4=i
				break
i=2300
for i in range(2338):              #iterates through the image 
    if img5[15,i] < 28 and img5[15,i] > 10:#filters out the squigle
	print "Found the something at x=" #filters out the squigle and any fragments
	print i
	if img5[25,i] < 35 and img5[25,i] > 10:
		print "Found the something at x=" 
		print i
		if img5[35,i] < 35 and img5[35,i] > 10:
			print "Found the something at x=" 
			print i
	   		if img5[45,i] < 35 and img5[45,i] > 10:
				print "Found the img5 line at x=" 
				print i, "M5"
				m5=i
				break

for i in range(2338):              #iterates through the image 
    if img6[15,i] < 28 and img6[15,i] > 10:#filters out the squigle
	print "Found the something at x=" #filters out the squigle and any fragments
	print i
	if img6[25,i] < 35 and img6[25,i] > 10:
		print "Found the something at x=" 
		print i
		if img6[35,i] < 35 and img6[35,i] > 10:
			print "Found the something at x=" 
			print i
	   		if img6[45,i] < 35 and img6[45,i] > 10:
				print "Found the img5 line at x=" 
				print i, "M6"
				m6=i
				break
for i in range(2338):              #iterates through the image 
    if img7[15,i] < 28 and img7[15,i] > 10:#filters out the squigle
	print "Found the something at x=" #filters out the squigle and any fragments
	print i
	if img7[25,i] < 35 and img7[25,i] > 10:
		print "Found the something at x=" 
		print i
		if img7[35,i] < 35 and img7[35,i] > 10:
			print "Found the something at x=" 
			print i
	   		if img7[45,i] < 35 and img7[45,i] > 10:
				print "Found the img5 line at x=" 
				print i, "M6"
				m7=i
				break
for i in range(2338):              #iterates through the image 
    if img8[15,i] < 28 and img8[15,i] > 10:#filters out the squigle
	print "Found the something at x=" #filters out the squigle and any fragments
	print i
	if img8[25,i] < 35 and img8[25,i] > 10:
		print "Found the something at x=" 
		print i
		if img8[35,i] < 35 and img8[35,i] > 10:
			print "Found the something at x=" 
			print i
	   		if img8[45,i] < 35 and img8[45,i] > 10:
				print "Found the img5 line at x=" 
				print i, "M6"
				m8=i
				break

background = zeros([15985,6994], dtype=np.uint8)
#background = zeros([6994,6717], dtype=np.uint8)
print 'ABCNBCBAC', background.shape
yb=(n1-n2) #y-axis for image2.... values for line saved
yyb=3197-yb #endpaste2
yc=yb+n3-n2
yyc=yyb-(n3-n2)
xb=(m1-m2)
xxb=xb-m1
xc=xb+m3-m2
xxc=2239-(m3-m2)
yd=3197-(n4+n1)
xd=m1-m4
xxd=xd-m1
ye=n4-n5
xe=m4+m5
yf=3197-(n5+n6)
xf=m3-m6
yg=0
xxg=xxd-m7
yg=3197-n7-2*yd-n1
xh=xe-m8
yh=3197-n7-2*yd-n1
yi=3197-n7-2*yd-n1
print "m1 ", m1
print yb
print yc
print 'Image 1 shape', img1.shape
background[3197*3:3197*4, 2239*2:2239*3]=img1[:3197, :2239]


background[3197*3-yb:3197*3+yyb, 2239-m1+xxb:2239*2+xxb]=img2[:3197, :2239]

background[3197*3-yc:3197*3+yyc, 0+(m3-m2):xxc+42]=img3[:3197, :2239]
background[3197*2+yd:3197*3+yd, 2239*2+xd:2239*3+xd]=img4[:3197, :2239]
background[3197*2+ye:3197*3+ye, 2239*1+xe:2239*2+xe]=img5[:3197, :2239]
background[3197*2+yf:3197*3+yf, 0+xe:2239*1+xe]=img6[:3197, :2239]
background[3197*1+yg:3197*2+yg, 2239*2+xxg:2239*3+xxg]=img7[:3197, :2239]
background[3197*1+yh:3197*2+yh, 2239*1+xh:2239*2+xh]=img8[:3197, :2239]
background[3197*1+yi:3197*2+yi, 0+xe:2239*1+xe]=img9[:3197, :2239]
background[3197*0+yg:3197*1+yg, 2239*2+xxg:2239*3+xxg]=img10[:3197, :2239]
background[3197*0+yh:3197*1+yh, 2239*1+xh:2239*2+xh]=img11[:3197, :2239]
background[3197*0+yi:3197*1+yi, 0+xe:2239*1+xe]=img12[:3197, :2239]
cv2.imwrite("outt.jpg",background) 
cv2.waitKey(0)
cv2.destroyAllWindows()



























































'''



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
    if img1[i,15] < 35 and img1[i,15] > 10:#filters out the squigle
	print "Found the something at y=" #filters out the squigle and any fragments
	print i
	if img1[i,25] < 35 and img1[i,25] > 10:
		print "Found the something at y=" 
		print i
		if img1[i,35] < 35 and img1[i,35] > 10:
			print "Found the something at y=" 
			print i
	   		if img1[i,45] < 35 and img1[i,45] > 10:
				print "Found the img1 line at y=" 
				print i
				n1=i
				break

img2 = cv2.imread('002.tif',0) #imports the image in true cv grey 
print img2                          #checks for image if 'None' then path is incorect
print img2.shape                    #prints the dimensions of the image 
for i in range(3196):              #iterates through the image 
    if img2[i,15] < 35 and img2[i,15] > 10:#filters out the squigle
	print "Found the something at y=" #filters out the squigle and any fragments
	print i
	if img2[i,25] < 35 and img2[i,25] > 10:
		print "Found the something at y=" 
		print i
		if img2[i,35] < 35 and img2[i,35] > 10:
			print "Found the something at y=" 
			print i
	   		if img2[i,45] < 35 and img2[i,45] > 10:
				print "Found the img2 line at y=" 
				print i
				n2=i
				break
img3 = cv2.imread('003.tif',0) #imports the image in true cv grey 
print img3                          #checks for image if 'None' then path is incorect
print img3.shape                    #prints the dimensions of the image 
for i in range(3196):              #iterates through the image 
    if img3[i,15] < 35 and img3[i,15] > 10:#filters out the squigle
	print "Found the something at y=" #filters out the squigle and any fragments
	print i
	if img3[i,25] < 35 and img3[i,25] > 10:
		print "Found the something at y=" 
		print i
		if img3[i,35] < 35 and img3[i,35] > 10:
			print "Found the something at y=" 
			print i
	   		if img3[i,45] < 35 and img3[i,45] > 10:
				print "Found the img3 line at y=" 
				print i
				n3=i
				break
    else:
	n3=n2
for i in range(2338):              #iterates through the image 
    if img1[15,i] < 28 and img1[15,i] > 10:#filters out the squigle
	print "Found the something at x=" #filters out the squigle and any fragments
	print i
	if img1[25,i] < 35 and img1[25,i] > 10:
		print "Found the something at x=" 
		print i
		if img1[35,i] < 35 and img1[35,i] > 10:
			print "Found the something at x=" 
			print i
	   		if img1[45,i] < 35 and img1[45,i] > 10:
				print "Found the img1 line at x=" 
				print i
				m1=i
				break	
for i in range(2338):              #iterates through the image 
    if img2[15,i] < 28 and img2[15,i] > 10:#filters out the squigle
	print "Found the something at x=" #filters out the squigle and any fragments
	print i
	if img2[25,i] < 35 and img2[25,i] > 10:
		print "Found the something at x=" 
		print i
		if img2[35,i] < 35 and img2[35,i] > 10:
			print "Found the something at x=" 
			print i
	   		if img2[45,i] < 35 and img2[45,i] > 10:
				print "Found the img2 line at x=" 
				print i
				m2=i
				break
for i in range(2338):              #iterates through the image 
    if img3[15,i] < 28 and img3[15,i] > 10:#filters out the squigle
	print "Found the something at x=" #filters out the squigle and any fragments
	print i
	if img3[25,i] < 35 and img3[25,i] > 10:
		print "Found the something at y=" 
		print i
		if img3[35,i] < 35 and img3[35,i] > 10:
			print "Found the something at x=" 
			print i
	   		if img3[45,i] < 35 and img3[45,i] > 10:
				print "Found the img3 line at x=" 
				print i
				m3=i
				break
    else:
        m3=m2	
background = zeros([15985,6994], dtype=np.uint8)
#background = zeros([6994,6717], dtype=np.uint8)
print 'ABCNBCBAC', background.shape
yb=(n1-n2)
yyb=3197-yb
yc=yb+n3-n2
yyc=yyb-(n3-n2)
xb=(m1-m2)
xxb=xb-m1
xc=xb+m3-m2
xxc=2239-(m3-m2)
print "m1 ", m1
print yb
print yc
print 'Image 1 shape', img1.shape
background[3197*3:3197*4, 2239*2:2239*3]=img1[:3197, :2239]

background[3197*3-yb:3197*3+yyb, 2239-m1+xxb:2239*2+xxb]=img2[:3197, :2239]

background[3197*3-yc:3197*3+yyc, 0+(m3-m2):xxc+42]=img3[:3197, :2239]

cv2.imwrite("outt.jpg",background) 
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

