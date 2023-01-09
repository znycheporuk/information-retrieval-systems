import re

from lab2.common_elements import common


def generate_inverted_index(filenames, inv_index, file_titles):
    for filename in filenames:
        f = open('input/' + filename, 'r')
        text = f.read()
        f.close()

        file_titles[filename] = text.split("\n")[0]
        words = split_text(text)
        for word in words:
            print("w: " + word)
            if len(word) > 0:
                if word not in inv_index:
                    inv_index[word] = []

                if filename not in inv_index[word]:
                    inv_index[word].append(filename)


def split_text(text):
    return re.sub('[^a-z \']+', "", text.lower().replace('\n', ' ')).split(' ')


def search_inverted_index(index, keyword):
    result = index[keyword] if keyword in index else []
    return result


def search(index, query):
    result = []
    query_keywords = query.split(' ')

    for keyword in query_keywords:
        if keyword not in index:
            print("keyword %s was not found" % keyword)
            continue

        filenames = index[keyword]
        if len(result) == 0:
            result = filenames
            continue

        result = common(result, filenames)
    return result


def combine_in_summary(filenames, file_titles):
    summary = []
    for filename in filenames:
        summary.append({'filename': filename, 'file title': file_titles[filename]})
    return summary


def main():
    index = {}
    file_titles = {}
    filenames = ["text1.txt", "text2.txt", "text3.txt"]
    generate_inverted_index(filenames, index, file_titles)
    while True:
        user_input = input("Please enter keywords to search:\n")
        if len(user_input) < 1:
            break

        found_filenames = search(index, user_input)
        if len(found_filenames) > 0:
            summary = combine_in_summary(found_filenames, file_titles)
            print(summary)
        else:
            print("No filenames were found.")


main()
