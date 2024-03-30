output "public_ip_aux_instance" {
  value = aws_instance.aux_instance.public_ip
}