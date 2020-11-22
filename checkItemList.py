def chkElement(k):
    t = list(range(2,5))
    for i in t:
        if i == k:
            print("found")
        else:
            print("not found")

n = int(input("Enter the number"))
chkElement(n)