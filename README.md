# py-password-generator 🔐

安全密码生成器，支持自定义字符集、强度评估。

## 快速开始

```bash
python3 password.py
```

## 用法

```bash
# 生成 16 位密码（默认）
python3 password.py

# 生成 20 位密码
python3 password.py -l 20

# 不含特殊字符
python3 password.py -s

# 生成 5 个密码
python3 password.py -c 5

# 排除易混淆字符
python3 password.py -a

# 检查密码强度
python3 password.py --check "MyP@ssw0rd!"
```

## 参数

| 参数 | 说明 | 默认 |
|------|------|------|
| `-l, --length` | 密码长度 | 16 |
| `-u, --no-upper` | 不含大写 | 否 |
| `-L, --no-lower` | 不含小写 | 否 |
| `-d, --no-digits` | 不含数字 | 否 |
| `-s, --no-special` | 不含特殊字符 | 否 |
| `-a, --no-ambiguous` | 排除易混淆字符 (l1IoO0) | 否 |
| `-c, --count` | 生成数量 | 1 |
| `--check` | 检查密码强度 | 无 |

## 特性

- ✅ 使用 `secrets` 模块（密码学安全随机）
- ✅ 强制包含所有选中的字符类型
- ✅ 密码强度评估（得分/熵值）
- ✅ 检测常见密码模式

## License

MIT