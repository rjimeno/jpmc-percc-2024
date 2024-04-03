resource "aws_ecr_repository" "jpmc_ecr" {
  name                 = "jpmc-ecr"
  image_tag_mutability = "MUTABLE"

  image_scanning_configuration {
    scan_on_push = true
  }
}