# ☁️ AWS S3 Data Processing Pipeline

## 📌 Overview
This project demonstrates a simple cloud-based data processing pipeline using AWS S3 and Python.

The pipeline reads raw data from an S3 bucket, performs basic data transformation using pandas, and uploads the processed dataset back to S3.

## 🏗 Architecture
S3 (Raw Data Layer) → Python Transformation Layer → S3 (Processed Data Layer)

## 🛠 Technologies Used
- AWS S3
- AWS IAM
- Python
- pandas
- boto3

## ✨ Features
- Structured S3 bucket with `raw/` and `processed/` layers
- Secure programmatic access using IAM
- Data transformation (Total, Average, Grade computation)
- Processed dataset uploaded back to S3

## 🚀 How to Run
1. Create an IAM user in AWS and generate access keys.
2. Replace placeholder credentials in `connect_s3.py`.
3. Install required libraries:
   ```
   pip install boto3 pandas
   ```
4. Run the script:
   ```
   python connect_s3.py
   ```

## 🔐 Credentials
AWS credentials are not included in this repository for security reasons.

Replace the placeholders in `connect_s3.py` with your own AWS IAM access keys before running the program.
