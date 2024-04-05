resource "aws_instance" "aux_instance" {
  iam_instance_profile        = aws_iam_instance_profile.ddb_profile.name
  ami                         = "ami-0e731c8a588258d0d" # Amazon Linux 2023
  instance_type               = "t2.micro"
  associate_public_ip_address = true
  key_name                    = "aws_key" # By default, user is admin, ec2-user or similar.
  vpc_security_group_ids      = [aws_security_group.sg_ssh.id]
  subnet_id                   = module.vpc.public_subnets[0] # Create this instance in the first public subnet (in the same VPC).
  user_data                   = <<-EOF
#!/bin/bash 

id # Obs.: This script runs as root; `sudo` is not required.
yum update -y
yum install docker -y
/bin/systemctl start docker.service  # service docker start
usermod -a -G docker ec2-user # so `ec2-user` can execute Docker commands without using `sudo`.
yum install git -y
# Now clone or fetch the source, `cd` into it and build the docker image.
git clone --recursive https://github.com/rjimeno/jpmc-percc-2024.git
pushd jpmc-percc-2024/load/
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
python load.py
EOF

  tags = {
    Name = "aux"
  }
}