import cv2

# Open the default camera (index 0)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

# Capture a single frame
ret, frame = cap.read()

if not ret:
    print("Error: Could not read frame.")
    exit()

# Release the camera
cap.release()

# Save the captured frame to an image file
cv2.imwrite('captured_image.jpg', frame)

# Display the captured image
cv2.imshow('Captured Image', frame)
cv2.waitKey(0)
cv2.destroyAllWindows()
