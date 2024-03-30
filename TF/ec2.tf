resource "aws_instance" "aux_instance" {
  iam_instance_profile = aws_iam_instance_profile.ddb_profile.name
  ami                  = "ami-0e731c8a588258d0d" # Amazon Linux 2023
  instance_type        = "t2.micro"
  key_name             = "aws_key" # By default, user is admin, ec2-user or similar.
  vpc_security_group_ids = [
    aws_security_group.sg_ssh.id
  ]
  user_data = <<-EOF
#!/bin/bash 
yum install -y git
sudo yum install -y git
EOF

  tags = {
    Name = "aux"
  }
}