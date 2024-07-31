import os


def generate_folder_structure(root_dir, output_file):
    with open(output_file, "w") as file:
        for dirpath, dirnames, filenames in os.walk(root_dir):
            # Ignore the .git directory
            dirnames[:] = [d for d in dirnames if d != ".git"]

            level = dirpath.replace(root_dir, "").count(os.sep)
            indent = " " * 4 * level
            file.write("{}{}/\n".format(indent, os.path.basename(dirpath)))
            sub_indent = " " * 4 * (level + 1)
            for f in filenames:
                file.write("{}{}\n".format(sub_indent, f))


if __name__ == "__main__":
    root_directory = "D:/shared-code/tothemoon-claimer"
    output_file_path = "D:/shared-code/tothemoon-claimer/README.md"
    generate_folder_structure(root_directory, output_file_path)
