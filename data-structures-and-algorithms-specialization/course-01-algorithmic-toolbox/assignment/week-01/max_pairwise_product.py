# python3

def max_pairwise_product(numbers):
    maxelem = -1
    maxelem2 = -1

    for num in numbers:
        if num >= maxelem:
            maxelem2 = maxelem
            maxelem = num
        elif num > maxelem2:
            maxelem2 = num
    return maxelem * maxelem2

if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
