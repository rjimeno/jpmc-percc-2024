# Adding Item Table for Gaming Inventory

resource "aws_dynamodb_table_item" "item1" {
    depends_on = [
        aws_dynamodb_table.Inventory_DB 
    ]
    table_name = aws_dynamodb_table.Inventory_DB.name # required hash key is used for the lookup and identifcation
    hash_key = aws_dynamodb_table.Inventory_DB.hash_key
item = <<ITEM
{
  "GamingInventoryItems": {"S": "Items"},
        "Products": {"S": "Retro Xbox Controller"}, 
        "In Stock": {"N": "12"}
}                                    
ITEM
}