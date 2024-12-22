def data_to_file():
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
    

    count = 0
    while count < num_exercises:
        pass



