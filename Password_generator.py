"""根据用户输入的长度生成一个随机字符串密码。"""

import secrets
import string

# 各字符类别
LOWER = string.ascii_lowercase
UPPER = string.ascii_uppercase
DIGITS = string.digits
SYMBOLS = "!@#$%^&*()-_=+[]{};:,.?"
ALL_CHARS = LOWER + UPPER + DIGITS + SYMBOLS

MIN_LENGTH = 4  # 每类字符至少一个，所以最短为 4


def generate_password(length: int) -> str:
    """生成指定长度的随机密码，保证包含大小写字母、数字和符号各至少一个。"""
    if length < MIN_LENGTH:
        raise ValueError(f"密码长度至少为 {MIN_LENGTH}")

    # 先各取一个，保证复杂度
    chars = [
        secrets.choice(LOWER),
        secrets.choice(UPPER),
        secrets.choice(DIGITS),
        secrets.choice(SYMBOLS),
    ]
    # 剩余位数随机填充
    chars += [secrets.choice(ALL_CHARS) for _ in range(length - MIN_LENGTH)]

    # 打乱顺序，避免前四位类别固定
    secrets.SystemRandom().shuffle(chars)
    return "".join(chars)


def read_length() -> int:
    """读取并校验用户输入的密码长度。"""
    while True:
        raw = input(f"请输入密码长度（不少于 {MIN_LENGTH}）：").strip()
        if not raw.isdigit():
            print("输入无效，请输入一个正整数。")
            continue
        length = int(raw)
        if length < MIN_LENGTH:
            print(f"长度太短，至少需要 {MIN_LENGTH} 位。")
            continue
        return length


def main() -> None:
    try:
        length = read_length()
    except (EOFError, KeyboardInterrupt):
        print("\n已取消。")
        return
    print("生成的密码：", generate_password(length))


if __name__ == "__main__":
    main()
