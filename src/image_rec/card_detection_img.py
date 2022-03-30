from statistics import mode
import cv2
import torch
from matplotlib import pyplot as plt
import numpy as np

#Loading current best model
model = torch.hub.load('ultralytics/yolov5', 'custom', path='src/image_rec/resources/models/trained/best.pt', force_reload=True)

img = 'src/image_rec/resources/images/testImg.jpg'

results = model(img)

results.print()


plt.imshow(np.squeeze(results.render()), aspect='auto')
plt.savefig("results.png")