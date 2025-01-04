class WordsFinder:
    file_names = []

    def __init__(self, file_name):
        self.file_name = file_name

    def get_all_words (self, all_words):
        all_words = {}
        with open(file_names) as file