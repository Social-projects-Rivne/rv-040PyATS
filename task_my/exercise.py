def order(sentence):
    a = {}
    for i in sentence.split():
        for j in i:
            if j.isdigit():
                a[j] = i
    ll = []
    for key in sorted(a):
        ll.append(a[key])
    print(" ".join(ll))


if __name__ == "__main__":
    order('3a Thi1s 4Test i2s')
