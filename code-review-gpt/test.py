def bubble_sort(arr):
    """
    冒泡排序函数

    参数:
    arr (list): 需要排序的列表

    返回:
    list: 排序后的列表
    """

    # 获取列表的长度
    n = len(arr)

    # 外部循环控制需要比较的轮数，总共需要比较n-1轮
    for i in range(n - 1):
        # 内部循环控制每一轮的比较过程
        # 注意内部循环每一轮都会把最大的元素冒泡到最后
        for j in range(n - 1 - i):
            # 如果当前元素比下一个元素大，交换它们的位置
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

# 示例用法
if __name__ == "__main__":
    unsorted_list = [64, 34, 25, 12, 22, 11, 90]
    sorted_list = bubble_sort(unsorted_list)
    print("排序后的列表:", sorted_list)
def bubble_sort(arr):
    """
    冒泡排序函数

    参数:
    arr (list): 需要排序的列表

    返回:
    list: 排序后的列表
    """

    # 获取列表的长度
    n = len(arr)

    # 外部循环控制需要比较的轮数，总共需要比较n-1轮
    for i in range(n - 1):
        # 内部循环控制每一轮的比较过程
        # 注意内部循环每一轮都会把最大的元素冒泡到最后
        for j in range(n - 1 - i):
            # 如果当前元素比下一个元素大，交换它们的位置
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

# 示例用法
if __name__ == "__main__":
    unsorted_list = [64, 34, 25, 12, 22, 11, 90]
    sorted_list = bubble_sort(unsorted_list)
    print("排序后的列表:", sorted_list)
    print("test")
