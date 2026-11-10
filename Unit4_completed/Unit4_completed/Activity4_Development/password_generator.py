"""Secure command-line password generator."""
import secrets
import string

CHARACTER_GROUPS = {
    'lowercase': string.ascii_lowercase,
    'uppercase': string.ascii_uppercase,
    'digits': string.digits,
    'symbols': '!@#$%^&*()-_=+[]{}?',
}


def generate_password(length=16, lowercase=True, uppercase=True, digits=True, symbols=True):
    """Generate a random password with at least one of each selected group."""
    if isinstance(length, bool) or not isinstance(length, int):
        raise TypeError('Length must be an integer')
    if not 4 <= length <= 128:
        raise ValueError('Length must be between 4 and 128')
    enabled = [chars for flag, chars in zip((lowercase, uppercase, digits, symbols), CHARACTER_GROUPS.values()) if flag]
    if not enabled:
        raise ValueError('Select at least one character type')
    if length < len(enabled):
        raise ValueError('Length is too short for selected character types')
    password = [secrets.choice(chars) for chars in enabled]
    pool = ''.join(enabled)
    password.extend(secrets.choice(pool) for _ in range(length - len(password)))
    # Fisher-Yates shuffle with a cryptographically secure random source.
    for index in range(len(password) - 1, 0, -1):
        swap = secrets.randbelow(index + 1)
        password[index], password[swap] = password[swap], password[index]
    return ''.join(password)


def ask_yes_no(prompt):
    while True:
        answer = input(prompt).strip().lower()
        if answer in ('y', 'yes'):
            return True
        if answer in ('n', 'no'):
            return False
        print('Please enter y or n.')


def main():
    print('Secure Password Generator')
    while True:
        try:
            length = int(input('Password length (4-128): ').strip())
            options = [ask_yes_no(f'Include {name}? (y/n): ') for name in CHARACTER_GROUPS]
            password = generate_password(length, *options)
        except (ValueError, TypeError) as error:
            print(f'Invalid input: {error}. Please try again.')
            continue
        except (EOFError, KeyboardInterrupt):
            print('\nGoodbye.')
            return
        print(f'Generated password: {password}')
        if not ask_yes_no('Generate another? (y/n): '):
            print('Goodbye.')
            return


if __name__ == '__main__':
    main()
