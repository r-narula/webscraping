from bs4 import BeautifulSoup
import pandas as pd

df = pd.DataFrame(columns=['price','title','stock','maftr'])
print(df)
with open('file.html') as f:
    soup = BeautifulSoup(f, 'html.parser')

    product_list = soup.find_all("div", {"class": "product"})

    for count,i  in enumerate(product_list):
        prices_list = i.find_all("div", {"class":"catalog-item-price"})
        products_desc = i.find_all("div",{"class":"product-description"})
        for span_price in prices_list:
            price_list = span_price.find("span",{"class":""})

            for price in price_list:
                print(price.text) # we gave got the price tag of each and every item on the webpage

        for product_desc in products_desc:
            # print(product_desc)
            title = product_desc.find('a',{"class":"catalog-item-name"}).text
            print(title)

            brand_name = product_desc.find('div',{"class":"catalog-item-brand-item-number"}).find('a',{"class":"catalog-item-brand"}).text
            print(brand_name)

        for stock_check in prices_list:
            in_stock = stock_check.find_all("span",{"class":"status"})[0].text

        print(f"All in ONE:, {price}, {title}, {brand_name}, {in_stock}")

        # print(count)
        df.loc[count] = pd.Series(data={'price':price,'title':title,'stock':in_stock,'maftr':brand_name})


df.to_csv("final.csv")
df.to_json("final.json",orient='records')