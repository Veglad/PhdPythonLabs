def point_inside_rectangle(xP, yP, xA, yA, xB, yB, xC, yC, xD, yD):
    ABCD = 0.5 * abs((yA - yC) * (xD - xB) + (yB - yD) * (xA - xC))

    ABP = 0.5 * abs(xA * (yB - yP) + xB * (yP - yA) + xP * (yA - yB))
    BCP = 0.5 * abs(xB * (yC - yP) + xC * (yP - yB) + xP * (yB - yC))
    CDP = 0.5 * abs(xC * (yD - yP) + xD * (yP - yC) + xP * (yC - yD))
    DAP = 0.5 * abs(xD * (yA - yP) + xA * (yP - yD) + xP * (yD - yA))

    return ABCD == (ABP + BCP + CDP + DAP)

def inside_specified_zone(x, y):
    inside_main_square = point_inside_rectangle(x, y, -2, -2, -2, 2, 2, 2, 2, -2)
    inside_rhomboid = point_inside_rectangle(x, y, 0, 1, 1, 0, 0, -1, -1, 0)

    return inside_main_square and not inside_rhomboid

if __name__ == '__main__':
    print("**** Check if a point is located within the specified zone ***")
    print("Enter values coordinates (x, y): ")

    x = float(input("x = "))
    y = float(input("y = "))

    if inside_specified_zone(x, y):
        print("{} point is inside specified zone".format((x, y)))
    else:
        print("{} point is outside of specified zone".format((x, y)))
