from mrjob.job import MRJob, MRStep
import re
import os

WORD_REGEX = re.compile(r"\b\w+\b")

class InvertedIndex(MRJob):
    def mapper(self, _, line):
        # Obtener la ruta del archivo actual
        file = os.environ['map_input_file']
        file_name = os.path.basename(file)
        words = WORD_REGEX.findall(line)

        for word in words:
            if len(word) > 10:
                yield (word.lower(), file_name)

    def reducer(self, word, file_names):
        # Contar la cantidad de libros 
        num_books = len(set(file_names))
        # Palabras que aparezcan en el 80% de los libros
        percentage = 0.8 * num_books   
        if num_books >= percentage:  
            yield None, (num_books, word)

    def reducer_top(self, _, word_count):
        # Obtener las 20 palabras más comunes entre los libros
        top20 = sorted(word_count, reverse=True)[:20]
        for count, word in top20:
            yield (word, f'Books: {count}')

    def steps(self):
        return [
            MRStep(mapper=self.mapper, reducer=self.reducer),
            MRStep(reducer=self.reducer_top)
        ]

if __name__ == "__main__":
    InvertedIndex.run()

