

def test1(nums, target):
    record = {}
    for i in range(len(nums)):
        complent = target - nums[i]
        if complent in list(record.keys()):
            a = (i,record[complent])
            return a
        record[nums[i]] = i
    return (0,0)


if __name__ == '__main__':
    print(test1([2,7,7,9], 9))