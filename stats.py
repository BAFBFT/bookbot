def count_words(book):
    word_list = book.split()
    word_count = len(word_list)

    return word_count

def count_characters(book):
    character_dict = {}
    for i in book: 
        if i.lower() in character_dict:
            character_dict[i.lower()] += 1
        else: 
            character_dict[i.lower()] = 1
    
    return character_dict

def sort_dict(character_dict):
    #characters array to store the dictionaries
    characters = []
    
    #append each dictionary to the characters array
    for key, value in character_dict.items():
        new_dict = {}
        new_dict["char"] = key
        new_dict["num"] = value
        characters.append(new_dict)
    
    #Sort with lambda function as the key, the comparison is made with 
    # the num value in the list of character arrays
    characters.sort(reverse=True, key=lambda character: character["num"])

    return characters


def print_report(characters, path_to_file, word_count):
    print("============ BOOKBOT ============ \nAnalyzing book found at {}...".format(path_to_file))

    print("----------- Word Count ----------\nFound {} total words\n--------- Character Count -------".format(word_count))

    for character in characters:
        if character["char"].isalpha():
            print("{}: {} \n".format(character["char"], character["num"]))
        else:
            pass

    print("============= END ===============")
    
    return