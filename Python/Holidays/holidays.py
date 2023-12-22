import sys
import argparse
import requests

def get_holidays(countrycode, year):
    """The function takes in the country code and year,
    creates a link based on these parameters, makes an
    HTTP GET request and converts the result into 
    a json file. Then by going through the json 
    file recieved it prints out all the dates and 
    holidays. 

    Args:
        code(str) - country code consisting of two letters
        year(int) - year consisting of four numbers
    """
    link = f'https://date.nager.at/Api/v1/Get/{countrycode}/{year}'
    request = requests.get(link)
    converted = request.json()

    for holiday in converted:
        print(f"{holiday['date']}: {holiday['name']}") 


def parse_args(args_list):
    """Takes a list of strings from the command prompt and passes them through as arguments
    
    Args:
        args_list (list) : the list of strings from the command prompt
    Returns:
        args (ArgumentParser)
    """
    parser = argparse.ArgumentParser() #Create an ArgumentParser object.
    
    parser.add_argument("countrycode", type=str)
    parser.add_argument("year", type=int)  
    
    args = parser.parse_args(args_list) #We need to parse the list of command line arguments using this object.
    return args

if __name__ == "__main__":
    countrycode, year = parse_args(sys.argv[1:]) #Pass in the list of command line arguments to the parse_args function.
    get_holidays(countrycode, year)
