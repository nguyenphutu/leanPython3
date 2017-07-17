def abbreviated_pages(n, page):
    """
    Return a string containing the list of numbers from 1 to `n`, with
    `page` indicated, and abbreviated with ellipses if too long.

    >>> abbreviated_pages(5, 3)
    '1 2 [3] 4 5'
    >>> abbreviated_pages(10, 10)
    '1 2 3 4 5 6 7 8 9 [10]'
    >>> abbreviated_pages(20, 1)
    '[1] 2 3 ... 18 19 20'
    >>> abbreviated_pages(80, 30)
    '1 2 3 ... 28 29 [30] 31 32 ... 78 79 80'
    """
    assert(0 < n)
    assert(0 < page <= n)

    # Build set of pages to display
    if n <= 10:
        pages = set(range(1, n + 1))
    else:
        pages = (set(range(1, 4))
                 | set(range(max(1, page - 2), min(page + 3, n + 1)))
                 | set(range(n - 2, n + 1)))
    # Display pages in order with ellipses
    def display():
        last_page = 0
        print(pages)
        for p in sorted(pages):
            if p != last_page + 1: yield '...'
            yield ('[{0}]' if p == page else '{0}').format(p)
            last_page = p
    list_page = []
    for i in display():
        list_page.append(i)
    return list_page

print(abbreviated_pages(11, 11))

print()
