import pathlib 
import re

# creating the function, which defines and returns the path to the text file:
def the_path_of_txt_file() -> str:
    
    return str(pathlib.Path(__file__).parent) + "\\employees_info.txt"      # return found directory in string format + the name of the text file itself


# a function which gets salary info from the text document and returns a list of all rows in the string format (employees' info)
# the argument of the function is a path to the text document which contains all relevant info"
def get_the_salary(path: str) -> list[str]:
                                                                            
    try:                                                                    # opening a text file and checking for exceptions if the file we need exists 
        with open(the_path_of_txt_file(), "r", encoding="utf-8") as file:   # returning a list of the entire text of the txt document: 1 row is a 1 elements of the list
            return file.readlines()

    except FileNotFoundError:                                               # check for an exception FileNotFoundError, return None in case of the error
        print(f"The file was not found")
        return None


# creating a function which gets the salary numbers from the list of the employees info:
def salaries_numbers() -> list[str]:
    list_of_salaries = []                                                   # creating a list, which is going to contain salary information only
    try:
        for salaries in get_the_salary(the_path_of_txt_file()):             # taking each element of the list with employees' info
            each_salary = salaries.split(",")[1]                            # splitting the element by "," symbol; leaving only part after this symbol as it supposed to indicate salary
            each_salary = re.sub(r"\s+", "", each_salary)                   # removing all excessive spaces, inside and outside the salary number, if they exist
            each_salary = re.sub(r"[\\t\\n\\r\\f\\v]", "", each_salary)     # removing all tabulation symbols
            
            if each_salary.isdigit() or float(each_salary):                 # checking, if the salary number is convertable into the int or float type, calling an exception if not
                list_of_salaries.append(each_salary)                        # adding the salary number to the list if it is convertable into the int or float type

        return list_of_salaries
    except ValueError:                                                      # check for an exception ValueError, return None in case of the inappropriate argument value and text
        print(f"Somethig went wrong. The salary should contain numbers only\
              \nPlease, go and check data in the {the_path_of_txt_file()}")
        return None


# creating a function total_salary, which analyzes text file in the same folder
# and returning total and average summary of the employees' salaries
# the argument of the function is a path to the text document which contains all relevant info
def total_salary(path: str) -> tuple[int]:
    sum = 0                                                                 # creating sum as for summary
    
    for salary_unit in salaries_numbers():                                  # getting each salary unit to summarize them in the sum
        sum += int(float(salary_unit))                                      # the summary is supposed to be integer
    avg = int(sum / len(salaries_numbers()))                                # finding average salary with dividing the summary into the amount of employees (rows)
    
    return int(sum), int(avg)                                               # return tuple of the summary and the average salary in the integer format

