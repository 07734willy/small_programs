

def get_hue(pixel):
    hi = max(pixel)
    delta = hi - min(pixel)
    
    r, g, b = pixel

    if r == hi:
        hue = (g - b) / delta
    elif g == hi:
        hue = 2 + (b - r) / delta
    else:
        hue = 4 + (r - g) / delta

    if hue < 0:
        hue += 6
    return hue * 60

def get_color(pixel):
    colors = ["red", "orange", "yellow", "green", "blue", "violet", "red"]
    splits = [20, 40, 70, 160, 270, 330]

    hue = get_hue(pixel)
    print(hue)

    color_idx = min(i for i, h in enumerate(splits + [360]) if h >= hue)
    return colors[color_idx]

def main():
    print(get_color((0, 230, 240)))


if __name__ == "__main__":
    main()
