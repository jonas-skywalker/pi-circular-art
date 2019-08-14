colorlist = []
with open("C:\Users\Jonas Biba\Documents\pi_digits\pi.txt", "r") as pi:
    pi_digits = list(pi.readlines()[0])

segment_div = 1000.0
count = 0
pre_digit = 3


def setup():
    size(500, 500)
    # background(51)
    colorMode(HSB, 100)
    for i in range(10):
        colorlist.append(i * 10 + 5)
    pi_digits.pop(0)
    pi_digits.pop(0)
    count = 0
    
    
def draw():
    global count
    global pre_digit
    translate(width/2, height/2)
    draw_outer()
    digit = pi_digits[count]
    draw_from_to(pre_digit, digit, count - 1, count)
    pre_digit = digit
    count += 1


def draw_outer():
    noFill()
    for j in range(10):
        colorMode(HSB, 100)
        stroke(color(colorlist[j], 100, 100))
        # fill(color(colorlist[j], 100, 100))
        arc(0, 0, 450, 450, radians(36 * j + 5), radians(36 * j + 36 - 5))


def draw_from_to(pre, now, pre_index, index):
    print("draw from " + str(pre) + " to " + str(now))
    global segment_div
    stroke(colorlist[int(pre)], 50, 100)
    x1, y1 = from_polar(225, 36 * int(pre) + 5 + (26/segment_div) * pre_index)
    x2, y2 = from_polar(225, 36 * int(now) + 5 + (26/segment_div) * index)
    mid_x = (x1 + x2) / 2
    mid_y = (y1 + y2) / 2
    mid_r, mid_theta = from_cart(mid_x, mid_y)
    mid_r -= 20 + (abs(int(now) - int(pre))) * 30
    mid_x, mid_y = from_polar(mid_r, mid_theta)
    cx, cy = calc_center(x1, y2, mid_x, mid_y, x2, y2)
    mid1x, mid1y = calc_middle_on_circle(x1, y1, mid_x, mid_y, cx, cy)
    mid2x, mid2y = calc_middle_on_circle(mid_x, mid_y, x2, y2, cx, cy)
    print(x1, y1)
    p1r, p1th = from_cart(x1, y1)
    print(p1r, p1th)
    p1x, p1y = from_polar(p1r, p1th)
    print(p1x, p1y)
    print(x2, y2)
    p2r, p2th = from_cart(x2, y2)
    print(p2r, p2th)
    p2x, p2y = from_polar(p2r, p2th)
    print(p2x, p2y)
    if index < 4:
        # line(x1, y1, mid_x, mid_y)
        # line(mid_x, mid_y, x2, y2)
        """
        beginShape()
        curveVertex(x1, y1)
        curveVertex(mid1x, mid1y)
        curveVertex(mid_x, mid_y)
        curveVertex(mid2x, mid2y)
        curveVertex(x2, y2)
        endShape()
        """
        rect(x1, y1, 20, 20)
        rect(x2, y2, 20, 20)
        rect(p1x, p1y, 20, 20)
        rect(p2x, p2y, 20, 20)
        bezier(x1, y1, p1x, p1y, p2x, p2y, x2, y2)
        #bezier(x1, y1, x1, y1, x2, y2, x2, y2)
        #noLoop()
    else:
        noLoop()


def from_polar(r, theta):
    if theta < 0:
        theta += 180
    x = r * cos(radians(theta))
    y = r * sin(radians(theta))
    return x, y


def from_cart(x, y):
    r = sqrt(x*x + y*y)
    theta = atan(y/x)
    return r, degrees(theta) 


def calc_center(x1, y1, x2, y2, x3, y3):
    ma = (y2-y1)/(x2-x1)
    mb = (y3-y2)/(x3-x2)
    x = (ma*mb*(y1-y3) + mb*(x1+x2) - ma*(x2 + x3))/(2*(mb-ma))
    y = (-1/ma) * (x - ((x1+x2)/(2)) + ((y1+y2)/(2)))
    return x, y


def calc_middle_on_circle(x1, y1, x2, y2, cx, cy):
    x1 += cx
    x2 += cx
    y1 += cy
    y2 += cy
    r1, theta1 = from_cart(x1, y1)
    r2, theta2 = from_cart(x2, y2)
    mid_r = r1
    mid_theta = (theta2 - theta1)/2
    mid_x, mid_y = from_polar(mid_r, mid_theta)
    return mid_x, mid_y
