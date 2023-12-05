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

    pattern = re.compile(r'(' + '|'.join(words_to_numbers.keys()) + r')')
    
    return re.sub(pattern, lambda x: words_to_numbers[x.group()], s)

sum = 0
for input in inputs:
    input_nums = re.findall(r'\d', convert_to_numbers(input))
    num = input_nums[0]+input_nums[-1]
    print(input + " : " + convert_to_numbers(input) + " : " + num)
    sum += int(num)
print(sum)