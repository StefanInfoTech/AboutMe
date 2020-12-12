# AboutMe

### My name is Stefan Tomovski and I've created this page to tell you a bit about me.

#### Personal Life

I moved to **Columbia, MO** my sophmore year of highschool and attended *Rockbridge Highschool*. I played lacrosse my sophomore and junior year. I applied to [*Mizzou*](https://missouri.edu/) and got accepted my senior year. I wasn't sure what I wanted to do so I decided to try out Information Technology. So far ive enjoyed the abstract concepts and plan to stick with the major.

#### Interests

My freetime is spent:
* Playing Video Games
* Golfing
* Running
* Lifting
* Going for walks
* Watching Movies

#### Video Games

Since the pandemic has been going on since March most of my freetime has been spent playing video games

<img src ="https://upload.wikimedia.org/wikipedia/en/5/51/Minecraft_cover.png" height="460" width="460"> <img src ="https://cdn.cloudflare.steamstatic.com/steam/apps/271590/header.jpg?t=1592866696" height="460" width="460"> ![Mojang](https://github.com/mojang.png)

#### Code

The best code ive ever written was:

`'''
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
`
It handles exceptions and reprompts you to the question if you don't enter valid input.
