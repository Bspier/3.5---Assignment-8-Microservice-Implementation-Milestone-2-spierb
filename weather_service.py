import json


weather_rec_dict = {
    "70": {
        "sunny": {
            "clothing": "Shorts and t-shirt",
            "activity": "Go for a walk in the park or have a picnic",
            "food": "Grilled hamburgers or hot dogs",
            "accessories": "Sunblock or hat"
        },
        "rainy": {
            "clothing": "Pants and raincoat",
            "activity": "Read a book or watch a movie",
            "food": "Hot soup",
            "accessories": "Umbrella"
        }
    },
    "35": {
        "sunny": {
            "clothing": "Pants and t-shirt",
            "activity": "Go for a walk in the park or have a picnic",
            "food": "Grilled hamburgers or hot dogs",
            "accessories": "Sunblock, hat and sweater"
        },
        "rainy": {
            "clothing": "Pants and raincoat",
            "activity": "Read a book or watch a movie",
            "food": "Hot soup",
            "accessories": "Umbrella"
        },
        "snowy": {
            "clothing": "Winter coat, gloves and boots",
            "activity": "Build a snowman or ski",
            "food": "Hot soup or hot cocoa",
            "accessories": "Beanie, sunglasses"
        }
    },
    "0": {
        "sunny": {
            "clothing": "Pants and jacket",
            "activity": "Go for a walk in the park or ice skate",
            "food": "Grilled hamburgers or hot dogs",
            "accessories": "Sunblock and hat"
        },
        "rainy": {
            "clothing": "Pants and raincoat",
            "activity": "Read a book or watch a movie",
            "food": "Hot soup",
            "accessories": "Umbrella"
        },
        "snowy": {
            "clothing": "Winter coat, gloves and boots",
            "activity": "Build a snowman or ski",
            "food": "Hot soup or hot cocoa",
            "accessories": "Beanie, sunglasses"
        }
    }
}

while True:
    with open("weather_service_in.txt", "r") as in_file:
        data_str = in_file.read()

    data = json.loads(data_str)
    if data is not None:
        weather = data["description"]
        temp = int(data["temperature"])

    if temp >= 70:
        if weather == "Sunny":
            weather_rec = weather_rec_dict["70"]["sunny"]
        else:
            weather_rec = weather_rec_dict["70"]["rainy"]

    elif temp >= 35:
        if weather == "Sunny":
            weather_rec = weather_rec_dict["35"]["sunny"]
        elif weather == "Rainy":
            weather_rec = weather_rec_dict["35"]["rainy"]
        else:
            weather_rec = weather_rec_dict["35"]["snowy"]
    else:
        if weather == "Sunny":
            weather_rec = weather_rec_dict["0"]["sunny"]
        elif weather == "Rainy":
            weather_rec = weather_rec_dict["0"]["rainy"]
        else:
            weather_rec = weather_rec_dict["0"]["snowy"]

    with open("weather_service_out.txt", "w") as out_file:
        json.dump(weather_rec, out_file)
    out_file.close()

    with open("weather_service_in.txt", "w") as in_file:
        in_file.truncate(0)
    break
