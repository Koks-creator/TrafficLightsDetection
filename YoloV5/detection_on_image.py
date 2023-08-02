import cv2

from TrafficLightsYolov5.yolov5_detector import Yolov5Detector

yolov5 = Yolov5Detector(model_path=r"model/last.pt")

img = cv2.imread(rf"../images/test1.png")
img_copy = img.copy()

converted = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

results_draw, results_df = yolov5.detect(converted)
h, w, _ = img.shape
for row in results_df.iterrows():
    detection = row[1]
    # print(detection)
    bbox = (int(detection.xmin), int(detection.ymin), int(detection.xmax), int(detection.ymax))
    conf = detection.confidence
    class_name = detection['name']
    print(class_name)

    cv2.putText(img_copy, f"{class_name}: {int(round(conf, 2)*100)}%", (bbox[0], bbox[1] - 5),
                cv2.FONT_HERSHEY_PLAIN, 1.5, (255, 0, 225), 2)
    cv2.rectangle(img_copy, (bbox[0], bbox[1]), (bbox[2], bbox[3]), (255, 0, 225), 2)

results_draw = cv2.cvtColor(results_draw, cv2.COLOR_RGB2BGR)
cv2.imshow('res', results_draw)
cv2.imshow('img', img_copy)
cv2.waitKey(0)
