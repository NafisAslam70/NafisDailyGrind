
from sys import stdin

def countBracketReversals(inputString):
    st = []

    if len(inputString) % 2 != 0:
        return -1

    for e in inputString:
        if e == '{':
            st.append(e)
        else:  # if e == '}'
            if st and st[-1] == '{':
                st.pop()  # cancel out valid pair
            else:
                st.append(e)

    # Now stack has only unbalanced brackets
    open_brackets = 0
    close_brackets = 0

    while st:
        top = st.pop()
        if top == '{':
            open_brackets += 1
        else:
            close_brackets += 1

    # Total operations = ceil(open/2) + ceil(close/2)
    ans = (open_brackets + 1) // 2 + (close_brackets + 1) // 2
    return ans



#main
print(countBracketReversals(stdin.readline().strip()))
