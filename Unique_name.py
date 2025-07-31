def unique_names(names1, names2):
    uni_name = []
    for name in names1:
        if name not in uni_name:
            uni_name.append(name)
            for name2 in names2:
                if name2 != name and name2 not in uni_name:
                    uni_name.append(name2)
    return uni_name

if __name__ == "__main__":
    names1 = ["Ava", "Emma", "Olivia"]
    names2 = ["Olivia", "Sophia", "Emma"]
    print(unique_names(names1, names2)) # should print Ava, Emma, Olivia, Sophia

