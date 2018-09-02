import os
import sys
"""
split core test set
for root,dirs,files in os.walk('./core-test/'):
    for name in files:
        if name.endswith('.wav'):
            if name.find('sx') == -1 and name.find('si') == -1:
                fullName = os.path.join(root,name)
                print root
                os.system("rm "+root+"/sa*")
"""
for root,dirs,files in os.walk('/home/atlantix/TIMIT/core-test/'):
    for name in files:
        if name.endswith('.wav'):
	    fullName = os.path.join(root,name)
	    os.system("ffmpeg -i "+fullName+' -ar 8000 '+fullName[:len(fullName)-4]+'_8000.wav')

