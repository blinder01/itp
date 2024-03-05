stacks = int(input("Give me a number between 1 and 8: "))

for i in range(stacks):
    for j in range(stacks - i):
      print(' ', end='')
    for k in range(i + 1):
        print ('#', end='')
    print()
