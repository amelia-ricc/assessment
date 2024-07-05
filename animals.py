# Import the libraries to connect to the database and present the information in tables
import sqlite3
from tabulate import tabulate

# This is the filename of the database to be used
DB_NAME = 'animals.db'
# This is the SQL to connect to all the tables in the database
TABLES = ("spca_animals "
          "LEFT JOIN diff_animals ON spca_animals.animal_id = diff_animals.animal_id "
          "LEFT JOIN location ON spca_animals.location_id = location.location_id "
          "LEFT JOIN animal_gender ON spca_animals.animal_sex_id = animal_gender.animal_sex_id "
          "LEFT JOIN animal_colour ON spca_animals.colour_id = animal_colour.colour_id ")

def print_parameter_query(fields:str, where:str, parameter):
    """ Prints the results for a parameter query in tabular form. """
    db = sqlite3.connect(DB_NAME)
    cursor = db.cursor()
    sql = ("SELECT " + fields + " FROM " + TABLES + " WHERE " + where)
    cursor.execute(sql,(parameter,))
    results = cursor.fetchall()
    print(tabulate(results,fields.split(",")))
    db.close

def print_query(view_name:str):
    ''' Prints the specified view from the database in a table '''
    # Set up the connection to the database
    db = sqlite3.connect(DB_NAME)
    cursor = db.cursor()
    # Get the results from the view
    sql = "SELECT * FROM '" + view_name + "'"
    cursor.execute(sql)
    results = cursor.fetchall()
    # Get the field names to use as headings
    field_names = "SELECT name from pragma_table_info('" + view_name + "') AS tblInfo"
    cursor.execute(field_names)
    headings = list(sum(cursor.fetchall(),()))
    # Print the results in a table with the headings
    print(tabulate(results,headings))
    db.close()


menu_choice =''
while menu_choice != 'Z':
    menu_choice = input('Welcome to the SPCA animals database\n\n'
                        'Type the letter for the information you want:\n'
                        'A: All guinea pigs\n'
                        'B: Animals under $100\n'
                        'C: Brown/ginger/chestnut animals (age descending)\n'
                        'D: Cats in Taupo\n'
                        'E: Christchurch cats or dogs\n'
                        'F: Farm animals (biggest to smallest, high price to low price)\n'
                        'G: Horses under 10 years old\n'
                        'H: Low maintenance colourful medium pet\n'
                        'I: Mixed breed shorthairs less than or equal to $250\n'
                        'J: Nelson or Christchurch (if in Christchurch they must be large)\n'
                        'K: Over 5 years and female\n'
                        'L: Pets in Greymouth that are good with kids\n'
                        'M: Plain black pets\n'
                        'N: Small or Medium pets in Wellington\n'
                        'O: Small young family pet in Masterton\n'
                        'P: South Island pets under $150 only\n'
                        'Q: Tabby or Tuxedo cats\n'
                        'R: Select all animals of a certain type\n'
                        'S: Select all animals that are located in a certain city\n'
                        'T: Select all animals of a certain breed\n'
                        'U: Select all animals of a certain colour\n'
                        'Z: Exit\n\nType option here: ')
    menu_choice = menu_choice.upper()
    if menu_choice == 'A':
        print_query('All guinea pigs')
    elif menu_choice == 'B':
        print_query('Animals under $100')
    elif menu_choice == 'C':
        print_query('Brown/ginger/chestnut animals (age descending)')
    elif menu_choice == 'D':
        print_query('Cats in Taupo')
    elif menu_choice == 'E':
        print_query('Christchurch cats or dogs')
    elif menu_choice == 'F':
        print_query('Farm animals (biggest to smallest, high price to low price)')
    elif menu_choice == 'G':
        print_query('Horses under 10 years old')
    elif menu_choice == 'H':
        print_query('Low maintenance colourful medium pet')
    elif menu_choice == 'I':
        print_query('Mixed breed shorthairs less than or equal to $250')
    elif menu_choice == 'J':
        print_query('Nelson or Christchurch (if in Christchurch they must be large)')
    elif menu_choice == 'K':
        print_query('Over 5 years and female')
    elif menu_choice == 'L':
        print_query('Pets in Greymouth that are good with kids')
    elif menu_choice == 'M':
        print_query('Plain black pets')
    elif menu_choice == 'N':
        print_query('Small or Medium pets in Wellington')
    elif menu_choice == 'O':
        print_query('Small young family pet in Masterton')
    elif menu_choice == 'P':
        print_query('South Island pets under $150 only')
    elif menu_choice == 'Q':
        print_query('Tabby or Tuxedo cats')
    elif menu_choice == 'R':
        animal = input('What type of animal do you want to see: ')
        print_parameter_query("animal, age_in_years, adoption_fee_dollars, location", "animal = ? ORDER BY age_in_years ASC",animal)
    elif menu_choice == 'S':
        location = input('What city do you want to see animals from: ')
        print_parameter_query("animal, age_in_years, adoption_fee_dollars, location, name", "location = ? ORDER BY adoption_fee_dollars DESC", location)
    elif menu_choice == 'T':
        breed = input('What breed of animal do you want to see: ')
        print_parameter_query("name, animal, fur_length, breed, colour, pattern", "breed = ?", breed)
    elif menu_choice == 'U':
        colour = input('What colour of animals do you want to see: ')
        print_parameter_query("animal, name, age_in_years, breed, colour", "colour = ?", colour)