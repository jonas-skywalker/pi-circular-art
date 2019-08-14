colorlist = []
with open("pi.txt", "r") as pi:
    pi_digits = list(pi.readlines()[0])

segment_div = 1000.0
count = 0
pre_digit = 3
digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def setup():
    #size(800, 700)
    fullScreen()
    background(51)
    colorMode(HSB, 100)
    for i in range(10):
        colorlist.append(i * 10 + 5)
    pi_digits.pop(0)
    pi_digits.pop(0)
    count = 0
    
    
def draw():
    #frameRate(2)
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
        arc(0, 0, height - 50, height - 50, radians(36 * j + 5), radians(36 * j + 36 - 5))


def draw_from_to(pre, now, pre_index, index):
    #print("draw from " + str(pre) + " to " + str(now))
    global segment_div
    stroke(colorlist[int(pre)], 30, 70)
    x1, y1 = from_polar(height/2 -25, 36 * int(pre) + 5 + (26/segment_div) * pre_index)
    x2, y2 = from_polar(height/2 - 25, 36 * int(now) + 5 + (26/segment_div) * index)
    push()
    translate(x1, y1)
    angle = atan2((y2 - y1), (x2 - x1))
    rotate(atan2((y2 - y1), (x2 - x1)))
    p1x = 0
    p2x = sqrt((x2-x1)*(x2-x1) + (y2-y1)*(y2-y1))
    if int(now) == digits[int(pre)] or int(now) == digits[int(pre) + 1] or int(now) == digits[int(pre) + 2] or int(now) == digits[int(pre) + 3] or int(now) == digits[int(pre) + 4] or int(now) == digits[int(pre) + 5]:
        p1y = 40
        p2y = 40
    else:
        p1y = -40
        p2y = -40
    if index < segment_div:
        bezier(0, 0, 0, p1y, p2x, p2y, p2x, 0)
        pop()
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
    if y < 0:
        return r, degrees(theta) + 180
    else:
        return r, degrees(theta)
