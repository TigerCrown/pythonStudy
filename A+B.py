raw_input = input() # "1 2"
raw_input = raw_input.split() #["1", "2"]
a = raw_input[0] #"1"
b = raw_input[1] #"2"

a = int(a)
b = int(b)

print(a + b)