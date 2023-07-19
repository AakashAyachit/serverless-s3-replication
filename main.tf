provider "aws" {

    access_key = "abc"
    secret_key = "xyz"

    region = "ap-south-1"
}


resource "aws_s3_bucket" "source_bucket-aak112" {
  bucket = "source-bucket-aak112"

  versioning {
    enabled = true
  }
}


resource "aws_s3_bucket" "destination_bucket-aak112" {
  bucket = "destination-bucket-aak112"

  versioning {
    enabled = true
  }
}

