String[] pi_digits_str = "1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095505822317253594081284811174502841027019385211055596446229489549303819644288109756659334461284756482337867831652712019091456485669234603486104543266482133936072602491412737245870066063155881748815209209628292540917153643678925903600113305305488204665213841469519415116094330572703657595919530921861173819326117931051185480744623799627495673518857527248912279381830119491298336733624406566430860213949463952247371907021798609437027705392171762931767523846748184676694051320005681271452635608277857713427577896091736371787214684409012249534301465495853710507922796892589235420199561121290219608640344181598136297747713099605187072113499999983729780499510597317328160963185950244594553469083026425223082533446850352619311881710100031378387528865875332083814206171776691473035982534904287554687311595628638823537875937519577818577805321712268066130019278766111959092164201989380952572010654858632788659361533818279682303019520353018529689957736225994138912497217752834791315155748572424541506959508295331168617278558890750983817546374649393192550604009277016711390098488240128583616035637076".split("");
int[] pi_digits = new int[pi_digits_str.length];
int[] colorlist = new int[10];
float segment_div = 1000.0;
int count = 0;
int pre_digit = 3;
int[] digits = new int[20];
int offset = 100;
int digit;
int size_;


void setup() {
  fullScreen();
  background(51);
  colorMode(HSB, 100);
  for (int i = 0; i < 10; i++) {
    colorlist[i] = i * 10 + 5;
  }
  for (int i = 0; i < 10; i++) {
    digits[i] = i;
  }
  for (int i = 0; i < 10; i++) {
    digits[i + 10] = i;
  }
  for (int i = 0; i < pi_digits.length; i++) {
    pi_digits[i] = int(pi_digits_str[i]);
    print(pi_digits[i]);
  }
  if (width > height) {
    size_ = height;
  } else {
    size_ = width;
  }
}

    
void draw() {
  translate(width/2, height/2);
  draw_outer();
  digit = pi_digits[count];
  draw_from_to(pre_digit, digit, count - 1, count);
  pre_digit = digit;
  count++;
}


void draw_outer() {
  noFill();
  for (int j = 0; j < 10; j++) {
    colorMode(HSB, 100);
    stroke(color(colorlist[j], 100, 100));
    arc(0, 0, size_ - 50, size_ - 50, radians(36 * j + 5), radians(36 * j + 36 - 5));
  }
}


void draw_from_to(int pre, int now, int pre_index, int index) {
  stroke(colorlist[pre], 30, 70);
  float[] xy = from_polar(size_/2 -25, 36 * int(pre) + 5 + (26/segment_div) * pre_index);
  float[] xy2 = from_polar(size_/2 - 25, 36 * int(now) + 5 + (26/segment_div) * index);
  float x1 = xy[0];
  float y1 = xy[1];
  float x2 = xy2[0];
  float y2 = xy2[1];
  pushMatrix();
  translate(x1, y1);
  float angle = atan2((y2 - y1), (x2 - x1));
  rotate(atan2((y2 - y1), (x2 - x1)));
  float p1x = 0;
  float p2x = sqrt((x2-x1)*(x2-x1) + (y2-y1)*(y2-y1));
  float p1y;
  float p2y;
  if (int(now) == digits[int(pre)] || int(now) == digits[int(pre) + 1] || int(now) == digits[int(pre) + 2] || int(now) == digits[int(pre) + 3] || int(now) == digits[int(pre) + 4] || int(now) == digits[int(pre) + 5]) {
      p1y = offset;
      p2y = offset;
  } else {
      p1y = -offset;
      p2y = -offset;
  } if (index < segment_div)  {
      bezier(0, 0, 0, p1y, p2x, p2y, p2x, 0);
      popMatrix();
  } else {
      noLoop();
  }
}


float[] from_polar(float r, float theta_) {
  float theta;
  if (theta_ < 0) {
    theta = theta_ + 180;
  } else {
    theta = theta_;
  }
  float x = r * cos(radians(theta));
  float y = r * sin(radians(theta));
  float[] xy = {x, y};
  return xy;
}


float[] from_cart(float x, float y) {
  float r = sqrt(x*x + y*y);
  float theta = atan(y/x);
  if (y < 0) {
    float[] rth = {r, (degrees(theta) + 180)};
    return rth;
  } else {
    float[] rth = {r, degrees(theta)};
    return rth;  
  }
}
