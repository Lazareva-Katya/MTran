def test1(nums):
    for i in range(len(nums)):
        lowest_value_index = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[lowest_value_index]:
                lowest_value_index = j
        nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]
    print('Сортировка выборкой')
    print(nums)

def test2():
    fib1 = fib2 = 1
    n = 10
    print(fib1, fib2, end=' ')
    for i in range(2, n):
        fib1, fib2 = fib2, fib1 + fib2
        print(fib2, end=' ')

def test3(nums):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True
    print('Сортировка пузырьком')
    print(nums)

def main_activity():
    num = int(input())
    if num == 1:
        random_list_of_nums = [12, 8, 3, 20, 11]
        test1(random_list_of_nums)
    elif num == 2:
        print('Нахождение n-го числа Фибоначчи')
        test2()
    elif num == 3:
        random_list_of_nums = [5, 2, 1, 8, 4]
        test3(random_list_of_nums)
    else:
        print('Ошибка! Неверное число!')

main_activity()