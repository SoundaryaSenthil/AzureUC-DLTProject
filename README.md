Azure Data Engineering Project

with Azure DevOps, Unity Catalog, and Delta Live Tables (DLT)

This project showcases a complete end-to-end Azure Data Engineering solution using Azure Data Factory, Azure DevOps, and Azure Databricks integrated with Unity Catalog. 

It demonstrates how to build a robust, scalable, and governed data pipeline from raw data ingestion to curated insights using the Bronze-Silver-Gold Lakehouse Architecture.

![Screenshot 2025-04-18 190904](https://github.com/user-attachments/assets/5fcbec3f-a29a-4731-8a06-86e241fb60dd)
Components:

	•	Source: GitHub Repository (CSV via HTTP API)
 
	•	Ingestion Layer: Azure Data Factory (ADF)
 
	•	Storage: Azure Data Lake Storage Gen2 (Raw, Bronze, Silver, Gold)
 
	•	Transformation: Azure Databricks Notebooks + DLT Pipelines
 
	•	Governance: Unity Catalog for centralized access control
 
	•	Automation: Azure DevOps CI/CD for version control & deployment

⸻

🪣 ADLS Integration & Lakehouse Zoning

	•	Created four containers: raw, bronze, silver, and gold
 
	•	Implemented systematic folder structures for each data layer
 
	•	Ensured secure and optimized access between Databricks and ADLS

⸻

🔧 Azure DevOps Integration 	🔁
	•	Set up an Azure DevOps Repo with dedicated development branches
 
	•	Linked ADF with DevOps for seamless source control & pipeline management
 
	•	Enabled CI/CD pipelines to automate deployment

⸻

🛠️ Azure Data Factory Pipelines	🔗

Built two dynamic, parameterized ADF pipelines:

	•	Pipeline 1: GitHub → Bronze
Ingests CSV files directly from GitHub using a parameterized HTTP URL

	•	Pipeline 2: Raw → Silver
Moves selected files based on matching conditions to structured layers in ADLS

⸻

🧪 Azure Databricks + Unity Catalog	🧠

	•	Configured DBFS + ABFS integration to access ADLS
 
	•	Registered External Locations in Unity Catalog for each zone
 
	•	Created Silver Schema and performed transformations:
 
	•	Handled null values, type casting, and duplicate checks
	•	Applied window functions to compute cumulative weight by country
	•	Cleaned and wrote data in Delta format

⸻

✨ Delta Live Tables (DLT) – Gold Layer

	•	Built a DLT Pipeline in Databricks for the Gold/Curated Layer
 
	•	Streamed Delta-formatted Silver data
 
	•	Created final Gold Delta Tables using declarative ETL logic in DLT

⸻

🌟 Key Features & Highlights

	•	Dynamic Ingestion: Parameterized GitHub URL enables flexible, reusable pipelines
 
	•	CI/CD with Azure DevOps: Track, test, and deploy all changes efficiently
 
	•	Lakehouse Architecture: Bronze → Silver → Gold structured and governed zones
 
	•	Real-time Transformation: Automated using DLT for streaming data
 
	•	Delta Lake + DLT: ACID-compliant, scalable, and reliable data processing
 
	•	Unity Catalog: Ensures centralized governance and secure access control.
