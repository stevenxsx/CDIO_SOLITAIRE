from statistics import mode
import cv2
import torch
from matplotlib import pyplot as plt
import numpy as np

#Loading current best model
torch.hub._validate_not_a_forked_repo=lambda a,b,c: True
model = torch.hub.load('ultralytics/yolov5', 'custom', path='src/image_rec/resources/models/trained/bests.pt', force_reload=True)

img = 'src/image_rec/resources/images/kabale6.jpeg'

results = model(img)

results.print()

print('\n', results.pandas().xyxy[0])

print(type(results.xyxy[0]))

plt.imshow(np.squeeze(results.render()), aspect='auto')
plt.savefig("results.png")