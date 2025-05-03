***AZURE DATA ENGINEERING PROJECT***

with Azure DevOps, Unity Catalog, and Delta Live Tables (DLT)

This project showcases a complete end-to-end Azure Data Engineering solution using Azure Data Factory, Azure DevOps, and Azure Databricks integrated with Unity Catalog. 

It demonstrates how to build a robust, scalable, and governed data pipeline from raw data ingestion to curated insights using the Bronze-Silver-Gold Lakehouse Architecture.

![Screenshot 2025-04-18 190904](https://github.com/user-attachments/assets/5fcbec3f-a29a-4731-8a06-86e241fb60dd)


## 📈 Project Flow

```
GitHub (Data Source)
       |
       v
Azure Data Factory (Dynamic Pipelines)
       |     
       |-- Data Ingestion (Parameterized HTTP API)
       |-- Data Validation & File Filtering
       |-- ForEach Activity (Parallel Processing)
       v
Azure Data Lake Storage Gen2 (Raw Zone)
       |
       v
Azure Databricks (Connected via DB Utils & Unity Catalog)
       |
       |-- Autoloader: Raw to Bronze (Streaming Ingestion)
       |-- Bronze: Data Format Standardization (Delta)
       |-- Silver: Data Cleansing, Type Conversion & Enrichment
       |-- Gold: Aggregation, Business Logic & Curation via DLT
       |
       v
Azure Data Lake Storage Gen2 (Bronze, Silver, Gold Zones)
       |
       v
Unity Catalog (Governance & Access Control)
       |
       v
Azure DevOps (CI/CD for ADF Pipelines & Databricks Notebooks)
       |
       v
 created Workflows and DLT to land curated data in Gold layer
```

---
![Screenshot 2025-04-19 095908](https://github.com/user-attachments/assets/48daf2a9-5af2-47af-8a07-20c4811418c7)

***KEY COMPONENTS***

***🎺ADLS Integration and Bronze-Silver-Gold Zones***

• Created four containers in ADLS for the Raw, Bronze, Silver, and Gold layers.

• Set up folder structures to organize raw, transformed, and curated data systematically.
	
***🎲 Azure DevOps Integration***

• Created an Azure DevOps account and set up a development branch.

• Connected Azure Data Factory (ADF) with Azure DevOps for version control and pipeline management.
	
***☄️ Azure Data Factory Pipelines***

• Built two parameterized ADF pipelines:

  1) GitHub to Bronze container in ADLS Gen 2:

     Ingests data directly from GitHub using a parameterized HTTP URL.
  
  2) Raw to Silver Layer Ingestion: 

     Ingests necessary files only if matches the condition from Azure Data Lake Storage (ADLS) to appropriate layers within the lake.
     ![Screenshot 2025-04-19 095947](https://github.com/user-attachments/assets/f73e0788-7fb5-4e49-afec-c8d71153106d)


***🎷 Azure Databricks with Unity Catalog***
 
• Integrated Azure Databricks with ADLS using the DB connector.

• Set up Unity Catalog with external locations for Bronze, Silver, and Gold zones.

• Created a schema for the Silver layer and performed the following transformations:

  - Handled null values and data type conversions (e.g., string to float). 
  - Applied a window function to calculate the cumulative weight of athletes by country. 
  - Performed duplicate checks and more and cleaned the data

• Saved the transformed data in Delta format.
![Screenshot 2025-04-19 094411](https://github.com/user-attachments/assets/78198d7c-fa8c-49fa-bfa6-2b1a903c037b)
![Screenshot 2025-04-17 171034](https://github.com/user-attachments/assets/c75180b6-4579-40c3-89da-ba1bca59ce25)


***🥁 Delta Live Tables (DLT) in Gold Layer*** 
 
• Created a DLT pipeline in the Gold (Curated) layer.

• Streamed Delta files from the Silver layer.

• Built final curated Delta tables using Databricks’ ETL framework (DLT).

***KEY FEATURES & HIGHLIGHTS:***

• Dynamic Ingestion: Parameterized GitHub URL allows flexible ingestion of different files without modifying the pipeline logic.

• CI/CD with DevOps: All changes are tracked, versioned, and deployed using Azure DevOps pipelines.

• Layered Lakehouse Architecture: Clean separation between raw, transformed, and curated data using the Bronze-Silver-Gold model.

• Automated Streaming: Real-time data ingestion and transformation with minimal manual intervention.

• Delta Lake + DLT: Reliable, scalable data storage and processing with ACID transactions and schema enforcement.

• Governance with Unity Catalog: Centralized data governance and access control across all layers.

## 🎯 Conclusion

This project demonstrates how Azure’s modern data engineering tools can work seamlessly together to build **scalable**, **automated**, and **governed** data solutions — ensuring data quality, integrity, and accessibility from raw ingestion to curated insights.

---

## Contact

If you have any questions, feel free to connect with me on [LinkedIn](linkedin.com/in/soundarya-s-dataengineer).

---
Happy learning!!


