# General
The code was done in python3; general pep8 guidelines were followed (mostly due to being use to them)

# SCRAPING
The model of a product is not always easily found.
	We try following the link to the product since it frequently has the model info.
	In case it can't be scraped, we use the reference instead
	For these cases, we store the information in a warnings file.

	A better idea would be a inteligent system that indentifies the model automaticly
		since it frequently follows a particular structure of letter and numbers

In case of errors, we store them in a errors file.

# MACHINE LEARNING
Low RAM on laptop
	Due to the nature of my laptop, I had to add some "del" statements
		in the python code so python's garbage collector will free some RAM for me.
	This would not be necessary on a normal/modern laptop/desktop

Initialy we get the product category from the scraping;
	This category simply means "ed": "eletro domestico"
	For the learning problem, this is useless to us so we change it to
	be either "washer" or "refrigerator"

Accuracy:
	Due to the 70-30 random split, the results fluctuate from around 97.0% - 98.0%
