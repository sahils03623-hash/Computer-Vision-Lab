import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Slow Motion (show every frame)
    cv2.imshow("Slow Motion", frame)

    # Skip two frames for fast motion
    cap.read()
    ret_fast, fast_frame = cap.read()

    if ret_fast:
        cv2.imshow("Fast Motion", fast_frame)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()