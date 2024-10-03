#extract

import os
import glob
import img2pdf
from PIL import Image
import os
from shutil import copy

listail=[]
nomerail=1
nambar=[]
namlam=[]
namsplam=[]
namspbar=[]
nopel=[]
listdok=["PDL","PK","BA", "SIP", "SLO","1","2","3","4","5","6","7","8","9","10","11","12" ]
listspjbtl=["SPJBTL 1","SPJBTL 2","SPJBTL 3","SPJBTL 4","SPJBTL 5"]
for x in glob.glob("*/*"):
    xbase=os.path.basename(x)
    # print(xbase)
    listail.append(xbase)
    xisi= x +"/**.jpg"
    namsubsplam=[]
    altnum=1
    for y in glob.glob(xisi):
        ybase=os.path.basename(y)
        #print(ybase)
        if "_"  not in ybase:
            namdok=str(altnum)
            altnum+=1
        else:
            namdok=ybase.split("_")[1].split(".")[0]
      

        
        for spjbtl in listspjbtl:
            if namdok ==spjbtl:
                namsubsplam.append(y)

        for dok in listdok:
            if namdok == dok: 
                nambar.append(str(nomerail)+"-"+namdok+".pdf")
                namlam.append(y)
    if namsubsplam is not []:
        namsplam.append(namsubsplam)
        namspbar.append(str(nomerail)+"-SPJBTL.pdf")
    
    nopel.append(str(nomerail)+","+xbase.split("_")[0])
    print(nopel[nomerail-1])
    nomerail+=1
    
    #print(xbase,jpeg)

#print(listail)
#namalama=list(listail.values())
#print(nam,len(namalama))
#print(list(zip(namlam,nambar)))
# print(list(zip(namsplam,namspbar)))
#print(nopel)
# images = [im1,im2,im3]
# images[0].save("out.pdf", save_all=True, append_images=images[1:])


# for aillam, ailbar in zip(namlam,nambar):
#     # try:
#     # # Attempt to open the image
#     # with Image.open(file_path) as img:
#     #     # Process the image
#     #     # (e.g., perform image classification, feature extraction, etc.)
#     #     print("Image processed successfully:", file_path)
            
#     # except (OSError, PIL.UnidentifiedImageError) as e:
#     #     # Handle the exception (e.g., skip the image)
#     #     print("Error processing image:", file_path)
#     #     print("Skipping...")
#     #     continue
#     try:
#         with Image.open(aillam) as img:
#             w,h=img.size
#             wnew=2480
#             r=h/w
#             hnew=int(h/r)
#             size=(wnew, hnew)
#             img.save(ailbar,dpi=size)
#             print(ailbar,"saved")
#     except (OSError, Image.UnidentifiedImageError) as e:
#         # Handle the exception (e.g., skip the image)
#         print("Error processing image:", aillam)
#         print("Skipping...")
#         continue

# for listsplam,ailspbar in zip(namsplam,namspbar):
#     imgspjbtl=[]
#     for splam in listsplam:
#         img=Image.open(splam)
#         imgspjbtl.append(img)
#         img.close
#     if len(imgspjbtl)==0:
#         continue
#     else:
#         w,h=img.size
#         wnew=2480
#         r=h/w
#         hnew=int(h/r)
#         size=(wnew, hnew)
#         try:
#             imgspjbtl[0].save(ailspbar,save_all=True, append_images=imgspjbtl[1:],dpi=size)
#         except (OSError, Image.UnidentifiedImageError) as e:
#             # Handle the exception (e.g., skip the image)
#             print("Error processing image:", aillam)
#             print("Skipping...")
#             continue
#         print(ailspbar,"saved")
#     imgspjbtl=[]

# print(len(namsplam))
# print(len(namspbar))
# 
for pel in nopel:
    with open("nopel.csv",'a') as tulnopel:
        tulnopel.write(pel+"\n")
# print(nopel)
# print(listail)

print("hello world")
