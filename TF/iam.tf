resource "aws_iam_role" "ddb_role" {
  name = "ddbrole"

  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "ec2.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
EOF
}

resource "aws_iam_role_policy_attachment" "ddb_attachment" {
  role       = aws_iam_role.ddb_role.name
  policy_arn = "arn:aws:iam::aws:policy/AmazonDynamoDBFullAccess"
}

resource "aws_iam_instance_profile" "ddb_profile" {
  name = "ddb_profile"
  role = aws_iam_role.ddb_role.name
}

resource "aws_instance" "ddb_instance" {
  ami           = "ami-06ca3ca175f37dd66"
  instance_type = "t2.micro"

  iam_instance_profile = aws_iam_instance_profile.ddb_profile.name

  tags = {
    Name = "exampleinstance"
  }
}