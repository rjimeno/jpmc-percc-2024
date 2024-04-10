# This file creates our DynamoDB table 

resource "aws_dynamodb_table" "movies_ddb" {
  name           = "movies"
  read_capacity  = var.read_capacity
  write_capacity = var.write_capacity
  # {'title': 'After Dark in Central Park', 'year': 1900, 'cast': [], 'genres': [], 'href': None}
  hash_key  = "id"
  attribute {
    name = "title"
    type = "S"
  }
  attribute {
    name = "year"
    type = "N"
  }
  attribute {
    name = "id"
    type = "N"
  }
global_secondary_index {
    name            = "title_i"
    hash_key        = "title"
    read_capacity   = var.read_capacity
    write_capacity  = var.write_capacity
    projection_type = "ALL"
  }
  global_secondary_index {
    name     = "year_i"
    hash_key = "year"
    read_capacity   = var.read_capacity
    write_capacity  = var.write_capacity
    projection_type = "ALL"
  }
  global_secondary_index {
    name            = "id_i"
    hash_key        = "id"
    read_capacity   = var.read_capacity
    write_capacity  = var.write_capacity
    projection_type = "ALL"
  }
}