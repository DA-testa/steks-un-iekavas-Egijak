# python3
# Egija Kokoreviča
'''L.'''

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    '''L.'''
    return (left + right) in ["()", "[]", "{}"]

def find_mismatch(text):
    '''l.'''

    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(next, i+1))
            # Process opening bracket, write your code here

        if next in ")]}":
            if not opening_brackets_stack or not are_matching(opening_brackets_stack[-1].char,next):
                return(i+1)

            opening_brackets_stack.pop()

    if not opening_brackets_stack:
        return "Success"
    else:
        return opening_brackets_stack[-1].position
        # Process closing bracket, write your code here

def main():
    '''Printing answer'''

    ievade = input("Ievdi F vai I:")
    if ievade == 'F':
        # filepath = input("Ievadi faila celu:")
        text = input()
        with open (text) as fp:
            text = fp.read()
            mismatch = find_mismatch(text)
            print(mismatch)

    elif ievade == 'I':
            text = input()
            mismatch = find_mismatch(text)
            print(mismatch)
    # Printing answer, write your code here


if __name__ == "__main__":
    main()
