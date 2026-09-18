from PIL import Image
import os, glob

files = sorted(glob.glob("assets/raw/*"))
thumb = 200
cols = 6
rows = (len(files)+cols-1)//cols
sheet = Image.new("RGB",(cols*thumb, rows*(thumb+20)), "white")
from PIL import ImageDraw
draw = ImageDraw.Draw(sheet)
for i,f in enumerate(files):
    try:
        im = Image.open(f).convert("RGB")
    except Exception as e:
        print(f, e); continue
    im.thumbnail((thumb,thumb))
    x = (i%cols)*thumb
    y = (i//cols)*(thumb+20)
    sheet.paste(im,(x,y))
    draw.text((x, y+thumb+2), os.path.basename(f)[:20], fill="black")
sheet.save("contact_sheet.png")
print("saved", len(files))
