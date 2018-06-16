# flying-information
My solution to a internship test

# The problem:
Scrape all the refrigerators from here and the washers from here
Create a file with the following data for each product:
	code, title, brand, model, price, category
Later on the category attribute as swapped for the a value to represent if it is a washer or a refrigerator.
Then a XGBoost model was learnt to try to predict this new category.

The end result was in average a 97.5% accuracy.

At the very end, the theorical questions were answered and can be found on answers.md
General comments/choices can be found on notes.md

# Requirements:
python3 and the following packages: XGBoost, pandas, sklearn, json, urllib3, bs4
