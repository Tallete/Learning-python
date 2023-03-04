import string 
def clean_text(text):
    special_chars = string.punctuation+"·"
    for letter in special_chars:
        text.replace(letter,"")
    return text

def only_words(text):
    # tomar solo aquellas que están formadas por letras, y las pasamos a minúscula.
    list = text.split(" ")
    only_words_letter = []
    alphabet = string.ascii_letters + "ñ"    # solo para el español  :)
    for word in list:
        for letter in word:
            if letter not in alphabet:
                break
        else:
            only_words_letter.append(word.lower())
    return only_words_letter

def count_word (list_word):
    counted_word = {}
    for word in list_word:
        if word in counted_word:
            counted_word[word] +=1
        else:
            counted_word[word] = 1
    return counted_word

   

text="Hola, me llamo Iñigo Montolla, tu mataste a mi padre preparate a morir! Hola, me llamo Iñigo Montolla, tu mataste a mi padre preparate a morir!!! Deja ya de decir eso !"


cleaned_text= clean_text(text)
list_word = only_words(cleaned_text)
counted_word = count_word(list_word)

print(counted_word)
