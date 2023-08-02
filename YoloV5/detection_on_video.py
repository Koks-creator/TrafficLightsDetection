from time import time
import cv2

from YoloV5.yolov5_detector import Yolov5Detector

yolov5 = Yolov5Detector(model_path=r"model/last.pt")
cap = cv2.VideoCapture(r"..\videos\video (720p).mp4")

p_time = 0
while cap.isOpened():
    _, frame = cap.read()
    frame_copy = frame.copy()

    converted = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results_draw, results_df = yolov5.detect(converted)
    h, w, _ = frame.shape
    for row in results_df.iterrows():
        detection = row[1]
        # print(detection)
        bbox = (int(detection.xmin), int(detection.ymin), int(detection.xmax), int(detection.ymax))
        conf = detection.confidence
        class_name = detection['name']
        print(class_name)

        cv2.putText(frame_copy, f"{class_name}: {round(conf, 2)}", (bbox[0], bbox[1]-5), cv2.FONT_HERSHEY_PLAIN, 1.5, (255, 0, 225), 2)
        cv2.rectangle(frame_copy, (bbox[0], bbox[1]), (bbox[2], bbox[3]), (255, 0, 225), 2)

    results_draw = cv2.cvtColor(results_draw, cv2.COLOR_RGB2BGR)

    c_time = time()
    fps = int(1 / (c_time - p_time))
    p_time = c_time

    cv2.putText(frame_copy, f"FPS: {fps}", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    cv2.imshow('res', results_draw)
    cv2.imshow('frame', frame_copy)
    key = cv2.waitKey(1)

    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
