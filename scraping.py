# coding: utf-8

import sys # For some basic error checks since we are not implementing exceptions
import json # For converting strings to dictionaries

# For scraping/crawling
import csv
import urllib3
import certifi
from bs4 import BeautifulSoup


ERROR_MESSAGES = []

# Use a better name for sys function
PROGRAM_CURRENT_LINE = sys._getframe().f_lineno

# Link relevant information
BASE_REFRIGERATOR_PAGE = "https://www.magazineluiza.com.br/\
                         geladeira-refrigerador/eletrodomesticos/s/ed/refr/"
BASE_WASHER_PAGE = "https://www.magazineluiza.com.br/\
                    lavadora-de-roupas-lava-e-seca/eletrodomesticos/s/ed/ela1/"

# A static count for now;
#   better would be to actually scrape and click on the next page until no longe possible
REFRIGERATOR_PAGES_COUNT = 6
WASHER_PAGES_COUNT = 5


class Appliance(object):
    """
    The Appliance class holds all usefull information for a appliance.
    Some of this information is pertinent to the customer, some of it is pertinent for our IA model.
    """
    def __init__(self, code, title, brand, model, price, category):
        self.code = code
        self.title = title
        self.brand = brand
        self.model = model
        self.price = price
        self.category = category

    def get_customer_info(self):
        return str(self.code), "\"" + self.title + "\"", self.brand,\
                   self.model, self.price, self.category

    def __str__(self):
        return ", ".join(self.get_customer_info())


def connect(url):
    http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
    headers = {}
    headers["User-Agent"] = "Mozilla/5.0 (X11; Linux x86_64)\
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    headers["X-Requested-With"] = "XMLHttpRequest"

    # Try to get the page and the soup.
    # A better implementation would use try/except to catch errors.
    req = http.request(
        "GET",
        url,
        headers=headers
    )

    page = req.data
    return BeautifulSoup(page, "lxml")


def get_product_info(product):
    # Json converts our string mess into a easy to use dictionary
    info_dict = json.loads(product.find("a")["data-product"])
    product_link = product.find("a")["href"]

    try:
        # Follow the link of the product since we want the model and it
        #   freqeuently can't be found on the search
        product_soup = connect(product_link)
        product_model = product_soup.find("table", {"class": "description__box--wildSand"})\
                        .find("tr").find_all("td")[1].find_all("table")[2]\
                        .find_all("td")[1].text
        product_model = product_model.strip()  # Remove white spaces
        info_dict["model"] = product_model
    except:
        ERROR_MESSAGES.append("No model information found for {}".format(product_link))

    # If we dont find the model, use the reference since it may contain the model
    return Appliance(code=int(info_dict["product"]), title=info_dict["title"],
                     brand=info_dict["brand"], model=info_dict["model"],
                     price=info_dict["price"], category=info_dict["category"])


def scrape_product(page, count):
    items = []

    for page_index in range(1, count+1):
        soup = connect(page + "{}/".format(page_index))
        content = soup.find_all("ul", {"class": "productShowCase big"})

        if len(content) != 1:
            ERROR_MESSAGES.append("Line {}: productShowCase big has changed"\
                                  .format(PROGRAM_CURRENT_LINE))

        product_list = content[0].find_all("li")

        # Remove the last item as it does not represent a product
        product_list = product_list[:-1]

        for product in product_list:
            # Json converts our string mess into a easy to use dictionary
            items.append(get_product_info(product))
    return items


def save_product(file_name, product_list):
    with open(file_name, "w", newline="") as csvfile:
        content_writer = csv.writer(csvfile)
        for item in product_list:
            content_writer.writerow([str(x) for x in item.get_customer_info()])


def main():
    refrigerators = scrape_product(BASE_REFRIGERATOR_PAGE, REFRIGERATOR_PAGES_COUNT)
    washers = scrape_product(BASE_WASHER_PAGE, WASHER_PAGES_COUNT)

    save_product("refrigerators.csv", refrigerators)
    save_product("washers.csv", washers)

    print("{} refrigerators and {} washers were scraped!".format(
        len(refrigerators), len(washers)))

    print("{} errors were found".format(len(ERROR_MESSAGES)))
    print(*ERROR_MESSAGES, sep="\n")


if __name__ == "__main__":
    main()
