"""A script that parses through a txt
file containing 10 thousand emails extracting 
all the necessary information from them, creating
a list contianing Email objects and returns 
the lenght of that list. 
"""

import re
import sys
import argparse


class Server:
    """This class stores the data for all
    emails found in the dataset. 
    """
   
    def __init__(self, path):
        """This __init__ function
        opens file in the path provided when 
        declaring a Server object and using 
        regular expressions extracts
        all the necessary information from
        each one of the emails in the txt
        file. Then a list of Email objects
        is created based on the data extracted

        Args: 
            path(str) - a name of the file containing emails
        """
        # python3 enron.py emails_10k.txt
        self.emails = []

        with open(path) as file: 

            file_str = file.read()

            id_pattern = r"(Message-ID: )(.*)"  
            date_pattern = r"(Date: )(.*)"          
            subject_pattern = r"(Subject: )(.*)"    
            sender_pattern = r"(From: )(.*)"
            reciever_pattern = r"(To: )(.*)"

            # regex for body does not seem to be working 
            body_pattern = r"(X-FileName:)([\S\s]+)"

            email_list = file_str.split("End Email\"")
            email_list.pop()
            
        for email in email_list:
            match_id = re.search(id_pattern, email)
            message_id = match_id.group(2)
            match_date = re.search(date_pattern, email)
            date = match_date.group(2)
            match_subject = re.search(subject_pattern, email)
            subject = match_subject.group(2)
            match_sender = re.search(sender_pattern, email)
            sender = match_sender.group(2)
            match_reciever = re.search(reciever_pattern, email)
            reciever = match_reciever.group(2)
            match_body = re.search(body_pattern, email)
            body = match_body.group(2)
            self.emails.append(Email(message_id, date, subject, sender, reciever, body)) 
        

class Email:
    """Class used for creating singular
    Email objects.
    """
    def __init__(self, message_id, date, subject, sender, receiver, body):
        self.message_id = message_id
        self.date = date
        self.subject = subject
        self.sender = sender
        self.receiver = receiver
        self.body = body

    
def main(path):
    """Creates an object of the Server class
    and returns the length of the emails attribute.

    Args:
        path(str) - a name of the file containing emails

    Returns:
        len(server.emails) - length of the emails attribute 
        of the Server object created
    """
    server = Server(path)
    return len(server.emails)


def parse_args(args_list):
    """Create an instance of the ArgumentParser 
    class from the argparse module. Use the 
    add_argument() method of your ArgumentParser 
    instance to add the required arguments.

    Args: 
        args_list - a list of strings containing 
        the command-line arguments for the program

    Returns: 
        args - the ArgumentParser object created.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=str)
    args = parser.parse_args(args_list)
    return args


if __name__ == "__main__": 
    value = parse_args(sys.argv[1:])
    main(value.path)
