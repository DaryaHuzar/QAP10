def reshape(numbers, width, length):
    assert len(numbers) == width * length, "Данные введены неверно"
    massive = iter([[] for _ in range(width)])
    current_list = next(massive)
    result_list = []
    for number in numbers:
        if len(current_list) < length:
            current_list.append(number)
        else:
            result_list.append(current_list)
            current_list = next(massive)
            current_list.append(number)
    result_list.append(current_list)
    return result_list


print(reshape([1, 2, 3, 4, 5, 6], 2, 3))
print(reshape([1, 2, 3, 4, 5, 6, 7, 8], 4, 2))
