# Databricks notebook source
# MAGIC %md
# MAGIC Silver Notebook

# COMMAND ----------

# MAGIC %md
# MAGIC  Read nocs folder

# COMMAND ----------

df = spark.read.format("csv")\
               .option("header", "true")\
               .option("inferSchema", "true")\
                .load("abfss://bronze@olympicsadls.dfs.core.windows.net/nocs/")
                

# COMMAND ----------

df.display()

# COMMAND ----------

df=df.drop("country_long").display()

# COMMAND ----------

from pyspark.sql.functions import*
from pyspark.sql.types import *

# COMMAND ----------

df = spark.read.format("csv")\
               .option("header", "true")\
               .option("inferSchema", "true")\
                .load("abfss://bronze@olympicsadls.dfs.core.windows.net/nocs/")
                

df = df.withColumn('tag', split(col('tag'), '-')[0])
df.display()

# COMMAND ----------

df.write.format("delta")\
    .mode("append")\
    .option("path","abfss://silver@olympicsadls.dfs.core.windows.net/nocs/")\
    .saveAsTable("olympics_catalog.silver_sch.nocs")

# COMMAND ----------

df.write.format("delta")\
        .mode("append")\
        .saveAsTable("olympics_catalog.silver_sch.nocs_managed")