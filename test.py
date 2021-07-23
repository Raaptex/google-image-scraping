from bs4 import BeautifulSoup
import requests
import os
import shutil
#https://www.google.com/search?hl=en-FR&q=webcam+model&tbm=isch&source=iu&ictx=1&tbs=simg:CAESkgIJbD3OpMEIVtMahgILELCMpwgaOwo5CAQSFP4nlzmlErw4_1huYDcUtqyrcIpIPGhtIZj4CKfd-8Gdijza0Im3CYWe8DwE_1cgfbkKggBTAEDAsQjq7-CBoKCggIARIEZEY4GgwLEJ3twQkapQEKIAoMd2ViY2FtIG1vZGVs2qWI9gMMCgovbS8wM2d4cjUxCiMKD3dvbWVuJ3MgZXJvdGljYdqliPYDDAoKL20vMDI3eTE4dgoaCgZlcm90aWPapYj2AwwKCi9tLzBoOG55bG4KHgoMbW9iaWxlIHBob25l2qWI9gMKCggvbS8wNTBrOAogCg1waWN0dXJlIGZyYW1l2qWI9gMLCgkvbS8wNnozN18M&fir=CrR-we-iLjq07M%252Cm5YvrfSYyE-J7M%252C_&vet=1&usg=AI4_-kQqo_C5P6dYWvCdl_e5Lkh9IhvySw&sa=X&ved=2ahUKEwjHkpT-svfxAhVN1hoKHadkAsoQ9QF6BAgNEAE&biw=1920&bih=969#imgrc=-VdLHJewhc-hNM
url = 'https://www.google.com/search?q=image&client=opera-gx&hs=eCH&sxsrf=ALeKk02aXQfSXiUUBhaUUiVtUEh7vgFDuQ:1627037701941&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiMhorig_nxAhXPy4UKHdf_AwMQ_AUoAXoECAEQAw&biw=1383&bih=691'

result = requests.get(url)
soup = BeautifulSoup(result.text, 'html.parser')
urlImage = soup.findAll('img', class_="t0fcAb")
for i, img in enumerate(urlImage):
  img = img.get("src")
  surl = requests.get(img, stream=True)

  finaldir= 'Image'
  if not os.path.exists(finaldir):
      os.makedirs(finaldir)

  surl.raw.decode_content = True
  with open(f"{finaldir}/Image{i}.png", 'wb') as file:
    shutil.copyfileobj(surl.raw, file)
  print(f"Image{i}.png Saveed ! [{finaldir}/Image{i}.png]")