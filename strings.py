

def main():
    phrase = "Giraffe Academy"
    print(phrase.upper().isupper())
    print(phrase.lower().islower())
    print(phrase[0])
    print(phrase[3])
    print(phrase.index("G"))
    print(phrase.index("a"))
    print(phrase.replace("Giraffe", "Elephant"))

if __name__ == "__main__":
    main()  