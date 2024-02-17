import requests

API_KEY = "6f99bb19092a4545759ea78b2649fb9f"


def get_data(place, days=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]

    # 8 - число наблюдений за 1 день (каждые 3 часа) согласно АПИ.
    # Мы это делам что бы показывать не все данные за 5 дней сразу, а столько сколько выбрано пользователем
    number_values = 8 * days
    filtered_data = filtered_data[:number_values]

    return filtered_data


if __name__ == "__main__":
    print(get_data(place="Tokyo", days=1))
