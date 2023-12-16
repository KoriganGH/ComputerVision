import cv2
import numpy as np

# Задание 1: Чтение изображения с камеры
video_path = 'VID.mp4'
cap = cv2.VideoCapture(video_path)

while True:
    ret, frame = cap.read()  # Чтение кадра с камеры
    if not ret:
        break

    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    cv2.imshow('HSV Frame', hsv_frame)
    # Задание 2: Фильтрация и вывод красной части изображения
    lower_red = np.array([0, 0, 100])
    upper_red = np.array([100, 100, 255])
    red_mask = cv2.inRange(frame, lower_red, upper_red)
    red_filtered = cv2.bitwise_and(frame, frame, mask=red_mask)

    # Задание 3: Морфологические преобразования
    kernel = np.ones((5, 5), np.uint8)
    opening = cv2.morphologyEx(red_filtered, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)

    # Задание 4: Преобразование в черно-белое изображение и поиск моментов
    gray = cv2.cvtColor(closing, cv2.COLOR_BGR2GRAY)
    contours, _ = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        area = cv2.contourArea(contour)
        print("Площадь объекта:", area)

    # Задание 5: Найти центр и построить прицел
    if contours:
        largest_contour = max(contours, key=cv2.contourArea)
        moments = cv2.moments(largest_contour)
        if moments["m00"] != 0:
            cx = int(moments["m10"] / moments["m00"])
            cy = int(moments["m01"] / moments["m00"])

            # # Рисование прицела (перекрестия)
            # # Вертикальная линия
            # cv2.line(frame, (cx, cy - 50), (cx, cy + 50), (0, 255, 0), 4)
            # # Горизонтальная линия
            # cv2.line(frame, (cx - 50, cy), (cx + 50, cy), (0, 255, 0), 4)
            #
            # cv2.circle(frame, (cx, cy), 35 // 1, (0, 255, 0), 4)

            # Рисование прямоугольника вокруг объекта с использованием координат центра масс и вычисленных ширины и
            # высоты.
            width = height = int(np.sqrt(area))+150
            cv2.rectangle(
                frame,
                (cx - (width // 4), cy - (height // 4)),  # Верхний левый угол
                (cx + (width // 4), cy + (height // 4)),  # Нижний правый угол
                (0, 0, 0),  # Цвет прямоугольника (черный в формате BGR)
                2  # Толщина линии прямоугольника
            )

    cv2.imshow("Original", frame)
    cv2.imshow("Filtered", closing)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
