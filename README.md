# Yüz Tanıma ile Ağız Hareketleri Analizi

Bu proje, dlib ve OpenCV kütüphanelerini kullanarak yüz tanıma ve ağız hareketlerini analiz etmek için bir Python betiğidir. Kullanıcıların yemek yeme hareketlerini tespit edebilir.

##Kullanım
Script’i çalıştırmak için, terminalden aşağıdaki komutu kullanın:
python mouth_movement_analyzer.py

##Fonksiyonlar
analyze_mouth: Ağız noktaları arasındaki mesafeyi hesaplar ve belirli bir eşiğin üzerinde hareket olup olmadığını kontrol eder.

##Geliştirme
Bu script, ağız hareketlerini analiz etmek için dlib’in yüz tanıma modelini kullanır. İlk frame’deki ağız noktalarını saklar ve her frame’de bu noktaları günceller.


## Kurulum
Projeyi çalıştırmadan önce, aşağıdaki kütüphanelerin yüklü olduğundan emin olun:

- OpenCV
- dlib
- numpy
- scipy

Eğer henüz yüklenmediyse, aşağıdaki komutları kullanarak yükleyebilirsiniz:

```bash
pip install opencv-python
pip install dlib
pip install numpy
pip install scipy

