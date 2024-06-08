from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time
import os

class CoinMarketCap:
    BASE_URL = "https://coinmarketcap.com/currencies/"

    def __init__(self):
        options = Options()
        options.headless = True  
        chrome_binary_path = "taskapp/chrome/chrome"
        options.binary_location = chrome_binary_path

        chromedriver_path = os.path.abspath("taskapp/drivers/chromedriver")
        if not os.path.isfile(chromedriver_path):
            raise FileNotFoundError(f"Chromedriver not found at path: {chromedriver_path}")

        service = Service(chromedriver_path)
        self.driver = webdriver.Chrome(service=service, options=options)

    def scrape(self, coin_acronyms):
        results = []
        for coin in coin_acronyms:
            url = f"{self.BASE_URL}{coin}/"
            self.driver.get(url)

            # Delay set to 2 minues to load page 
            time.sleep(2)  

            try:
                
                # Finding elements using the XPATH
                price = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div/div/div[2]/section/div/div[2]/span').text
                price_change = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div/div/div[2]/section/div/div[2]/div/div/p').text
                market_cap = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div/div/div[2]/div[2]/section[2]/div/div[1]/div/dl/div[1]/div[1]/dd').text
                market_cap_rank = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div/div/div[2]/div[2]/section[2]/div/div[1]/div/dl/div[1]/div[2]/div/span').text
                volume = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div/div/div[2]/div[2]/section[2]/div/div[1]/div/dl/div[2]/div[1]/dd').text
                volume_rank = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div/div/div[2]/div[2]/section[2]/div/div[1]/div/dl/div[2]/div[2]/div/span').text
                volume_change = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div/div/div[2]/div[2]/section[2]/div/div[1]/div/dl/div[3]/div/dd').text
                circulating_supply = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div/div/div[2]/div[2]/section[2]/div/div[1]/div/dl/div[4]/div/dd').text
                total_supply = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div/div/div[2]/div[2]/section[2]/div/div[1]/div/dl/div[5]/div/dd').text
                diluted_market_cap = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div/div/div[2]/div[2]/section[2]/div/div[1]/div/dl/div[7]/div/dd').text
                contracts_name = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div/div/div[2]/div[2]/section[2]/div/div[2]/div[1]/div[2]/div/div[1]/a/span[1]').text
                contract_address = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div/div/div[2]/div[2]/section[2]/div/div[2]/div[1]/div[2]/div/div[1]/a/span[2]').text
                official_links = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div/div/div[2]/div[2]/section[2]/div/div[2]/div[2]/div[2]/div/div/a').get_attribute('href')
                twitter = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div/div/div[2]/div[2]/section[2]/div/div[2]/div[3]/div[2]/div/div[1]/a').text
                twitter_url = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div/div/div[2]/div[2]/section[2]/div/div[2]/div[3]/div[2]/div/div[1]/a').get_attribute('href')
                telegram = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div/div/div[2]/div[2]/section[2]/div/div[2]/div[3]/div[2]/div/div[2]/a').text
                telegram_url = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div/div/div[2]/div[2]/section[2]/div/div[2]/div[3]/div[2]/div/div[2]/a').get_attribute('href')

                coin_data = {
                    "coin": coin,
                    "output": {
                        "price": price,
                        "price_change": price_change,
                        "market_cap": market_cap,
                        "market_cap_rank": market_cap_rank,
                        "volume": volume,
                        "volume_rank": volume_rank,
                        "volume_change": volume_change,
                        "circulating_supply": circulating_supply,
                        "total_supply": total_supply,
                        "diluted_market_cap": diluted_market_cap,
                        "contracts": [
                            {
                                "name": contracts_name,
                                "address": contract_address
                            }
                        ],
                        "official_links": [
                            {
                                "name": "website",
                                "link": official_links
                            }
                        ],
                        "socials": [
                            {
                                "name": "twitter",
                                "url": twitter_url
                            },
                            {
                                "name": "telegram",
                                "url": telegram_url
                            }
                        ]
                    }
                }
                results.append(coin_data)
            except Exception as e:
                results.append({"coin": coin, "error": "-"})

        self.driver.quit()
        return results


