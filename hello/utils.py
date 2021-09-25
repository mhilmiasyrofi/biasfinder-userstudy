import pandas as pd
import string


def is_placeholder(token):
    #     print(token)
    return token[0] == "<" and token[-1] == ">"


def is_punctuation(token):
    return token == "'s" or token in string.punctuation

df = pd.read_csv("./notebook/gender-unlabelled.csv")


def get_template(id):
    return df.iloc[int(id)]["template"]

def get_original_text(id):
    return format_text(df.iloc[int(id)]["original_text"], get_template(id))

def get_mutated_text(id):
    return format_text(df.iloc[int(id)]["mutated_text"], get_template(id))

def format_text(text, template):
    left_mark = "<span style='background-color: #FFFF00'>"
    right_mark = "</span>"

    i = 0
    j = 0

    text = text.split()
    template = template.split()

    fmt_text = []

    while j < len(template):
        if is_placeholder(template[j]):
            fmt_text.append(left_mark)

            fmt_text.append(text[i])
            i += 1
            j += 1
            next_token = template[j]
            while is_punctuation(next_token):
                j += 1
                next_token = template[j]

            while i < len(text) and text[i] != next_token:
                fmt_text.append(text[i])
                i += 1
            fmt_text.append(right_mark)
        else:
            fmt_text.append(text[i])
            i += 1
            j += 1

    return " ".join(fmt_text)

