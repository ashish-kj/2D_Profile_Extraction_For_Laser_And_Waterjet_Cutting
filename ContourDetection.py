# Ashish Hoshika
#Algo 2
#Using Contour and edge Detection using Canny Edge Detector

#imports
import cv2
import numpy as np
import imutils

def nothing(x):
    pass

f = open("result_contour.txt", "w")


def hough():
    img = cv2.imread('saved/savedimg.jpg')
    #h, w, c = img.shape
    #img = imutils.resize(img, width=600)
    cv2.namedWindow('Output')
    cv2.namedWindow('Parameters')
    cv2.resizeWindow('Parameters', 600, 300)
    cv2.createTrackbar('Gaussian','Parameters',5,20,nothing)
    cv2.createTrackbar('Median','Parameters',7,20,nothing)
    cv2.createTrackbar('Min Rad','Parameters',22,300,nothing)
    cv2.createTrackbar('Max Rad','Parameters',25,300,nothing)
    cv2.createTrackbar('Min Dist','Parameters',22,400,nothing)

    while(1):    
        #creating a copy of the original image
        output = img.copy()
        gaussian = cv2.getTrackbarPos('Gaussian','Parameters')
        med = cv2.getTrackbarPos('Median','Parameters')
        minrad = cv2.getTrackbarPos('Min Rad','Parameters')
        maxrad = cv2.getTrackbarPos('Max Rad','Parameters')
        mindist = cv2.getTrackbarPos('Min Dist','Parameters')
        

        gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        if gaussian%2 == 0:
            gaussian += 1
        if med%2 == 0:
            med += 1

        gray_image = cv2.GaussianBlur(gray_image, (gaussian, gaussian), 0)
        gray_image = cv2.medianBlur(gray_image, med)
        # gray_image= cv2.GaussianBlur(gray_image, (7, 7), 0)
        ret, th1 = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)
        th2 = cv2.adaptiveThreshold(gray_image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 3, 5)
        th3 = cv2.adaptiveThreshold(gray_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 3, 5)

        # https://www.pyimagesearch.com/2021/04/28/opencv-morphological-operations/#:~:text=Morphological%20operations%20are%20simple%20transformations,and%20structures%20inside%20of%20images.
        kernel = np.ones((5, 5), np.uint8)
        erosion = cv2.erode(th2, kernel, iterations=1)
        dilation = cv2.dilate(erosion, kernel, iterations=1)

        imgray = cv2.Canny(erosion, 30, 100)

        circles = cv2.HoughCircles(imgray, method=cv2.HOUGH_GRADIENT, dp=1, minDist=mindist, param1=50, param2=30,
                                minRadius=minrad, maxRadius=maxrad)

        if circles is not None:
            circles = np.uint16(np.around(circles))
            blue = (0, 0, 255)
            green = (0, 255, 0)
            for i in circles[0, :]:
                # draw the outer circle
                cv2.circle(output,(i[0],i[1]),i[2], green, 2)
                # draw the center of the circle
                cv2.circle(output, (i[0], i[1]), 2, blue, 3)
        cv2.imshow("Output",output)

        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break
        elif k == ord('s'):
            cv2.imwrite('saved/savedimg.jpg', output)
            if circles is not None:
                circles = np.uint16(np.around(circles))
                for i in circles[0, :]:
                    center = (i[0], i[1])
                    radius = i[2]
                    
                    f.write("Centre: ")
                    f.write(str(center))
                    f.write("Radius: ")
                    f.write(str(radius))
                    f.write("\n")
                    
                    print("Centre: ",center)
                    print("Radius: ",radius)
            cv2.destroyAllWindows()
            hough()
            

    # close all open windows
    f.close()
    cv2.destroyAllWindows()


#variables
frameWidth = 640
frameHeight = 480

#Video/Image Params
'''
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
'''
cv2.namedWindow("Result")
cv2.resizeWindow("Result",700,700)
cv2.namedWindow("Parameters")
cv2.resizeWindow("Parameters",640,120)
cv2.createTrackbar("Threshold1","Parameters",150,255,lambda x:x)
cv2.createTrackbar("Threshold2","Parameters",255,255,lambda x:x)
cv2.createTrackbar("Area","Parameters",5000,30000,lambda x:x)
img = cv2.imread('resources/Pics_Redrawn/1.jpg')
h, w, c = img.shape
img = imutils.resize(img, width=1000)

while(1):
    #success, img = cap.read()
    #img = cv2.imread('resources/Pics_Redrawn/1.jpg')

    imgContour = img.copy()

    imgBlur = cv2.GaussianBlur(img, (7,7), 1)
    imgGray = cv2.cvtColor(imgBlur, cv2.COLOR_BGR2GRAY)

    threshold1 = cv2.getTrackbarPos("Threshold1","Parameters")
    threshold2 = cv2.getTrackbarPos("Threshold2","Parameters")
    imgCanny = cv2.Canny(imgGray, threshold1, threshold2)

    kernel = np.ones((5,5))
    imgDil = cv2.dilate(imgCanny,kernel,iterations=1)

    contours, hierarchy = cv2.findContours(imgDil, cv2.RETR_CCOMP,cv2.CHAIN_APPROX_NONE)

    for cnt in contours:
        area = cv2.contourArea(cnt)
        areaMin = cv2.getTrackbarPos("Area","Parameters")
        if area > areaMin :
            cv2.drawContours(imgContour, cnt, -1,(255,0,255), 7)
            perimeter = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt, 0.02*perimeter,True)
            #print(len(approx))

            #x , y , w , h = cv2.boundingRect(approx)
            #cv2.rectangle(imgContour, (x , y),(x + w, y + h),(2,255,0),5)

            #cv2.putText(imgContour,"Points: " + str(len(approx)), (x + w + 20, y  + 20), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0,255,0) , 2)
            #cv2.putText(imgContour,"Area: " + str(int(area)), (x + w + 20, y + 45), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0,255,0) , 2)

    cv2.imshow("Result", imgContour)

    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        cv2.destroyAllWindows()
        break
    elif k == ord('s'):
        cv2.imwrite('saved/savedimg.jpg', imgContour)
        cv2.destroyAllWindows()
        hough()
        break







