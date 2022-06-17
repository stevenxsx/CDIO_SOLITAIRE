import subprocess
#subprocess.check_call(["git", "clone", "https://github.com/ultralytics/yolov5.git","src/image_rec/resources/yolov5"])
subprocess.run(['python', 'src/image_rec/resources/yolov5/detect.py', '--source','0','--weights','src/image_rec/resources/models/trained/bests.pt','--view-img'])