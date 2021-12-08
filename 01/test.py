from submarine import count_measurement_increases


def test_find_one_increase():
    data = [199, 200]
    c = count_measurement_increases(to_text(data))
    assert c == 1

def test_find_two_increases():
    data = [199, 200, 201]
    c = count_measurement_increases(to_text(data))
    assert c == 2

def to_text(data):
    return "\n".join(str(number) for number in data)

def test_static():
    data = [199, 199, 199]
    c = count_measurement_increases(to_text(data))
    assert c == 0

