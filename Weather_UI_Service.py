import time

while True:
    userInput = input("Enter 1 to obtain JSON weather object or 2 to quit: ")
    '''while userInput != 1 or userInput != 2:
        userInput = input("Invalid input. Enter 1 to obtain JSON weather object or 2 to quit: ")'''

    if userInput == '1':
        weather_service_file = open('weather_service_in.txt', 'w')
        weather_service_file.write('{"temperature": 75,"description": "Sunny",'
                                   '"humidity": 50,"wind_speed": 10}')
        weather_service_file.close()
        time.sleep(10)

        weather_service_file = open('weather_service_out.txt', 'r')
        weather_obj = weather_service_file.read()
        weather_service_file.close()
        print(weather_obj)

        with open("weather_service_out.txt", "w") as in_file:
            in_file.truncate(0)

    if userInput == '2':
        print("Good Bye")
        exit()
