import boto3
import pandas as pd
from io import StringIO


aws_access_key_id = "YOUR_ACCESS_KEY"
aws_secret_access_key = "YOUR_SECRET_KEY"
region_name = "ap-south-2"

bucket_name = "jahnavi-data-pipeline-2026"
input_key = "raw/Students.csv"
output_key = "processed/Students_processed.csv"


s3 = boto3.client(
    's3',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=region_name
)

try:
    print("Reading raw data from S3...")

    response = s3.get_object(Bucket=bucket_name, Key=input_key)
    csv_content = response['Body'].read().decode('utf-8')
    df = pd.read_csv(StringIO(csv_content))

    print("Raw data loaded successfully.")
    print("Total records:", len(df))

    

    df["Total"] = df["Math"] + df["English"] + df["Science"]
    df["Average"] = df["Total"] / 3

    def assign_grade(avg):
        if avg >= 85:
            return "A"
        elif avg >= 70:
            return "B"
        else:
            return "C"

    df["Grade"] = df["Average"].apply(assign_grade)

    print("Data processed successfully.")

    
    csv_buffer = StringIO()
    df.to_csv(csv_buffer, index=False)

    s3.put_object(
        Bucket=bucket_name,
        Key=output_key,
        Body=csv_buffer.getvalue()
    )

    print("Processed file uploaded to S3 successfully!")
    print("Location:", output_key)

except Exception as e:
    print("Error occurred:", e)
