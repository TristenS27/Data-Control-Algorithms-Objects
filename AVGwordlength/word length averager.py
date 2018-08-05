def if_low_count(my_string): #function to determine if there are white spaces as a 1st iteration
    low_count = 0
    high_count = 0
    for i in my_string:
        if i: #if a letter at all
            break
        else:
            while not i: #if a whitespace
                low_count += 1
    if low_count >= 1:
        high_count = low_count - (low_count - 1) #forces high_count to always be 1
        return high_count
    elif low_count == 0:
        return high_count
#--------------------------------------------------------
def if_space(my_string): #function to determine if there are multiple spaces in between words
    subcount = 0
    count = 0
    for i in my_string:
            if i == " ":
                subcount += 1
                if subcount == 1:
                    count += 1
                else:
                    subcount += 1
            else:
                subcount = 0
    if count == 0: #strict conditional
        count += 1
        return count
    elif count == 1: #strict conditional
        count += 1
        return count
    elif count >= 2: #elastic conditional for every other scenario
        i = my_string[0]
        if i == " ":
            return count
        else:
            count += 1
            return count
#--------------------------------------------------------
def average_word_length(my_string):
    letter = 0
    special = "!?$%,@#&"
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    try:
        for i in my_string:
            if i in alphabet or i in alphabet.upper():
                letter += 1
            if i in special:
                letter += 0
        if letter == 0:
            return "No words"
        if_new_count = if_low_count(my_string) #calls the function 1
        new_count = if_space(my_string) #calls the function 2
        result = letter / (new_count - if_new_count) #result may vary based on func 1 and func 2
        return result
    except:
        return "Not a string"
#--------------------------------------------------------
#When your function works, the following code should
#output:
#2.0
#3.0
#4.0
#Not a string
#No words
#4.0
#3.333333333
#--------------------------------------------------------
print(average_word_length("Hi"))
print(average_word_length("Hi, Lucy"))
print(average_word_length("   What   big spaces  you    have!"))
print(average_word_length(True))
print(average_word_length("?!?!?! ... !"))
print(average_word_length("Four words are here!"))
print(average_word_length("VAbThJ iha  Xs mPz oJG  cCD"))