def filter_by_state(data_logs: list[dict], state:str="EXECUTED") -> list:

    """Функция распределения по спискам"""

    new_list = []
    new_list_2 = []
    for i in data_logs:
        if i.get('state') == 'EXECUTED':
            new_list.append(i)
        else:
            new_list_2.append(i)
    return new_list, new_list_2

if __name__=='__main__':
    list1,list2 = filter_by_state([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}])
    print(list1)
    print(list2)


def sort_by_data(data_logs:list[dict],reverse:bool=True) -> list[dict]:

    """Функция сортировки по дате"""

    return sorted(data_logs, key=lambda x: x['date'],reverse=reverse)

print(sort_by_data([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]))