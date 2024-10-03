#spjbtlagregat



import glob
import os
from PIL import Image




suffix=[".pdf","_1.pdf","_2.pdf","_3.pdf","_4.pdf","_5.pdf","_6.pdf"]
for nomerail in range(1,1200):
    nompath=str(nomerail)+"-SPJBTL_1.pdf"
    if os.path.exists(nompath):
        print(str(nomerail)+" ada")
        listspj=[]
        rpath=glob.glob(str(nomerail)+"*SPJBTL*")
        for x in rpath :
            if os.path.exists (x):
                listspj.append(x)
        print(listspj)
        # spjsaves=[]
        # for spjsave in listspj:
        #     img=Image.open(spjsave)
        #     img.thumbnail((2000,2000))
        #     spjsaves.append(img)
        #     img.close
        # if len(spjsaves)==0:
        #     continue
        # else:
        #     spjsaves[0].save(f"{nomerail}-SPJBTLbaru.pdf",save_all=True, append_images=spjsaves[1:])
        # spjsaves=[]
        # print("berhasil gabung")