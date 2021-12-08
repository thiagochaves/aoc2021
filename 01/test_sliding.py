from submarine import count_sliding_window_measurement_increases

def to_text(data):
    return "\n".join(str(number) for number in data)

def test_find_one_increase():
    data = [199, 200, 201, 202]
    c = count_sliding_window_measurement_increases(to_text(data))
    assert c == 1

def test_find_two_increases():
    data = [199, 200, 201, 202, 203]
    c = count_sliding_window_measurement_increases(to_text(data))
    assert c == 2

