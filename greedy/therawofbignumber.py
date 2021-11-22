def main(nmk: str, number: str):
    n, m, k = map(int, nmk.split(" "))
    number = list(map(int, number.split(" ")))
    number.sort(reverse=True)
    number = number[:2]
    
    result = (number[0] * k + number[1]) * (m // (k + 1)) + number[0] * (m % (k + 1))

    return result



if __name__ == "__main__":
    assert main("5 8 3", "2 4 5 4 6") == 46