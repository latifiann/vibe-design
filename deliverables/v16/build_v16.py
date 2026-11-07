"""Build two complete editable brochure candidates with PhotoCraft CLI headless.

No image generation. Supplied decorative images remain embedded Smart Objects.
Manual feature illustrations consist of separate editable vector shapes.
"""
from pathlib import Path
import argparse
import json
import math
import subprocess
from PIL import Image

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
INK, WHITE, MUTED, ACCENT = '#0B0D10', '#F4F5F6', '#B7BEC5', '#DB241C'
WORK = Path('assets/screenshots/ravenxcope/working')


def gradient(a, b, angle=65):
    return {'gradient': {'stops': [[0, a], [1, b]], 'style': 'linear', 'angle': angle}}

def fade(color, angle=90, style='linear'):
    return {'gradient': {'stops': [[0,color],[1,color]], 'opacityStops': [[0,0],[1,1]],
                         'style':style,'angle':angle}}

def glow():
    return {'gradient': {'stops': [[0,'#A02B21'],[1,'#A02B21']],
                         'opacityStops': [[0,0.6],[1,0]],'style':'radial'}}


class Canvas:
    def __init__(self, option, side):
        self.option, self.side = option, side
        self.ops, self.groups, self.placements = [], [], []
        self.folder = OUT / f'option-{option}'
        self.folder.mkdir(parents=True, exist_ok=True)
        self.stem = self.folder / f'ravenxcope-a5-{side}-{option}-v16'

    def cmd(self, command, **params):
        self.ops.extend(['--cmd', command, '--params', json.dumps(params, ensure_ascii=False)])

    def group(self, name):
        self.cmd('layer.select', name='Background')
        self.cmd('layer.new.group', name=name)
        self.groups.append(name)

    def shape(self, name, kind, rect, fill, stroke=None, **extra):
        self.cmd('shape.create', name=name, kind=kind, rect=rect, fill=fill, stroke=stroke, **extra)

    def rect(self, name, x, y, w, h, fill, radius=0, stroke=None):
        self.shape(name, 'roundedRect' if radius else 'rect', [x, y, w, h], fill,
                   stroke=stroke, **({'radii': radius} if radius else {}))

    def ellipse(self, name, x, y, w, h, fill, stroke=None):
        self.shape(name, 'ellipse', [x, y, w, h], fill, stroke)

    def path(self, name, points, fill, stroke=None, closed=True):
        self.cmd('shape.create', kind='path', name=name,
                 path={'subpaths': [{'closed': closed, 'knots': points}]}, fill=fill, stroke=stroke)

    def line(self, name, x1, y1, x2, y2, color, weight=2):
        self.cmd('shape.create', kind='line', name=name, **{'from': [x1, y1], 'to': [x2, y2]},
                 weight=weight, fill=color)

    def text(self, name, value, x, y, size=10, color=WHITE, headline=False, weight=400, align='left', italic=False):
        self.cmd('type.create', name=name, text=value, x=x, y=y, size=size, color=color,
                 font='Avenir Next Condensed' if headline else 'Inter', weight=700 if headline else weight,
                 align=align, italic=italic, **({'fontStyle':'Bold Italic'} if italic and headline else {}))

    def lines(self, name, values, x, y, size=10, step=53, **extra):
        for i, value in enumerate(values):
            self.text(f'{name} {i+1}', value, x, y+i*step, size, **extra)

    def place(self, path, scale, center, name=None, opacity=None):
        self.cmd('file.placeEmbedded', path=str(ROOT/path), scale=scale, center=center, smartObject=True)
        if name:
            self.cmd('layer.setProps', name=name)
        if opacity is not None:
            self.cmd('layer.setProps', opacity=opacity)
        im = Image.open(ROOT/path)
        self.placements.append(dict(source=str(path), scale_percent=scale,
                                    source_px=list(im.size), center=center, effective_ppi=300/(scale/100)))

    def shadow(self, size=28, distance=18, opacity=45):
        self.cmd('layer.layerStyle.dropShadow', color='#000000', opacity=opacity,
                 angle=100, distance=distance, size=size, spread=0)

    def icon(self, kind, x, y, size=200, suffix=''):
        """Manual 2.5D vector illustration, normalized to a 200 px square."""
        self.group(f'07_ILLUSTRATION_{kind.upper()}{suffix}')
        s = size/200
        metal = gradient('#60707C', '#182129', 65)
        glass = gradient('#303D48', '#10171E', 70)
        edge = gradient('#F05A4F', '#9C251D', 30)
        def pts(values):
            return [[x+a*s, y+b*s] for a,b in values]
        def p(name, values, fill, stroke=None, closed=True):
            self.path(f'{kind} / {name}', pts(values), fill, stroke, closed)
        def e(name, a,b,w,h, fill, stroke=None):
            self.ellipse(f'{kind} / {name}',x+a*s,y+b*s,w*s,h*s,fill,stroke)
        def line(name,a,b,c,d,color,width=2):
            self.line(f'{kind} / {name}',x+a*s,y+b*s,x+c*s,y+d*s,color,width*s)
        outline = {'width': 1.5*s, 'color': '#73818D', 'opacity': 65}
        e('soft base', 10,155,180,27, '#10171C')
        if kind == 'inventory':
            for n, dy in enumerate([48,25,0]):
                p(f'plate depth {n}',[(18,65+dy),(124,30+dy),(186,67+dy),(78,108+dy),(78,120+dy),(18,77+dy)],'#11181E')
                p(f'plate top {n}',[(18,65+dy),(124,30+dy),(186,67+dy),(78,108+dy)],glass if n<2 else metal,outline)
                line(f'plate edge {n}',18,65+dy,78,108+dy,ACCENT if n==1 else '#6D7E89',2)
            for i in range(3):
                dx,dy=30+i*26,69-i*8
                p(f'asset tile {i}',[(dx,dy),(dx+18,dy-6),(dx+28,dy+1),(dx+10,dy+7)],edge if i==1 else '#A6B2BC')
            line('context line',84,83,143,62,'#B8C1C8',3)
            line('context line secondary',96,92,156,71,'#7F909D',2)
            p('highlight tab',[(141,35),(161,28),(181,40),(161,48)],edge)
        elif kind == 'risk':
            for i,(a,b,h) in enumerate([(18,112,24),(65,85,51),(112,47,89)]):
                p(f'step front {i}',[(a,b),(a+38,b+17),(a+38,b+17+h),(a,b+h)],glass)
                p(f'step side {i}',[(a+38,b+17),(a+66,b+5),(a+66,b+5+h),(a+38,b+17+h)],'#11191F')
                p(f'step top {i}',[(a,b),(a+28,b-12),(a+66,b+5),(a+38,b+17)],edge if i==2 else metal,outline)
                line(f'step rim {i}',a,b,a+38,b+17,'#F57866' if i==2 else '#9AA8B2',2)
            line('focus stem',146,14,146,43,'#F05A4F',3)
            p('focus diamond',[(146,3),(156,10),(146,17),(136,10)],'#F05A4F')
        elif kind == 'analytics':
            p('handle depth',[(123,119),(143,111),(181,153),(160,170)],'#11181E')
            p('handle face',[(128,112),(145,106),(184,148),(167,159)],metal,outline)
            line('handle accent',162,141,179,133,ACCENT,6)
            e('lens depth',26,29,123,123,'#11181E')
            e('lens outer',23,17,123,123,metal,outline)
            e('lens bevel',34,28,101,101,'#14202A',{'width':3*s,'color':'#8898A4'})
            e('lens glass',42,36,85,85,gradient('#263945','#10181E',120))
            p('analytical contour',[(49,90),(66,75),(83,81),(102,57),(118,65)],None,
              {'width':4*s,'color':'#F05A4F','cap':'round','join':'round'},False)
            line('glass reflection',53,50,77,42,'#8699A7',3)
            line('glass reflection small',50,58,66,53,'#536A7B',2)
        else:
            p('back sheet',[(41,33),(140,18),(170,138),(69,157)],glass,outline)
            p('front depth',[(23,47),(126,34),(152,154),(48,170)],'#10171D')
            p('review sheet',[(23,36),(126,23),(152,143),(48,159)],metal,outline)
            p('header accent',[(23,36),(126,23),(130,43),(27,56)],edge)
            for i in range(3):
                yy=75+i*23
                line(f'review rule {i}',64,yy,118,yy-7,'#C0CBD2' if i==0 else '#8495A1',3)
                p(f'review mark {i}',[(40,yy-2),(45,yy+2),(52,yy-8)],None,
                  {'width':3*s,'color':'#F05A4F' if i==0 else '#8B9CA8','cap':'round','join':'round'},False)
            e('annotation bezel',125,113,50,50,glass,outline)
            line('annotation stroke',150,124,150,141,'#F05A4F',4)
            e('annotation dot',147,147,6,6,'#F05A4F')

    def finish(self):
        if self.stem.with_suffix('.pcraft').exists():
            raise RuntimeError(f'Refusing overwrite: {self.stem}')
        for name in reversed(self.groups):
            self.cmd('layer.moveTo',layer=name,target='Background',position='above')
        for orient, positions in [('vertical',[35,1784,130,1689]),('horizontal',[35,2516,130,2421])]:
            for position in positions:
                self.cmd('view.newGuide', orientation=orient, position=position)
        result = subprocess.run(['photocraft-cli','run','--new',json.dumps(dict(
            width=1819,height=2551,resolution=300,profile='srgb',background=INK,
             name=f'RavenXcope {self.option.upper()} {self.side} v16'))]+self.ops+
            ['--out',str(self.stem.with_suffix('.pcraft'))],capture_output=True,text=True,timeout=300)
        self.stem.with_suffix('.build.log').write_text(result.stdout+result.stderr)
        if result.returncode:
            raise RuntimeError(result.stdout[-2000:]+result.stderr)
        subprocess.run(['photocraft-cli','convert',str(self.stem.with_suffix('.pcraft')),
                        str(self.stem.with_suffix('.png'))],check=True,timeout=180)
        self.stem.with_suffix('.placements.json').write_text(json.dumps(self.placements,indent=2))
        print(f'{self.option.upper()} {self.side}: master and PNG saved',flush=True)


def brand(c, front=True):
    c.group('02_BRAND_MARK')
    c.place(Path('assets/ravenxcope-logo-transparan.png'),24,
            [258,245],name='Unchanged official full lockup')
    c.group('03_CATEGORY')
    c.text('Category','NIDS TERDISTRIBUSI',1660,205,9,MUTED,weight=600,align='right')
    c.text('Category detail','Analisis berbasis konteks aset',1660,258,8,MUTED,align='right')


def cta(c):
    c.group('08_QR_AND_CONTACT')
    c.rect('CTA field',35,2100,1749,416,gradient('#251817','#11161B',15))
    c.line('CTA upper rule',155,2100,1664,2100,'#5C3837',2)
    c.lines('Closing',['Fokuskan perhatian pada ancaman yang relevan','bagi aset penting Anda.'],
            155,2185,9.5,57,color=MUTED)
    c.text('CTA','Jelajahi demo',155,2340,19,headline=True)
    c.text('Demo URL','demo.ravenxcope.mataelang.net',155,2407,9.5,MUTED)
    c.place(WORK/'qr-demo-v01.png',62,[1525,2315],name='Demo QR with original quiet zone')


def feature_blocks(c, start=1450):
    blocks = [
        ('inventory',155,start,['Inventaris &','konteks aset'],
         ['Inventaris host dan jaringan','beserta konteks dan','kekritisan aset terkait.']),
        ('risk',955,start,['Prioritas','risiko'],
         ['Severity, kekritisan aset,','dan matriks risiko untuk','prioritas penelaahan.']),
        ('analytics',155,start+340,['Analitik &','investigasi'],
         ['Tren, klasifikasi, protokol,','dan aliran IP. Filter waktu,','sensor, IP, port, dan alert.']),
        ('triage',955,start+340,['Triase','peringatan'],
         ['Tinjau detail peringatan','dan tandai false positive','untuk mendukung triase.'])]
    for i,(kind,x,y,title,body) in enumerate(blocks):
        c.icon(kind,x-10,y-90,190)
        c.group(f'07_FEATURE_COPY_{i+1}')
        c.lines(f'Feature {i+1} heading',title,x+205,y-35,13,55,headline=True)
        c.lines(f'Feature {i+1} body',body,x+205,y+92,9.5,54,color=MUTED)


def institution_logos(c):
    c.group('10_INSTITUTION_LOGOS')
    c.rect('Plain white institution badge',145,2255,1529,160,'#FFFFFF',28)
    logos = [
        ('kemendiktisaintek.png', 43, 380),
        ('diktisaintek-berdampak.png', 43, 687),
        ('ditjen-risbang.png', 46, 927),
        ('hiliriset.png', 54, 1112),
        ('pens.png', 39, 1252),
        ('len-defend-id.png', 53, 1487),
    ]
    for filename,scale,x in logos:
        c.place(Path('assets/logo-instansi')/filename,scale,[x,2335],name='Institution logo / '+filename)


def front_a():
    c=Canvas('a','front')
    c.group('01_BACKGROUND')
    c.place(Path('assets/generated/ravenxcope-hero-a-background.png'),182,[909.5,1275.5],name='Owner supplied decorative background A - assumed sRGB')
    c.ellipse('Atmospheric vermilion radial',0,910,1819,1250,glow())
    brand(c)
    c.group('03_HEADLINE_AND_COPY')
    c.lines('Approved headline',['Kenali Asetnya.','Pahami Ancamannya.'],155,535,32,165,headline=True)
    c.text('Approved headline 3','Tentukan Prioritasnya.',155,865,32,'#F05A4F',headline=True,italic=True)
    c.lines('Positioning',['RavenXcope menghubungkan peringatan jaringan','dengan konteks dan kekritisan aset untuk','mendukung penentuan prioritas.'],155,1000,10.5,56,color=MUTED)
    # Laptop source 1536x1024 at 104%: [111,743] screen origin in source coordinates.
    # Actual screen aperture derived from corners and kept as separate editable vector mask.
    c.group('06_PRODUCT_VISUAL_DEPTH')
    c.ellipse('Laptop contact shadow',340,1990,1100,40,glow())
    c.group('04_LAPTOP_SCREEN')
    c.path('Black screen padding',[[453,1293],[1476,1280],[1472,1891],[440,1891]],'#0A1018')
    c.place(Path('assets/ravenxcope/Screenshot 2026-11-06 192316.png'),59,[960,1660],name='Full original Security Analytics screenshot 192316')
    # Preserve aspect; moderate perspective matches the screen slope without cropping panels.
    c.cmd('edit.transform',quad=[[476,1345],[1444,1331],[1438,1815],[463,1818]])
    c.cmd('layer.vectorMask.add',path={'subpaths':[{'closed':True,'knots':[[453,1293],[1476,1280],[1472,1891],[440,1891]]}]})
    c.group('04_LAPTOP_BODY')
    c.place(Path('assets/generated/working/ravenxcope-laptop-v05-cutout.png'),89.44,[916.6,1667.3],name='Decorative laptop clean cutout - screen transparent')
    
    cards = [
        ('Alert analysis','Analitik peringatan','alert-analysis-v13.png',16,330,1470),
        ('Asset context','Konteks aset','asset-context-v13.png',16,1490,1570),
        ('Risk priority','Prioritas risiko','risk-priority-v16.png',16,330,1900),
        ('IP flow','Alur komunikasi IP','ip-flow-v16.png',17,1490,1940),
    ]
    for name,label,icon,scale,x,y in cards:
        c.group('07_FOREGROUND_CARD / '+name)
        c.place(Path('assets/generated/working/glass-shell-v16.png'),31,[x,y],name=name+' / translucent glass shell')
        c.place(Path('assets/generated/working')/icon,scale,[x,y-32],name=name+' / conceptual icon')
        c.text(name+' / single-line label',label,x,y+103,7,WHITE,weight=600,align='center')
    c.group('09_FOOTER')
    c.lines('Benefit',['Bukan sekadar melihat alert,','tetapi memahami konteks aset di baliknya.'],155,2163,13,59,headline=True,italic=True)
    institution_logos(c)
    c.finish()


def front_b():
    c=Canvas('b','front')
    c.group('01_BACKGROUND')
    c.place(Path('assets/generated/ravenxcope-hero-b-analytics-concept.png'),182,[909.5,1275.5],name='Conceptual background B',opacity=0.33)
    c.ellipse('Editorial atmospheric accent',550,1000,1200,1000,glow())
    c.ellipse('Warm peripheral gradient',-300,1500,1100,800,glow())
    brand(c)
    c.group('03_HEADLINE_AND_COPY')
    c.lines('Approved headline',['Kenali Asetnya.','Pahami Ancamannya.'],155,510,32,165,headline=True)
    c.text('Approved headline 3','Tentukan Prioritasnya.',155,840,32,'#F05A4F',headline=True,italic=True)
    c.lines('Editorial positioning',['Analitik peringatan dan konteks aset','untuk mendukung prioritas penelaahan.'],155,980,10.5,58,color=MUTED)
    c.group('04_PRODUCT_SCREENSHOT')
    c.rect('Screenshot frame',143,1150,1533,770,gradient('#63717B','#222A32'),8)
    c.shadow(32,20,45)
    c.place(Path('assets/ravenxcope/Screenshot 2026-11-06 192316.png'),78,[909,1535],name='Original Security Analytics screenshot - full viewport')
    c.group('07_PRODUCT_LABELS')
    c.text('Product caption','SECURITY ANALYTICS • TAMPILAN PRODUK ASLI',155,2010,8.5,MUTED,weight=600)
    c.line('Editorial accent',155,2070,1664,2070,'#99362F',3)
    c.lines('Product definition',['Peringatan jaringan,','dipahami dalam konteks aset.'],155,2225,18,80,headline=True)
    c.finish()


def back(option):
    c=Canvas(option,'back')
    c.group('01_BACKGROUND')
    if option=='a':
        c.place(Path('assets/generated/ravenxcope-hero-a-background.png'),182,[909.5,1275.5],name='Decorative background A - assumed sRGB',opacity=0.35)
    else:
        c.place(Path('assets/generated/ravenxcope-hero-b-analytics-concept.png'),105,[1430,540],name='Conceptual hero B detail - assumed sRGB',opacity=0.22)
    c.ellipse('Back atmospheric gradient',850,900,1200,950,glow())
    c.cmd('layer.setProps',opacity=0.20)
    brand(c,False)
    c.group('03_EDITORIAL_INTRO')
    c.lines('Back lead',['Pahami risiko.','Tentukan fokus penelaahan.'] if option=='a' else ['Dari peringatan,','ke pemahaman.'],
            155,450,25,120,headline=True)
    c.lines('Product description',[
        'RavenXcope adalah platform NIDS terdistribusi yang berfokus',
        'pada visibilitas aset dan analisis ancaman jaringan. Konteks',
        'host, jaringan, dan kekritisan aset mendukung prioritas penelaahan.'
    ],155,680,10,56,color=MUTED)
    c.group('03_OPEN_EDITORIAL')
    c.text('Editorial kicker','KONTEKS UNTUK PRIORITAS',155,920,8.5,'#F05A4F',weight=600)
    if option=='a':
        c.lines('Editorial emphasis',['Tidak semua peringatan membutuhkan','perhatian yang sama.'],155,1010,17,75,headline=True,italic=True)
        c.lines('Editorial explanation',['Severity peringatan dan kekritisan aset membantu tim','menentukan fokus penelaahan.'],155,1160,10,55,color=MUTED)
        c.text('Severity label','Severity peringatan',155,1300,10,WHITE,weight=600)
        c.text('Criticality label','Kekritisan aset terkait',955,1300,10,WHITE,weight=600)
    else:
        c.lines('Editorial emphasis',['Peringatan lebih bermakna saat','konteks aset dipahami.'],155,1010,17,75,headline=True,italic=True)
        c.lines('Editorial explanation',['Konteks host, jaringan, dan kekritisan aset membantu','tim memahami temuan serta menentukan fokus penelaahan.'],155,1160,10,55,color=MUTED)
    feature_blocks(c,1490)
    cta(c)
    c.finish()


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    # The active back is the preserved v09 master, not this script's back().
    parser.add_argument('--only',choices=['a-front'],default='a-front')
    args=parser.parse_args()
    tasks={'a-front':front_a}
    for name,fn in tasks.items():
        if args.only is None or name==args.only:
            fn()
