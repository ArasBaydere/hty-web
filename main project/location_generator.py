# location.generator.py

import random
import json
import time

def generate_random_coordinates():
    # Belirli bir bölgenin koordinat sınırları
    min_latitude, max_latitude = (36, 42)  # Örnek değerler, projenize uygun şekilde değiştirin
    min_longitude, max_longitude = (26, 45)  # Örnek değerler, projenize uygun şekilde değiştirin

    # Belirli bir bölge içinde rastgele koordinat üretme
    latitude = random.uniform(min_latitude, max_latitude)
    longitude = random.uniform(min_longitude, max_longitude)
    
    return {"latitude": latitude, "longitude": longitude}

while True:
    data = generate_random_coordinates()

    # Veriyi JSON dosyasına yazma
    with open("coordinates.json", "w") as json_file:
        json.dump(data, json_file)

    # JavaScript tarafına veriyi göndermek için dosyaya yazma
    with open("static/coordinates.js", "w") as js_file:
        js_file.write("var coordinates = {};".format(json.dumps(data)))

    # Arduino'nun belirlediğiniz aralıklarla veri gönderdiğini simüle etmek için bekleme süresi
    time.sleep(5)

    # Log ekle
    print("Coordinates updated:", data)