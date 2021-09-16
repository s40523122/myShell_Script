import pyzbar.pyzbar as pyzbar
import numpy as np
import cv2

first = True
decodedObjects = []
tracker = cv2.TrackerCSRT_create()

cap = cv2.VideoCapture(0)        # 選擇攝影機

# Set the video resolution to HD720 (2560*720)
#cap.set(cv2.CAP_PROP_FRAME_WIDTH, 4416)
#cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1242)

def decode(img):
  labels, points = [], []
  # Find barcodes and QR codes
  decodedObjects = pyzbar.decode(img)
  # If read barcode return ret as True and the list of labels and points
  if len(decodedObjects) != 0:
    for decodedObject in decodedObjects:
      labels.append(decodedObject.data.decode("utf-8"))
      points.append(decodedObject.polygon)
      # we need the first point always at left-top
      if points[-1][0][1] > points[-1][2][1]:
        points[-1].insert(0, points[-1].pop(-1))
    ret = True
  else: 
    ret = False

  return (ret, labels, points)

# Display QR code location
def display(img, labels, points):
  for i in range(len(labels)):
    # Draw the convext hull
    cv2.polylines(img, pts=np.int32([points[i]]), isClosed=True, color=(0,255,0), thickness=2)
    cv2.putText(img, labels[i], points[i][0], cv2.FONT_HERSHEY_SIMPLEX, 1,  (0,155,255), 2, cv2.LINE_AA)


# Main
if __name__ == '__main__':
  ex = 50       # expansion of the roi
  bbox = [50, 50, 10, 10]
  while 1:
    
    _, frame = cap.read()

    if first:
      ret, _, points = decode(frame)
      if ret:
        bbox = (points[-1][0][0], points[-1][0][1], abs(points[-1][2][0]-points[-1][0][0]), abs(points[-1][2][1]-points[-1][0][1]))
        tracker.init(frame, bbox)
        first = False
    else:
      _, bbox = tracker.update(frame)

      p1 = (bbox[0]-ex, bbox[1]-ex)
      p2 = (bbox[0] + bbox[2]+ex, bbox[1] + bbox[3]+ex)
      cv2.rectangle(frame, p1, p2, (255, 0, 0), 2, 1)

      '''
      left_right_frame = np.split(frame, 2, axis=1)
      lframe = left_right_frame[0]
      rframe = left_right_frame[1]
      '''

      
      fbbox = frame[bbox[1]-ex if bbox[1] > ex else 0 : bbox[1]+bbox[3]+ex, 
                    bbox[0]-ex if bbox[0] > ex else 0 : bbox[0]+bbox[2]+ex]

      _, labels, points = decode(fbbox)

      if len(points) == 1:
        newpoints = [[[], [], [], []]]
        for i in range(len(points[0])):
          newpoints[0][i].append(points[0][i][0] + bbox[0] - ex)
          newpoints[0][i].append(points[0][i][1] + bbox[1] - ex)
        #opoints = points[0]
        #print(opoints)
        display(frame, labels, newpoints)
    cv2.imshow('frame', frame)    # 顯示圖片
    #cv2.imshow('bbox', fbbox)    # 顯示圖片


    # 若按下 q 鍵則離開迴圈
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break

  cap.release()                    # 釋放攝影機
  cv2.destroyAllWindows()          # 關閉所有 OpenCV 視窗