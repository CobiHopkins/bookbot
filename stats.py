def get_word_count(data):
    words = data.split()
    return len(words)

def get_char_count(data):
    data = data.lower()
    char_dict = {}
    for char in data:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    
    return char_dict

def dict_to_sorted_list(data):
    sorted_list = [{k: v} for k, v in data.items()]
    sorted_list.sort(key=lambda x: list(x.values())[0], reverse=True)
    
    return sorted_list