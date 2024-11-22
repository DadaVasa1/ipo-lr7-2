import json
with open('dump.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
numberQualification = input("Введи значение x:")
qualification = {}
speciality = {}
for college in data:
     if "fields" in college:
        if "code" in college["fields"]:
            if numberQualification == college["fields"]["code"]:
                speciality.update({"code": college["fields"]["code"]})
                speciality.update({"title": college["fields"]["title"]})
                speciality.update({"c_type": college["fields"]["c_type"]})
                continue
            if numberQualification in college["fields"]["code"]:
                qualification.update({college["fields"]["code"]: college["fields"]["title"]})


if len(speciality) > 0:
    print("=============== Найдено ===============")
    print(f"{speciality["code"]} >> Специальность {speciality["title"]}, {speciality["c_type"]}")
    for key in qualification:
        print(f'{key} >> Квалификация {qualification[key]}')
else:
    print("=============== Не найдено ===============")

