from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time


class FlightScraper:
    def __init__(self, selenium_hub_url):
        # 设置 Chrome 选项
        chrome_options = Options()
        chrome_options.add_argument("--disable-dev-shm-usage")  # 无头模式
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
        # 连接到 Docker 容器中的 Chrome

        self.driver = webdriver.Remote(
            command_executor=selenium_hub_url,
            options=chrome_options
        )

    def scrape_flights(self, dep_city, arr_city, dep_date):
        try:
            # 打开目标页面
            url = f"https://sjipiao.fliggy.com/homeow/trip_flight_search.htm?spm=181.11358650.flight.dflightSearch1&tripType=0&depCity={dep_city}&arrCity={arr_city}&depDate={dep_date}"
            self.driver.set_page_load_timeout(60)  # 设置页面加载超时时间为 60 秒
            self.driver.get(url)

            # 等待页面加载
            time.sleep(10)  # 根据网络情况调整等待时间

            # 提取航班信息
            flights = self.driver.find_elements(By.CLASS_NAME, "flight-list-item")  # 根据实际页面结构调整
            results = []
            for flight in flights:
                try:
                    airline = flight.find_element(By.CLASS_NAME, "airline-name").text
                    deptime = flight.find_element(By.CLASS_NAME, "flight-time-deptime").text
                    arrtime = flight.find_element(By.CLASS_NAME, "s-time").text
                    price = flight.find_element(By.CLASS_NAME, "pi-price").text
                    results.append({
                        "airline": airline,
                        "deptime": deptime,
                        "arrtime": arrtime,
                        "price": price
                    })
                except Exception as e:
                    print(f"提取失败: {e}")
            return results

        finally:
            # 关闭浏览器
            self.driver.quit()