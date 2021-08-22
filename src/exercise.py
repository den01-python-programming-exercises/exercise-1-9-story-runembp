def main():
    #write your code below this line
    print("I will tell you a story, but I need some information first.")
    mainCharacter = input("What is the main character called?")
    mainCharJob = input("What is their job?")

    print("Here is the story:")
    print("Once upon a time there was " + mainCharacter + ", who was " + mainCharJob + ".")
    print("On the way to work, " + mainCharacter + " reflected on life.");
    print("Perhaps " + mainCharacter + " will not be " + mainCharJob + " forever.")

if __name__ == '__main__':
    main()
