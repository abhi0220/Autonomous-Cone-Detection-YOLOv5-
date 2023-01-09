
final: 0.85 mAP


## training; in command line
python3 train.py --batch 10 --epochs 300 --data 'data.yaml' --weights 'yolov5n.pt'

## validation; in command line
python3 val.py --weights '/Users/abhi/Documents/FEB_recruitment_project/Perception/cones.v4-addmoredata.yolov5pytorch/yolov5/runs/train/exp19/weights/best.pt' --batch 10 --data 'data.yaml'


## inference; in command line

# on test
python3 detect.py --source '/Users/abhi/Documents/FEB_recruitment_project/Perception/cones.v4-addmoredata.yolov5pytorch/dataset/images/test' --weights '/Users/abhi/Documents/FEB_recruitment_project/Perception/cones.v4-addmoredata.yolov5pytorch/yolov5/runs/train/exp19/weights/best.pt' --conf 0.4
# went to path: detect exp16

# on actual output images
python3 detect.py --source '/Users/abhi/Documents/FEB_recruitment_project/Perception/cones.v4-addmoredata.yolov5pytorch/images' --weights '/Users/abhi/Documents/FEB_recruitment_project/Perception/cones.v4-addmoredata.yolov5pytorch/yolov5/runs/train/exp19/weights/best.pt' --conf 0.4
# final output images went to path: FEB --> cones.pytorch--> yolov5 --> runs --> detect exp17

# detecting on expected_input video
python3 detect.py --source '/Users/abhi/Documents/FEB_recruitment_project/Perception/cones.v4-addmoredata.yolov5pytorch/Expected_Input.mp4' --weights '/Users/abhi/Documents/FEB_recruitment_project/Perception/cones.v4-addmoredata.yolov5pytorch/yolov5/runs/train/exp19/weights/best.pt' --conf 0.4
# final output saved to path: detect exp19

What I did:
use PyTorch (creating .yaml data file for inputs)
Trained YOLOv5 pre-trained model on custum inputs to classify different colored cones and create bounding boxes
Used custom data augmentation and Ultralytics 'albumentations' to reach 0.85 mAP on only 10 provided training images