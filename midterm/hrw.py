'''
Port this below Golang SortByWeight() function into Python.
see@ https://godoc.org/github.com/codahale/hrw
No need to port TopN() function.
'''

def sort_by_weight(nodes=[], key=None):
    '''
    TODO: Implements Highest Random Weight hashing and returns the given 
    list of nodes sorted in decreasing order of their weight for the given key.
    see@ https://github.com/codahale/hrw/blob/master/hrw.go#L20
    Feel free to use any Python hash function.
    '''
    after = {}

    for i in nodes:
        key = hash(i)
        after[key] = i

    sor = sorted(after.keys(), reverse = True)

    res = []
    for i in sor:
        res.append(after[i])
    return res


def test():
    nodes = [
        "one.example.com",
        "two.example.com",
        "three.example.com",
        "four.example.com",
        "five.example.com",
        "six.example.com"
    ]
    sorted_nodes = sort_by_weight(nodes, '/items/123')
    print(sorted_nodes)


if __name__ == "__main__":
    test()