import os
import shutil

folder = input("Enter folder path: ")

if os.path.exists(folder):

    for file in os.listdir(folder):

        file_path = os.path.join(folder, file)

        if os.path.isfile(file_path):

            extension = file.split(".")[-1].lower()

            if "." not in file:
                extension = "Others"

            new_folder = os.path.join(folder, extension)

            if not os.path.exists(new_folder):
                os.mkdir(new_folder)

            shutil.move(
                file_path,
                os.path.join(new_folder, file)
            )

    print("Files organized successfully!")

else:
    print("Folder does not exist!")