# 3.5---Assignment-8-Microservice-Implementation-Milestone-2-spierb
weather recommendations microservice
This README provides instructions to send dictionary objects to weather_service.py and recieve dictionary objects from weather_serrvice.py

1. Create a txt file named weather_service_in.txt as a pipeline to send dictionary objects to weather_service.py.
2. Create a txt file named weather_service_out.txt as a pipeline to recieve dictionary objects from weather_service.py.
3. to send an object to weather_service.py use.
        weather_service_file = open('weather_service_in.txt', 'w')
        weather_service_file.write('{"temperature": 75,"description": "Sunny" )
        weather_service_file.close()
        a. the object does not need to be the one listed above.
        b. for description key accepted values are { "sunny", "rainy", "snowy"}
        c. for temperature key any whole number value as a string is accepted.
4. to recieve an object to weather_service.py use. 
        weather_service_file = open('weather_service_out.txt', 'r')
        weather_obj = weather_service_file.read()
        weather_service_file.close()
        with open("weather_service_out.txt", "w") as in_file:
            in_file.truncate(0)
5. data from the weather_service.py is stored in the weather_obj variable as a dictionary object.

Weather Microservice UML

![weather_microservice_uml_diagram](https://user-images.githubusercontent.com/75771767/236983683-60ee9ab0-7930-443b-95ce-ab55dbbbda2f.png)
