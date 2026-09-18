from PIL import Image, ImageOps
import os

# (src, dest, max_dim)
jobs = [
    ("assets/raw/p9_0_74.jpeg", "assets/img/hero-bts-silhouette.jpg", 1800),
    ("assets/raw/p13_0_92.jpeg", "assets/img/founder-cover.jpg", 1200),
    ("assets/raw/p10_0_79.jpeg", "assets/img/work-portrait-01.jpg", 1400),
    ("assets/raw/p3_0_40.png", "assets/img/work-product-bag.jpg", 1400),
    ("assets/raw/p3_1_41.jpeg", "assets/img/bts-smoke-01.jpg", 1400),
    ("assets/raw/p4_0_45.png", "assets/img/work-portrait-02.jpg", 1400),
    ("assets/raw/p4_1_46.jpeg", "assets/img/work-fineart-wings.jpg", 1400),
    ("assets/raw/p4_2_47.jpeg", "assets/img/work-food-01.jpg", 1200),
    ("assets/raw/p4_3_48.jpeg", "assets/img/work-food-02.jpg", 1200),
    ("assets/raw/p4_4_49.png", "assets/img/work-flatlay.jpg", 1600),
    ("assets/raw/p5_1_54.png", "assets/img/bts-night.jpg", 1200),
    ("assets/raw/p6_0_58.jpeg", "assets/img/work-food-03.jpg", 1200),
    ("assets/raw/p6_1_60.jpeg", "assets/img/work-letshoot.jpg", 1200),
    ("assets/raw/p7_0_63.jpeg", "assets/img/work-portrait-blinds.jpg", 1400),
    ("assets/raw/p7_1_64.jpeg", "assets/img/work-product-hair.jpg", 1400),
    ("assets/raw/p7_2_65.jpeg", "assets/img/work-campaign.jpg", 1600),
    ("assets/raw/p8_0_69.jpeg", "assets/img/work-smoke-portrait.jpg", 1200),
    ("assets/raw/p1_1_264.jpeg", "assets/img/bts-camera-man.jpg", 1400),
    ("assets/raw/p11_0_314.png", "assets/img/work-tablescape.jpg", 1600),
    ("assets/raw/p9_1_75.jpeg", "assets/img/bts-studio-wide.jpg", 1400),
]

for src, dest, maxdim in jobs:
    im = Image.open(src)
    im = ImageOps.exif_transpose(im)
    if im.mode in ("RGBA","P"):
        bg = Image.new("RGB", im.size, (10,10,10))
        im = im.convert("RGBA")
        bg.paste(im, mask=im.split()[-1])
        im = bg
    else:
        im = im.convert("RGB")
    w,h = im.size
    scale = maxdim / max(w,h)
    if scale < 1:
        im = im.resize((int(w*scale), int(h*scale)), Image.LANCZOS)
    im.save(dest, "JPEG", quality=86, optimize=True)
    print(dest, im.size, os.path.getsize(dest))
