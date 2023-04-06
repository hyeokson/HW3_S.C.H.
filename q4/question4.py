def factorial(num):
    if(num==0):
        return 1
    else:
        return num*factorial(num-1)


def main():
    for i in range(0, 16, 2):
        print("{0:d}! = {1:d}".format(i, factorial(i)))

if __name__ == '__main__':
    main()
