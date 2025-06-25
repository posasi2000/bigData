from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
import time


def CoffeeBean_store(result):
    CoffeeBean_URL = "https://www.coffeebeankorea.com/store/store.asp"
    driver = webdriver.Chrome() 
             
    for i in range(1, 20):  #마지막 매장번호(최근 신규 매장번호 for i in range(1, 389): 
        driver.get(CoffeeBean_URL)
        time.sleep(1)  #웹페이지 연결할 동안 1초 대기
        try:
            driver.execute_script("storePop2(%d)" %i)
            time.sleep(1) # 1초 대기
            html = driver.page_source
            soupCB = BeautifulSoup(html, 'html.parser')
            store_name_h2 = soupCB.select("div.store_txt > h2")
            print( 'store_name_h2결과' , store_name_h2 )
            store_name = store_name_h2[0].string
            print(store_name)  #매장 이름 출력하기
            store_info = soupCB.select("div.store_txt > table.store_table > tbody > tr > td")
            store_address_list = list(store_info[2])
            print('store_address_list 결과 ',store_address_list)
            store_address = store_address_list[0]
            store_phone = store_info[3].string
            result.append([store_name]+[store_address]+[store_phone])
        except:
            continue 
    return

def main():
    result = []
    CoffeeBean_store(result) 
    bean_tbl = pd.DataFrame(result, columns=('store', 'address','phone'))
    bean_tbl.to_csv('./data/CoffeeBean.csv', encoding='cp949', mode='w', index=False)

if __name__ == '__main__':
     main()
