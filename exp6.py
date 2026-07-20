import cv2

cap = cv2.VideoCapture("demonslayer.mp4")

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

out = cv2.VideoWriter("output_video.mp4",
                      cv2.VideoWriter_fourcc(*'mp4v'),
                      fps,
                      (width, height))

while True:
    ret, frame = cap.read()

    if not ret:
        break

    out.write(frame)

    cv2.imshow("Video", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()