# Databricks notebook source
# MAGIC %md
# MAGIC ##  DELTA LIVE TABLE-GOLD LAYER

# COMMAND ----------

import dlt
from pyspark.sql.functions import *
from pyspark.sql.types import *

# COMMAND ----------

# MAGIC %md
# MAGIC ## EXPECTATIONS FOR DATA QUALITY
# MAGIC

# COMMAND ----------

expec_coaches = {
    "rule1": "code is not null",
    "rule2": "current is True"
            }


# COMMAND ----------

expec_nocs = {
    "rule1": "code is not null"
            }


# COMMAND ----------

expec_events = {
    "rule1": "event is not null"
        }


# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## COACHES-DLT PIPELINE
# MAGIC

# COMMAND ----------

@dlt.table

def source_coaches():
    df = spark.readStream.table("olympics_catalog.silver_sch.coaches")
    return df

# COMMAND ----------

@dlt.view

def view_coaches():
    df = spark.readStream.table("LIVE.source_coaches")
    df.fillna("unknown")
    return df

# COMMAND ----------

@dlt.table
@dlt.expect_all(expec_coaches)
def coaches():
  df = spark.readStream.table("LIVE.view_coaches")
  return df

# COMMAND ----------

# MAGIC %md
# MAGIC ## NOCS DLT PIPELINE

# COMMAND ----------

@dlt.view

def view_nocs():
    
    df = spark.readStream.table("olympics_catalog.silver_sch.nocs")
    return df
    

# COMMAND ----------

@dlt.table
@dlt.expect_all_or_drop(expec_nocs)
def nocs():
    
    df = spark.readStream.table("LIVE.view_nocs")
    return df

# COMMAND ----------

# MAGIC %md
# MAGIC ## EVENTS DLT PIPELINE

# COMMAND ----------

@dlt.view

def view_events():
    df = spark.readStream.table("olympics_catalog.silver_sch.events")
    return df

# COMMAND ----------

@dlt.table

@dlt.expect_all(expec_events)
def events():
    df=spark.readStream.table("LIVE.view_events")

    return df

# COMMAND ----------

# MAGIC %md
# MAGIC ## CDC -APPLY CHANGES DLT

# COMMAND ----------

import dlt

# COMMAND ----------

@dlt.view

def source_athletes():
    df= spark.readStream.table("olympics_catalog.silver_sch.athletes")
    return df

# COMMAND ----------

dlt.create_streaming_table("athletes")

# COMMAND ----------

dlt.apply_changes(
    target = "athletes",
    source = "source_athletes",
    keys = ["Athlete_id"],
    sequence_by = col("height"),
    stored_as_scd_type = 1
)