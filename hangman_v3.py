import random

def open_file(file):
    with open(file, "r") as p:
        all_words = p.read()
        all = all_words.lower().split()


        # lowered = all_words.lower()
        # splitted = lowered.splitlines
        # return splitted
        # words = all_words.split().lower()
        # return random.choice(words)


def play_game():
    word = open_file(file)
    print(word)
    #print('Your word is', len(word), 'letters long.')


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        play_game()
    else:
        print(f"{file} does not exist!")
        exit(1)
