provider "aws" {
  region  = "us-east-1"
  profile = "default"
}

module "s3" {
  source       = "./s3"
  bucket_name  = "sylva"
  project_name = "sylva"
  tags = {
    "Name" = "sylva"
    "Freq" = "Weekly"
  }
}

module "iam" {
  source       = "./iam"
  project_name = "sylva"
}

output "bucket_name" {
  value = module.s3.bucket_name
}

output "bucket_arn" {
  value = module.s3.bucket_arn
}

output "user_access_key_id" {
  value     = module.iam.user_access_key_id
  sensitive = true
}

output "user_secret_key" {
  value     = module.iam.user_secret_key
  sensitive = true
}
