#!/usr/local/bin/python3
# -*- coding: utf-8 -*-


def read_file(filename):
    """
    reads a file and returns its content as text

    :param filename: name of the file to read
    :return: file's content as a string, if the file exists and could be red,
             None, otherwise
    """
    try:
        with open(filename, 'r', encoding='utf-8') as infile:
            file_content = infile.read()
    except Exception as e:
        print(e)
        file_content = None

    return file_content


def write_file(filename, content):
    """
    creates a new file with the given content, interpreted as text

    :param filename: name of the file including path information
    :param content:  the file's content
    :return: True, if the file was created and filled with the content successfully
             False, otherwise
    """

    try:
        with open(filename, 'w', encoding='utf-8') as outfile:
            outfile.write(content)
        return True
    except Exception as e:
        print(e)

    return False