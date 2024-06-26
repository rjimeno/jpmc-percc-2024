output "public_ip_aux_instance" {
  value = aws_instance.aux_instance.public_ip
}

output "cluster_endpoint" {
  description = "Endpoint for EKS control plane"
  value       = module.eks.cluster_endpoint
}

output "cluster_security_group_id" {
  description = "Security group ids attached to the cluster control plane"
  value       = module.eks.cluster_security_group_id
}

output "region" {
  description = "AWS region"
  value       = var.region
}

output "cluster_name" {
  description = "Kubernetes Cluster Name"
  value       = module.eks.cluster_name
}

output "registry_id" {
  description = "The account ID of the registry holding the repository."
  value       = aws_ecr_repository.jpmc_ecr.registry_id
}

output "repository_url" {
  description = "The URL of the repository."
  value       = aws_ecr_repository.jpmc_ecr.repository_url
}