from bs4 import BeautifulSoup
import requests
import os

# 輸入搜尋關鍵字
input_image = "outfits"

# 獲取 html 網頁 並使用 BeautifulSoup 解析內容
response = requests.get(f"https://unsplash.com/s/photos/{input_image}")
soup = BeautifulSoup(response.text, "lxml")

# 找到所有圖片元素
results = soup.find_all("img", {"class": "ApbSI z1piP vkrMA"}, limit=3)

image_links = [result.get("src") for result in results]  # 取得圖片來源連結

# 下載圖片並存儲到本地資料夾
for index, link in enumerate(image_links):
    if not os.path.exists(f"{input_image}"):
        os.mkdir(f"{input_image}")  # 建立資料夾

    img = requests.get(link)  # 下載圖片

    with open(f"{input_image}" + "\\" + input_image + str(index+1) + ".jpg", "wb") as file:  # 開啟資料夾及命名圖片檔
        file.write(img.content)  # 寫入圖片的二進位碼

