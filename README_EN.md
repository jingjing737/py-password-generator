# py-password-generator 🔐

Secure password generator with strength assessment.

## Quick Start

```bash
# Install dependencies
python3 -m pip install colorama

# Generate a password
python3 password.py

# Custom length and count
python3 password.py -l 16 -n 5

# Exclude ambiguous characters
python3 password.py --no-ambiguous
```

## Features

- Customizable length and count
- Character set options (upper, lower, digits, symbols)
- Strength assessment (weak/medium/strong)
- Copy to clipboard support

## License

MIT
