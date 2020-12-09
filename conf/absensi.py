import zbar
import cv2

cap = cv2.VideoCapture('sample1.mkv')
cv2.namedWindow('frame',cv2.WINDOW_NORMAL)
cv2.resizeWindow('frame', 800,800)

while(cap.isOpened()):
    ret, frame = cap.read()
    #np_frame = cv2.imread('video', frame) # does not work
    np_frame = np.asarray(cv2.GetMat(frame)) # does not work
    print(np_frame.shape)

    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
#cap.release()
#cv2.destroyAllWindows()

# image = read_image_into_numpy_array(...) # whatever function you use to read an image file into a numpy array
# scanner = zbar.Scanner()
# results = scanner.scan(image)
# for result in results:
#     print(result.type, result.data, result.quality, result.position)