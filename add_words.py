def write_unique_words(input_file_paths, output_file_path):
    try:
        unique_words = set()
        for input_file_path in input_file_paths:
            with open(input_file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                for line in lines:
                    words = line.strip().split()
                    for word in words:
                        cleaned_word = ''.join(char for char in word if char.isalnum()).lower()
                        if cleaned_word:
                            unique_words.add(cleaned_word)
        with open(output_file_path, 'w', encoding='utf-8') as file:
            for word in sorted(unique_words):
                file.write(word + '\n')
        print(f"The file has been successfully written to {output_file_path}")
    except FileNotFoundError:
        print(f"File {input_file_paths} not found")
    except Exception as e:
        print(f"An error has occurred:{e}")


input_file_paths = ['input.txt', '1600-words.txt']
output_file_path = 'words.txt'
write_unique_words(input_file_paths, output_file_path)