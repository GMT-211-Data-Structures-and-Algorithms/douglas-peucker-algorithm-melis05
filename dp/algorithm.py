import math


def perpendicular_distance(point, line_start, line_end):
    """
    Bir nokta ile iki nokta arasındaki doğruya olan
    dik mesafeyi hesaplar.
    
    Formül: |((y2-y1)*px - (x2-x1)*py + x2*y1 - y2*x1)| / sqrt((y2-y1)^2 + (x2-x1)^2)
    """
    x1, y1 = line_start
    x2, y2 = line_end
    px, py = point

    # Payı hesapla (alan formülü)
    numerator = abs((y2 - y1) * px - (x2 - x1) * py + x2 * y1 - y2 * x1)

    # Paydayı hesapla (line_start ile line_end arası mesafe)
    denominator = math.sqrt((y2 - y1) ** 2 + (x2 - x1) ** 2)

    # line_start ve line_end aynı nokta ise mesafeyi direkt hesapla
    if denominator == 0:
        return math.sqrt((px - x1) ** 2 + (py - y1) ** 2)

    return numerator / denominator


def douglas_peucker(points, epsilon):
    """
    Douglas-Peucker algoritmasının recursive implementasyonu.
    
    Parametreler:
        points  : [(x1,y1), (x2,y2), ...] şeklinde nokta listesi
        epsilon : tolerans değeri (küçük → daha fazla nokta, büyük → daha az nokta)
    
    Döndürür:
        Sadeleştirilmiş nokta listesi
    """
    # Base case: 2 veya daha az nokta varsa direkt döndür
    if len(points) < 3:
        return points

    # Adım 1: İlk ve son noktayı birleştiren doğruyu çiz
    line_start = points[0]
    line_end = points[-1]

    # Adım 2: Ara noktaların dik mesafelerini hesapla
    max_distance = 0
    max_index = 0

    for i in range(1, len(points) - 1):
        dist = perpendicular_distance(points[i], line_start, line_end)
        if dist > max_distance:
            max_distance = dist
            max_index = i

    # Adım 3: En uzak nokta epsilon'dan büyükse böl ve recursive uygula
    if max_distance > epsilon:
        # Sol segment: baştan max_index'e kadar
        left_part = douglas_peucker(points[:max_index + 1], epsilon)
        # Sağ segment: max_index'ten sona kadar
        right_part = douglas_peucker(points[max_index:], epsilon)

        # İki parçayı birleştir (ortadaki nokta iki kez gelmesin diye [:-1])
        return left_part[:-1] + right_part

    else:
        # Adım 4: Tüm ara noktalar epsilon içinde → sadece başı ve sonu tut
        return [line_start, line_end]
