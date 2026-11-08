"""Historical v20 edit record; removed source masters prevent a fresh rebuild."""
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
WORK = Path('/private/var/folders/lv/3fv0z_0x7tg6s96m3rvvfr8c0000gn/T/opencode/v20-work')
OUT = ROOT / 'deliverables/v20/option-a'
SHELL = ROOT / 'assets/generated/working/back-glass-shell-v20.png'

def run(source, destination, commands):
    if destination.exists():
        raise RuntimeError(f'Refusing to overwrite {destination}')
    args = ['photocraft-cli', 'run', str(source)]
    for command, params in commands:
        args += ['--cmd', command, '--params', json.dumps(params, ensure_ascii=False)]
    subprocess.run(args + ['--out', str(destination)], check=True, stdout=subprocess.DEVNULL)

front = [
    ('type.edit', {'layer': 21, 'text': 'RavenXcope merupakan platform Network Intrusion'}),
    ('type.edit', {'layer': 22, 'text': 'Detection System (NIDS) terdistribusi untuk visibilitas'}),
    ('type.edit', {'layer': 23, 'text': 'aset dan analisis ancaman jaringan. Konteks serta'}),
    ('layer.select', {'layer': 23}),
    ('type.create', {'name': 'Positioning 4 v20', 'text': 'kekritisan aset membantu tim memahami peringatan', 'x': 155, 'y': 1160, 'size': 10.5, 'font': 'Inter', 'color': '#AAB4BD'}),
    ('type.create', {'name': 'Positioning 5 v20', 'text': 'dan menentukan prioritas penelaahan.', 'x': 155, 'y': 1216, 'size': 10.5, 'font': 'Inter', 'color': '#AAB4BD'}),
]
run(WORK / 'front-source.pcraft', WORK / 'front-draft.pcraft', front)
refine = [
    ('type.edit', {'layer': 21, 'text': 'RavenXcope merupakan platform Network Intrusion Detection System', 'move': [0, -30]}),
    ('type.edit', {'layer': 22, 'text': '(NIDS) terdistribusi untuk visibilitas aset dan analisis ancaman jaringan.', 'move': [0, -30]}),
    ('type.edit', {'layer': 23, 'text': 'Konteks serta kekritisan aset membantu tim memahami peringatan', 'move': [0, -30]}),
    ('type.edit', {'layer': 176, 'text': 'dan menentukan prioritas penelaahan.', 'move': [0, -53]}),
    ('layer.setProps', {'layer': 177, 'visible': False}),
]
run(WORK / 'front-draft.pcraft', OUT / 'ravenxcope-a5-front-a-v20.pcraft', refine)

back = [
    ('type.edit', {'layer': 20, 'text': 'Peringatan jaringan dikaitkan dengan aset sumber dan tujuan'}),
    ('type.edit', {'layer': 21, 'text': 'beserta kekritisannya, sehingga tim dapat menelaah temuan'}),
    ('type.edit', {'layer': 22, 'text': 'dalam konteks aset yang terdampak.'}),
]
for name, panel, glint, x, y in [
    ('Inventory',24,25,512.5,1070), ('Risk',37,38,1307.5,1070),
    ('Analytics',49,50,512.5,1625), ('Triage',62,63,1307.5,1625),
]:
    back.extend([
        ('layer.setProps', {'layer': panel, 'visible': False}),
        ('layer.setProps', {'layer': glint, 'visible': False}),
        ('layer.select', {'layer': panel}),
        ('file.placeEmbedded', {'path': str(SHELL), 'scale': 52.6, 'center': [x, y], 'smartObject': True}),
        ('layer.setProps', {'name': name + ' / v20 glass shell'}),
    ])
run(WORK / 'back-source.pcraft', OUT / 'ravenxcope-a5-back-a-v20.pcraft', back)
