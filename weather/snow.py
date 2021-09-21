import cv2 as cv
import numpy as np

# Function generating random snow
def generate_random_balls(imshape,ball_size):
    balls=[]
    numBalls = (imshape[0] * imshape[1]) // 120

    for i in range(numBalls): ## If You want heavy fall, try increasing this                  
        x= np.random.randint(0,imshape[1])        
        y= np.random.randint(0,imshape[0])        
        balls.append((x,y))    
    return balls


# Function adding snow
def add_snow(image):        
    imshape = image.shape

    ball_size = 3
    ball_color = (255, 255, 255)

    balls = generate_random_balls(imshape, ball_size)

    for ball in balls:
        cv.circle(image, (ball[0], ball[1]), 1, ball_color, thickness=-1)
    
    return image

# Reading image
img = cv.imread(r"C:\Users\Vishwam\Desktop\Mini\Computer_Vision\dataset\images\img2.jpg")
cv.imshow('Original Image',img)

# Adding rain
snowy = add_snow(img)
cv.imshow('Snowy Image',snowy)

cv.waitKey(0)