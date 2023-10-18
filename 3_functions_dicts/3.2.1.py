# не добавляйте кода вне функции
def update_dictionary(d, key, value):
    if key in d:
        d[key] += [value]
    else:
        d.setdefault(2 * key, []).append(value)

# не добавляйте кода вне функции