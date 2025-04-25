# Automating-Data-Analytics-with-AWS-Airflow

# 🚀 Cloud ETL Pipeline with Airflow, S3 & Redshift

This project demonstrates an end-to-end **ETL (Extract, Transform, Load)** pipeline using **AWS S3, Amazon Redshift**, and **Apache Airflow**. It automates the process of ingesting data from AWS S3, transforming it, and loading it into Redshift for analytical querying.

---

## 🔧 Tech Stack

- **Apache Airflow** – Workflow orchestration & scheduling
- **AWS S3** – Source data storage
- **Amazon Redshift** – Data warehousing and Transformation
- **boto3** – AWS interaction via Python
- **SQL** – For loading and analytics


---

## 📊 Project Flow

1. **Data Generation**  
   - Sample data are generated 
   - Data is saved as CSV .
     

2. **Upload to S3**  
   - Files are uploaded to an AWS S3 bucket .

3. **Trigger Airflow DAG**  
   - Airflow detects new files in S3 and starts the ETL process.

4. **ETL Pipeline (via Airflow DAGs)**
   - `extract`: Download files from S3
   - `transform`: Clean and preprocess data using sql.
   - `load`: Insert data into Redshift staging & analytics tables

---

## 📁 Project Structure

```bash
.
├── dags/
│   └── etl_s3_to_redshift.py     # Airflow DAG file
├── data/
│   └── sales.csv  # Sample data file in s3         #
├── sql/
│   └── create_tables.sql         # Redshift DDL scripts

