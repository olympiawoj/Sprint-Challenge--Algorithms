'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.


1. Understand

Function count should
- Receive a word
- Count how many occurrences of 'th' occur within word
- Do not loop
- Use recursion
- We're looping over every two letters of a string to determine if it's th or not


Maybe use the the find method? It returns an integer which is the index of the beginning of the substring 

Edge cases
If the found is negative, that means it has not been found in this section of the word

'''


def count_th(word, count=0):
    print('count', count)

    # found is the index where we find the two letters, i.e. 0 for the first

    found = word.find('th', 0, len(word))
    print('found', found)
    if found < 0:
        print('found is less than 0')
        return count

    else:
        # Recurse the function, calling count_th
        # slicing word to make the 0 index at the index of found +2 - this make sure we do  not take into account first two letters found

        return count_th(word[found+2:], count + 1)


print(count_th("abcthefthghith"))
