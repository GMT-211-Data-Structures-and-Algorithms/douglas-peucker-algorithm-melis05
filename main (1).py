from dp import *

# ── GeoJSON kullanımı (hocadan istenen format) ──────────────────────
input_file = 'Trabzon.geojson'
out_file = 'out.geojson'

epsilon = 0.01  # the higher the epsilon, the less number of points kept

execute_douglas_peucker(input_file, out_file, epsilon)


# ── Text dosyası kullanımı ──────────────────────────────────────────
# input_line_file = "line.txt"
# epsilon = 6
#
# # 2. Koordinatları listeye çevir
# input_line = convert_coordinates_to_line(input_line_file)
#
# # 3. Douglas-Peucker algoritmasını uygula
# result_list = douglas_peucker(input_line, epsilon)
#
# # 4. Sonuçları yazdır
# for point in result_list:
#     print(point[0], point[1])
