import os
import datetime as dt
import shutil

src = 'C:\\A\\'
dst = 'C:\\B\\'
now = dt.datetime.now()
ago = now-dt.timedelta(days=1)

for root, dirs,files in os.walk('C:\\A\\'):
    for fname in files:
        path = os.path.join(root, fname)
        st = os.stat(path)    
        mtime = dt.datetime.fromtimestamp(st.st_mtime)
        if mtime > ago:
            shutil.move(path,dst)
            print('%s modified %s'%(path, mtime))
