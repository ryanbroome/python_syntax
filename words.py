words = ['one', 'two', 'three']


def print_upper_words(words):
    for word in words:
        # if word.startswith("e") or word[0] == "E": # just playing around different stuff, [0] is how i did it first
            print(word.upper())



def print_upper_words3(words, must_start_with):
    # """accepts an array of words and returns a capitalized version using for loop and upper()""
    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())
                break
    
    
print_upper_words3(["hello", "hey", "goodbye", "yo", "yes"],
                   must_start_with={"h", "y"})

