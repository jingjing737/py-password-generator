#!/usr/bin/env python3
"""
py-password-generator — 安全密码生成器
支持：自定义长度、字符集、密码强度评估
"""
import argparse
import random
import string
import secrets
import hashlib


def generate_password(length: int = 16,
                     use_upper: bool = True,
                     use_lower: bool = True,
                     use_digits: bool = True,
                     use_special: bool = True,
                     exclude_chars: str = "",
                     no_ambiguous: bool = False) -> str:
    """生成安全密码"""

    ambiguous = "l1IoO0"
    if no_ambiguous:
        exclude_chars += ambiguous

    chars = ""
    if use_lower:
        chars += string.ascii_lowercase
    if use_upper:
        chars += string.ascii_uppercase
    if use_digits:
        chars += string.digits
    if use_special:
        chars += string.punctuation

    if not chars:
        chars = string.ascii_letters + string.digits

    # 移除排除的字符
    for c in exclude_chars:
        chars = chars.replace(c, "")

    # 使用 secrets 生成密码（密码学安全）
    password = ''.join(secrets.choice(chars) for _ in range(length))

    # 确保包含所有选中的字符类型
    if use_lower and not any(c in string.ascii_lowercase for c in password):
        password = password[:-1] + secrets.choice(string.ascii_lowercase)
    if use_upper and not any(c in string.ascii_uppercase for c in password):
        password = password[:-1] + secrets.choice(string.ascii_uppercase)
    if use_digits and not any(c in string.digits for c in password):
        password = password[:-1] + secrets.choice(string.digits)
    if use_special and not any(c in string.punctuation for c in password):
        password = password[:-1] + secrets.choice(string.punctuation)

    return password


def check_strength(password: str) -> dict:
    """评估密码强度"""
    score = 0
    feedback = []

    length = len(password)
    if length >= 8:
        score += 1
    if length >= 12:
        score += 1
    if length >= 16:
        score += 1

    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)

    type_count = sum([has_lower, has_upper, has_digit, has_special])
    if type_count >= 3:
        score += 1
    if type_count == 4:
        score += 1

    # 检查常见模式
    common = ["password", "123456", "qwerty", "admin", "letmein"]
    if any(p in password.lower() for p in common):
        score = max(0, score - 2)
        feedback.append("❌ 包含常见密码模式")

    # Entropy 计算
    pool_size = 0
    if has_lower:
        pool_size += 26
    if has_upper:
        pool_size += 26
    if has_digit:
        pool_size += 10
    if has_special:
        pool_size += 32
    entropy = length * (pool_size.bit_length() - 1) if pool_size else 0

    level = ["非常弱", "弱", "一般", "强", "非常强"][min(score, 4)]

    return {
        "score": score,
        "level": level,
        "entropy": entropy,
        "feedback": feedback
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="安全密码生成器")
    parser.add_argument("-l", "--length", type=int, default=16, help="密码长度")
    parser.add_argument("-u", "--no-upper", action="store_true", help="不含大写字母")
    parser.add_argument("-L", "--no-lower", action="store_true", help="不含小写字母")
    parser.add_argument("-d", "--no-digits", action="store_true", help="不含数字")
    parser.add_argument("-s", "--no-special", action="store_true", help="不含特殊字符")
    parser.add_argument("-a", "--no-ambiguous", action="store_true", help="排除易混淆字符(l1IoO0)")
    parser.add_argument("-c", "--count", type=int, default=1, help="生成数量")
    parser.add_argument("--check", metavar="PASSWORD", help="检查密码强度")
    args = parser.parse_args()

    if args.check:
        result = check_strength(args.check)
        print(f"\n密码: {args.check}")
        print(f"强度: {result['level']} (得分: {result['score']}/6)")
        print(f"熵值: {result['entropy']} bits")
        if result["feedback"]:
            for fb in result["feedback"]:
                print(fb)
    else:
        for i in range(args.count):
            pwd = generate_password(
                args.length,
                use_upper=not args.no_upper,
                use_lower=not args.no_lower,
                use_digits=not args.no_digits,
                use_special=not args.no_special,
                no_ambiguous=args.no_ambiguous
            )
            print(pwd)