import cv2

cap1 = cv2.VideoCapture("demonslayer.mp4")
cap2 = cv2.VideoCapture("demonslayer.mp4")

while True:
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()

    if not ret1 or not ret2:
        break

    # Skip one extra frame for fast motion
    cap2.read()

    cv2.imshow("Slow Motion", frame1)
    cv2.imshow("Fast Motion", frame2)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap1.release()
cap2.release()
cv2.destroyAllWindows()