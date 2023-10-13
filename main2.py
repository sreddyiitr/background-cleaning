from rembg import remove
from rembg import new_session
from PIL import Image
from pathlib import Path

# Create session
session = new_session("u2netp")

def process(session, image, *, size=None, bgcolor='white'):
    "session is a rembg Session, and image is a PIL Image"
    if size is not None:
        image = image.resize(size)
    else:
        size = image.size
    result = Image.new("RGB", size, bgcolor)
    out = remove(image, session=session)
    result.paste(out, mask=out)
    return result

for path_in in Path(r'images').glob('*.png'):
    path_out = path_in.parent / f"{path_in.stem}-out.jpeg"
    # no point processing images that have already been done!
    if path_out.exists():
        continue
    with Image.open(path_in) as img:
        out = process(session, img, size=img.size, bgcolor='#FFFFFF')
        out.save(path_out)
