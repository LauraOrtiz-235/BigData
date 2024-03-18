import pyspark
import re

WORD_REGEX = re.compile(r"\b\w+\b")
sc = pyspark.SparkContext()

lines = sc.textFile("/data/gutenberg")
words = lines.flatMap(lambda l: WORD_REGEX.findall(l))
#words = lines.flatMap(lambda l: l.split() )

count = words.map(lambda w: (w.lower(),1)).reduceByKey(lambda a,b: a+b)

count.saveAsTextFile("outpysparkcount")
