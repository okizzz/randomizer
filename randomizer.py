#!/usr/bin/python3.6

from random import *


def load_unicode_table():
    table ={}
    with open('unicode.csv') as unicode:
        for line in unicode.readlines():
            line = line.replace("\n","")
            splitted = line.split(",")
            table[splitted[0]] = splitted


    return table

def randomize(text, table):
    openbrackets =0

    for letter  in text:
        if letter == '[':
            openbrackets+=1
        if letter == ']':
            openbrackets -= 1

        if openbrackets == 0:
            sub = ""
            if letter in table:
                while sub == "":
                    sub = choice(table[letter])
                yield sub
            else:
                yield letter
        else:
            yield letter


if __name__ == '__main__':
    for i in range(0,300):
        table = load_unicode_table()
        result = ""
        with open("input.txt") as input:
            text = input.read()

            for next_s in randomize(text,table):
                result+=next_s
            print(result)
