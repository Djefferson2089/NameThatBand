def show_banner():
    banner = r'''
       _   _                   _______ _           _   ____                  _ 
      | \ | |                 |__   __| |         | | |  _ \                | |
      |  \| | __ _ _ __ ___   ___| |  | |__   __ _| |_| |_) | __ _ _ __   __| |
      | . ` |/ _` | '_ ` _ \ / _ \ |  | '_ \ / _` | __|  _ < / _` | '_ \ / _` |
      | |\  | (_| | | | | | |  __/ |  | | | | (_| | |_| |_) | (_| | | | | (_| |
      |_| \_|\__,_|_| |_| |_|\___|_|  |_| |_|\__,_|\__|____/ \__,_|_| |_|\__,_|

                               NameThatBand v1.0
                  Generate legendary band names in seconds!

                 https://github.com/Djefferson2089/namethatband
    '''
    print(banner)


if __name__ == "__main__":
    show_banner()
    usr_city = input("What city did you grow up in? ")
    usr_pet = input("What is the name of a pet of yours? ")
    print("Your band name is the following: " + usr_city + " " + usr_pet)
