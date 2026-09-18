import fitz, os
src = r"D:\Mario\John Farag – Photographer (2).pdf"
doc = fitz.open(src)
os.makedirs("assets/raw", exist_ok=True)
count = 0
for pno in range(len(doc)):
    page = doc[pno]
    imgs = page.get_images(full=True)
    for i, img in enumerate(imgs):
        xref = img[0]
        try:
            base = doc.extract_image(xref)
        except Exception as e:
            print("err", pno, i, e)
            continue
        ext = base["ext"]
        w = base.get("width",0); h = base.get("height",0)
        if w < 150 or h < 150:
            continue
        fname = f"assets/raw/p{pno+1}_{i}_{xref}.{ext}"
        with open(fname, "wb") as f:
            f.write(base["image"])
        count += 1
        print(fname, w, h)
print("total", count)
