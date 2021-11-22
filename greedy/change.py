def main(money: int):
    coins = [500, 100, 50, 10]
    total = 0

    for coin in coins:
        total += money // coin
        money = money % coin
        if money == 0:
            break
    
    return total

if __name__ == "__main__":
    assert main(1260) == 6 
