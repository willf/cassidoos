import unittest

# This week’s question:
# When you’re representing colors in a program, you typically use HEX, RGB, or HSL.
# Write a program that converts between the different formats.
#
# Example:
#
# $ convertColor('rgb', 'hex', (255,0,0))
# $ '#FF0000'
#
# $ convertColor('hsl', 'rgb', (65,80,80))
# $ (238,245,163)
#
# $ convertColor('hsl', 'hex', (65,80,80))
# $ '#EEF5A3'

def convertColor(color1, color2, color3):
    if color1 == 'rgb' and color2 == 'hex':
        return rgb_to_hex(color3)
    elif color1 == 'hex' and color2 == 'rgb':
        return hex_to_rgb(color3)
    elif color1 == 'hsl' and color2 == 'rgb':
        return hsl_to_rgb(color3)
    elif color1 == 'rgb' and color2 == 'hsl':
        return rgb_to_hsl(color3)
    elif color1 == 'hsl' and color2 == 'hex':
        return hsl_to_hex(color3)
    elif color1 == 'hex' and color2 == 'hsl':
        return hex_to_hsl(color3)


def rgb_to_hex(rgb):
    r, g, b = rgb
    return ('#%02x%02x%02x' % (r, g, b)).upper()


def hex_to_rgb(hex):
    # From #RRGGBB to (R, G, B)
    hex = hex.strip('#')
    r = int(hex[0:2], 16)
    g = int(hex[2:4], 16)
    b = int(hex[4:6], 16)
    return (r, g, b)


def hsl_to_rgb(hsl):
    h, s, l = hsl
    h /= 360.0
    s /= 100.0
    l /= 100.0
    if s == 0:
        r = g = b = l
    else:
        def hue_to_rgb(p, q, t):
            if t < 0:
                t += 1
            if t > 1:
                t -= 1
            if t < 1/6:
                return p + (q - p) * 6 * t
            if t < 1/2:
                return q
            if t < 2/3:
                return p + (q - p) * (2/3 - t) * 6
            return p

        q = l * (1 + s) if l < 0.5 else l + s - l * s
        p = 2 * l - q
        r = hue_to_rgb(p, q, h + 1/3)
        g = hue_to_rgb(p, q, h)
        b = hue_to_rgb(p, q, h - 1/3)
    r, g, b = int(r * 255), int(g * 255), int(b * 255)
    return (r, g, b)



def rgb_to_hsl(rgb):
    r, g, b = rgb
    r, g, b = r / 255.0, g / 255.0, b / 255.0
    cmax, cmin = max(r, g, b), min(r, g, b)
    delta = cmax - cmin
    if delta == 0:
        h = 0
    elif cmax == r:
        h = ((g - b) / delta) % 6
    elif cmax == g:
        h = (b - r) / delta + 2
    else:
        h = (r - g) / delta + 4
    h = round(h * 60)
    if h < 0:
        h += 360
    l = (cmax + cmin) / 2
    if delta == 0:
        s = 0
    else:
        s = delta / (1 - abs(2 * l - 1))
    s = round(s * 100)
    l = round(l * 100)
    return (h, s, l)


def hsl_to_hex(hsl):
    return rgb_to_hex(hsl_to_rgb(hsl))


def hex_to_hsl(hex):
    return rgb_to_hsl(hex_to_rgb(hex))



class TestColorConversion(unittest.TestCase):
    def test_hsl_to_rgb(self):
        self.assertEqual(hsl_to_rgb((0, 100, 50)), (255, 0, 0))
        self.assertEqual(hsl_to_rgb((120, 100, 50)), (0, 255, 0))
        self.assertEqual(hsl_to_rgb((240, 100, 50)), (0, 0, 255))
        self.assertEqual(hsl_to_rgb((0, 0, 0)), (0, 0, 0))
        self.assertEqual(hsl_to_rgb((0, 0, 100)), (255, 255, 255))
        self.assertEqual(hsl_to_rgb((60, 50, 50)), (191, 191, 63))
        self.assertEqual(hsl_to_rgb((180, 50, 50)), (63, 191, 191))
        self.assertEqual(hsl_to_rgb((300, 50, 50)), (191, 63, 191))

    def test_rgb_to_hsl(self):
        self.assertEqual(rgb_to_hsl((255, 0, 0)), (0, 100, 50))
        self.assertEqual(rgb_to_hsl((0, 255, 0)), (120, 100, 50))
        self.assertEqual(rgb_to_hsl((0, 0, 255)), (240, 100, 50))
        self.assertEqual(rgb_to_hsl((0, 0, 0)), (0, 0, 0))
        self.assertEqual(rgb_to_hsl((255, 255, 255)), (0, 0, 100))
        self.assertEqual(rgb_to_hsl((191, 191, 63)), (60, 50, 50))
        self.assertEqual(rgb_to_hsl((64, 191, 191)), (180, 50, 50))
        self.assertEqual(rgb_to_hsl((191, 64, 191)), (300, 50, 50))

    def test_rgb_to_hex(self):
        self.assertEqual(rgb_to_hex((255, 0, 0)), "#FF0000")
        self.assertEqual(rgb_to_hex((0, 255, 0)), "#00FF00")
        self.assertEqual(rgb_to_hex((0, 0, 255)), "#0000FF")
        self.assertEqual(rgb_to_hex((0, 0, 0)), "#000000")
        self.assertEqual(rgb_to_hex((255, 255, 255)), "#FFFFFF")
        self.assertEqual(rgb_to_hex((191, 191, 64)), "#BFBF40")
        self.assertEqual(rgb_to_hex((64, 191, 191)), "#40BFBF")
        self.assertEqual(rgb_to_hex((191, 64, 191)), "#BF40BF")

    def test_hex_to_rgb(self):
        self.assertEqual(hex_to_rgb("FF0000"), (255, 0, 0))
        self.assertEqual(hex_to_rgb("#00FF00"), (0, 255, 0))
        self.assertEqual(hex_to_rgb("0000FF"), (0, 0, 255))
        self.assertEqual(hex_to_rgb("#000000"), (0, 0, 0))
        self.assertEqual(hex_to_rgb("FFFFFF"), (255, 255, 255))
        self.assertEqual(hex_to_rgb("#BFBF40"), (191, 191, 64))
        self.assertEqual(hex_to_rgb("40BFBF"), (64, 191, 191))
        self.assertEqual(hex_to_rgb("#BF40BF"), (191, 64, 191))

    def test_hsl_to_hex(self):
        self.assertEqual(hsl_to_hex((0, 100, 50)), "#FF0000")
        self.assertEqual(hsl_to_hex((120, 100, 50)), "#00FF00")
        self.assertEqual(hsl_to_hex((240, 100, 50)), "#0000FF")
        self.assertEqual(hsl_to_hex((0, 0, 0)), "#000000")
        self.assertEqual(hsl_to_hex((0, 0, 100)), "#FFFFFF")
        self.assertEqual(hsl_to_hex((60, 50, 50)), "#BFBF3F")
        self.assertEqual(hsl_to_hex((180, 50, 50)), "#3FBFBF")
        self.assertEqual(hsl_to_hex((300, 50, 50)), "#BF3FBF")

    def test_hex_to_hsl(self):
        self.assertEqual(hex_to_hsl("#FF0000"), (0, 100, 50))
        self.assertEqual(hex_to_hsl("#00FF00"), (120, 100, 50))
        self.assertEqual(hex_to_hsl("#0000FF"), (240, 100, 50))
        self.assertEqual(hex_to_hsl("#000000"), (0, 0, 0))
        self.assertEqual(hex_to_hsl("#FFFFFF"), (0, 0, 100))
        self.assertEqual(hex_to_hsl("#BFBF40"), (60, 50, 50))
        self.assertEqual(hex_to_hsl("#40BFBF"), (180, 50, 50))
        self.assertEqual(hex_to_hsl("#BF40BF"), (300, 50, 50))

if __name__ == '__main__':
    unittest.main()
