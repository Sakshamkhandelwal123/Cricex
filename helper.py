import cv2
print("Enter the video path")
path = input()
print("FPS of the video is: ")
cap = cv2.VideoCapture(path)
fps = cap.get(cv2.CAP_PROP_FPS)
print(fps)
frame_count=0
print("Enter the number of frames after which screenshot will be taken: ")
ss = int(input())
print("Please wait......\n")
while(cap.isOpened()):
  # Capture frame-by-frame
  ret, frame = cap.read()
  
  if ret == True:
    # print("hello")
    frame=cv2.pyrDown(frame)
    frame_count+=1
    if frame_count%ss==0 :
        cv2.imwrite("screenshot/ss"+str(frame_count)+".jpg", frame)
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
print("Process Successfull!!!")
print("Number of screenshots : ")
cap = cv2.VideoCapture(path)
length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
print(length//ss)