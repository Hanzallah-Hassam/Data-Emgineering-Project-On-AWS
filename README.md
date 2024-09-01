# Data Engineering Project on AWS

## Overview

This project focuses on developing an ETL pipeline using AWS services to prepare eCommerce transaction data for downstream consumers. We utilize datasets from REES46, specifically the electronics transaction data, to demonstrate the pipeline's functionality.
![Untitled Diagram drawio(1)](https://github.com/user-attachments/assets/f6071031-8e0d-4ed5-87ce-2134a046116a)


## Project Goal

The primary goal of this project is to build an ETL pipeline that ingests, transforms, and stores data in a way that is optimized for consumption by downstream applications and analytics tools.

## Data Source

- **REES46 Electronics Transaction Data**: This dataset provides eCommerce behavior data across various categories such as electronics, cosmetics, and more.
- **Dataset Link**: [REES46 Datasets](https://rees46.com/en/datasets)

## Project Steps
![image](https://github.com/user-attachments/assets/64667cf9-9a56-47ca-b27c-03c004f091f8)

### 1. Create S3 Buckets for Data Lake

- **Landing Zone**: Create a bucket named `landing-zone`.
- **Cleaning Zone**: Create a bucket named `cleaning-zone`.

### 2. Upload Data to Landing Zone

- In the `landing-zone` bucket, create a folder named `electronics`.
- Upload the provided CSV files containing transaction data to this folder.

### 3. Set Up IAM Role

- Navigate to **IAM** and create a new role.
- Name the role and attach the following policies:
  - `AmazonS3FullAccess`
  - `AWSGlueServiceRole`
  
### 4. Create and Run an AWS Glue Crawler

- Go to **AWS Glue** and create a new crawler.
- Name the crawler as desired and proceed with the default settings.
- Add the S3 location from Step 2 as the data source.
- Attach the IAM role created in Step 3.
- Create a new database or select an existing one, and optionally provide a prefix.
- Review and complete the crawler creation, then run it.
- Upon successful completion, verify the database and table creation in the AWS Glue Console.

### 5. Create and Run an AWS Glue ETL Job

- From the AWS Glue sidebar, navigate to **Jobs**.
- Create a new job and select the **Script** editor.
- Paste the ETL script (provided in the project repository) into the editor.
- Run the job to perform data transformation and load it into the cleaning zone.

### 6. Set Up a New Crawler for the Cleaning Zone

- Create another crawler as in Step 4, but this time point the source to the `cleaning-zone` S3 path.
- Run the crawler to create a new table in the Glue Data Catalog.

### 7. Query Data Using AWS Athena

- Navigate to **AWS Athena** via the Glue Console by clicking "View Data" on the new table created.
- Run the following SQL query to find the top 10 most sold brands:

  ```sql
  SELECT brand, COUNT(*) AS most_sold_brand
  FROM your_table_name
  GROUP BY brand
  ORDER BY most_sold_brand DESC
  LIMIT 10;
  ```

- You should see results with "Samsung" as a top brands listed at the top.
  ![image](https://github.com/user-attachments/assets/66383cfe-66f8-4f6d-bf65-49bcfdd47676)

## Conclusion

This project demonstrates the end-to-end process of setting up an ETL pipeline on AWS using services like S3, Glue, IAM, and Athena. The pipeline efficiently ingests raw eCommerce transaction data, transforms it, and makes it available for analysis.


  
