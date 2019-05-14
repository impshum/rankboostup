import pickledb
import glob

for name in glob.glob('data/*.db'):
    print(f'\n{name}'.replace('data/', '').replace('.db', ''))
    db = pickledb.load(name, False)
    for x in db.getall():
        print(x, db.get(x))
