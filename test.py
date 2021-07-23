from bs4 import BeautifulSoup
import requests
import os
import shutil

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
