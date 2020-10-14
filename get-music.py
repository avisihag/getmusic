import subprocess
import re
import time
from songdwnld import ytlink


with open('musicplist.txt', 'r') as f:
    for i in f:
        j = ytlink(i)
        time.sleep(1)
        p1 = subprocess.run(['youtube-dl', '-x', '--audio-format', 'mp3', '-o',
                             '/Users/avisihag/Desktop/Music/%(title)s.%(ext)s', j], capture_output=True, text=True)
        x = p1.stdout
        time.sleep(1)
        obj = re.compile(r"Music/[^/]+.mp3")
        mo = obj.search(x)
        smo = mo.group()[6:]
        '\ '.join(smo.strip().split())
        print('Downloaded ' + smo)

        k = re.compile(r"([\s\w\d]+)[,(\s\-)]?[\w\d\s,]*- ([^\$]+)")
        mo1 = k.findall(i)
        smo1 = mo1

        p2 = subprocess.run(['mid3v2', '-q', '-a', smo1[0][0], '-t',
                             smo1[0][1], smo])

        time.sleep(1)

        print('Tagged with \ntitle=' +
              smo1[0][1] + ' artist=' + smo1[0][0] + '\n \n')

        with open('plist.txt', 'a') as p:
            p.write(i)
