# itp

## Brianna

**Power**

I had a few different iterations for this one. My main train of thought was to define the two main functions, then call them in one main for loop. The for loop was a bit difficult for me to figure out. I looked back on our class notes in the section called "passing passing arguments into function calls" and saw that the base and exponent were defined in that function, so that is what I tried first. Then I tried to call the previous functions in a print.
Here is my first attempt:

def print_graph(n):
    print('*' * n)

def get_power(x, n):
    return x ** n

for i in range(8, -9):
    power = get_power(i, 2)
    print(print_graph(power))

The "print(print_graph(power))" section should first look at the parenthesis "power", and multiply x by the base 2. Then it should finish the "print_graph" function to print "*", multiplied by the range value in the for loop. I think.

This simply did not return anything. I thought I was missing a return, but I was using a for loop instead of another def function. I re-read the instructions, and realized I forgot to add the extra "print()" line at the end. So that brought me here:

def print_graph(n):
    print("*" * n)

def get_power(x, n):
    return x ** n

for i in range(-8, 9):
    power = get_power(i, 2)
    print(print_graph(power))
print()

This was SUPER close to what you wanted. It prints this:

****************************************************************
None
*************************************************
None
************************************
None
*************************
None
****************
None
*********
None
****
None
*
None

None
*
None
****
None
*********
None
****************
None
*************************
None
************************************
None
*************************************************
None
****************************************************************
None

This was a big head scratcher for me. I spent a LOT of time re-reading the notes from class. when comparing my prints with the ones in the "functions with for loops" section, mine were "tabbed" over, the ones from the notes were not. I figured that this had something to do with it. Any other prints that I saw that were tabbed over in a function always had "" on the inside of the parenthesis. Then I looked a bit farther up, and saw that the earlier def functions did not need to be called in a print function. So I tried this next:

def print_graph(n):
    print("*" * n)

def get_power(x, n):
    return x ** n

for i in range(-8, 9):
    power = get_power(i, 2)
    print_graph(power)
print()

I took the out the extra "print()" that I had, and this fixed my problem. I realize that it is unnecessary to call that function in a print function, because the operations will happen on their own since I already defined what I wanted the function to do. Yay!
