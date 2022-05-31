#Takes a word or phrase and checks if it's a palindrome

def is_palindrome(text: str):

    #String padronizing
    text = text.lower()
    text = text.replace(" ","")

    #Reversing string using list slicing
    reverse = text[::-1]

    if text == reverse:
        return True

    return False