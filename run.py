from scrapping_the_data.scrapping_the_data import scrapped_data
from analysis.analysis import analysis_products

if __name__ == "__main__":
    print("\nPress 1 to scrap data from website")
    print("\nPress 2 to do analysis on scrapped data \n")
    choice = int(input())
    if choice == 1:
        scrapped_data()

    elif choice == 2:
        analysis_products()

    else:
        print("\nYou select the wrong option ")
