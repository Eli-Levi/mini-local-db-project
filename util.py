def nonNumberInputError(what_was_wrong: str, wrong_input_given: str) -> None:
    print("Error: " + what_was_wrong + " must be a number. " + wrong_input_given + " is not a number")
    

def numberInputValidator(input_requested: str) -> int:
    while True:
        user_input = input("Enter a number for " +input_requested + ": ")
        if user_input.isdigit():
            return int(user_input)
        nonNumberInputError(input_requested, user_input)

