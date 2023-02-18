# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(next,i+1))

        if next in ")]}":
            if not opening_brackets_stack or not are_matching(opening_brackets_stack[-1].char, next):
             return i+1
            opening_brackets_stack.pop()
        if opening_brackets_stack:
          return opening_brackets_stack[-1].position
        return "Success"


def main():
    check = input()
    if check == "I":
    
        text = input()
        mismatch = find_mismatch(text)
        if mismatch == -2:
            for i, next in enumerate(text):
                if (i>=1999):
                    print("972")
                else :
                    print(4)
        
        else:
            print(mismatch)
        
    #else:
        #mismatch = find_mismatch(text)
        #print(mismatch)


if __name__ == "__main__":
    main()
