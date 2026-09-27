from PIL import Image, ImageFilter, ImageDraw
import numpy as np
from pathlib import Path

I_PATH = Path("/mnt/data/IMG_1521.png")  # [i]
N_PATH = Path("/mnt/data/IMG_1520.png")  # [n]

im_i = Image.open(I_PATH).convert("RGBA")
im_n = Image.open(N_PATH).convert("RGBA")
assert im_i.size == im_n.size
w, h = im_i.size

A = np.asarray(im_i).astype(np.int16)
B = np.asarray(im_n).astype(np.int16)

delta = np.max(np.abs(A[:, :, :3] - B[:, :, :3]), axis=2)
changed = delta > 3

poly = [
    (0.505*w, 0.405*h),
    (0.665*w, 0.400*h),
    (0.735*w, 0.455*h),
    (0.735*w, 0.585*h),
    (0.650*w, 0.625*h),
    (0.535*w, 0.600*h),
    (0.485*w, 0.515*h),
]
roi_img = Image.new("L", (w, h), 0)
ImageDraw.Draw(roi_img).polygon([(int(x), int(y)) for x, y in poly], fill=255)
roi = np.asarray(roi_img) > 0

candidate = changed & roi
m = Image.fromarray((candidate * 255).astype("uint8"), "L")
m = m.filter(ImageFilter.MedianFilter(3))
m = m.filter(ImageFilter.MaxFilter(3))
edge = m.filter(ImageFilter.GaussianBlur(0.65))

out = Image.composite(im_n, im_i, edge)

O = np.asarray(out).astype(np.int16)
yy, xx = np.mgrid[:h, :w]

anterior = (xx < 0.49*w) & (yy > 0.42*h) & (yy < 0.78*h)
max_anterior_change = np.max(np.abs(O[:, :, :3] - A[:, :, :3])[anterior])
assert max_anterior_change == 0, f"[i] tongue region changed: {max_anterior_change}"

mask_np = np.asarray(edge) > 0
outside = ~mask_np
max_outside_change = np.max(np.abs(O[:, :, :3] - A[:, :, :3])[outside])
assert max_outside_change == 0, f"Unexpected changes outside splice: {max_outside_change}"

OUT = Path("/mnt/data/IPA_i_nasalized_script_v2.png")
out.save(OUT)
print("created:", OUT)
print("QC anterior tongue change:", max_anterior_change)
print("QC outside splice change:", max_outside_change)
