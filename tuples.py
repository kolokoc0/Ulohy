def create_intervals(data):
    nums = sorted(data)
    if nums:
        temp = (nums[0],nums[0])
    else:
        return []
    intervals = []
    for i in range(1,len(nums)):
        if nums[i]!=nums[i-1]+1:
            intervals.append(temp)
            temp = (nums[i],nums[i])

        elif nums[i] == nums[i-1]+1:
            temp = (temp[0],nums[i])

    if nums[len(nums)-1] == temp[0]:
        temp = (temp[0],temp[0])

    intervals.append(temp)
    return intervals


