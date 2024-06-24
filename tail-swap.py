def tail_swap(strings):
    begin, end = strings[0].split(':')
    begin2, end2 = strings[1].split(':')
    return [begin + ':' + end2, begin2 + ':' + end]


print(tail_swap(["abc:123", "cde:456"]))
print(tail_swap(["a:12345", "777:xyz"]))