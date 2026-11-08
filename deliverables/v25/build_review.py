#!/usr/bin/env python3
"""Build a raster review PDF, not a PDF/X or production print file."""
from pathlib import Path
import zlib

from PIL import Image

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).with_name('ravenxcope-a5-review-baseline.pdf')
SOURCES = [
    ROOT / 'deliverables/v25/option-a/ravenxcope-a5-front-a-v25.png',
    ROOT / 'deliverables/v25/option-a/ravenxcope-a5-back-a-v25.png',
]


def stream(data, entries=''):
    return f'<< {entries} /Length {len(data)} >>\nstream\n'.encode() + data + b'\nendstream'


objects = [None]


def add(value):
    objects.append(value)
    return len(objects) - 1


catalog = add(None)
pages = add(None)
page_ids = []
for path in SOURCES:
    with Image.open(path) as image:
        icc = image.info.get('icc_profile')
        if not icc or image.size != (1819, 2551):
            raise ValueError(f'Missing ICC or unexpected dimensions: {path}')
        pixels = image.convert('RGB').tobytes()
    profile = add(stream(zlib.compress(icc), '/N 3 /Filter /FlateDecode'))
    image_id = add(stream(zlib.compress(pixels), f'/Type /XObject /Subtype /Image /Width 1819 /Height 2551 /ColorSpace [/ICCBased {profile} 0 R] /BitsPerComponent 8 /Filter /FlateDecode'))
    # Exact 154 × 216 mm page; centered 148 × 210 mm trim.
    width, height = 154 * 72 / 25.4, 216 * 72 / 25.4
    bleed = 3 * 72 / 25.4
    commands = f'q\n{width:.6f} 0 0 {height:.6f} 0 0 cm\n/Im0 Do\nQ\n'.encode()
    content = add(stream(commands))
    page = add((f'<< /Type /Page /Parent {pages} 0 R /MediaBox [0 0 {width:.6f} {height:.6f}] '
                f'/BleedBox [0 0 {width:.6f} {height:.6f}] '
                f'/TrimBox [{bleed:.6f} {bleed:.6f} {width-bleed:.6f} {height-bleed:.6f}] '
                f'/Resources << /XObject << /Im0 {image_id} 0 R >> >> /Contents {content} 0 R >>').encode())
    page_ids.append(page)
objects[catalog] = f'<< /Type /Catalog /Pages {pages} 0 R >>'.encode()
objects[pages] = f'<< /Type /Pages /Count 2 /Kids [{" ".join(f"{i} 0 R" for i in page_ids)}] >>'.encode()
output = bytearray(b'%PDF-1.7\n%\xe2\xe3\xcf\xd3\n')
offsets = [0]
for i, obj in enumerate(objects[1:], 1):
    offsets.append(len(output))
    output.extend(f'{i} 0 obj\n'.encode() + obj + b'\nendobj\n')
xref = len(output)
output.extend(f'xref\n0 {len(objects)}\n0000000000 65535 f \n'.encode())
for offset in offsets[1:]:
    output.extend(f'{offset:010d} 00000 n \n'.encode())
output.extend(f'trailer\n<< /Size {len(objects)} /Root {catalog} 0 R >>\nstartxref\n{xref}\n%%EOF\n'.encode())
if OUT.exists():
    raise FileExistsError(f'Refusing to overwrite {OUT}')
OUT.write_bytes(output)
print(OUT)
