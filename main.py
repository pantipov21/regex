from pprint import pprint
import csv
import re


def get_email(source_str):
    return re.findall(r"[\w.]+@[\w.]+.ru", source_str, re.U)


def get_phone(source):
    phone_number = "+7"
    if len(source) > 0:
        if source[0] == '8':
            source.pop(0)
        else:
            source.pop(0)
            source.pop(0)

        phone_number += '('
        for i in range(0, 3):
            phone_number += source[0]
            source.pop(0)
        phone_number += ')'

        for i in range(0, 7):
            phone_number += source[0]
            source.pop(0)
            if i == 2 or i == 4:
                phone_number += '-'

        if len(source) > 0:
            phone_number += " доб."
            while len(source) > 0:
                phone_number += source[0]
                source.pop(0)
    return phone_number


if __name__ == '__main__':
    with open("phonebook_raw.csv") as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)

    # TODO 1: выполните пункты 1-3 ДЗ
    # ваш код
    contact_list_res = contacts_list.copy()

    for i in range(1, len(contacts_list)):
        result = ','.join(contacts_list[i])
        res = re.findall(r"[\w]+", result, re.U)
        contact_list_res[i][0] = res[0]
        contact_list_res[i][1] = res[1]
        contact_list_res[i][2] = res[2]
        contact_list_res[i][5] = get_phone(re.findall(r"[+\d]", result, re.U))

    for elem_i in contact_list_res:
        for elem_j in contact_list_res:
            if elem_i != elem_j and elem_i[0] == elem_j[0]:
                for i in range(0,7):
                    if len(elem_j[i]) > len(elem_i[i]):
                        elem_i[i] = elem_j[i]
                contact_list_res.remove(elem_j)
                break

    # TODO 2: сохраните получившиеся данные в другой файл
    # код для записи файла в формате CSV
    with open("phonebook.csv", "w") as f:
        datawriter = csv.writer(f, delimiter=',')
        # Вместо contacts_list подставьте свой список
        datawriter.writerows(contact_list_res)