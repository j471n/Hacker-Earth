# Date : Oct 7, 2020 By Jatin Sharma

nu = list(input())
a = []
d = ""

DNA = ['G', 'C', 'T', 'A']
RNA = ['C', 'G', 'A', 'U']

for i in nu:
    if i in DNA:
        b = DNA.index(i)
        a = a + list(RNA[b])
        print(d.join(a))

    else:
        print("Invalid Input")
        break

