def bubble_sort(nums):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums), 1):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    return nums
