from Person import Person
from Employee import Employee
from Student import Student
from Enums.MenuListEnum import MenuListEnum
from Enums.PersonTypeEnum import PersonTypeEnum
import pandas as pd
import util

# Global variable containing all people classes
type_of_people = {PersonTypeEnum.STUDENT: Student, PersonTypeEnum.EMPLOYEE: Employee, PersonTypeEnum.PERSON: Person}

def printPersonMenu() -> None:
    for index, person in enumerate(type_of_people):
        print(f'For {person.name.lower()}, press {index+1}')


def saveNewEntry(user_data: dict, id_index_list: list) -> bool:
    given_id = util.numberInputValidator("ID")
    if given_id in user_data:
        print(f'Error: ID already exists: {user_data[given_id].getPersonAsDict()}')
        return False
    given_name = input("Name: ")
    given_age =  util.numberInputValidator("age")
    printPersonMenu()
    user_choice = util.numberInputValidator("choice")
    try:
        user_choice = PersonTypeEnum(int(user_choice))
    except ValueError:
        print(f"Invalid choice: '{user_choice}' is not a valid person type.")
        return False
    new_person = type_of_people[user_choice](given_id, given_name, given_age)
    user_data[given_id] = new_person
    id_index_list.append(given_id)
    print(f'ID [{given_id}] saved successfully')
    return True


def extractAgeForSum(user_data: dict, id_index_list: list) -> int:
    saved_id = id_index_list[-1] # Supposed to access the last element in the array.
    user_entry = user_data[saved_id]
    return int(user_entry.getAge())


def searchById(user_data: dict) -> None:
    given_id = util.numberInputValidator("ID search")
    if given_id not in user_data:
        print(f'Error: ID {given_id} not saved')
    else:
        user_data[given_id].printMyself()


def printAgesAverage(sum_before_divide: int, divide_by: int) -> None:
    try:
        print(sum_before_divide/divide_by)
    except ZeroDivisionError:
        print(f'You can\'t divide by {divide_by}. Please add some new entries and then try again.')


def printAllNames(user_data: dict, user_size: int) -> None:
    if user_size != 0:
        for index, id in enumerate(user_data):
            print(f'{index}. {user_data[id].getName()}')


def printAllIds(user_data: dict, user_size: int) -> None:
    if  user_size != 0:
        for index, id in enumerate(user_data):
            print(f'{index}. {user_data[id].getId()}')


def printAllEntries(user_data: dict, user_size: int) -> None:
    if user_size != 0:
        for person in user_data.values():
            person.printMyself()


def printEntryByIndex(user_data: dict, id_index_list: list) -> None:
    user_input = util.numberInputValidator("index to print")
    try:
        retrieved_id = id_index_list[int(user_input)]
        user_data[retrieved_id].printMyself()
    except IndexError:
        raise IndexError(f'Error: Index out of range. The maximum index allowed is {len(user_data) - 1}')
        
       
def printMenu() -> None:
    for index, option in enumerate(MenuListEnum):
        print(f'{index+1}. {option.name.replace("_", " ").title()}')
    

def saveAllData(user_data: dict) -> None:
    file_name = input("What is your output file name? ")
    if not file_name.endswith(".csv"):
        file_name += ".csv"
        print("adding .csv extension")
    
    headers = []
    csv_format_data = []
    for user_id in user_data:
        dict_form_entry = user_data[user_id].getPersonAsDict()
        for key in dict_form_entry.keys():
            if not key in headers:
                headers.append(key)
        prep_entry_for_export = {key: dict_form_entry.get(key, None) for key in headers}
        csv_format_data.append(prep_entry_for_export)   
    df = pd.DataFrame(csv_format_data)
    df = df[headers]
    df.to_csv(file_name, index=False)

       
def toExitOrNotExit() -> bool: 
    while True:
        user_choice = input("Are you sure? (y/n) ")
        if user_choice.lower() in ["y", "yes"]:
            print("Goodbye!")
            return False
        elif user_choice.lower() in ["n", "no"]:
            return True
       
       
def main():
    # collection of variables and data structures
    age_sum_before_averaging = 0
    id_index_list = []
    user_data = {}
    running_flag = True
    try:
        while running_flag:
            try:
                printMenu()
                user_choice = input("Please enter your choice: ")
                user_choice = int(user_choice)
                
                if user_choice == MenuListEnum.SAVE_NEW_ENTRY.value:
                    save_success = saveNewEntry(user_data, id_index_list)
                    if save_success:
                        age_sum_before_averaging += extractAgeForSum(user_data, id_index_list)

                elif user_choice == MenuListEnum.SEARCH_BY_ID.value:
                    searchById(user_data)

                elif user_choice == MenuListEnum.PRINT_AVARAGE_ALL_AGES.value:
                    printAgesAverage(age_sum_before_averaging, len(id_index_list))

                elif user_choice == MenuListEnum.PRINT_ALL_NAMES.value:
                    printAllNames(user_data, len(user_data))

                elif user_choice == MenuListEnum.PRINT_ALL_IDS.value:
                    printAllIds(user_data, len(user_data))

                elif user_choice == MenuListEnum.PRINT_ALL_ENTRIES.value:
                    printAllEntries(user_data, len(user_data))

                elif user_choice == MenuListEnum.PRINT_ENTRY_BY_INDEX.value:
                    printEntryByIndex(user_data, id_index_list)
        
                elif user_choice == MenuListEnum.SAVE_ALL_DATA.value:
                    saveAllData(user_data)

                elif user_choice == MenuListEnum.EXIT.value:
                    running_flag = toExitOrNotExit()
                
                else:
                    raise ValueError or IndexError

            except ValueError:
                print(f'Error: Option [{user_choice}] does not exist. Please try again.')
                    
            finally:
                if running_flag:
                    input("Press Enter to continue")
                    
    except KeyboardInterrupt:
        print("\nI see you're trying to escape the Matrix...")
        print("Here, let me help you (;")
        exit()


main()