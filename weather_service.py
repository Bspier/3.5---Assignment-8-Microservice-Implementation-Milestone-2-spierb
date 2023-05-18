import json

weather_rec_dict = {
    "95": {
        "clear sky": {
            "clothing": "Shorts and t-shirt",
            "activity": "Go for a walk in the park or have a picnic",
            "precautions": "Avoid prolonged sun exposure",
            "accessories": "Sunblock or hat"
        },
        "rain": {
            "clothing": "Shorts and t-shirt",
            "activity": "Read a book or watch a movie",
            "precautions": " ",
            "accessories": "Umbrella"
        },
        "clouds": {
            "clothing": "Shorts and t-shirt",
            "activity": "Read a book or watch a movie",
            "precautions": " ",
            "accessories": "Umbrella"
        },
        "thunderstorm": {
            "clothing": "Pants and raincoat",
            "activity": "Read a book or watch a movie",
            "precautions": " ",
            "accessories": "Umbrella"
        },
        "mist": {
            "clothing": "Pants and raincoat",
            "activity": "Read a book or watch a movie",
            "precautions": " ",
            "accessories": "Umbrella"
        },
        "poor air quality": {
            "clothing": "Shorts and t-shirt",
            "activity": "Read a book or watch a movie",
            "precautions": " ",
            "accessories": "Umbrella"
        },
        "snow": {
            "clothing": "Shorts and t-shirt",
            "activity": "Read a book or watch a movie",
            "precautions": " ",
            "accessories": "Umbrella"
        }
    },
    "85": {
        "clear sky": {
            "clothing": "Shorts and t-shirt",
            "activity": "Go for a walk in the park or have a picnic",
            "precautions": "Avoid prolonged sun exposure",
            "accessories": "Sunblock or hat"
        },
        "rain": {
            "clothing": "Shorts and t-shirt",
            "activity": "Read a book or watch a movie",
            "precautions": " ",
            "accessories": "Umbrella"
        },
        "clouds": {
            "clothing": "Shorts and t-shirt",
            "activity": "Read a book or watch a movie",
            "precautions": " ",
            "accessories": "Umbrella"
        },
        "thunderstorm": {
            "clothing": "Pants and raincoat",
            "activity": "Read a book or watch a movie",
            "precautions": " ",
            "accessories": "Umbrella"
        },
        "mist": {
            "clothing": "Pants and raincoat",
            "activity": "Read a book or watch a movie",
            "precautions": " ",
            "accessories": "Umbrella"
        },
        "poor air quality": {
            "clothing": "Shorts and t-shirt",
            "activity": "Read a book or watch a movie",
            "precautions": " ",
            "accessories": "Umbrella"
        },
        "snow": {
            "clothing": "Shorts and t-shirt",
            "activity": "Read a book or watch a movie",
            "precautions": " ",
            "accessories": "Umbrella"
        }
    },
    "70": {
        "clear sky": {
            "clothing": "Shorts and t-shirt",
            "activity": "Go for a walk in the park or have a picnic",
            "precautions": "Avoid prolonged sun exposure",
            "accessories": "Sunblock or hat"
        },
        "rain": {
            "clothing": "Shorts and t-shirt",
            "activity": "Read a book or watch a movie",
            "precautions": " ",
            "accessories": "Umbrella"
        },
        "clouds": {
            "clothing": "Shorts and t-shirt",
            "activity": "Read a book or watch a movie",
            "precautions": " ",
            "accessories": "Umbrella"
        },
        "thunderstorm": {
            "clothing": "Pants and raincoat",
            "activity": "Read a book or watch a movie",
            "precautions": " ",
            "accessories": "Umbrella"
        },
        "mist": {
            "clothing": "Pants and raincoat",
            "activity": "Read a book or watch a movie",
            "precautions": " ",
            "accessories": "Umbrella"
        },
        "poor air quality": {
            "clothing": "Shorts and t-shirt",
            "activity": "Read a book or watch a movie",
            "precautions": " ",
            "accessories": "Umbrella"
        },
        "snow": {
            "clothing": "Shorts and t-shirt",
            "activity": "Read a book or watch a movie",
            "precautions": " ",
            "accessories": "Umbrella"
        }
    },
    "50": {
        "clear sky": {
            "clothing": "Shorts and t-shirt",
            "activity": "Go for a walk in the park or have a picnic",
            "precautions": "Avoid prolonged sun exposure",
            "accessories": "Sunblock or hat"
        },
        "rain": {
            "clothing": "Shorts and t-shirt",
            "activity": "Read a book or watch a movie",
            "precautions": " ",
            "accessories": "Umbrella"
        },
        "clouds": {
            "clothing": "Shorts and t-shirt",
            "activity": "Read a book or watch a movie",
            "precautions": " ",
            "accessories": "Umbrella"
        },
        "thunderstorm": {
            "clothing": "Pants and raincoat",
            "activity": "Read a book or watch a movie",
            "precautions": " ",
            "accessories": "Umbrella"
        },
        "mist": {
            "clothing": "Pants and raincoat",
            "activity": "Read a book or watch a movie",
            "precautions": " ",
            "accessories": "Umbrella"
        },
        "poor air quality": {
            "clothing": "Shorts and t-shirt",
            "activity": "Read a book or watch a movie",
            "precautions": " ",
            "accessories": "Umbrella"
        },
        "snow": {
            "clothing": "Shorts and t-shirt",
            "activity": "Read a book or watch a movie",
            "precautions": " ",
            "accessories": "Umbrella"
        }
    },
    "30": {
        "clear sky": {
            "clothing": "Shorts and t-shirt",
            "activity": "Go for a walk in the park or have a picnic",
            "precautions": "Avoid prolonged sun exposure",
            "accessories": "Sunblock or hat"
        },
        "rain": {
            "clothing": "Shorts and t-shirt",
            "activity": "Read a book or watch a movie",
            "precautions": " ",
            "accessories": "Umbrella"
        },
        "clouds": {
            "clothing": "Shorts and t-shirt",
            "activity": "Read a book or watch a movie",
            "precautions": " ",
            "accessories": "Umbrella"
        },
        "thunderstorm": {
            "clothing": "Pants and raincoat",
            "activity": "Read a book or watch a movie",
            "precautions": " ",
            "accessories": "Umbrella"
        },
        "mist": {
            "clothing": "Pants and raincoat",
            "activity": "Read a book or watch a movie",
            "precautions": " ",
            "accessories": "Umbrella"
        },
        "poor air quality": {
            "clothing": "Shorts and t-shirt",
            "activity": "Read a book or watch a movie",
            "precautions": " ",
            "accessories": "Umbrella"
        },
        "snow": {
            "clothing": "Shorts and t-shirt",
            "activity": "Read a book or watch a movie",
            "precautions": " ",
            "accessories": "Umbrella"
        }
    },
    "10": {
        "clear sky": {
            "clothing": "Shorts and t-shirt",
            "activity": "Go for a walk in the park or have a picnic",
            "precautions": "Avoid prolonged sun exposure",
            "accessories": "Sunblock or hat"
        },
        "rain": {
            "clothing": "Shorts and t-shirt",
            "activity": "Read a book or watch a movie",
            "precautions": " ",
            "accessories": "Umbrella"
        },
        "clouds": {
            "clothing": "Shorts and t-shirt",
            "activity": "Read a book or watch a movie",
            "precautions": " ",
            "accessories": "Umbrella"
        },
        "thunderstorm": {
            "clothing": "Pants and raincoat",
            "activity": "Read a book or watch a movie",
            "precautions": " ",
            "accessories": "Umbrella"
        },
        "mist": {
            "clothing": "Pants and raincoat",
            "activity": "Read a book or watch a movie",
            "precautions": " ",
            "accessories": "Umbrella"
        },
        "poor air quality": {
            "clothing": "Shorts and t-shirt",
            "activity": "Read a book or watch a movie",
            "precautions": " ",
            "accessories": "Umbrella"
        },
        "snow": {
            "clothing": "Shorts and t-shirt",
            "activity": "Read a book or watch a movie",
            "precautions": " ",
            "accessories": "Umbrella"
        }
    },
    "0": {
        "clear sky": {
            "clothing": "Shorts and t-shirt",
            "activity": "Go for a walk in the park or have a picnic",
            "precautions": "Avoid prolonged sun exposure",
            "accessories": "Sunblock or hat"
        },
        "rain": {
            "clothing": "Shorts and t-shirt",
            "activity": "Read a book or watch a movie",
            "precautions": " ",
            "accessories": "Umbrella"
        },
        "clouds": {
            "clothing": "Shorts and t-shirt",
            "activity": "Read a book or watch a movie",
            "precautions": " ",
            "accessories": "Umbrella"
        },
        "thunderstorm": {
            "clothing": "Pants and raincoat",
            "activity": "Read a book or watch a movie",
            "precautions": " ",
            "accessories": "Umbrella"
        },
        "mist": {
            "clothing": "Pants and raincoat",
            "activity": "Read a book or watch a movie",
            "precautions": " ",
            "accessories": "Umbrella"
        },
        "poor air quality": {
            "clothing": "Shorts and t-shirt",
            "activity": "Read a book or watch a movie",
            "precautions": " ",
            "accessories": "Umbrella"
        },
        "snow": {
            "clothing": "Shorts and t-shirt",
            "activity": "Read a book or watch a movie",
            "precautions": " ",
            "accessories": "Umbrella"
        }
    },
}

while True:
    with open("weather_service_in.txt", "r") as in_file:
        data_str = in_file.read()

    data = json.loads(data_str)
    if data is not None:
        weather = data["description"]
        temp = int(data["temperature"])
        unit = (data["unit"])

    if unit == "c" or "C":
        temp = (temp * (9 / 5)) + 32

    if weather == {"smoke", "haze", "sand/dust whirls", "sand", "dust", "volcanic ash", "squalls", "tornado"}:
        weather = "poor air quality"

    if weather == {"overcast clouds", "few clouds", "scattered clouds", "broken clouds"}:
        weather = "clouds"

    if weather == "fog":
        weather = "mist"

    if weather == {"thunderstorm with light rain", "thunderstorm with rain", "thunderstorm with heavy rain",
                   "light thunderstorm", "thunderstorm", "heavy thunderstorm", "ragged thunderstorm",
                   "thunderstorm with light drizzle", "thunderstorm with drizzle", "thunderstorm with heavy drizzle"}:
        weather = "thunderstorm"

    if weather == {"light intensity drizzle", "drizzle", "heavy intensity drizzle", "light intensity drizzle rain",
                   "drizzle rain", "heavy intensity drizzle rain", "shower rain and drizzle",
                   "heavy shower rain and drizzle", "shower drizzle"}:
        weather = "rain"

    if weather == {"light rain", "moderate rain", "heavy intensity rain", "very heavy rain", "extreme rain",
                   "freezing rain", "light intensity shower rain", "shower rain", "heavy intensity shower rain",
                   "ragged shower rain"}:
        weather = "rain"

    if weather == {"light snow", "snow", "heavy snow", "sleet", "light shower sleet", "shower sleet",
                   "light rain and snow", "rain and snow", "light shower snow", "shower snow", "heavy shower snow"}:
        weather = "snow"

    if temp >= 95:
        weather_rec = weather_rec_dict["95"][weather]

    elif temp < 95 or temp >= 85:
        weather_rec = weather_rec_dict["85"][weather]

    elif temp < 85 or temp >= 70:
        weather_rec = weather_rec_dict["70"][weather]

    elif temp < 70 or temp >= 50:
        weather_rec = weather_rec_dict["50"][weather]

    elif temp < 50 or temp >= 30:
        weather_rec = weather_rec_dict["30"][weather]

    elif temp < 30 or temp >= 10:
        weather_rec = weather_rec_dict["10"][weather]

    else:
        weather_rec = weather_rec_dict["0"][weather]

    with open("weather_service_out.txt", "w") as out_file:
        json.dump(weather_rec, out_file)
    out_file.close()

    with open("weather_service_in.txt", "w") as in_file:
        in_file.truncate(0)
