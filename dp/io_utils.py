import json


# ─────────────────────────────────────────────
#  TEXT FILE  (.txt)  fonksiyonları
# ─────────────────────────────────────────────

def convert_coordinates_to_line(file_path):
    """
    Her satırda 'x y' olan text dosyasını okur,
    (x, y) tuple listesi döndürür.
    
    Örnek dosya içeriği:
        1 2
        -1 -1
        4 -1
        ...
    """
    points = []
    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            if line == '':
                continue
            parts = line.split()
            x = float(parts[0])
            y = float(parts[1])
            points.append((x, y))
    return points


def save_line_to_file(points, file_path):
    """
    Nokta listesini text dosyasına yazar.
    Her satır: 'x y'
    """
    with open(file_path, 'w') as f:
        for (x, y) in points:
            f.write(f"{x} {y}\n")
    print(f"Sonuc kaydedildi: {file_path}")
    print(f"Toplam nokta sayisi: {len(points)}")


# ─────────────────────────────────────────────
#  GEOJSON  fonksiyonları
# ─────────────────────────────────────────────

def read_geojson(file_path):
    """
    GeoJSON dosyasını okur ve koordinatları döndürür.
    LineString veya MultiLineString desteklenir.
    
    Döndürür: koordinat listelerinin listesi
              [ [(lon1,lat1), (lon2,lat2), ...], [...], ... ]
    """
    with open(file_path, 'r') as f:
        data = json.load(f)

    all_lines = []

    # GeoJSON formatındaki feature'ları gez
    features = data.get('features', [])

    # Eğer features yoksa direkt geometry bak
    if len(features) == 0:
        geometry = data.get('geometry', data)
        features = [{'geometry': geometry}]

    for feature in features:
        geometry = feature.get('geometry', {})
        geom_type = geometry.get('type', '')
        coords = geometry.get('coordinates', [])

        if geom_type == 'LineString':
            # Koordinatlar: [[lon, lat], [lon, lat], ...]
            points = [(c[0], c[1]) for c in coords]
            all_lines.append(points)

        elif geom_type == 'MultiLineString':
            # Koordinatlar: [[[lon,lat],...], [[lon,lat],...]]
            for line_coords in coords:
                points = [(c[0], c[1]) for c in line_coords]
                all_lines.append(points)

        elif geom_type == 'Polygon':
            # Polygon'un dış halkası
            for ring in coords:
                points = [(c[0], c[1]) for c in ring]
                all_lines.append(points)

        elif geom_type == 'MultiPolygon':
            for polygon in coords:
                for ring in polygon:
                    points = [(c[0], c[1]) for c in ring]
                    all_lines.append(points)

    return all_lines


def save_geojson(simplified_lines, file_path):
    """
    Sadeleştirilmiş koordinat listelerini GeoJSON olarak kaydeder.
    """
    features = []

    for line_points in simplified_lines:
        # (x, y) tuple'larını [lon, lat] formatına çevir
        coords = [[p[0], p[1]] for p in line_points]

        feature = {
            "type": "Feature",
            "geometry": {
                "type": "LineString",
                "coordinates": coords
            },
            "properties": {}
        }
        features.append(feature)

    geojson_data = {
        "type": "FeatureCollection",
        "features": features
    }

    with open(file_path, 'w') as f:
        json.dump(geojson_data, f, indent=2)

    print(f"GeoJSON kaydedildi: {file_path}")


# ─────────────────────────────────────────────
#  ANA FONKSİYON  (hocadan istenen yapı)
# ─────────────────────────────────────────────

def execute_douglas_peucker(input_file, output_file, epsilon):
    """
    Hocadan istenen ana fonksiyon.
    GeoJSON veya txt dosyasını okur, DP uygular, kaydeder.
    
    Kullanım:
        execute_douglas_peucker('bodrum.geojson', 'out.geojson', 0.01)
    """
    from dp.algorithm import douglas_peucker

    # Dosya uzantısına göre okuma yöntemini seç
    if input_file.endswith('.geojson') or input_file.endswith('.json'):
        print(f"GeoJSON dosyasi okunuyor: {input_file}")
        all_lines = read_geojson(input_file)

        print(f"Toplam hat sayisi: {len(all_lines)}")
        total_before = sum(len(l) for l in all_lines)
        print(f"Epsilon = {epsilon}")
        print(f"DP oncesi toplam nokta: {total_before}")

        # Her hat için DP uygula
        simplified_lines = []
        for line_points in all_lines:
            simplified = douglas_peucker(line_points, epsilon)
            simplified_lines.append(simplified)

        total_after = sum(len(l) for l in simplified_lines)
        print(f"DP sonrasi toplam nokta: {total_after}")
        reduction = (1 - total_after / total_before) * 100 if total_before > 0 else 0
        print(f"Azalma orani: %{reduction:.1f}")

        save_geojson(simplified_lines, output_file)

    else:
        # txt dosyası
        print(f"Text dosyasi okunuyor: {input_file}")
        points = convert_coordinates_to_line(input_file)

        print(f"Onceki nokta sayisi: {len(points)}")
        print(f"Epsilon = {epsilon}")

        result = douglas_peucker(points, epsilon)

        print(f"Sonraki nokta sayisi: {len(result)}")
        print("Sonuc noktalar:")
        for p in result:
            print(f"  {p[0]} {p[1]}")

        save_line_to_file(result, output_file)
