import pyzbar.pyzbar as pyzbar
import numpy as np
import cv2

cap = cv2.VideoCapture(0)        # 選擇攝影機

# Set the video resolution to HD720 (2560*720)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 4416)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1242)

#cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1344)
#cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 376)

def decode(img) :
  # Find barcodes and QR codes
  decodedObjects = pyzbar.decode(img)
  '''
  # Print results
  for obj in decodedObjects:
    print('Type : ', obj.type)
    print('Data : ', obj.data,'\n')
  '''
  return decodedObjects

# Display barcode and QR code location
def display(img, decodedObjects):

  # Loop over all decoded objects
  for decodedObject in decodedObjects:
    points = decodedObject.polygon

    # Draw the convext hull
    cv2.polylines(img, pts=np.int32([points]), isClosed=True, color=(0,255,0), thickness=2)
    cv2.putText(img, decodedObject.data.decode("utf-8"), points[0], cv2.FONT_HERSHEY_SIMPLEX, 1,  (0,155,255), 2, cv2.LINE_AA)


# Main
if __name__ == '__main__':
  while 1:
    ret, frame = cap.read()

    left_right_frame = np.split(frame, 2, axis=1)
    lframe = left_right_frame[0]
    rframe = left_right_frame[1]

    for i in [lframe, rframe]:
      decodedObjects = decode(i)
      display(i, decodedObjects)

    #cv2.imshow('frame', frame)    # 顯示圖片
    cv2.imshow('Lframe', lframe)    # 顯示圖片
    cv2.imshow('Rframe', rframe)    # 顯示圖片

    # 若按下 q 鍵則離開迴圈
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break

  cap.release()                    # 釋放攝影機
  cv2.destroyAllWindows()          # 關閉所有 OpenCV 視窗
  # Read image


