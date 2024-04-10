# The file terraform.tfvas is not in version control. Minimally,
# it should contain a single line similar to the following:
# region = "us-east-1"

variable "region" {
  description = "The region Terraform deploys your instance"
  type        = string
  nullable    = false
  default     = "us-east-1"
}

variable "read_capacity" {
  description = "Placeholder for DDB read capacity (tables and indexes."
  type        = number
  nullable    = false
  default     = 50
}

variable "write_capacity" {
  description = "Placeholder for DDB write capacity (tables and indexes."
  type        = number
  nullable    = false
  default     = 50
}