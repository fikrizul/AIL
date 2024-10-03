# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 15:43:03 2022

@author: Fikri Z
"""


from pdf2image import convert_from_path
from PIL import Image
import re
import os
import pytesseract
# from Levenshtein import distance
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


TabelentryAIL= ""
# whitelist='-c tessedit_char_whitelist=:_.-abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
# custom_config='preserve_interword_spaces=1 --psm 6 --oem 1 '+ whitelist
awal=1
akhir=867
tipedok=["","PK","BA","SPJBTL","SIP","PDL", "SLO","1","2","3","4","5","6","7","8","8","10","11","12"]

while awal<akhir+1:
 l= str(awal)
 pages=[]
 for k in tipedok:
  pdfs =  l+ r"-" + str(k) + r".pdf"
  if os.path.exists(pdfs):
   read = convert_from_path(pdfs,poppler_path="C:/Installer/envs/AIL/Library/bin",fmt="jpeg",jpegopt={'optimize':True,'progressive':False,'quality':50},size=(2480,3508))
   try:
    read = convert_from_path(pdfs,poppler_path="C:/Installer/envs/AIL/Library/bin",fmt="jpeg",jpegopt={'optimize':True,'progressive':False,'quality':50},size=(2480,3508))
   except (OSError, Image.UnidentifiedImageError) as e:
    # Handle the exception (e.g., skip the image)
    print("Error processing image:", pdfs)
    print("Skipping...")
   for r in read:
       convert = r.convert('P',palette=Image.ADAPTIVE)
       pages.append (convert)

 j=0
 text=""
 for page in pages:
  if pages == []:
   break
  text += str(pytesseract.image_to_string(pages[j], config='ail --psm 1 --oem 1'))
  # print(j)
  # print(text)
  j+=1
#tessedit_char_whitelist=:" _.-\|abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"


 patternNama = r"Nama[\-\:\.\_\s\|]+(?:P?(?=[elangq ]))[elangq ]*[\-\:\.\_\s\|]*([A-Z\.\d\_ ]+(?![a-z ]))"
 patternNoPel = r"[NoID]+[\.\s\-\_\|]+Pelan[cagq]+[ae]+n[\§\_\.\s\-\:\|]+(\d+)"
 patternNoPel2 = r"\n?\b(5612\d{8}|53951\d{7})\b"
 patternNoAg = r"[Nomr\.]+[\.\s\-\:\_\|\,\*]+A[gaq]+enda[\§\_\.\s\-\:\|\,\*]+(\d+)"
 patternNoAg2 = r"KEDUA[\§\_\.\s\-\:\|]+Nomor[\§\_\.\s\-\:\|]+(\d+)"
 patternNoAg3 = r"\n?\b(5613\d{14}|53951\d{13})\b"
 
 print(l)
 NamaPelsearch = re.search(patternNama,text)
 if NamaPelsearch == None:
     NamaPel=""
 else:
     NamaPel = NamaPelsearch.group(1)
 print(NamaPel)
 
 NoPellist=['','']
 NoPelsearch = re.search(patternNoPel,text)
 NoPelsearch2 = re.search(patternNoPel2,text)
 if NoPelsearch != None:
  NoPellist[0]=NoPelsearch.group(1)
 if     NoPelsearch2!=None:
  NoPellist[1]=NoPelsearch2.group(1)
 NoPel=','.join(NoPellist)
 print(NoPel)
 
 NoAglist=[]
 NoAgsearch = re.search(patternNoAg,text)
 NoAgsearch2 = re.search(patternNoAg2,text)
 NoAgsearch3 = re.search(patternNoAg3,text)
 if NoAgsearch != None:
  NoAglist.append(NoAgsearch.group(1))
 if NoAgsearch2 != None:
  NoAglist.append(NoAgsearch2.group(1))
 if NoAgsearch3 != None:
  NoAglist.append(NoAgsearch3.group(1))
 NoAg=','.join(NoAglist)
 print(NoAg)
 
 # print(text)
 # print(NoAgsearch)
 # print(NoAgsearch2)

 entryAIL= "\n" + l +"," + NamaPel + ","+ NoPel+","+ NoAg
 with open("TabelentryAILsplit2.csv","a") as tulisTabel:
  tulisTabel.write(entryAIL)
 TabelentryAIL +=entryAIL
 awal+=1
print(TabelentryAIL)

 
 
