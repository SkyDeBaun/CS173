import nltk
import re


def repl_func(match):
  if match == True:
    return " "



string = "Hello-world... How are you?! Where have you been?!"
new_string = re.sub(r"""[-!?'".<>(){}@%&*/[/]""", " ", string)
print(new_string)