def remove_short(names, min_len):
    for n in names:              
        if len(n) < min_len:
            names.remove(n)      
    return names


if __name__ == "__main__":
    data = ["A", "B", "Cat", "Do"]
    print(remove_short(data, 2))
