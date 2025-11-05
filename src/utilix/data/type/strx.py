from collection import defaultdict


class Strx:
    def __init__(self, raw_str_input:str):
        self._raw_str_input:str = raw_str_input


    def get_key_counter(self, document:str)->None:
        words = document.split()
        word_counts = defaultdict(int)
        for word in words:
            word_counts[word] += 1