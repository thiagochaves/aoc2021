def count_measurement_increases(text):
    depths = [int(x) for x in text.splitlines()]
    latest = depths[0]
    count = 0
    for depth in depths:
        if depth > latest:
            count = count + 1
        latest = depth
    return count


def count_sliding_window_measurement_increases(text):
    depths = [int(x) for x in text.splitlines()]
    count = 0
    a = depths[0]
    b = depths[1]
    c = depths[2]
    latest_window_sum = a + b + c
    for depth in depths[3:]:
        a, b, c = b, c, depth
        sum = a + b + c
        if sum > latest_window_sum:
            count += 1
        latest_window_sum = sum
    return count


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        content = file.read()
    print(count_measurement_increases(content))
    print(count_sliding_window_measurement_increases(content))
