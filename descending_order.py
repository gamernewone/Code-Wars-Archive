def descending_order(num):
    # This function sort a number in descending order
    # int -> int
    # Example: 123 -> 321
    # Example: 123456789 -> 987654321

    result = 0
    cheat = []
    for i in str(num):
        cheat.append(i)
    cheat.sort(reverse=True)
    for i in cheat:
        result = result * 10 + int(i)
    return result