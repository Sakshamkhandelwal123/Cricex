# cap = cv.VideoCapture(r'C:\Users\DELL\Downloads\cricket1.mp4')
check = 0
def coordinates() :
    print("Enter path to a sample frame")
    temp = "yes"
    path = input()
    while temp=="yes":
    
        # function to display the coordinates of
        # of the points clicked on the image 
        lst = []
        def click_event(event, x, y, flags, params):
            # checking for left mouse clicks
            if event == cv2.EVENT_LBUTTONDOWN:
        
                # displaying the coordinates
                # on the Shell
                print(x, ' ', y)
                lst.append((x,y))
        
                # displaying the coordinates
                # on the image window
                font = cv2.FONT_HERSHEY_SIMPLEX
                # cv2.putText(img, str(x) + ',' +
                #             str(y), (x,y), font,
                #             1, (255, 0, 0), 2)
                cv2.imshow('image', img)
        
            # checking for right mouse clicks     
            if event==cv2.EVENT_RBUTTONDOWN:
        
                # displaying the coordinates
                # on the Shell
                print(x, ' ', y)
        
                # displaying the coordinates
                # on the image window
                font = cv2.FONT_HERSHEY_SIMPLEX
                b = img[y, x, 0]
                g = img[y, x, 1]
                r = img[y, x, 2]
                cv2.putText(img, str(b) + ',' +
                            str(g) + ',' + str(r),
                            (x,y), font, 1,
                            (255, 255, 0), 2)
                cv2.imshow('image', img)
        
        
            # reading the image
        img = cv2.imread(path, 1)
        
            # displaying the image
        cv2.imshow('image', img)
        
            # setting mouse hadler for the image
            # and calling the click_event() function
        cv2.setMouseCallback('image', click_event)
        
            # wait for a key to be pressed to exit
        cv2.waitKey(0)
        
            # close the window
        cv2.destroyAllWindows()
        print(lst)
        x = lst[0][1]
        y = lst[0][0]
        h = lst[-1][1] - lst[0][1]
        w = lst[-1][0] - lst[0][0]
        print(x,y,h,w)
        img = cv2.imread(path)
        # frame=cv2.pyrDown(img)
        sub_frame = img[x:x+h, y:y+w]
        cv2.imshow("frame", sub_frame)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        print("do you want to retry?")
        temp = input()
    return x,y,h,w

import cv2
import numpy as np
import pytesseract
from pytesseract import image_to_string
lst1 = []
# Create a VideoCapture object and read from input file
# If the input is the camera, pass 0 instead of the video file name
print("Enter the file path")
path = input()
print("Enter the file output path (File extension should be in .avi)")
output = input()
cap = cv2.VideoCapture(path)
fps = cap.get(cv2.CAP_PROP_FPS)
print(fps)
frame_count=0
pytesseract.pytesseract.tesseract_cmd = r'Tesseract-OCR\Tesseract.exe'

# Check if camera opened successfully
if (cap.isOpened()== False): 
  print("Error opening video stream or file")

# Read until video is completed
lst = []
x,y,h,w = coordinates()
print("Please wait.....")
while(cap.isOpened()):
  # Capture frame-by-frame
  ret, frame = cap.read()
  
  if ret == True:
    # print("hello")
    frame=cv2.pyrDown(frame)
    # if(frame_count==100) : 
    #     cv2.imwrite("frames.jpg", frame)
    # print(cap.get(cv2.CAP_PROP_POS_MSEC))
    frame_count+=1
    time = float(frame_count)/fps
    lst1.append((time,frame_count))
    # lst1.append(cv2.CAP_PROP_POS_MSEC)
    # Display the resulting frame
    sub_frame = frame[x:x+h, y:y+w]
    # print(frame)
    # print(sub_frame)
    # lst.append((text, frame_count))
    # print(text)
    if(len(sub_frame)>0):
      cv2.imshow('Frame',sub_frame)
      if(frame_count%15==0):
        text = pytesseract.image_to_string(sub_frame, config='digits')
        lst.append((text, frame_count))
        # print(text)
      # Press Q on keyboard to  exit
      if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    else:
      pass

  # Break the loop
  else: 
    break

# When everything done, release the video capture object
cap.release()

# Closes all the frames
cv2.destroyAllWindows()
# print(lst1)
# print(lst)

result=""
result_fin = []
for i in lst:
    for j in i[0]:
        if(j.isnumeric() or j=='-'):
            # if(j == '\x0c' or j == '\n' or j == ' ' or j == ')'):
            #     pass
            # else:
            result = result + j
    if '-' in result:
        if(len(result)>2):
            result_fin.append((result, i[1]))
    result = ""
# print(result_fin)
result_fin.append(result_fin[-1])
# for i in result_fin:
#     print(i[0])
# print(result_fin)

#475-4
#75-4
score = []
for i in range(len(result_fin)-1):
    temp = 0
    temp1 = 0
    for j in range(len(result_fin[i][0])):
        # if(result_fin[i+1][0][j]) :
        if(result_fin[i][0][j] == '-'):
            temp = j+1
            # len(i[0]-j-1)
    for k in range(len(result_fin[i+1][0])):
        if(result_fin[i+1][0][k] == '-'):
            temp1 = k+1
    try:
        diff =  int(result_fin[i+1][0][0:temp1-1]) - int(result_fin[i][0][0:temp-1])
    except :
        diff = 10
    if(diff <= 6 and diff >= 0) :
            score.append(result_fin[i])
    else:
        if(diff<0):
            # print(result_fin[i+1][0][temp1:len(result_fin[i+1][0])])
            try:
                if(int(result_fin[i+1][0][temp1:len(result_fin[i+1][0])]) == 0):
                    score.append(result_fin[i])
            except:
                pass
            
# print(score)
    # if(result_fin[i][0][temp:len(result_fin[i][0])]==result_fin[i+1][0][temp1:len(result_fin[i+1][0])]):
        # diff = int(result_fin[i][0][0:temp-1]) - int(result_fin[i+1][0][0:temp1-1])
        # print(diff)
        # print(result_fin[i][0][temp:len(result_fin[i][0])])
        # print(result_fin[i][0][0:temp-1])
        # if(diff <= 6 and diff >= 0) :
        #     lst.append(result_fin[i])
# for i in lst:
#     print(i)

fps1 = 30*25
fps2 = 30*10
lstt = []
for i in range(len(score)-1):
    z = score[i][0].split("-")
    # print(z)
    z1 = score[i+1][0].split("-")
    z[0] = int(z[0])
    z[1] = int(z[1])
    z1[0] = int(z1[0])
    z1[1] = int(z1[1])
    if(z1[0]-z[0] > 3 or z1[1]-z[1] == 1) :
        temp = score[i+1][1]
        lstt.append((temp-fps1, temp+fps2))
# print(lstt)

cap = cv2.VideoCapture(path)
fps = cap.get(cv2.CAP_PROP_FPS)
frame_count=0
# height, width, layers = cap.shape
# size = (500,500)
# out = cv2.VideoWriter(r'D:\project.avi',cv2.VideoWriter_fourcc(*'DIVX'), 15, size)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(output, fourcc, 20.0, (1280, 720))
lstt.sort(key=lambda x:x[0])
while(cap.isOpened()):
  # Capture frame-by-frame
  ret, frame = cap.read()
  if ret == True:
    frame=cv2.pyrDown(frame)
    # print(cap.get(cv2.CAP_PROP_POS_MSEC))
    frame_count+=1
    time = float(frame_count)/fps
    # lst1.append(cv2.CAP_PROP_POS_MSEC)
    # Display the resulting frame
    # sub_frame = frame[x:x+h, y:y+w]
    # lst.append((text, frame_count))
    # print(text)
    # print(frame_count)
    if(len(lstt)!=0) :
        check = 1
        val_check = lstt[0]
        if(frame_count>=val_check[0] and frame_count<=val_check[1]):
            # cv2.imshow("hello", frame)
            b = cv2.resize(frame,(1280,720),fx=0,fy=0, interpolation = cv2.INTER_CUBIC)
            out.write(b)
            # text = pytesseract.image_to_string(sub_frame)
            # lst.append((text, frame_count))
            # print(text)
        # Press Q on keyboard to  exit
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        elif(frame_count>val_check[1]):
            lstt.pop(0)
        else:
            pass

  # Break the loop
  else: 
    break
if check!=0:
    print("File written successfully at path: ", output)
else:
    print("No highlight found. Please try again.")
# When everything done, release the video capture object
cap.release()
out.release()
# Closes all the frames
cv2.destroyAllWindows()


#4710
#5340