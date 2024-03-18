import pyspark
import re

WORD_REGEX = re.compile(r"\b\w+\b")
sc = pyspark.SparkContext()
lines = sc.textFile("input")
words = lines.flatMap(lambda l: l.split() )
result = words.map(lambda w: (w.lower(),1)).reduceByKey(lambda a,b: a+b)
result.saveAsTextFile("outpysparkcount")

inmem = result.persist()

inmem.filter(lambda pair: pair[0] == "summer").collect()

inmem.saveAsTextFile("out-labSpark")