# TrafficLightsDetection

[![video](https://img.youtube.com/vi/lBZ-F-OED_I/0.jpg)](https://www.youtube.com/watch?v=lBZ-F-OED_I)

<h3>Models: https://drive.google.com/drive/u/0/folders/1h-s9bHixhPk3HbrkRkoV1QYL-TKi2V9y</h3>

<h3>How to train custom data using ultralitycis Yolov5</h3>
<ol>
  <li>Copy this notebook: https://colab.research.google.com/github/ultralytics/yolov5/blob/master/tutorial.ipynb</li>
  <li>Add the following cells in Train section (after logging) to intergrate notebook with Google Drive: </li>
  <br>
  from google.colab import drive <br>
  drive.mount('/content/gdrive')<br>
  !ln -s /content/gdrive/My\ Drive/ /mydrive<br>
  !ls /mydrive<br>
  <br>
  !unzip /mydrive/yolov5/train_data.zip -d /content <br>
  <br>
  !cp /mydrive/yolov5/custom_data.yaml /content/yolov5/data

  <li>Create folder on your Google Drive and name it yolov5</li>
  <li>Upload your dataset (train_data.zip)</li>
  <li>Setup ultralytics yolov5 (Setup section in notebook)</li>
  <li>Download: /content/yolov5/data/coco128.yaml</li>
  <li>Adjust it the same as I did in /YoloV5/model/custom_data.yaml</li>
  <li>Start training, adjust the number of epochs (I suggest starting with 50)</li>
  <li>Model will be saved in /runs/train/exp/weights</li>
</ol>
