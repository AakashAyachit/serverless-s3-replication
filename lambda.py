import boto3

def lambda_handler(event, context):
    source_bucket = "source-bucket-aak112"
    destination_bucket = "destination-bucket-aak112"

    object_key = event["Records"][0]["s3"]["object"]["key"]

    s3 = boto3.client("s3")

    copy_source = {
        "Bucket": source_bucket,
        "Key": object_key
    }

    s3.copy_object(Bucket=destination_bucket, Key=object_key, CopySource=copy_source)
