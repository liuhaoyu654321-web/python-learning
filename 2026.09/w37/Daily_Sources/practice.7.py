numbers = [1, 2, 3, 4, 5, 6]
def count_numbers(numbers):
    count = 0
    odd_count = 0
    for number in numbers:
        if number%2 ==  0:
           count += 1
        else:
            odd_count += 1
    return count,odd_count
even_count,odd_count = count_numbers(numbers)
print("偶数：", even_count)
print("奇数：", odd_count)
        

            
