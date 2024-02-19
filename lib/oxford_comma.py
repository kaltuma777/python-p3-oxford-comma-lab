def oxford_comma(items):
    if len(items) == 1:
        return items[0]
    elif len(items) == 2:
        return ' and '.join(items)
    elif len(items) >= 3:
        formatted = ', '.join(items[:-1])
        return f"{formatted}, and {items[-1]}"

print(oxford_comma(['one','two','three','four']))
