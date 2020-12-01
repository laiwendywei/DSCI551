from pyspark.sql import SparkSession, functions
from pyspark.sql.functions import struct
from pyspark.sql.functions import to_date, col, month,concat
from pyspark.sql.functions import *
import json
from pyspark.sql.types import IntegerType
import collections

sparker = SparkSession.builder.getOrCreate()
#sparker.conf.set("spark.sql.execution.arrow.enabled", "true")
d = sparker.read.option("header","true").csv('us-counties.csv')
d = d.withColumn("area",concat(col("county"),lit(','),col("state")))
d = d.withColumn("cases", d["cases"].cast(IntegerType()))
adjustedDf = d.withColumn('month', month("date"))

covid_month = adjustedDf.groupBy(['area','month']).agg((functions.max('cases')-functions.min('cases')).alias('casecnt')).orderBy(['month','area'])
#pd = covid_month.toPandas()
#pd.to_csv("finalcovid.csv")
#i=0
covid_dict = collections.defaultdict(list)
for row in covid_month.collect():
    county = row[0].split(',')[0]
    state = row[0].split(',')[1]
    date = row[1]
    num_cases = row[2]
    area = county+','+state
    if area not in covid_dict:
        covid_dict[area] = [[date,num_cases]]
    else:
        covid_dict[area].append([date,num_cases])

with open('data_covid.json', 'w') as outfile:
    json.dump(covid_dict, outfile)

