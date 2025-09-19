import cv2
import cvlib as cv 
from cvlib.object_detection import draw_bbox
import mediapipe


video = cv2.VideoCapture(0)
labels =[]

while True:
    ret, frame = video.read()
    bbox, label, conf = cv.detect_common_objects(frame)
    output_image = draw_bbox(frame, bbox, label, conf)
    
    cv2.imshow("object Detection", output_image)
    
    for item in label:
        if item in label:
            pass
        else:
            labels.append(item)
            
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    
#print(labels)
i=0 
new_sentence =[]
for label in labels:
    if i == 0:
        new_sentence.append(f"I found a {label}, and , ")
    else:
        new_sentence.append(f"a {label}")
        
    i += 1
    
print(" ".join(new_sentence))