from mrjob.job import MRJob, MRStep
import time

class TweetActivity(MRJob):
    def mapper(self, _, line):
        fields = line.split(";")

        time_epoch = int(fields[0]) / 1000
        minute = time.strftime("%M", time.gmtime(time_epoch))
        yield(minute, 1)

    def combiner(self, minute, values):
        yield(minute, sum(values))

    def reducer(self, minute, values):
        total_tweets = sum(values)
        yield(None, (minute, total_tweets))

    def reducer_popular_minute(self, _, minute):
        # Buscar el minuto con más tweets
        max_minute, max_tweets = max(minute, key=lambda x: x[1])
        yield("The most popular minute is", max_minute)
        yield("Number of tweets", max_tweets)

    def steps(self):
        return [
            MRStep(mapper=self.mapper, combiner=self.combiner, reducer=self.reducer),
            MRStep(reducer=self.reducer_popular_minute)
        ]

if __name__ == "__main__":
    TweetActivity.run()
