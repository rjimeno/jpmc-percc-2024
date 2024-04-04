resource "aws_ecr_repository" "jpmc_ecr" {
  name                 = "jpmc-ecr"
  image_tag_mutability = "MUTABLE" # May be better to make it IMMUTABLE instead (undecided).

  image_scanning_configuration {
    scan_on_push = true
  }
}