#!/usr/bin/env python
import numpy as np
import cv2
from scipy.misc import imread
from scipy.misc import imsave
from numpy import zeros
from PIL import Image
from scipy import ndimage


def generate_workspace():
    ''' This creates a black background that the images are pasted onto '''
    background = zeros([13000,6994], dtype=np.uint8)
    print "generated background/workspace"
    return background

def import_first_six_images():
    ''' This imports the first six images then saves them to list 
        and returns the list 
        '''
    img1 = cv2.imread('001.tif',0)
    img2 = cv2.imread('002.tif',0)
    img3 = cv2.imread('003.tif',0)
    img4 = cv2.imread('004.tif',0)
    img5 = cv2.imread('005.tif',0)
    img6 = cv2.imread('006.tif',0)
    empty_img0 = 0
    ''' The empty image is used to index the list by one 
        so the images' names corispond with their index
    '''
    imgs = (empty_img0, img1, img2, img3, img4, img5, img6)
    print "imported all images"
    return imgs

def rotate_images():
    ''' This imports the last six images then rotates them 
        because the panel is rotated when they are taken 
        saves them to list and returns the list 
        '''
    img7 = cv2.imread('007.tif',0)
    img8 = cv2.imread('008.tif',0)
    img9 = cv2.imread('009.tif',0)
    img10 = cv2.imread('010.tif',0)
    img11 = cv2.imread('011.tif',0)
    img12 = cv2.imread('012.tif',0)

    img7 = ndimage.rotate(img7, 180)
    img8 = ndimage.rotate(img8, 180)
    img9 = ndimage.rotate(img9, 180)
    img10 = ndimage.rotate(img10, 180)
    img11 = ndimage.rotate(img11, 180)
    img12 = ndimage.rotate(img12, 180)
    print "rotated 007-012"
    empty_img0 = 0
    empty_img1 = 0
    empty_img2 = 0
    empty_img3 = 0
    empty_img4 = 0
    empty_img5 = 0
    empty_img6 = 0
    ''' The empty images are used to index the list by 7 
        so the images' names corispond with their index
    '''
    rot_imgs = (empty_img0, empty_img1, empty_img2, empty_img3, empty_img4, 
                empty_img5, empty_img6, img7, img8, img9, img10, img11, img12)
    return rot_imgs

def scan_top_to_bottom(img,starting_point):
    ''' This for loop iterates down the image looking for a hoizontal guideline 
        and returns its location. If it doesn't find one, 
        it asumes it is at the very top of the image and retuns a zero
    '''
    imgx = img
    for i in range(starting_point, 3196):              #iterates through the image 
        if imgx[i,150] < 35 and imgx[i,150] > 10:#filters out the squigle
            if imgx[i,250] < 35 and imgx[i,250] > 10:
                if imgx[i,350] < 35 and imgx[i,350] > 10:
                       if imgx[i,450] < 35 and imgx[i,450] > 10:
                        return i
    return 0

def scan_left_to_right(img, starting_point):
    ''' This for loop iterates across the image looking for a vertical guideline 
        and returns its location. If it doesn't find one, 
        it asumes it is at the very left of the image and retuns a zero
    '''
    imgx = img
    for i in range(2337,starting_point):              #iterates through the image 
        if imgx[150,i] < 28 and imgx[150,i] > 10:#filters out the squigle
            if imgx[250,i] < 35 and imgx[250,i] > 10:
                if imgx[350,i] < 35 and imgx[350,i] > 10:
                       if imgx[450,i] < 35 and imgx[450,i] > 10:
                            if(i<30):
                                return i                    
    return 0

def place_image(img_name, img, n, m, updated_background):
    ''' This recives an integer name, one through 12, for an image(img_name), the image, 
        the list containing the horizontal(n) and veritcal(m) guideline locations, 
        and the background containing any pasted images 
        It calculates the correct offset based on the locations of the guidelines and pastes the images 
    '''
    background = updated_background
    uniform_x_offset = 138 #used to center the new image in the workspace horizontally
    vertical_length = 3196 #the number of pixels when count down the y-axis

    ''' The y_axis_coefficent and x_axis_coefficent determine the general area in which the images are placed
        this is the same for every panel because the images are always taken in the same order see the procedure doc 
    '''
    if (img_name == 1 or img_name == 2 or img_name == 3):
        y_axis_coefficent = 3
    elif (img_name == 4 or img_name == 5 or img_name == 6):
        y_axis_coefficent = 2
    elif (img_name == 7 or img_name == 8 or img_name == 9):
        y_axis_coefficent = 1
    else:#10, 11, 12
        y_axis_coefficent = 0

    if (img_name == 1 or img_name == 4 or img_name == 7 or img_name == 10):
        x_axis_coefficent = 2
    elif (img_name == 2 or img_name == 5 or img_name == 8 or img_name == 11):
        x_axis_coefficent = 1
    else:#3, 6, 9, 12
        x_axis_coefficent = 0

    ''' This is where the actual stitching takes place. First img1 is placed and used as an origin.
        The location of the guidelines are used to calculate offsets, as the images get further 
        from the origin the offsets are sumed in order to minimize gaps within the final image.
        For images 1, 2, 3 the horizontal guideline is expected at the top of the image (0).
        For all others it is expected at the bottom of the image (3196).
        For all images the veritcal guideline is expected at the left edge (0).
        Offsets are based off distances from these expected locations. 
    '''
    if(img_name == 1):    
        precise_y_offset =0
        precise_x_offset =0
    elif(img_name == 2):    
        precise_y_offset = n[2]-n[1]
        precise_x_offset = m[1]-m[2]
    elif(img_name == 3):    
        precise_y_offset = n[3]-n[1]
        precise_x_offset = m[1]-m[2]-m[3]
    elif(img_name == 4):    
        precise_y_offset = -n[4]+n[1]
        precise_x_offset = m[1]-m[4]
    elif(img_name == 5):    
        precise_y_offset = -n[5]+n[1]+vertical_length
        precise_x_offset = m[1]-m[2]-m[3]-m[5]
    elif(img_name == 6):    
        precise_y_offset = -n[6]+n[1]+vertical_length
        precise_x_offset = m[1]-m[2]-m[3]-m[5]-m[6]
    elif(img_name == 7):    
        precise_y_offset = -n[7]-n[4]+n[1]+vertical_length
        precise_x_offset = m[1]-m[7]
    elif(img_name == 8):    
        precise_y_offset = -n[8]+n[1]+vertical_length
        precise_x_offset = m[1]-m[7]-m[8]        
    elif(img_name == 9):    
        precise_y_offset = -n[9]+n[1]+vertical_length
        precise_x_offset = m[1]-m[7]-m[8]-m[9]    
    elif(img_name == 10):    
        precise_y_offset = -n[10]-n[7]-n[4]+n[1]+vertical_length*2
        precise_x_offset = m[1]-m[10]
    elif(img_name == 11):    
        precise_y_offset = -n[11]-n[7]-n[4]+n[1]+vertical_length*2
        precise_x_offset = m[1]-m[10]-m[11]    
    elif(img_name == 12):    
        precise_y_offset = -n[12]-n[7]-n[4]+n[1]+vertical_length*2
        precise_x_offset = m[1]-m[10]-m[11]-m[12]    
    ''' This is where the paste occurs. A space is prepared in a particular locaton 
        then the contents of the image are writen into that space.
    '''
    background[3197*y_axis_coefficent+precise_y_offset:3197*(y_axis_coefficent+1)+precise_y_offset, 
               2239*x_axis_coefficent+precise_x_offset+uniform_x_offset:2239*(x_axis_coefficent+1)+uniform_x_offset+precise_x_offset]=img[:3197, :2239]
    return background


if __name__ == '__main__':
    

    background = generate_workspace()
    imgs=import_first_six_images()
    rot_imgs = rotate_images()
    n1 = scan_top_to_bottom(imgs[1], 0)
    n2 = scan_top_to_bottom(imgs[2], 0)
    n3 = scan_top_to_bottom(imgs[3], 0)
    n4 = scan_top_to_bottom(imgs[4], 3000)
    n5 = scan_top_to_bottom(imgs[5], 3000)
    n6 = scan_top_to_bottom(imgs[6], 3000)
    n7 = scan_top_to_bottom(rot_imgs[7], 3000)
    n8 = scan_top_to_bottom(rot_imgs[8], 3000)
    n9 = scan_top_to_bottom(rot_imgs[9], 3000)
    n10 = scan_top_to_bottom(rot_imgs[10], 3000)
    n11 = scan_top_to_bottom(rot_imgs[11], 3100)
    n12 = scan_top_to_bottom(rot_imgs[12], 3000)
    empty_n0=0
    ''' The empty location is used to index the list by one 
        so the locations' names corispond with their index
    '''
    n = (empty_n0, n1, n2, n1, n3, n4, n5, n6, n7, n8, n9, n10, n11, n12)
    m1 = scan_left_to_right(imgs[1],0)
    m2 = scan_left_to_right(imgs[2],0)
    m3 = scan_left_to_right(imgs[3],0)
    m4 = scan_left_to_right(imgs[4],0)
    m5 = scan_left_to_right(imgs[5],0)
    m6 = scan_left_to_right(imgs[6],0)
    m7 = scan_left_to_right(rot_imgs[7],0)
    m8 = scan_left_to_right(rot_imgs[8],0)
    m9 = scan_left_to_right(rot_imgs[9],0)
    m10 = scan_left_to_right(rot_imgs[10],0)
    m11 = scan_left_to_right(rot_imgs[11],0)
    m12 = scan_left_to_right(rot_imgs[12],0)
    empty_m0=0
    ''' The empty location is used to index the list by one 
        so the locations' names corispond with their index
    '''
    m = (empty_m0, m1, m2, m1, m3, m4, m5, m6, m7, m8, m9, m10, m11, m12)
    background = place_image(1,imgs[1], n, m, background)
    background = place_image(2,imgs[2], n, m, background)
    background = place_image(3,imgs[3], n, m, background)
    background = place_image(4,imgs[4], n, m, background)
    background = place_image(5,imgs[5], n, m, background)
    background = place_image(6,imgs[6], n, m, background)
    background = place_image(7,rot_imgs[7], n, m, background)
    background = place_image(8,rot_imgs[8], n, m, background)
    background = place_image(9,rot_imgs[9], n, m, background)
    background = place_image(10,rot_imgs[10], n, m, background)
    background = place_image(11,rot_imgs[11], n, m, background)
    background = place_image(12,rot_imgs[12], n, m, background)
    cv2.imwrite("NEWDSF***.jpg",background) 
    cv2.waitKey(0)
    cv2.destroyAllWindows()
