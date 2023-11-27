import os
import csv

def create_csv_annotation(class_name: str, annotation_name: str) -> None:
    """This function generates a CSV annotation by taking three inputs: the absolute file path, the relative file path, the file's class name."""
    path_to_class = os.path.join('dataset')
    class_names = os.listdir(path_to_class)
    with open(annotation_name, mode="w", newline='') as file:
        file_writer = csv.writer(file, delimiter=",")
        for name in class_names:
            file_writer.writerow(
                [os.path.abspath(name), os.path.join(path_to_class, name), class_name])

def run1(class_name: str, annotation_name: str) -> None:
    create_csv_annotation(class_name, annotation_name)