# itp

## Brianna

**Python Pyramid**

This was SO HARD for me for some reason, I think I had 25 different attempts at this before getting it. I started with the code you gave us on your GitHub page:

for i in range(10):
  for j in range(10):
    if j >= i:
      print(j, end='')
  print()

And changed the numbers/letters accordingly. Here I also added in the input from the user, to get to here:

stacks = int(input("Give me a number between 1 and 8: "))
for i in range(stacks):
  for j in range(8):
    if j <= i:
      print("#", end='')
  print()

This seemed like a good starting point, at least I had the hashes and the user input for the number of stacks.

The next thing I tried was changing the > sign to a < sign. That just flipped the pyramid on its head. I knew i would need to add in a print function to add space to the beginning of the lines. The first iteration I had was this:

stacks = int(input("Give me a number between 1 and 8: "))

for i in range(stacks):
  for j in range(8):
    if j >= i:
      while (stacks > 0):
        stacks = stacks - 1
        print(" " * stacks, '#')   

This did add the spaces in front, but no longer put the hashes there. Big head scratcher hahahaha. I tried adding this to the last print function

print(" " * stacks, "#" * stacks)

It actually just printed a bunch of space on the terminal. I also tried just adding another print funtion after the last one in the chain. Like this:

for i in range(stacks):
  for j in range(8):
    if j >= i:
      while (stacks > 0):
        stacks = stacks - 1
        print(" " * stacks)   
        print('#')

This also did not work at all, so I scrapped it. After this I tried to alter the other iteration in some minor ways, moving around > or < signs, swapping "i"s and "j"s. None of these got the result. I knew I was missing something big. I read the md document for the pyramid a bit closer, and saw that you said something about nesting loops, and saw that they were "for" loops. I scrapped my while loop and tried it as more "for" loops. Like this:

for i in range(stacks):
    for j in range(stacks - 1):
      print(' ', end='')
    for k in range(i + 1):
        print ('#', end='')
    print()

This moved the pyramid to the left, but did not change the way it leaned. I tried moving around a bunch of other numbers, addition signs, subtraction signs, etc. None of them worked. I was stumped at this stage for a couple of days. I looked back on the original code with the numbers counting down. The relationship between i and j was still kind of confusing. I realized that my "for j in range" function was missing the "i" in the nested loop. I tried to replace the "stacks" first. Like this:

for i in range(stacks):
    for j in range(i - 1):
      print(' ', end='')
    for k in range(i + 1):
        print ('#', end='')
    print()

This got me a bit closer, still leaning to the left though. After some more contemplation, it seemed logical that I would need to keep "stacks" in the range, considering that I need the user input number to dertermine how many times the space (" ") needs to occur. So I added it like this:

for i in range(stacks):
    for j in range(stacks - i):
      print(' ', end='')
    for k in range(i + 1):
        print ('#', end='')
    print()

This worked!!! My brain hurts now.

**FizzBuzz Write Up**

Thankfully, this was not nearly as difficult as the pyramid python script.

I started with your code from class:

for index in range(1500, 2701, 1):
  if index % 7 == 0 and index % 5 == 0:
    print(index)

From here, I played around with the numbers in the range to get a little more understanding of each one. I then decided to use my own numbers. Like this:

for index in range(1, 100):
    print(index)

Just to get the terminal to show the range asked for in the assignment. Then I added the modulus that we needed:

for index in range(1, 100):
  if index % 3 == 0 and index % 5 == 0:

And added the print function associated:

for index in range(1, 100):
  if index % 3 == 0 and index % 5 == 0:
      print("fizzbuzz")

Here, it only printed fizzbuzz 6 numbers divisible by both 3 and 5. Then I added the other bits of the function:

for index in range(1, 100):
  if index % 3 == 0 and index % 5 == 0:
    print("fizzbuzz")
  elif index % 3 == 0:
    print("fizz")
  elif index % 5 == 0:
    print("buzz")

This way, it printed all of the numbers divisible by 3 and 5 seperately, and those divisible by both 3 and 5.
Now, I just needed to add in the last bit of the function:

for index in range(1, 100):
  if index % 3 == 0 and index % 5 == 0:
    print("fizzbuzz")
  elif index % 3 == 0:
    print("fizz")
  elif index % 5 == 0:
    print("buzz")
  else:
    print(index)

This now prints all of the numbers inbetween along with the correct words on the correct numbers! (I totally did not have to check on google to see all the numbers divisible by BOTH 3 and 5 just to check)
