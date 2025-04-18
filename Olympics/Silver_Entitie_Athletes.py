# Databricks notebook source
from pyspark.sql.functions import *
from pyspark.sql.types import*

# COMMAND ----------

df = spark.read.format("parquet").load("abfss://bronze@olympicsadls.dfs.core.windows.net/athletes")

# COMMAND ----------

display(df)

# COMMAND ----------

df_filter = df.filter((col('current')==True) & (col('name').isin('TAPIA VIDAL Rosa Maria','TOSCANO Pamela','RUBAIAWI Ali Ammar Yusur')))
display(df_filter)

# COMMAND ----------

df1 =df.fillna({"birth_place" : "xyz" ,"birth_country" : "abc", "residence_place" : "unknown", "residence_country" : "unknown"})
df1.display()

# COMMAND ----------

df2=df1.withColumn("height",col("height").cast(FloatType()))\
      .withColumn("weight",col("weight").cast(FloatType()))
    
df2.display()

# COMMAND ----------

df_sorted = df2.sort("height","weight",ascending=[0,]).filter(col('weight')>0)
df_sorted.display()

# COMMAND ----------

df_sorted = df_sorted.withColumn("nationality",regexp_replace(col("nationality"),"United States","US"))
df_sorted.display()

# COMMAND ----------

df.groupBy("code").agg(count("code").alias("total_count")).filter(col("total_count")>1).display()

# COMMAND ----------

df_sorted = df_sorted.withColumnRenamed("code","Athlete_id")
df_sorted.display()

# COMMAND ----------

df_split= df_sorted.withColumn("occupation",split("occupation",','))
df_split.display()

# COMMAND ----------

df_split.columns

# COMMAND ----------

df_final = df_split.select('Athlete_id',
 'current',
 'name',
 'name_short',
 'name_tv',
 'gender',
 'function',
 'country_code',
 'country',
 'country_long',
 'nationality',
 'nationality_long',
 'nationality_code',
 'height',
 'weight')

display(df_final)

# COMMAND ----------

from pyspark.sql.window import Window

# COMMAND ----------

df_final = df_final.withColumn("cum_weight", sum("weight").over(Window.partitionBy("nationality").orderBy("height").rowsBetween(Window.unboundedPreceding, Window.unboundedFollowing)))

df_final.display()

# COMMAND ----------

df_final.createOrReplaceTempView("athletes")

# COMMAND ----------

df_sql = spark.sql('''
                   select sum(weight) over(partition By nationality order By height rows between unbounded preceding and current row )as cumweight from athletes''')

df_sql.display()

# COMMAND ----------

df_final.write.format("delta")\
    .mode("append")\
    .option("path", "abfss://silver@olympicsadls.dfs.core.windows.net/athletes")\
    .saveAsTable("olympics_Catalog.silver_sch.athletes")