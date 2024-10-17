import sys
import PIL
from PIL import Image
def main():
   try:
        if len(sys.argv) > 3:
            sys.exit("Too many command-line arguments")
        input = sys.argv[1]
        after = sys.argv[2]
        end = (".jpg",".jpeg",".png")
        if not input.lower().endswith(end) or not after.lower().endswith(end):
            sys.exit("Invalid input")
        list_input=[]
        for char in input:
            list_input.append(char)
        list_after = []
        for char in after:
            list_after.append(char)
        if list_input[-3:] != list_after[-3:]:
            sys.exit("Input and output have different extensions")
        picture = Image.open(input)
        shirt = Image.open("shirt.png")
        size = shirt.size
        width, height = size
        fitted_picture = PIL.ImageOps.fit(picture,( width, height))
        fitted_picture.paste(shirt,shirt)
        fitted_picture.save(after)

   except IndexError:
        sys.exit("too few command-line arguments")
   except FileNotFoundError:
        sys.exit("Input does not exist")




if __name__ == "__main__":
    main()
