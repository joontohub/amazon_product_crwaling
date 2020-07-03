import requests
from bs4 import BeautifulSoup


def url_pattern(i):
    url = "https://www.amazon.com/s?i=toys-and-games-intl-ship&rh=n%3A%2116225015011&page=2&qid=1566397221&ref=lp_16225015011_pg_"+str(i)
    return url

def get_string(url):
    data = requests.get(url)
    object = BeautifulSoup(data.content, "html.parser")

    return object

def get_products(object,number):
    print("###########################")
    print(object)
    div = object.find("div",{'class':"sg-col-20-of-24 sg-col-28-of-32 sg-col-16-of-20 sg-col s-right-column sg-col-32-of-36 sg-col-8-of-12 sg-col-12-of-16 sg-col-24-of-28"})

    small_div = div.find_all("span",{'class':'a-size-base-plus a-color-base a-text-normal'})
    product_box = small_div[number]
    return get_product(product_box)

def get_product(product_box):

    return product_box.text


for i in range(100):
    url = url_pattern(i+1)
    print(url)
    string = get_string(url)
    for j in range (23):
        product = get_products(string,j)
        print(product)
