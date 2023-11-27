from email import generator
import random
import os
import shutil
from Script2 import create_dir
import csv

def get_element(dataset: str, class_name: str) -> generator:
    for file_name in os.listdir(os.path.join(dataset, class_name)):
        yield file_name

def create_randomname_file(dataset: str, annotation_name: str, dir_copy: str) -> None:
    file_number = list(range(10001))
    random.shuffle(file_number)
    counter = 1
    create_dir(dir_copy)
    for dataset_class in os.listdir(os.path.join(dataset)):
        for file_name in get_element(dataset, dataset_class):
            shutil.copy(os.path.join(os.path.join(dataset, dataset_class), file_name),
                        os.path.join(dir_copy, f"{file_number[counter]}.txt"))

            with open(os.path.join(dir_copy, annotation_name), mode="a", newline='') as file:
                file_writer = csv.writer(file, delimiter=",")
                file_writer.writerow([f"{file_number[counter]}.txt", dataset_class])
            counter += 1

def run3(dataset: str, annotation_name: str, dir_copy: str) -> None:
    create_randomname_file(dataset, annotation_name, dir_copy)