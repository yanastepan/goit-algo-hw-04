import pathlib
import re

# creating the function, which defines and returns the path to the text file:
def the_path_of_txt_file() -> str:
        return str(pathlib.Path(__file__).parent / "cats_info.txt")         # return parent directory in string format + the name of the text file itself


# creating a function, which is supposed to issue the whole information from txt file
# and return a list of all data (1 row of text is 1 element of the list)
def get_all_info_about_the_cats() -> list[str]:

    try:                                                                    # opening a text file and checking for exceptions if the file we need exists 
        with open(the_path_of_txt_file(), "r", encoding="utf-8") as file:   # returning a list of the entire text of the txt document
            return file.readlines()
    # check for an exception FileNotFoundError, return None in case of the error
    except FileNotFoundError:
        print(f"The file was not found")
        return None
    # check for an exception IOError, return None in case of the error
    except IOError as e:
        print(f"An I/O error occurred: {e}")
        return None
    # check for an exception UnicodeDecodeError, return None in case of the error
    except UnicodeDecodeError as e:
        print(f"Unicode decode error: {e}")
        return None


# creating a function, which creates a list with dictionaries, using provided keys in the arguments and list of values
def dictionary_creation(values: list, keys = ["id", "name", "age"]) -> list[dict]:
    dictionaries = []                                                       # the final list is supposed to be held in this variable
    try:
        for each_value in values:                                           # values is supposed to be a list, containing several lists; breaking them down
            dictionary_unit = dict(zip(keys, each_value))                   # forming a dictionary, based on the provided keys and values in the list
            
            if (dictionary_unit["age"]).isdigit():                          # checking, if the age is written as a number
                dictionaries.append(dictionary_unit)                        # adding formed dictionary to the final list, if so
            else:                                                           # print an error message, if not
                print(f"Somethig went wrong. The age is supposed to be a number in a row of the {dictionary_unit["name"]} cat. " \
                    "This cat's information is not going to be provided")
    # this exception is calling out if any information about the cat is missing in the text file           
    except KeyError:    
        print("The list of the information is not full. Please, make sure you have all variables for " \
              "all the cats")
        return None
    return dictionaries


# creating a function which creates a list of information about each cat, formed in the list each separately
def the_list_of_info_per_cat() -> list[list[str]]:
    all_cats_info = []                                                      # the final list will be placed in this variable
    try:
        for one_row in get_all_info_about_the_cats():                       # getting each element to separate and form it into the sublist
            cat_info_list = []                                              # the sublist is supposed to be placed in this variable
            for info_unit in one_row.split(","):                            # as the data is deparated with ",", separating all of them into separate elements
                
                info_unit = re.sub(r"\s+", "", info_unit)                   # removing all excessive spaces, inside and outside the info unit about the cat, if they exist
                info_unit = re.sub(r"[\t\n\r\f\v]", "", info_unit)          # removing all tabulation symbols
                
                cat_info_list.append(info_unit)                             # forming the sublist after the processing the data
            all_cats_info.append(cat_info_list)                             # combining sublists into the final list of information
    # check for an exception ValueError, return None in case of the inappropriate argument value and text
    except ValueError:  
        print(f"Somethig went wrong. Please, go and check data in the {the_path_of_txt_file()}")
        return None
    
    return all_cats_info


# creating a fucntion which takes path to the text file as an argument
# the file contains data about cats, where each entry contains a unique identifier, the cat's name, and its age.
# The function should return a list of dictionaries, where each dictionary contains information about one cat.
def get_cats_info(path: str) -> list[dict]:
    try:                                                                    # using formed functions before dictionary_creation and 
        the_list_of_dict = dictionary_creation(the_list_of_info_per_cat())  # the_list_of_info_per_cat as its parameter, processing needed operation
        return the_list_of_dict
    # check for an exception TypeError
    except TypeError:
        print("Please, make sure the file you need exists")
    