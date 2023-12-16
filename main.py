import math

import cv2
import numpy as np

file_name = 'peng.jpg'


def task2():
    image1 = cv2.imread(file_name, cv2.IMREAD_GRAYSCALE)
    cv2.namedWindow('Window 1', cv2.WINDOW_FULLSCREEN)
    cv2.imshow('Window 1', image1)
    cv2.waitKey(0)

    image2 = cv2.imread(file_name, cv2.IMREAD_COLOR)
    cv2.namedWindow('Window 2', cv2.WINDOW_NORMAL)
    cv2.imshow('Window 2', image2)
    cv2.waitKey(0)

    image3 = cv2.imread(file_name, cv2.IMREAD_ANYDEPTH)
    cv2.namedWindow('Window 3', cv2.WINDOW_AUTOSIZE)
    cv2.imshow('Window 3', image3)
    cv2.waitKey(0)

    cv2.destroyAllWindows()


def task3():
    cap = cv2.VideoCapture('video.mp4')

    while True:
        ret, frame = cap.read()
        cv2.imshow('video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


def task4():
    cap = cv2.VideoCapture(0)

    w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('outputtt.mp4', fourcc, 25, (w, h))

    while True:
        ret, frame = cap.read()
        out.write(frame)

        cv2.imshow('Recording', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()


def task5():
    image = cv2.imread(file_name)

    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    cv2.imshow('Original Image', image)
    cv2.imshow('HSV Image', hsv_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def draw_pentagram_with_circle(image, center, size, color, thickness):
    points = []
    for i in range(5):
        x = int(center[0] + size * math.cos(2 * math.pi * i / 5))
        y = int(center[1] + size * math.sin(2 * math.pi * i / 5))
        points.append((x, y))
    for i in range(5):
        cv2.line(image, points[i], points[(i + 2) % 5], color, thickness)

    # Рисование круга в центре пентаграммы
    cv2.circle(image, center, size // 1, color, thickness)


def task6():
    input_video_path = 'video.mp4'
    cap = cv2.VideoCapture(input_video_path)

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        height, width, _ = frame.shape

        pentagram_image = np.copy(frame)
        center = (width // 2, height // 2)
        size = 100  # Размер пентаграммы
        color = (0, 0, 255)  # Красный цвет
        thickness = 15  # Толщина линий

        draw_pentagram_with_circle(pentagram_image, center, size, color, thickness)

        cv2.imshow('Pentagram with Circle', pentagram_image)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


# def task6():
#     input_video_path = 'video.mp4'
#
#     # Открываем видеофайл для чтения
#     cap = cv2.VideoCapture(input_video_path)
#
#     while True:
#
#         ret, frame = cap.read()
#
#         # Получаем высоту, ширину и количество каналов в изображении
#         height, width, _ = frame.shape
#
#         # Создаем копию кадра для добавления красного креста Необходимо для того, чтобы не изменять оригинальный
#         # кадр, а добавлять красный крест к его копии. Если бы мы работали напрямую с оригинальным кадром (
#         # frame), все изменения, такие как # рисование прямоугольников, влияли бы на оригинальное изображение.
#         cross_image = np.copy(frame)
#         # Рисуем два прямоугольника, образующих крест, красным цветом (0, 0, 255)
#         cv2.rectangle(cross_image, (width // 2 - 100, height // 2 - 20), (width // 2 + 100, height // 2 + 20),
#                       (0, 0, 255), 15)
#         cv2.rectangle(cross_image, (width // 2 - 20, height // 2 - 100), (width // 2 + 20, height // 2 + 100),
#                       (0, 0, 255), 15)
#
#         cv2.imshow('Red Cross', cross_image)
#
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#
#     cap.release()
#     cv2.destroyAllWindows()


def task7():
    video = cv2.VideoCapture(0)

    _, vid = video.read()

    w = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # type: ignore
    video_writer = cv2.VideoWriter("video1.mp4", fourcc, 25, (w, h))

    while True:
        # Читаем следующий кадр из видеопотока
        ok, vid = video.read()

        # Отображаем текущий кадр в окне с именем 'Video'
        cv2.imshow('Video', vid)

        # Записываем текущий кадр в видеофайл
        video_writer.write(vid)

        # Если нажата клавиша 'q', выходим из цикла
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video.release()
    video_writer.release()
    cv2.destroyAllWindows()


def task8():
    input_video_path = 0
    cap = cv2.VideoCapture('http://192.168.0.102:4747/video')

    # Бесконечный цикл для обработки каждого кадра видео
    while True:
        # Читаем кадр из видеофайла
        ret, frame = cap.read()

        # Если чтение завершено (например, конец файла), выходим из цикла
        if not ret:
            break

        # Получаем размеры кадра (высоту, ширину)
        height, width, _ = frame.shape

        # Определяем координаты центрального пикселя
        center_x, center_y = width // 2, height // 2

        # Преобразуем цвет центрального пикселя в цветовое пространство HSV frame[center_y, center_x]: Получаем цвет
        # пикселя в центре кадра (center_x, center_y - координаты центрального пикселя). np.uint8([[...]]):
        # Создаем массив NumPy, приводя значения цвета к 8-битному беззнаковому целому типу данных (
        # uint8). cv2.cvtColor(..., cv2.COLOR_BGR2HSV): Преобразуем цвет из цветового #
        # пространства BGR (цветовое пространство по умолчанию в OpenCV) в HSV (оттенок, # насыщенность, значение). [
        # 0][0]: Извлекаем значение цвета в цветовом пространстве HSV. Результат # представлен в
        # виде массива [H, S, V], где H - оттенок, S - насыщенность, V - значение.
        hsv_color = cv2.cvtColor(
            np.uint8([[frame[center_y, center_x]]]), cv2.COLOR_BGR2HSV)[0][0]

        # Определяем цвет для рисования прямоугольников в зависимости от оттенка (Hue)
        if 0 <= hsv_color[0] < 20:
            # Ближе к красному (по HSV)
            fill_color = (0, 0, 255)  # Красный
        elif 40 <= hsv_color[0] < 80:
            # Ближе к зеленому (по HSV)
            fill_color = (0, 255, 0)  # Зеленый
        else:
            # Ближе к синему (по HSV)
            fill_color = (255, 0, 0)  # Синий

        # Рисуем два прямоугольника в центре кадра с выбранным цветом
        cv2.rectangle(frame, (width // 2 - 100, height // 2 - 20), (width // 2 + 100, height // 2 + 20),
                      fill_color, 15)
        cv2.rectangle(frame, (width // 2 - 20, height // 2 - 100), (width // 2 + 20, height // 2 + 100),
                      fill_color, 15)

        # Отображаем обработанный кадр в окне с именем 'Image'
        cv2.imshow('Image', frame)

        # Если нажата клавиша 'q', выходим из цикла
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()

    cv2.destroyAllWindows()


def task9():
    cap = cv2.VideoCapture('http://192.168.0.102:4747/video')

    while True:
        ok, frame = cap.read()

        # Проверка, было ли успешно чтение кадра
        if not ok:
            break

        cv2.imshow("camera", frame)

        # Если нажата клавиша 'q', выходим из цикла
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    # task2()
    # task3()
    # task4()
    # task5()
    task6()
    # task7()
    # task8()
    # task9()
