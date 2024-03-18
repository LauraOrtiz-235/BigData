from mrjob.job import MRJob
import time

class AverageLength(MRJob):
    def mapper(self, _, line):
        fields = line.split(";")
        tweet_text = fields[3].strip()  
        tweet_length = len(tweet_text)
        # Tupla con el largo del tweet y la cantidad de tweets
        # esto para en el reducer sumar el largo de los tweets 
        # y la cantidad de tweets para calcular el promedio
        yield("Tweets", (tweet_length, 1)) 

    def reducer(self, _, values):
        total_length = 0
        total_tweets = 0

        # Recorremos las tuplas del mapper
        for length, count in values:
            # Sumamos el largo del tweet y el total de tweets
            total_length += length
            total_tweets += count
        
        avg = total_length / total_tweets

        yield("Average tweet length", avg)

if __name__ == "__main__":
    AverageLength.run()