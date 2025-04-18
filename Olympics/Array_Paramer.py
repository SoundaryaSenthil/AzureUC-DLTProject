# Databricks notebook source
my_array = [
           { "source_cont" : "bronze",
            "sink_cont" : "silver",
            "folder" : "events"},
           { "source_cont" : "bronze",
            "sink_cont" : "silver",
            "folder" : "coaches"},         
 ]



# COMMAND ----------

dbutils.jobs.taskValues.set(key = "my_output", value = my_array)