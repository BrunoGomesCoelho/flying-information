
# coding: utf-8

# In[1]:


# import used libraries
import sys # For some basic error checks since we are not implementing exceptions

# For scraping/crawling
import urllib3
from bs4 import BeautifulSoup
import certifi
import re

# For converting strings to dictionaries
import json


ERROR_MESSAGES = []


# In[2]:


# Use a better name for sys function
program_current_line = sys._getframe().f_lineno


# In[3]:


# A static count for now; better would be to actually scrape and click on the next page until no longe possible
BASE_REFRIGERATOR_PAGE = "https://www.magazineluiza.com.br/geladeira-refrigerador/eletrodomesticos/s/ed/refr/"
REFRIGERATOR_PAGES_COUNT = 6

BASE_WASHER_PAGE = "https://www.magazineluiza.com.br/lavadora-de-roupas-lava-e-seca/eletrodomesticos/s/ed/ela1/"
WASHER_PAGES_COUNT = 5


# In[4]:


def connect(url):
    http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
    headers = {}
    headers["User-Agent"] = "Mozilla/5.0 (X11; Linux x86_64)             \AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
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


# In[5]:


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
        return str(self.code), self.title, self.brand, self.model, self.price, self.category

    def __str__(self):
        return ", ".join(self.get_customer_info())
        


# In[17]:


# I was here

def get_product_info(product):
    # Json converts our string mess into a easy to use dictionary
    info_dict = json.loads(product.find("a")["data-product"])
    product_link = product.find("a")["href"]

    try:
        # Follow the link for the product model since it frequently can't be found on the search
        # A better idea would be to use string searches/regex probably, done this way due to time constraints.
        product_soup = connect(product_link)
        product_model = product_soup.find("table", {"class": "description__box--wildSand"})                        .find("tr").find_all("td")[1].find_all("table")[2]                        .find_all("td")[1].text
        product_model = product_model.strip()  # Remove white spaces
        info_dict["model"] = product_model
    except:
        ERROR_MESSAGES.append("No model information found for {}".format(refrigerator_link))
    
    # If we dont find the model, use the reference since it may contain the model
    return Appliance(code=int(info_dict["product"]), title=info_dict["title"],
                     brand=info_dict["brand"], model=info_dict["model"], 
                     price=info_dict["price"], category=info_dict["category"])

def scrape_refrigerators():
    refrigerators = []
    #washers
    
    for page_index in range(1, REFRIGERATOR_PAGES_COUNT+1):
            soup = connect(BASE_REFRIGERATOR_PAGE + "{}/".format(page_index))
            content = soup.find_all("ul", {"class": "productShowCase big"})

            if len(content) != 1:
                ERROR_MESSAGES.append("Line {}: productShowCase big has changed".format(program_current_line))
            
            product_list = content[0].find_all("li")

            # Remove the last item as it does not represent a product
            product_list = product_list[:-1]
       
            for product in product_list[:10]:
                # Json converts our string mess into a easy to use dictionary
                refrigerators.append(get_product_info(product))
    return refrigerators, washers
                            

all_refrigerators = scrape_refrigerators()


# In[18]:


print("{} refrigerators scraped!".format(len(all_refrigerators)))


# In[19]:


print(*all_refrigerators)


# In[20]:


import csv
print(str(all_refrigerators[0].code))

with open("refrigerators.csv", "w", newline="") as csvfile:
    content_writer = csv.writer(csvfile, delimiter=' ',
                        quotechar='"')
    for item in all_refrigerators:
        print(item)
        content_writer.writerow([str(x) for x in item.get_customer_info()])

