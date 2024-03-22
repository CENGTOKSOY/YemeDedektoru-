import cv2
import dlib
import numpy as np
from scipy.spatial import distance as dist

# Dlib'in yüz tanıma için önceden eğitilmiş modelini yüklüyoruz
predictor_path = "shape_predictor_68_face_landmarks.dat"
face_detector = dlib.get_frontal_face_detector()
face_predictor = dlib.shape_predictor(predictor_path)

# Ağız hareketlerini analiz etmek için fonksiyon:
def analyze_mouth(mouth_points, prev_mouth_points, frame_count, movement_threshold=0.04, frames_stable=3):
    # Ağız noktaları arasındaki mesafeyi hesaplama
    mouth_movement = dist.euclidean(mouth_points[3], prev_mouth_points[3])

    # Eğer belirli bir eşiğin üzerinde hareket varsa, hareket sayacını artır:
    if mouth_movement > movement_threshold:
        frame_count += 1
    else:
        frame_count = 0

    # Eğer belirli bir sayıda frame boyunca hareket tespit edilirse, kişinin yemek yediğini varsay:
    if frame_count >= frames_stable:
        return True, frame_count
    else:
        return False, frame_count

# Kamera akışını başlat:
cap = cv2.VideoCapture(0)

# İlk frame'deki noktaları saklamak için değişkenler:
prev_mouth_points = None
frame_count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Gri tonlamaya çevir ve yüzleri algıla:
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_detector(gray)

    for face in faces:
        shape = face_predictor(gray, face)
        landmarks = np.array([[p.x, p.y] for p in shape.parts()])

        # Ağız bölgesini belirle (örnek olarak 48-67 arası dlib noktaları):
        mouth_points = landmarks[48:68]

        # İlk frame'deki noktaları sakla:
        if prev_mouth_points is None:
            prev_mouth_points = mouth_points
            continue

        # Ağız hareketlerini analiz et ve durumu güncelle:
        eating, frame_count = analyze_mouth(mouth_points, prev_mouth_points, frame_count)
        eating_status = "Yemek Yiyiyor" if eating else "Yemek Yemiyor"

        # Sonucu ekranda göster:
        cv2.putText(frame, eating_status, (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # Mevcut noktaları önceki noktalar olarak sakla:
        prev_mouth_points = mouth_points

    cv2.imshow('Frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
