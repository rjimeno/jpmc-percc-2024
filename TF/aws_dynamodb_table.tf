# This file creates our DynamoDB table 

resource "aws_dynamodb_table" "movies_ddb" {
  name           = "movies" #Name of table
  read_capacity  = 5
  write_capacity = 5
  # {'title': 'After Dark in Central Park', 'year': 1900, 'cast': [], 'genres': [], 'href': None}
  hash_key = "title" # required. Forces new resource 
  attribute {
    name = "title" # required
    type = "S"
  }
  tags = {
    Name = "movies tag"
  }
}