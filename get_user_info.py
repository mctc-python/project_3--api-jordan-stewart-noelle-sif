def main():
    get_user_info()

def get_user_info():
    user_name = input('What is your name, wonderer?: ')

    user_sign = input('Please tell me your zodiac sign: ')

    return user_name, user_sign

if __name__ == '__main__':
    main()