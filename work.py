

test_num = input("Enter your ID number to check its validity: ")

#below are the calculations that is used to determine if the id is valid or not 

def add_odds(id_num):
    total = 0
    for ch in range(0, len(id_num[:-1]), 2):
        total += int(id_num[ch])
    return total


def multiply_evens(id_num):
    total = 0
    string = ""
    for ch in range(1, len(id_num),2):
        string += id_num[ch]
        total = int(string) * 2
    return total


def add_digits_from_multiply_evens(x):
    string = str(x)
    total = 0
    for ch in string:
        total += int(ch)
    return total


def add_second_to_first():
    first_func = add_odds(test_num)
    second_func = add_digits_from_multiply_evens(multiply_evens(test_num))
    answer = first_func + second_func
    return answer


def check_validity(id_num):
    x = add_second_to_first()
    usable_num = str(x)
    last_digit = int(usable_num[1])
    answer = str(10 - last_digit)

    if answer == id_num[-1]:
        return f"answer = {answer} - IS A VALID ID NUMBER"
    else:
        return f"answer = {answer} - IS NOT A VALID ID NUMBER"



print(f"This is the test number: {test_num}")
print("")
print(f"1. Add odds: {add_odds(test_num)}")
print(f"2. Multiply evens by 2: {multiply_evens(test_num)}")
print(f"3. Add individual digits from the prev result: {add_digits_from_multiply_evens(multiply_evens(test_num))}")
print(f"4. Return the sum of the 3rd Q and the 1st Q: {add_second_to_first()}")
print(f"5. Check validity: {check_validity(test_num)}")







