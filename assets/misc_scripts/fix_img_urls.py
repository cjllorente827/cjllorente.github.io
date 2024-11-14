import os, re




file_path = os.path.abspath("assets/images/cats/water_tribe")

def main():
    #add_leading_zeros()
    make_sequential()


# ensures that all images are numbered from 0 - # of images
# assumes that file names have been named with leading zeros
# up to 4 digits
def make_sequential():

    pattern = re.compile("[0-9]+")

    i = 0
    for img in os.listdir(file_path):

        if img[-4:] != ".jpg":
            continue
        match = pattern.search(img)

        number = match.group()

        split_name = img.split(number)

        new_file_name = f"{split_name[0]}{i:04d}{split_name[1]}"

        old_path = os.path.join(file_path, img)
        new_path = os.path.join(file_path, new_file_name)
        os.rename(old_path, new_path)
        if img != new_file_name:
            print(f"Moved {img} to {new_file_name}")
        i+=1

# Changes image filenames in the given directory to express
# numbers with leading zeros up to 4 digits
def add_leading_zeros():
    pattern = re.compile("[0-9]+")

    for img in os.listdir(file_path):

        if img[-4:] != ".jpg":
            continue
        match = pattern.search(img)

        number = match.group()

        split_name = img.split(number)

        new_file_name = f"{split_name[0]}{int(number):04d}{split_name[1]}"

        old_path = os.path.join(file_path, img)
        new_path = os.path.join(file_path, new_file_name)
        os.rename(old_path, new_path)
        print(f"Moved {img} to {new_file_name}")


if __name__ == "__main__":
    main()