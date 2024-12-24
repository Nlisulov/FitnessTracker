def dataToFile():
    pass

def getDatabaseData():
    pass

def RowedStars():
    for x in range(100):
        print("*", end="")

def RowedDashes():
    for x in range(100):
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

   
    #   This loop stylizes the console terminal while also checking the response for a valid integer 
    valid_num = False
    while not valid_num:
        print("\n\n\n\n\nNote: Any numbers with a decimal point will have the floor function applied to it. \nFor Example: 2.7 ---> 2 and 3.4 ---> 3")
        RowedDashes()
        print("\n\n")
        num_exercises = input("Please enter the number of excercises you plan to do (Must be greater than or equal to one):      ")
        
        try:
            num_exercises = int(num_exercises)
            
            if num_exercises >= 1:
                valid_num = True
            else:
                RowedDashes()
                print("\n|REMINDER: Please enter in a integer >= 1|")
                RowedDashes()


        except ValueError:
            RowedDashes()
            print("\n|WARNING: Please enter in a integer|")
            RowedDashes()
    print("\n\n\n")


    #   Loop cycles through the number of exercises and asks for workout type, weight, sets, and repetitions for each set
    count = 0
    while count < num_exercises:
        valid_num = False
        print(f"EXCERCISE #{(count + 1)}")
        RowedDashes()
        print("\n")

        while not valid_num:
            num_sets = input("Please enter the amount of sets you wish to perform for this exercise:   ")
            try:
                num_sets = int(num_sets)
                
                if num_sets >= 1:
                    valid_num = True
                else:
                    RowedDashes()
                    print("\n|REMINDER: Please enter in a integer >= 1|")
                    RowedDashes()


            except ValueError:
                RowedDashes()
                print("\n|WARNING: Please enter in a integer|")
                RowedDashes()
            print("\n\n\n\n\n\n")
        
        
        count += 1



