#ransom note assignment 2

def create(mag,ransom):
    for ch in mag:
        if ch not in mag or ch not in ransom:
            return True
        else:
            return False

def main():
    magazine = input('Enter text: ')
    ransom_note = input('Enter note: ')

    d_magazine = create(magazine,ransom_note)
    print(d_magazine)


main()
