def sort():
    nums = [5,3,8,6,7,2]
    n = len(nums)

    for i in range(n):  # i is index value of the nums
        swapped = False
        for j in range(n-i-1):
            if nums[j]> nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                swapped = True
        if not swapped:
            break
        print(nums)
sort()