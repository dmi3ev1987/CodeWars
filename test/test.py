import csv
import re


categories_example = {}

tags_example = {}


with open("categories_example.csv", "r") as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        if row[0] == "slug":
            continue
        categories_example[row[0]] = row[2]


with open("tags_example.csv", "r") as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        if row[0] == "slug":
            continue
        tags_example[row[0]] = row[2]


def get_slugs(categories_example, tags_example):
    result = {}
    for category in categories_example:
        slugs = []
        for tag in tags_example:
            pattern = category.split("-")
            string = tags_example[tag].lower()

            if len(pattern) == 1:
                if re.search(pattern[0], string):
                    slugs.append(tag)
            else:
                if re.search(pattern[0], string) or re.search(pattern[1], string):
                    slugs.append(tag)
        result[category] = slugs
    return result


print(get_slugs(categories_example, tags_example))
