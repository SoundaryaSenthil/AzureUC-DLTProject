# Databricks notebook source
# MAGIC %md
# MAGIC # Dynamic Data Reading
# MAGIC # ## 

# COMMAND ----------

# MAGIC %md
# MAGIC # parameters

# COMMAND ----------

dbutils.widgets.text("source_cont","")
dbutils.widgets.text("sink_cont","")
dbutils.widgets.text("folder","")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Fetching Parameters

# COMMAND ----------

source_cont = dbutils.widgets.get("source_cont")
sink_cont = dbutils.widgets.get("sink_cont")
folder = dbutils.widgets.get("folder")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Parameterizing code

# COMMAND ----------

#f-string
df = spark.read.format("parquet")\
    .load(f"abfss://{source_cont}@olympicsadls.dfs.core.windows.net/{folder}")



# COMMAND ----------

df.display()

# COMMAND ----------

df.write.format("delta").mode("append")\
        .option("path", f"abfss://{sink_cont}@olympicsadls.dfs.core.windows.net/{folder}")\
        .saveAsTable(f"olympics_catalog.{sink_cont}_sch.{folder}")