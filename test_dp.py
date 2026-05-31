"""
Douglas-Peucker algoritması test dosyası.
Hocadan verilen örnek ile test edilir.

Beklenen sonuçlar (PDF slide 13):
  epsilon = 6   → [(1.0, 2.0), (8.0, 6.0)]
  epsilon = 0.1 → [(1.0, 2.0), (6.0, -2.0), (9.0, 4.0), (8.0, 6.0)]
"""

from dp.algorithm import douglas_peucker, perpendicular_distance


def test_perpendicular_distance():
    """Dik mesafe hesabını test et."""
    # Basit test: (0,0) ile (4,0) arası yatay doğruya (2,3) noktası
    dist = perpendicular_distance((2, 3), (0, 0), (4, 0))
    assert abs(dist - 3.0) < 0.001, f"Beklenen 3.0, bulunan {dist}"
    print("test_perpendicular_distance: BASARILI")


def test_epsilon_large():
    """epsilon=6 ile sadece 2 nokta kalmali."""
    # Hocadan verilen örnek noktalar
    points = [
        (1, 2), (-1, -1), (4, -1), (5, -2),
        (6, -2), (6, 1), (8, 2), (9, 4), (8, 6)
    ]
    result = douglas_peucker(points, 6)
    print(f"epsilon=6 sonucu: {result}")
    assert result[0] == (1, 2), "Ilk nokta yanlis"
    assert result[-1] == (8, 6), "Son nokta yanlis"
    print("test_epsilon_large: BASARILI")


def test_epsilon_small():
    """epsilon=0.1 ile daha fazla nokta kalmali."""
    points = [
        (1, 2), (-1, -1), (4, -1), (5, -2),
        (6, -2), (6, 1), (8, 2), (9, 4), (8, 6)
    ]
    result = douglas_peucker(points, 0.1)
    print(f"epsilon=0.1 sonucu: {result}")
    assert result[0] == (1, 2), "Ilk nokta yanlis"
    assert result[-1] == (8, 6), "Son nokta yanlis"
    assert len(result) > 2, "Kucuk epsilon ile daha fazla nokta olmali"
    print("test_epsilon_small: BASARILI")


def test_two_points():
    """2 nokta verilirse aynen donmeli."""
    points = [(0, 0), (5, 5)]
    result = douglas_peucker(points, 1.0)
    assert result == [(0, 0), (5, 5)], "Iki nokta testi basarisiz"
    print("test_two_points: BASARILI")


def test_straight_line():
    """Düz çizgideki tüm noktalar sadeleşmeli."""
    points = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)]
    result = douglas_peucker(points, 0.1)
    # Düz çizgide sadece başlangıç ve bitiş kalmalı
    assert result == [(0, 0), (4, 0)], f"Duz cizgi testi basarisiz: {result}"
    print("test_straight_line: BASARILI")


if __name__ == "__main__":
    print("=" * 40)
    print("Douglas-Peucker Testleri Basliyor")
    print("=" * 40)
    test_perpendicular_distance()
    test_two_points()
    test_straight_line()
    test_epsilon_large()
    test_epsilon_small()
    print("=" * 40)
    print("Tum testler BASARILI!")
    print("=" * 40)
