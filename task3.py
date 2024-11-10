for i in range(int(input()), int(input())+1):
    print('Fizz Buzz' if i %3==0 and i%5==0 else 'fizz' if i%3==0 else 'Buzz' if i%5==0 else i)  