import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
import gs_array_to_cols
import gs_split
import gs_concat
import re

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Script generated for node AWS Glue Data Catalog
AWSGlueDataCatalog_node1725180674332 = glueContext.create_dynamic_frame.from_catalog(database="electronics", table_name="electronics", transformation_ctx="AWSGlueDataCatalog_node1725180674332")

# Script generated for node Split String
SplitString_node1725182443091 = AWSGlueDataCatalog_node1725180674332.gs_split(colName="event_time", pattern="\s", newColName="event_time_arr")

# Script generated for node Array To Columns
ArrayToColumns_node1725182570193 = SplitString_node1725182443091.gs_array_to_cols(colName="event_time_arr", colList="Event_Date, Event_Time, Event_Time_Zone")

# Script generated for node Concatenate Columns
ConcatenateColumns_node1725182822776 = ArrayToColumns_node1725182570193.gs_concat(colName="event_clock_time", colList=["Event_Time", "Event_Time_Zone"], spacer=" ")

# Script generated for node Change Schema
ChangeSchema_node1725183155117 = ApplyMapping.apply(frame=ConcatenateColumns_node1725182822776, mappings=[("order_id", "bigint", "order_id", "long"), ("product_id", "bigint", "product_id", "long"), ("category_id", "bigint", "category_id", "long"), ("category_code", "string", "category_code", "string"), ("brand", "string", "brand", "string"), ("price", "double", "price", "double"), ("user_id", "bigint", "user_id", "long"), ("Event_Date", "string", "Event_Date", "date"), ("event_clock_time", "string", "event_clock_time", "string")], transformation_ctx="ChangeSchema_node1725183155117")

# Script generated for node Filter
Filter_node1725190996982 = Filter.apply(frame=ChangeSchema_node1725183155117, f=lambda row: (bool(re.match("^(?!\s*$).+", row["brand"])) and bool(re.match("^(?!\s*$).+", row["category_code"]))), transformation_ctx="Filter_node1725190996982")

# Script generated for node Amazon S3
AmazonS3_node1725183187515 = glueContext.write_dynamic_frame.from_options(frame=Filter_node1725190996982, connection_type="s3", format="glueparquet", connection_options={"path": "s3://dataeng-cl-z-gse23/electronics/", "partitionKeys": []}, format_options={"compression": "uncompressed"}, transformation_ctx="AmazonS3_node1725183187515")

job.commit()