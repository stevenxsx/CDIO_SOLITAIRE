import cv2
import torch
import numpy as np

#Loading current best model
model = torch.hub.load('ultralytics/yolov5', 'custom', path='src/image_rec/resources/models/trained/best.pt', force_reload=True)

cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()
    
    # Make detections 
    results = model(frame)
    
    cv2.imshow('YOLO', np.squeeze(results.render()))
    
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()