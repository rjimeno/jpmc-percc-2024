# This file creates our DynamoDB table 

resource "aws_dynamodb_table" "movies_ddb" {
  name           = "movies"   #Name of table
  read_capacity  = 5
  write_capacity = 5
  # {'title': 'After Dark in Central Park', 'year': 1900, 'cast': [], 'genres': [], 'href': None}
  hash_key       = "title" # required. Forces new resource 
  attribute {
    name = "title" # required
    type = "S"
  }
  attribute {
    name = "year"
    type = "N"
  }
  attribute {
    name = "cast"
    type = "L"
  }
  attribute {
    name = "genres"
    type = "L"
  }
  tags = {
    Name = "movies tag"
  }
}

# This file creates our DynamoDB table 


resource "aws_dynamodb_table" "Inventory_DB" {
  name           = "Inventory"   #Name of table
  billing_mode   = "PROVISIONED" #billing mode is optional as it is defaulted to provisioned 
  read_capacity  = 5
  write_capacity = 5
  hash_key       = "GamingInventoryItems" # required. Forces new resource 
  attribute {
    name = "GamingInventoryItems" # required
    type = "S"
  }
  tags = {
    Name = "Game Inventory"
  }
}
