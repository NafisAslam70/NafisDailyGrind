class Solution(object):
    def evalRPN(self, tokens):
        st = []
        opr = "+-*/"

        for e in tokens:
            if e not in opr:
                st.append(int(e))  # Convert to int immediately
            else:
                f = st.pop()
                s = st.pop()
                if e == '+':
                    r = s + f
                elif e == '-':
                    r = s - f
                elif e == '*':
                    r = s * f
                elif e == '/':
                    r = int(float(s) / f)  # ✅ correct division
                st.append(r)

        return st[-1]

