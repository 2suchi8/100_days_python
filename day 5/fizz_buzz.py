#if number divisible by 3 print Fizz
#if number divisible by 5 print Buzz
#if number divisible by 3 and 5 print FizzBuzz
for num in range(1,101):
    if(num%3==0 and num%5==0):
        print("FizzBuzz")
    elif(num%5==0):
        print("Buzz")
    elif(num%3==0):
        print("Fizz")
    else:
        print(num)