from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import os
import time


# 輸入搜尋關鍵字
input_image = "outfits"

# 初始化 Selenium 瀏覽器
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # 不開啟瀏覽器

# 使用 Selenium WebDriver 啟動 Chrome 瀏覽器
driver = webdriver.Chrome(options=options)

try:
    # 前往 Unsplash 的搜尋結果頁面
    driver.get(f"https://unsplash.com/s/photos/{input_image}")

    # css 選擇器
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR,".LaaWe.Qzy6N.ogSND.ZR5jm.cs1e4.ibgtd.v2BPu.mP89P.szXtT.wACgf.ZR5jm"))
    )

    # 如果需要點擊的按鈕是動態生成的，使用 Selenium 找到並點擊它
    button = driver.find_element(By.CSS_SELECTOR, '.LaaWe.Qzy6N.ogSND.ZR5jm.cs1e4.ibgtd.v2BPu.mP89P.szXtT.wACgf.ZR5jm')
    button.click()

    time.sleep(2)   # 點擊後給一些加載時間

    # 獲取更新後的網頁內容
    updated_html = driver.page_source
    soup = BeautifulSoup(updated_html, 'html.parser')

    # 找到所有圖片元素
    results = soup.find_all("img", {"class": "ApbSI z1piP vkrMA"}, limit=3)
    image_links = [result.get("src") for result in results]  # 取得圖片來源連結

    # 下載圖片並存儲到本地資料夾
    for index, link in enumerate(image_links):
        if not os.path.exists(f"{input_image}"):
            os.mkdir(f"{input_image}")  # 建立資料夾

        img = requests.get(link)  # 下載圖片

        with open(f"{input_image}/" + input_image + str(index + 1) + ".jpg", "wb") as file:  # 開啟資料夾及命名圖片檔
            file.write(img.content)  # 寫入圖片的二進位碼



except KeyboardInterrupt:
    # 無論是否成功，都關閉瀏覽器
    driver.quit()
    print("keyboard interrupt")

except Exception:
    # 無論是否成功，都關閉瀏覽器
    driver.quit()
    print("error anyway")

finally:
    # 無論是否成功，都關閉瀏覽器
    driver.quit()
