variable "aws_region" {
  description = "AWS region used for SentinelOps AI"
  type        = string
  default     = "ap-south-1"
}

variable "state_bucket_name" {
  description = "Globally unique S3 bucket used for Terraform remote state"
  type        = string
}
