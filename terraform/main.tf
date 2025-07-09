provider "aws" {
  region = "us-east-1"
}
resource "aws_ecs_cluster" "travel_ease_cluster" {
  name = "travel-ease-cluster"
}
