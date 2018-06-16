# flying-information
My solution to a internship test

# The problem:
Scrape all the refrigerators from [here](https://www.magazineluiza.com.br/geladeira-refrigerador/eletrodomesticos/s/ed/refr/) and the washers from [here](https://www.magazineluiza.com.br/lavadora-de-roupas-lava-e-seca/eletrodomesticos/s/ed/ela1/)

Create a file with the following data for each product:	code, title, brand, model, price, category

Later on the category attribute is swapped for a value that represents if it is a washer or a refrigerator.

Then a XGBoost model was trained to predict this new category.

The end result was in average a **97.5% accuracy.**

At the very end, the theorical questions were answered and can be found on answers.md

General comments/choices can be found on [notes.md](https://github.com/BrunoGomesCoelho/flying-information/blob/master/notes.md)

# Requirements:
python3 and the following packages: XGBoost, pandas, sklearn, json, urllib3, bs4
