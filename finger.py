import cv2

def count_digits(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Correct the color conversion
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)  # Correct the thresholding
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)  # Fix typo in 'contours' and 'digit_count'

    digit_count = 0

    for contour in contours:
        area = cv2.contourArea(contour)

        if area > 100:
            digit_count += 1  # Fix typo in 'digit_count'
    return digit_count

cap = cv2.VideoCapture(0)  # Use the default camera (0) instead of camera (1)

while True:
    ret, frame = cap.read()

    if not ret:
        break
    num_digits = count_digits(frame)
    cv2.putText(frame, f'Number of Digits: {num_digits}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow('Hand Image', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

