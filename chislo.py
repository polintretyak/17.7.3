def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left

def sort_list(arr):
    return sorted(arr)

try:
    user_input = input("Введите последовательность чисел через пробел: ")
    numbers = list(map(int, user_input.split()))

    user_number = int(input("Введите любое число: "))

    sorted_numbers = sort_list(numbers)
    position = binary_search(sorted_numbers, user_number)

    if position == len(sorted_numbers):
        print("Нет чисел меньше введенного и больше или равного ему.")
    else:
        print("Позиция элемента в отсортированном списке:", position)
except ValueError:
    print("Ошибка ввода. Пожалуйста, введите числа в правильном формате.")
