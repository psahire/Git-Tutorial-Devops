started = False
while True:
    inputval = input("> ").lower()
    if inputval == "start":
        if started:
            print("Car Already Started")
        else:
            started = True
            print("Car Started")
    elif inputval == "stop":
        if not started:
            print("Car already stopped")
        else:
            started = False
            print("Car Stopped")
    elif inputval == "quit":
        print("Exiting")
        break
    elif inputval == "help":
        print("""
start - star the car
stop  - stop the car
help  - to list the car commands
        """)
    else:
        print("Invalid Command")