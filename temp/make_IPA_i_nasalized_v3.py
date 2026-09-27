from PIL import Image, ImageDraw
import numpy as np

I_PATH = "IMG_1521.png"   # [i]
N_PATH = "IMG_1520.png"   # [n]
OUT_PATH = "IPA_i_nasalized_v3.png"

i_img = Image.open(I_PATH).convert("RGBA")
n_img = Image.open(N_PATH).convert("RGBA")
assert i_img.size == n_img.size == (1920, 2716)

A = np.array(i_img)
B = np.array(n_img)
h, w = A.shape[:2]

# Anatomical splice corridor: posterior palate / velum / nasopharynx only.
# The boundary deliberately stays posterior to the tongue body.
corridor_pts = [
    (990, 1310), (1370, 1310), (1370, 1480),
    (1285, 1510), (1215, 1580), (1160, 1665),
    (1080, 1700), (990, 1680)
]
corridor = Image.new("L", (w, h), 0)
ImageDraw.Draw(corridor).polygon(corridor_pts, fill=255)
C = np.array(corridor) > 0

# Only pixels that actually differ between the two CC0 originals are eligible.
rgb_delta = np.max(np.abs(A[:,:,:3].astype(np.int16) -
                          B[:,:,:3].astype(np.int16)), axis=2)
D = rgb_delta > 2

# Replace complete differing anatomy inside the corridor.
# No blur, dilation, erosion, or generated/redrawn pixels.
M = C & D
out = A.copy()
out[M] = B[M]

changed = np.any(out != A, axis=2)

# QC: all changed pixels come exactly from [n].
assert np.all(out[changed] == B[changed])

# QC: nothing outside the anatomical corridor changes.
assert not np.any(changed & ~C)

# QC: protect anterior tongue/oral region.
protect = np.zeros((h, w), dtype=bool)
protect[1450:2300, 1300:1920] = True
assert not np.any(changed & protect)

Image.fromarray(out, "RGBA").save(OUT_PATH)
print(f"saved {OUT_PATH}")
print(f"changed pixels: {changed.sum()}")
