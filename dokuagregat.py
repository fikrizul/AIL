#spjbtlagregat



import glob
import os
from PIL import Image
from pdf2image import convert_from_path


listdok=["BA","PK","SPJBTL","SLO","SIP","PDL"]
suffix=[".pdf","_1.pdf","_2.pdf","_3.pdf","_4.pdf","_5.pdf","_6.pdf"]
for nomerail in range(1,1200):
    for dok in listdok:
        nompath=f"{nomerail}-{dok}_1.pdf"
        if os.path.exists(nompath):
            print(f"{nomerail} {dok} ada")
            listdoku=[]
            rpath=glob.glob(f"{nomerail}-{dok}*")
            for x in rpath :
                if os.path.exists (x):
                    listdoku.append(x)
            print(listdoku)
            dokusaves=[]
            for dokusave in listdoku:
                img=convert_from_path(dokusave,poppler_path="C:/Installer/envs/AIL/Library/bin", fmt="jpeg",jpegopt={'optimize':True,'progressive':False,'quality':50},size=(2480,3508))
                dokusaves.extend(img)
            if len(dokusaves)==0:
                continue
            else:
                w,h=dokusaves[0].size
                wnew=2480
                r=h/w
                hnew=int(wnew*r)
                size=(wnew, hnew)
                print(size)
                try:
                    dokusaves[0].save(f"{nomerail}-{dok}.pdf",save_all=True, append_images=dokusaves[1:],dpi=size)
                except (OSError, Image.UnidentifiedImageError) as e:
            # Handle the exception (e.g., skip the image)
                    print("Error processing image:", listdoku[0])
                    print("Skipping...")
                    continue
            dokusaves=[]
            print("berhasil gabung")