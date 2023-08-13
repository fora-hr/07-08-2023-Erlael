import json

def read_json(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

def read_results(filename):
    results = {}
    with open(filename, 'r', encoding='utf-8-sig') as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            # Проверяем, что строка не пустая
            if line:
                values = line.split(" ")
                number = values[0]
                time = values[2]
                results[number] = time
    return results

# Читаем данные о спортсменах
competitors = read_json("competitors2.json")

# Читаем результаты первой попытки
results = read_results("results_RUN.txt")

# Сортируем результаты по времени
sorted_results = sorted(results.items(), key=lambda x: x[1])

# Выводим результаты
print("Занятое место Нагрудный номер Имя Фамилия Результат")
for i, (number, time) in enumerate(sorted_results):
    athlete = competitors[number]
    full_name = "{} {}".format(athlete["Name"], athlete["Surname"])
    print("{} {} {} {} {}".format(i+1, number, athlete["Name"], athlete["Surname"], time))