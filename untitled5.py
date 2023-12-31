# -*- coding: utf-8 -*-
"""Untitled5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/133Kf_pjDv5GnR77sE2EpuPBEH4N49RCr
"""

#read an entire text file
with open('filename.txt', 'r') as file:
    content = file.read()
    print(content)
#read the first n lines of a file
n = 5  # Change this to the desired number of lines
with open('filename.txt', 'r') as file:
    for _ in range(n):
        line = file.readline()
        if not line:
            break
        print(line, end='')

#read the last n lines of a file
n = 5  # Change this to the desired number of lines
with open('filename.txt', 'r') as file:
    for _ in range(n):
        line = file.readline()
        if not line:
            break
        print(line, end='')

#get the number of words in a text file
def count_words(filename):
    with open(filename, 'r') as file:
        content = file.read()
        words = content.split()
        return len(words)

filename = 'filename.txt'  # Replace with your file's name
word_count = count_words(filename)
print(f"Number of words: {word_count}")

#bonus:read the last n lines of a file
def read_last_n_lines(filename, n):
    with open(filename, 'r') as file:
        lines = file.readlines()
        last_n_lines = lines[-n:]
        for line in last_n_lines:
            print(line, end='')

filename = 'filename.txt'  # Replace with your file's name
n = 5  # Change this to the desired number of lines
read_last_n_lines(filename, n)