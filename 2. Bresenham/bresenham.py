def get_line(x0, y0, x1, y1):
    points = []

    #Absoluto para saber la magnitu
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)

    #Para ver la dirección : se mueve para arriba, abajo, derecha o izquierda
    sx = 1 if x0 < x1 else -1 #1 = derecha, -1 = izquierda
    sy = 1 if y0 < y1 else -1 #1 = arriba, -1 = abajo

    while True:
        points.append((x0, y0))
        if x0 == x1 and y0 == y1:
            break #determina el punto final
        Pk = 2 * dx - dy
        if Pk > -dy:
            Pk -= dy
            x0 += sx
        if Pk < dx:
            Pk += dx
            y0 += sy

    return points


if __name__ == "__main__":
    x0 = 2
    y0 = 5
    x1 = 8
    y1 = 5
    points = get_line(x0, y0, x1, y1)
    print(points)
