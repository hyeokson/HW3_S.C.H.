def reverse_words(str):
    str2=str.split()
    str2.reverse()
    return " ".join(str2).strip()
    

def main():
    str1="""Two roads diverged in a yellow wood, And sorry I could not travel both And
be one traveler, long I stood And looked down one as far as I could To where
it bent in the undergrowth;"""
    str2="""Then took the other, as just as fair, And having perhaps the better claim,
Because it was grassy and wanted wear; Though as for that the passing there
Had worn them really about the same,"""
    
    print("Input String 1: {0:s}\n".format(str1))
    print("Reversed String 1: {0:s}\n".format(reverse_words(str1)))
    
    print("Input String 2: {0:s}\n".format(str2))
    print("Reversed String 2: {0:s}\n".format(reverse_words(str2)))



if __name__ == '__main__':
    main()
