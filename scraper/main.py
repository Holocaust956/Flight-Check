import argparse
from scraper import FlightScraper
import os

def main():
    # 解析命令行参数
    parser = argparse.ArgumentParser(description="航班信息爬取工具")
    parser.add_argument("--dep", required=True, help="出发地城市代码（如 BJS）")
    parser.add_argument("--arr", required=True, help="目的地城市代码（如 HGH）")
    parser.add_argument("--date", required=True, help="出发日期（格式：YYYY-MM-DD）")
    args = parser.parse_args()
    # 从环境变量中读取 Selenium Hub URL
    selenium_hub_url = os.getenv("SELENIUM_HUB_URL", "http://localhost:4444/wd/hub")

    # 初始化爬虫
    scraper = FlightScraper(selenium_hub_url=selenium_hub_url)
    # 爬取航班信息
    flights = scraper.scrape_flights(args.dep, args.arr, args.date)

    # 输出结果
    for flight in flights:
        print(f"航空公司: {flight['airline']}")
        print(f"起飞时间: {flight['deptime']}, 到达时间: {flight['arrtime']}")
        print(f"价格: {flight['price']}")
        print("-" * 40)


if __name__ == "__main__":
    main()