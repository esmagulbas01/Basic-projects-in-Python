character=input("Enter a character: ")
if(len(character) != 1):
    print("Please! Enter A character")
else:
    if(character.isalpha()):
        if(character.isupper()):
            case="upperletter"
        else:
            case="lowerletter"

        vowels="AEIOUaeıou"
        if(character in vowels):
            letter_type="vowels"
        else:
            letter_type="consonant"
        print(f"This {character} is a {letter_type} {case}")
    else:
        print("This character is not a letter")
        
