import operator

ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv,  # use operator.div for Python 2
    '%' : operator.mod,
    '^' : operator.xor,
}
while True:
    answer = ops[operator](first_number, second_number)
    
    if ['exit'] == answer:
        print("answer")
        break
      
    if operator in ops.keys():
        print(answer)
        break
if ['exit'] == answer:
        print("answer")
       # break

first_number = float(input())
second_number = float(input())
operator = input()

if operator in ops.keys():
    answer = ops[operator](first_number, second_number)
    print(answer)
#    print(ops[operator])
    # print("here")


else:
    print("invalid operator")
    #break