import json
import sys


def generate_forward_index(text):
    fw_index = []
    words = text.replace('\n', ' ').split(' ')
    for word in words:
        transformed_word = word.lower()
        if transformed_word not in fw_index:
            fw_index.append(transformed_word)

    fw_index.sort()
    return fw_index


def search_forward_index(index, keyword):
    filenames = []
    for fname in index:
        if keyword in index[fname]:
            filenames.append(fname)
    return filenames


if __name__ == "__main__":
    input_filenames = ['text1.txt', 'text2.txt', 'text3.txt']
    output_filename = 'resources/output/forward_index.json'
    forward_index_results = {}
    for filename in input_filenames:
        f = open('resources/input/' + filename, 'r')
        forward_index_results[filename] = generate_forward_index(f.read())
        f.close()

    output = open(output_filename, 'w')
    output.write(json.dumps(forward_index_results, indent=4))
    output.close()

    try:
        index_file = open(output_filename, 'r')
    except:
        raise "Forward index was not found!"

    index = json.loads(index_file.read())
    keywords = sys.argv[1:]
    for keyword in keywords:
        filenames = search_forward_index(index, keyword)
        result = ', '.join(filenames)
        print(f'{keyword}: {result}')
