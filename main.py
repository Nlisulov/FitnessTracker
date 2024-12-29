#Declaring a global variable for the terminal output display
bannerLen = 100


def dataToFile():
    pass

def getDatabaseData():
    pass

def validateInput(prompt: str):
    validNum = False
    while  not validNum:
        num = input(f"\n\n\n{prompt}")

        try:
            num = int(num)

            if num >= 1:
                validNum = True
            else:
                RowedDashes()
                print("\n|REMINDER: Please enter in a integer >= 1|")
                RowedDashes()

        except ValueError:
            RowedDashes()
            print("\n|WARNING: Please enter in a integer|")
            RowedDashes()
    return num

def RowedStars():
    for x in range(bannerLen):
        print("*", end="")

def RowedDashes():
    for x in range(bannerLen):
        print("-", end="")        

def WelcomeAscii():
    print("*", end="")
    print("")

def WelcomeBanner():
    RowedStars()
    print("\n* Welcome *")
    RowedStars()
    

if __name__ == "__main__":
    WelcomeBanner()
    print("\nThis is application is meant to track fitness goals and progress in terms of weight lifting.")

    print("\n\n\n\n\nNote: Any numbers with a decimal point will have the floor function applied to it. \nFor Example: 2.7 ---> 2 and 3.4 ---> 3")
    RowedDashes()
    print("\n\n")
    #   This loop stylizes the console terminal while also checking the response for a valid integer 
    
    num_exercises = validateInput("Please enter the number of excercises you plan to do (Must be greater than or equal to one):      ")
    print("\n\n\n")


    #   Loop cycles through the number of exercises and asks for workout type, weight, sets, and repetitions for each set
    count = 0
    set_counter = 0
    while count < num_exercises:
        print(f"EXCERCISE #{(count + 1)}")
        RowedDashes()
        print("\n")
        num_sets = validateInput("Please enter the amount of sets you wish to perform for this exercise:   ")
        print("\n\n\n\n\n\n")
        
        while set_counter < num_sets:
            num_reps = validateInput()
            rep_weight = validateInput()
            set_counter += 1

        count += 1



