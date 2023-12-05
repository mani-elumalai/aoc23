import re
import inputdata
#inputs = ["two1nine", "eightwothree", "abcone2threexyz", "xtwone3four", "4nineeightseven2", "zoneight234", "7pqrstsixteen"]
inputs = inputdata.inputs

def convert_to_numbers(s):
    words_to_numbers = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
        'zero': '0'
    }

    return s if s.isdigit() else words_to_numbers[s]

sum = 0
for input in inputs:
    input_nums = re.findall(r'(?=(one|two|three|four|five|six|seven|eight|nine|\d))', input)
    num = convert_to_numbers(input_nums[0]) + convert_to_numbers(input_nums[-1])
    print(input + " : " + ','.join(input_nums) + " : " + num)
    sum += int(num)
print(sum)