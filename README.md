# TrafficLightsDetection
<h3>Models: https://drive.google.com/drive/u/0/folders/1h-s9bHixhPk3HbrkRkoV1QYL-TKi2V9y</h3>
<br>

<h2>YoloV5</h2>

[![video](https://img.youtube.com/vi/lBZ-F-OED_I/0.jpg)](https://www.youtube.com/watch?v=lBZ-F-OED_I)


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
  <li>Upload your dataset (train_data.zip). It has to have the following structure:</li>
  
  ![structure](https://github.com/Koks-creator/TrafficLightsDetection/assets/73878161/708d82e3-833c-4912-963a-da8931640739)

  
  <li>Setup ult![Uploading structure.png…]()
ralytics yolov5 (Setup section in notebook)</li>
  <li>Download: /content/yolov5/data/coco128.yaml</li>
  <li>Adjust it the same as I did in /YoloV5/model/custom_data.yaml</li>
  <li>Start training, adjust the number of epochs (I suggest starting with 50). Training process is much faster comparing to
  YoloV3</li>
  <li>Model will be saved in /runs/train/exp/weights</li>
</ol>

<h2>YoloV3</h2>

[![video](https://img.youtube.com/vi/X4F-iaeY6fI/0.jpg)](https://www.youtube.com/watch?v=X4F-iaeY6fI)
<h3>How to train custom data using ultralitycis Yolov3</h3>
<ol>
  <li>Copy my notebook from YoloV3 directory</li>
  <li>Create yolov3 folder in your Google Drive and upload images.zip file (there is just 1 folder with images and labels called images)</li>
  <li>Modify 7th cell:  
    <br><b>max_batches</b>: number of classes * 2000
    <br><b>classes</b>: number of classes
    <br><b>filters</b>: 18 + ((number of classes - 1) * 3)
  </li>
  <li>Modify next cell, set classes names, for example: <b>!echo -e 'green light\nred light\nyellow light' > data/obj.names</b></li>
  <li>Run whole notebook, it will take few hours to train a model but you can re-run training from weights</li>
</ol>
