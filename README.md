# flying-information
My solution to a internship test

# The problem:
Scrape all the refrigerators from [here](https://www.magazineluiza.com.br/geladeira-refrigerador/eletrodomesticos/s/ed/refr/) and the washers from [here](https://www.magazineluiza.com.br/lavadora-de-roupas-lava-e-seca/eletrodomesticos/s/ed/ela1/)

Create a file with the following data for each product:	code, title, brand, model, price, category

Later on the category attribute is swapped for a value that represents if it is a washer or a refrigerator.

Then a XGBoost model was trained to predict this new category.

The end result was in average a **97.5% accuracy.**

At the very end, the theorical questions were answered and can be found on [answers.md](https://github.com/BrunoGomesCoelho/flying-information/blob/master/answers.md)

General comments/choices can be found on [notes.md](https://github.com/BrunoGomesCoelho/flying-information/blob/master/notes.md)

# Code structure
All the scraping is done with the help of `scraping.py` and the model trained and tested in `learn_category.py`

# Requirements
python3 and the following packages: XGBoost, pandas, sklearn, json, urllib3, bs4

All of them should be easily instalable with `pip3 install PACKAGE` if not already present.

# Running
First run
> python3 scraping.py

if you would like to re-scrape/create the csv files.Then

> python3 learn_category.py

to train a model and predict, outputting the accuracy.

