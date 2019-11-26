Note: All of the given instructions are for linux


-First of all create a python virtual enviroment
--virtualenv venv

-Then activate it by the following command
-- source venv/bin/activate

-After that install all the requirements in the virtual enviroment by the following command
-- pip install -r requirements.txt

-When all of the above procedure is complete, run the program from the following the command in main directory
--python run.py

-There you will get 2 options, 1 for scrapping and 2 for analysis.
    By choosing option 1, the program will automatically start scrapping data and will save it in pandas dataframe
    By choosing option 2, the program will do the analysis on the data (csv file) and will find mean max and average of the products
    In analysis part, there will be a count for number of sales for each product

-There will be a delay of 4 second for each of the product while scrapping