import re
import inputs
#inputs.inputs = ["1abc2", "398878", "a1b2c3d4e5f", "treb7uchet"]

sum = 0
for input in inputs.inputs:
    input_nums = re.findall(r'\d', input)
    num = input_nums[0]+input_nums[-1]
    #print(num)
    sum += int(num)
print(sum)