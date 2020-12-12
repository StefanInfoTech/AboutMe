'''
A sample program to calculate distance: distance = rate * time
to demonstrate exception handling.
This program asks the user if they want to continue and execute the program again
'''
def main():

    while True:

        bad_input = True

        #while bad_input is True the loop will continue to execute
        while bad_input:   
            try: 
                #ask user for input: distance and time
                rate = float(input("Enter the rate: "))
                time = float(input("Enter the time: "))

                #if the user enters a negative number go back to the beginning of the loop
                if rate < 0 or time < 0:
                    print("Values for rate and time must be 0 or greater.")
                    print("Please enter input again\n")
                    continue

                #calculate the distance
                distance = (rate * time)

                #print distance to use
                print("The distance is", distance)

                #Set bad_input to False if all previous code in the try block executes successfully
                #Setting bad_input to False will cause the while loop to end
                bad_input = False
            except Exception as error:
                print("The following error occured:", error)
                print("Please enter input again\n")

        do_again = input("Would you like the program to continue? Y/y: ")
        if do_again != "Y" or do_again != "y":
            print("Thank you & Goodbye")
            break


#call main to begin the program
main()
