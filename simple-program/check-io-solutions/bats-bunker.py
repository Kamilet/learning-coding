def checkio(bunker):
    # set
    waypoints = []
    blocks = []
    for i in range(len(bunker)):
        for k in range(len(bunker[0])):
            if bunker[i][k] == 'B':
                waypoints.append([i, k])
            elif bunker[i][k] == 'W':
                blocks.append([i, k])
            elif bunker[i][k] == 'A':
                endpoint = (i, k)
    startpoint = waypoints[0][:]
    waypoints = waypoints[1:]
    print(blocks)
    # try any routes
    routes = []

    # change this
    distances = []
    for route in routes:
        distances.append(distance(route))
    return max(distances)


def access(point_1, point_2, blocks):
    # return True if access
    _xl = abs(point_1[1] - point_2[1])
    _yl = abs(point_1[0] - point_2[0])
    _x = min(point_1[1], point_2[1])
    _y = min(point_1[0], point_2[0])
    if not _yl and _xl:
        for x in range(1, _xl+1):
            if [_x + x, _y] in blocks:
                return False
    if not _xl and _yl:
        for y in range(1, _yl):
            if [_x, _y + y] in blocks:
                return False
    if _xl and _yl:
        if _xl == _yl:
            for i in range(1, _xl):
                if [_x + i, _y + i] in blocks:
                    return False
        else:
            if _xl > _yl:
                for x in range(1, _xl):
                    for y in range(0, _yl+1):
                        if [_x + x, _y + y] in blocks:
                            return False
            else:
                for y in range(1, _yl):
                    for x in range(0, _xl+1):
                        if [_x + x, _y + y] in blocks:
                            return False
    return True


def distance(points):
    # return distance from begin to end
    from math import sqrt
    distance = 0
    for i in range(len(points)-1):
        distance += sqrt((points[i][0] - points[i+1][0])**2 +
                         (points[i][1] - points[i+1][1])**2)
    return round(distance, 2)


# These "asserts" using only for self-checking and not necessary for
# auto-testing
if __name__ == '__main__':
    def almost_equal(checked, correct, significant_digits=2):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    assert almost_equal(checkio([
        "BW-",
        "---",
        "-SA"]), 2.83), "XXX"
    assert almost_equal(checkio([
        "B--",
        "---",
        "--A"]), 2.83), "1st example"
    assert almost_equal(checkio([
        "B-B",
        "BW-",
        "-BA"]), 4), "2nd example"
    assert almost_equal(checkio([
        "BWB--B",
        "-W-WW-",
        "B-BWAB"]), 12), "3rd example"
    assert almost_equal(checkio([
        "B---B-",
        "-WWW-B",
        "-WA--B",
        "-W-B--",
        "-WWW-B",
        "B-BWB-"]), 9.24), "4th example"
