print ('''
Here are the following comands:
              start - to start the car
              stop  - to stop the car
              quit  - to exit''')
command = ""
started = False
while True:
    command = input("Enter your command: ").lower()
    if command == "start":
        if started:
            print("Car already started!!")
        else:
            started = True
            print("Car has started...")
    elif command == "stop":
        if not started:
            print("Car already stoped!!")
        else:
            started = False
            print("Car has stopped.")
    elif command == "quit":
        print("You have quit the game")
        break
    else:
        print("Sorry I do not understand that!!")
