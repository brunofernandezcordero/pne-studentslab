import json
import termcolor
from pathlib import Path

# -- Read the json file
# Note: Ensure your file is named correctly and contains the [ ] brackets
jsonstring = Path("people-e1.json").read_text()

# Create a list of people from the json string
# This is now a LIST, not a single dictionary
people_list = json.loads(jsonstring)

# Loop through each person in the list
for person in people_list:
    print("-" * 30)  # Visual separator between people

    termcolor.cprint("Name: ", 'green', end="")
    print(person['Firstname'], person['Lastname'])

    termcolor.cprint("Age: ", 'green', end="")
    print(person['age'])

    # Get the phoneNumber list for THIS specific person
    phoneNumbers = person['phoneNumber']

    termcolor.cprint("Phone numbers: ", 'green', end='')
    print(len(phoneNumbers))

    # Print all the numbers for this person
    for i, dictnum in enumerate(phoneNumbers):
        termcolor.cprint("  Phone " + str(i + 1) + ": ", 'blue')

        termcolor.cprint("\t- Type: ", 'red', end='')
        print(dictnum['type'])

        termcolor.cprint("\t- Number: ", 'red', end='')
        print(dictnum['number'])

print("-" * 30)