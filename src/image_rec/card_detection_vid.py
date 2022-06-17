import cv2
import torch
import numpy as np

#Loading current best model
torch.hub._validate_not_a_forked_repo=lambda a,b,c: True
model = torch.hub.load('ultralytics/yolov5', 'custom', path='src/image_rec/resources/models/trained/bests.pt', force_reload=True)

detections = []

cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()
    
    # Make detections 
    results = model(frame)
    
    results.xyxy[0]  # im predictions (tensor)
    
    #print('\n', results.xyxy[0])
    
    cv2.imshow('YOLO', np.squeeze(results.render()))
    # This is for detecting the cards, and adding them to the detection array, which will be sent over to our algorithm.
    if cv2.waitKey(10) & 0xFF == ord('d'):
        detectedCard = results.pandas().xyxy[0]['name']
        cardName = detectedCard.to_string()[5:]
      
        cardConvert = {"AceOfCloves": 'C1', "AceOfSpades": 'S1', "AceOfHearts": 'H1', "AceOfDiamonds": 'D1', "2OfCloves": 'C2', "2OfSpades": 'S2', "2OfHearts": 'H2', "2OfDiamonds": 'D2', "3OfCloves": 'C3', "3OfSpades": 'S3', "3OfHearts": 'H3', "3OfDiamonds": 'D3', "4OfCloves": 'C4', "4OfSpades": 'S4', "4OfHearts": 'H4', "4OfDiamonds": 'D4',"5OfCloves": 'C5', "5OfSpades": 'S5', "5OfHearts": 'H5', "5OfDiamonds": 'D5', "6OfCloves": 'C6', "6OfSpades": 'S6', "6OfHearts": 'H6', "6OfDiamonds": 'D6', "7OfCloves": 'C7', "7OfSpades": 'S7', "7OfHearts": 'H7', "7OfDiamonds": 'D7',
"8OfCloves": 'C8', "8OfSpades": 'S8', "8OfHearts": 'H8', "8OfDiamonds": 'D8', "9OfCloves": 'C9', "9OfSpades": 'S9', "9OfHearts": 'H9', "9OfDiamonds": 'D9', "10OfCloves": 'C10', "10OfSpades": 'S10', "10OfHearts": 'H10', "10OfDiamonds": 'D10', "JackOfCloves": 'C11', "JackOfSpades": 'S11', "JackOfHearts": 'H11', "JackOfDiamonds": 'D11', "QueenOfCloves": 'C12', "QueenOfSpades": 'S12', "QueenOfHearts": 'H12', "QueenOfDiamonds": 'D12',"KingOfCloves": 'C13', "KingOfSpades": 'S13', "KingOfHearts": 'H13', "KingOfDiamonds": 'D13'}

        card = cardConvert.get(cardName, "Card not recognized, please point camera at the corner of the card.")

        if len(card) > 3:
            print(card)
        else:
            detections.append(card)
            print("Succesfully entered a card")
            print(detections)
            
    # Prints whatever is in the detection array, can be used to check if any of the inputs are incorrect.
    if cv2.waitKey(11) & 0xFF == ord('p'):
        print(detections)

    # Prints whatever is in the detection array, can be used to check if any of the inputs are incorrect.
    if cv2.waitKey(12) & 0xFF == ord('c'):
        detections.clear()
        print("Succesfully cleared detection array")
        print(detections)

    # Prints whatever is in the detection array, can be used to check if any of the inputs are incorrect.
    if cv2.waitKey(13) & 0xFF == ord('l'):
        lastcard = len(detections)-1
        detections.pop(lastcard)
        print("Succesfully cleared detełtion array")
        print(detections)
        
    # This is for manually inputting the cards, if the detection for some reason fails.
    if cv2.waitKey(14) & 0xFF == ord('m'):
        manual_Detection = input("Enter card suit and rank: ") # The format is f.x King of hearts = H13
        detections.append(manual_Detection)
        print("Succesfully entered a card")
        print(detections)
    
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()