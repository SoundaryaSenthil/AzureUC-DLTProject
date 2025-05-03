
# Azure Data Engineering Project with Azure DevOps, Unity Catalog & Delta Live Tables

This project showcases a complete **end-to-end Azure Data Engineering solution** leveraging **Azure Data Factory**, **Azure DevOps**, and **Azure Databricks** integrated with **Unity Catalog**. It demonstrates how to build a **robust**, **scalable**, and **governed** data pipeline — from raw data ingestion to curated insights — using the **Bronze-Silver-Gold Lakehouse Architecture**.

---

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
Scheduled Workflows (Databricks Lookup Notebooks & Monitoring)
```

---

## 🛠️ Tools & Technologies

- **Azure Data Factory** (Pipelines, Linked Services, Datasets)
- **Azure Data Lake Storage Gen2** (Raw, Bronze, Silver, Gold layers)
- **Azure Databricks** (Notebooks, Delta Lake, Autoloader, DLT)
- **Unity Catalog** (Data Governance & Metastore)
- **Azure DevOps** (Repos, CI/CD Pipelines)
- **GitHub API** (Source CSV data)
- **Delta Lake** (ACID Transactions, Schema Enforcement)
- **Databricks Utilities (DBUtils)** (ADLS connectivity)
- **PySpark**, **SQL**, **Parameterization**, **Window Functions**

---

## 🙌 My Contributions

- Designed and implemented **Bronze-Silver-Gold Lakehouse architecture** on ADLS Gen2.

- Developed **dynamic ADF pipelines** to ingest and validate GitHub-hosted CSV files.
- Configured **Databricks Autoloader** for streaming ingestion from Raw to Bronze.
- Performed **extensive data cleansing, transformation**, and **enrichment** in Databricks (Silver layer).
- Built **Delta Live Tables (DLT)** pipelines to curate and aggregate data into the Gold layer.
- Set up **Unity Catalog** for centralized governance and access control on all Delta tables.
- Integrated **Azure DevOps** for CI/CD of ADF pipelines and Databricks notebooks.
- Orchestrated **scheduled workflows** and monitoring solutions using Databricks notebooks.

---

## ⚡ Challenges Faced & Solutions

- **Challenge:** Parameterizing dynamic file ingestion from GitHub API into ADF.

  **Solution:** Leveraged **ADF expression language** and **dynamic content** to construct URLs and filenames on the fly.

- **Challenge:** Ensuring schema evolution and consistency in streaming ingestion (Autoloader).

  **Solution:** Enabled **schema inference** and set **mergeSchema** option for seamless schema updates.

- **Challenge:** Managing access control across multiple zones and environments.

  **Solution:** Configured **Unity Catalog external locations** and **secure schemas** to control access per layer.

- **Challenge:** Handling large-scale parallel processing in ADF.

  **Solution:** Utilized **ForEach activities with batch concurrency** and configured **retry policies**.

- **Challenge:** Version controlling Databricks notebooks and ADF pipelines.

  **Solution:** Integrated **Azure DevOps Git repos** with Databricks and ADF for seamless versioning and deployments.

---

## 🚀 Key Features & Highlights

- **Dynamic Ingestion**: Parameterized GitHub URLs enable flexible ingestion without modifying pipeline logic.
- **CI/CD with Azure DevOps**: Full version control and automated deployments.
- **Layered Lakehouse Architecture**: Clean separation of raw, transformed, and curated data.
- **Automated Streaming**: Near real-time data ingestion and transformation.
- **Delta Lake + DLT**: Reliable storage with ACID transactions and schema enforcement.
- **Governance with Unity Catalog**: Centralized governance and secure access control.

---

## 🎯 Conclusion

This project demonstrates how Azure’s modern data engineering tools can work seamlessly together to build **scalable**, **automated**, and **governed** data solutions — ensuring data quality, integrity, and accessibility from raw ingestion to curated insights.

> Empower your organization with a future-proof **Lakehouse** solution by combining **Azure Data Services** and **Databricks Unity Catalog**.

---

**Built with ❤️ by Soundarya Senthilkumar**
