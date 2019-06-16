

def test1(nums, target):
    record = {}
    for i in range(len(nums)):
        complent = target - nums[i]
        if complent in list(record.keys()):
            a = (i,record[complent])
            return a
        record[nums[i]] = i
    return (0,0)


def test2(x):
    if x < 0:
        a = -x
    else:
        a = x

    li = []
    step = 1
    while (a > 10):
        li.append(int(a % 10))
        a = int(a / 10)
        step = step * 10
        li.append(a)
        s = 0
        for item in li:
            s = s + item * step
        step = step / 10
        if x < 0:
            return -s
    return s

def romanToInt(s: str) -> int:
    params = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    par = {
        'IV': 4,
        'IX': 9,
        'XL': 40,
        'XC': 90,
        'CD': 400,
        'CM': 900
    }
    sum1 = 0
    for i in range(len(s)):
        if s[i:i + 2] in list(par.keys()):
            sum1 = sum1 + par[s[i:i + 2]]
            i = i + 2
        else:
            sum1 = sum1 + params[s[i]]
    return sum1


def isValid( s: str) -> bool:
    if len(s) % 2 == 1:
        return False
    params = {
        '(': ')',
        '[': ']',
        '{': '}'
    }
    while (len(s) > 0):
        if not s[0] in params.keys():
            return False
        if params[s[0]] == s[-1]:
            s = s[1:-1]
        else:
            return False
    return True

def search(nums, target: int) -> int:
    l = 0
    r = len(nums)
    mid = int((r + l) / 2)
    while mid != 0 and mid != len(nums) - 1:
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l = mid
            mid = int((r + l) / 2)
        else:
            r = mid
            mid = int((r + l) / 2)
    return -1

if __name__ == '__main__':
    # print(test1([2,7,7,9], 9))
    # print(romanToInt('IV'))
    print(search([-1,0,3,4,5,9],9))