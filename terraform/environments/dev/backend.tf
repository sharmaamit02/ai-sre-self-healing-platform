terraform {
  backend "s3" {
    bucket       = "sentinelops-ai-tfstate-624606539716-ap-south-1"
    key          = "sentinelops-ai/dev/terraform.tfstate"
    region       = "ap-south-1"
    encrypt      = true
    use_lockfile = true
  }
}
