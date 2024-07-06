from salary_get import the_path_of_txt_file, total_salary, salaries_numbers, get_the_salary

# define a function which executes total_salary function, checking for exceptions in case if exist:
def main() -> None:

    try:                                                                    # issue 2 variables from the tuple of summary and average salaries
        total, average = total_salary(the_path_of_txt_file())               # printing needed variables in the output
        print(f"The total summary of the work compensation: {total}, The average work compensation: {average}")
                                                                            # the text was translated to maintain the same language throughout the task   
    except TypeError:                                                       # checking for an exception TypeError in case of inapropriate type of salaries when tried 
        print("The error occured: TypeError")                               # to convert to int or float;
    except OSError:                                                         # checking for an exception OSError in case if someting is wrong with the name of the text file
        print("Are you sure the data entered correctly?")

if __name__ == "__main__":                                                  # entry point
    main()                                                                  # excecution of the main function if the code is running in the main.py file