import os
from typing import Optional


def get_next_element(class_mark: str, current_path: str = "dataset") -> Optional[str]:
    """This function returns gradually elements of class"""
    path = os.path.join(current_path, class_mark)
    names_list = os.listdir(path)
    names_list.append(None)
    for item in names_list:
        yield os.path.join(path, item) if item is not None else None

