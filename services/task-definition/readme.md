# Deploy services

to deploy your task definition you can create the resource using Terraform. Below is an example of a ecs cluster & task definition 
You can locate the resource here https://www.terraform.io/docs/providers/aws/r/ecs_task_definition.html https://www.terraform.io/docs/providers/aws/r/ecs_service.html

## Push image

To push your docker image to an ECR repository

```docker
run docker push <ECR repository ARN> ```

Once this is successful you can create your ECS cluster and task definition where you will attach you new used docker image
## Usage

```terraform

resource "aws_ecs_cluster" "foo" {
  name = "diginex-services"
}

resource "aws_ecs_task_definition" "service" {
  family                = "service"
  container_definitions = "${file("task-definitions/service.json")}"

  volume {
    name      = "service-storage"
    host_path = "/ecs/service-storage"
  }

  placement_constraints {
    type       = "memberOf"
    expression = "attribute:ecs.availability-zone in [us-west-2a, us-west-2b]"
  }
}


execute 'Terraform Plan' and 'terraform apply' to lauch your ecs cluster and task definition to AWS
```

(please be aware that other services such as NLB, ALB, DNS, auto scaling all must be configured as well)

