def heapify(nums, heap, root):
    largest = root
    left = (2 * root) + 1
    right = (2 * root) + 2
    if left < heap and nums[left] > nums[largest]:
        largest = left
    if right < heap and nums[right] > nums[largest]:
        largest = right
    if largest != root:
        nums[root], nums[largest] = nums[largest], nums[root]
        heapify(nums, heap, largest)

def heap_sort(nums):
    n = len(nums)
    for i in range(n, -1, -1):
        heapify(nums, n, i)
    for i in range(n - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)

def test1():
    random_nums = [46, 18, 1, 35, 26]
    heap_sort(random_nums)
    print('Пирамидальная сортировка')
    print(random_nums)

def merge(left_list, right_list):
    sorted = []
    left_index = right_index = 0
    left_length, right_length = len(left_list), len(right_list)
    for _ in range(left_length + right_length):
        if left_index < left_length and right_index < right_length:
            if left_list[left_index] <= right_list[right_index]:
                sorted.append(left_list[left_index])
                left_index += 1
            else:
                sorted.append(right_list[right_index])
                right_index += 1
        elif left_index == left_length:
            sorted.append(right_list[right_index])
            right_index += 1
        elif right_index == right_length:
            sorted.append(left_list[left_index])
            left_index += 1
    return sorted

def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left_list = merge_sort(nums[:mid])
    right_list = merge_sort(nums[mid:])
    return merge(left_list, right_list)

def test2():
    random_nums = [64, 83, 50, 168, 5]
    random_nums = merge_sort(random_nums)
    print('Сортировка слиянием')
    print(random_nums)

test1()
test2()