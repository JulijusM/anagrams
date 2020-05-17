import sys
import load_words
from collections import Counter


def find_anagrams(phrase, words_list):
    ''' find all (different length) anagrams in a phrase '''
    anagrams = []
    phrase_letters = Counter(phrase)
    for word in words_list:
        test = ''
        word_letters = Counter(word.lower())
        
        for letter in word_letters:
            if word_letters[letter] <= phrase_letters[letter]:
                test += letter
        if Counter(test) == word_letters:
            anagrams.append(word)

    print(*anagrams, sep='\n')
    print()
    print(f"Remaining letters = {phrase}") 
    print(f"Number of remaining letters = {len(phrase)}")
    print(f"Number of remaining (real world) anagrams = {len(anagrams)}\n")



def process_choice(name):
    '''check user choice for validity, return choice & leftover letters.'''
    while True:
        choice = input('\nMake a choice; else Enter to start over; or # to end:')
        if choice == '':
            main()
        elif choice == "#":
            sys.exit()
        else:
            candidate = "".join(choice.lower().split())

        left_over_list = list(name)
        for letter in candidate:
            if letter in left_over_list:
                left_over_list.remove(letter) 
                                                                # cia yra modifikuojamas left_over_list sarasas
        if len(name) - len(left_over_list) == len(candidate):   # todel cia jei name - modifikuotas(name) == kandidatas tada iseinam
            break                                               # nes viskas gerai.. taip ir turi buti. 
        else:
            print("Won't work! Make another choice!", file=sys.stderr)
    name = "".join(left_over_list) # makes display more readable
    return choice, name


def main():
    '''help user build anagram phrase from their name'''
    name = ''.join(init_name.lower().split())
    name = name.replace('-', '')
    limit = len(name)
    phrase = ''
    running = True

    while running:
        temp_phrase = phrase.replace(' ', '')

        if len(temp_phrase) < limit:
            print(f"Length of anagram phrase = {len(temp_phrase)}")
            find_anagrams(name, words)
            print(f"Currend anagram phrase = {phrase}", )
            choice, name =  process_choice(name)
            phrase += choice + ' '

        elif len(temp_phrase) == limit:
            print("\n*****FINISHED!!!******\n")
            print('Anagram of name = ', end='')
            print(phrase, file=sys.stderr)
            print()
            try_again = input("\n\nTry again? (press Enter else 'n' to quit)\n")

            if try_again.lower() == "n":
                running = False
                sys.exit()
            else:
                main()



# words_url = r'http://greenteapress.com/thinkpython2/code/words.txt' # 113.000 zodziu
words_url = r'https://inventwithpython.com/dictionary.txt'          # 45.000 words


words = load_words.get_words(words_url)
words.append('a')
words.append('i')

user_phrase = input(str('Please enter a word or a phrase and we will find an anagram of it: '))
user_phrase = user_phrase.lower()

init_name = user_phrase

if __name__ == '__main__':
    main()