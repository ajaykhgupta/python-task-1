list_1 = [
    {"id": "1", "name": "Shrey", "age": 25},
    {"id": "3", "age": 10, "name": "Hello"},
    {"id": "2", "name": "World", "age": 24},
]

list_2 = [
    {"id": "1", "marks": 100},
    {
        "id": "3",
        "marks": 90,
        "roll_no": 11,
        "extra_info": {
            "hello": "world",
        },
    },
]


def merge_lists(list_1, list_2) -> list:
    """
    Complete this function, by merging the information from list_1 and list_2
    to create a new list, which has all the information about each student from
    both lists in one single dict.

    - Both lists are unsorted
    - Both lists can have missing values (for ex list_2 has missing id=2)
    """
    merged = []
    merged.extend(list_1)
    list_1.extend(list_2)
    set_of_id = set()
    for d1 in list_1:
        for d2 in list_2:
            if d1.get("id") not in set_of_id and d1.get("id") == d2.get("id"):
                # if the id is not present in set_of_id and both the id of d1 and d2 matches
                set_of_id.add(d1.get("id"))
                d1.update(d2)
                if d1 not in merged:
                    merged.append(d1)
                break
    return merged


list_3 = merge_lists(list_1, list_2)
print(list_3)
