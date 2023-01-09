import copy
import json
import sys


def generate_inverted_index(text, existing_index, filename):
    inv_index = copy.deepcopy(existing_index) if existing_index else {}
    words = text.replace('\n', ' ').split(' ')
    for word in words:
        transformed_word = word.lower()
        if len(word) > 0:
            if transformed_word not in inv_index:
                inv_index[transformed_word] = []

            if filename not in inv_index[transformed_word]:
                inv_index[transformed_word].append(filename)

    return inv_index


def search_inverted_index(index, keyword):
    result = index[keyword] if keyword in index else []
    return result


if __name__ == "__main__":
    input_filenames = ['text1.txt', 'text2.txt', 'text3.txt']
    output_filename = 'resources/output/inverted_index.json'
    inverted_index_results = {}
    for filename in input_filenames:
        f = open('resources/input/' + filename, 'r')
        inverted_index_results = generate_inverted_index(f.read(), inverted_index_results, filename)
        f.close()

    output = open(output_filename, 'w')
    output.write(json.dumps(inverted_index_results, indent=4))
    output.close()

    try:
        index_file = open(output_filename, 'r')
    except:
        raise "Inverted index was not found!"

    index = json.loads(index_file.read())
    keywords = sys.argv[1:]
    for keyword in keywords:
        filenames = search_inverted_index(index, keyword)
        result = ', '.join(filenames)
        print(f'{keyword}: {result}')
