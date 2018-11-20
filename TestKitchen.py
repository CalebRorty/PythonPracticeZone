"""This is my playground Where I mess around with code to see if my ideas
work without creating a bunch of random code inside a project"""


def solve(st):
    st = st.split('(')
    print ( st )
    for i in st:
        try:
            intST = int(st[i])
            print (intST)
            st = st.remove(str(intST))
            print ( st )
        except:
            pass




print (solve('3(b(2(c)))'))