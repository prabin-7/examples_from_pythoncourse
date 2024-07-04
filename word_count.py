def freq(string):
    words = []
    dict = {}

    words = string.lower().split()

    for key in words:
        dict[key] = words.count(key)

    print("the freq of words is",dict)

freq("Mary had a little lamb Little lamb, little lamb Mary had a little lamb.Its fleece was white as snow And everywhere that Mary went Mary went, Mary went \
Everywhere that Mary went The lamb was sure to go")