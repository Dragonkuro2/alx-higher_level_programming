#!/usr/bin/python3
""" the module of the function text_identation. """


def text_indentation(text):
    """
    Print a text with 2 new lines after each of these characters: ., ? and :.

    Args:
        text (str): the text that we want to print.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for delimitre in ".:?":
        text = (delimitre + "\n\n").join(
            [line.strip(" ") for line in text.split(delimitre)])

    print(text, end="")
