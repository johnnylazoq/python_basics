def looks(is_male: bool , is_tall: bool) -> str:
        if is_male and is_tall:
            print("You are a    tall    male")
        elif is_male and not(is_tall):
            print("You are a short male ")
        elif not(is_male) and is_tall:
            print("You are not a male but you are tall")
        else:
            print("You are not a tall male")   

def main():
     looks(False, False)
    
    
    
           


if __name__ == "__main__":
    main()  