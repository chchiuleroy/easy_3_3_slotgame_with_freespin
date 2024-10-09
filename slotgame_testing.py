import random
import os

# 定义符号及其对应的赔率
symbols = {
    '🍒': 2,
    '🍋': 3,
    '🔔': 5,
    '⭐': 10,
    '🍀': 8,
    '🍇': 4,
    '7️⃣': 50,
    '🍉': 9,
    '👑': 30,
    '🎰': 0  # Free Spin符号，赔率为0
}

def generate_slot_machine():
    return [[random.choice(list(symbols.keys())) for _ in range(3)] for _ in range(3)]

def print_slot_machine(machine):
    for row in machine:
        print(" | ".join(row))

def check_winning(machine):
    # 检查水平线
    for row in machine:
        if row[0] == row[1] == row[2] and row[0] != '🎰':  # 忽略Free Spin符号的水平中奖
            return row[0]

    # 检查对角线
    if machine[0][0] == machine[1][1] == machine[2][2] and machine[0][0] != '🎰':
        return machine[0][0]
    if machine[0][2] == machine[1][1] == machine[2][0] and machine[0][2] != '🎰':
        return machine[0][2]

    return None

def count_symbols(machine):
    symbol_count = {}
    for row in machine:
        for symbol in row:
            if symbol in symbol_count:
                symbol_count[symbol] += 1
            else:
                symbol_count[symbol] = 1
    return symbol_count

def calculate_payout(symbol):
    return symbols[symbol] * bet

def play_slot_machine():
    balance = int(input("请输入初始余额: "))  # 用户输入初始余额
    global bet
    bet = int(input("请输入每次投注金额: "))  # 用户输入每次投注金额
    free_spins = 0
    spins_count = 0  # 记录下注次数

    while True:
        if free_spins > 0:
            print(f"你有 {free_spins} 次免費旋轉機會。")
            free_spins -= 1
        else:
            print(f"当前余额: ${balance}")
            if balance < bet:
                choice = input("余额不足，是否要重新输入初始余额？(y/n): ").strip().lower()
                if choice == 'y':
                    balance = int(input("请输入初始余额: "))
                    continue
                else:
                    print("余额不足，游戏结束。再见！")
                    break

            input("按下空白鍵後開始遊戲...")
            balance -= bet

        spins_count += 1
        print(f"第 {spins_count} 次下注")

        os.system('cls' if os.name == 'nt' else 'clear')

        machine = generate_slot_machine()
        print_slot_machine(machine)

        winning_symbol = check_winning(machine)
        symbol_count = count_symbols(machine)

        for symbol, count in symbol_count.items():
            if symbol == '🎰' and count >= 4:
                free_spins += 5
                print(f"\n恭喜！{symbol} 出現了 {count} 次，你赢得了 5 次免費旋轉機會！\n")
                break

        if winning_symbol:
            payout = calculate_payout(winning_symbol)
            balance += payout
            print(f"\n恭喜！你贏了！你赢得了 ${payout}!\n")
        elif not any(count >= 5 and symbol == '🎰' for symbol, count in symbol_count.items()):
            print("\n很遺憾，你沒有中獎。\n")

        print(f"当前余额: ${balance}\n")

if __name__ == "__main__":
    play_slot_machine()
