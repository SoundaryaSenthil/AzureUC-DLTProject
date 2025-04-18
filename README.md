Azure Data Engineering Project with Azure Devops,Unity Catalog and DLT
This project showcases an end-to-end Azure Data Engineering solution using Azure Data Factory, Azure DevOps, and Azure Databricks with Unity Catalog. It demonstrates how to build a robust, scalable data pipeline from raw ingestion to curated insights following the Bronze-Silver-Gold architecture.
![Screenshot 2025-04-18 190904](https://github.com/user-attachments/assets/5fcbec3f-a29a-4731-8a06-86e241fb60dd)

Key Components
1. Azure DevOps Integration
• Created an Azure DevOps account and set up a development branch.
• Connected Azure Data Factory (ADF) with Azure DevOps for version control and pipeline management.

2. Azure Data Factory Pipelines
• Built two parameterized ADF pipelines:
• GitHub to Bronze container in ADLS Gen 2: Ingests data directly from GitHub using a parameterized HTTP URL.
• ADLS to Azure Data Lake: Ingests files from Azure Data Lake Storage (ADLS) to appropriate layers within the lake.

3. Azure Databricks with Unity Catalog
• Integrated Azure Databricks with ADLS using the DB connector.
• Set up Unity Catalog with external locations for Bronze, Silver, and Gold zones.
• Created a schema for the Silver layer and performed the following transformations:
• Handled null values and data type conversions (e.g., string to float).
• Applied a window function to calculate the cumulative weight of athletes by country.
• Performed duplicate checks and cleaned the data.
• Saved the transformed data in Delta format.

4. Delta Live Tables (DLT) in Gold Layer
• Created a DLT pipeline in the Gold (Curated) layer.
• Streamed Delta files from the Silver layer.
• Built final curated Delta tables using Databricks’ ETL framework (DLT).
