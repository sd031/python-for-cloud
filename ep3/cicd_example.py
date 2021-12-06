import os
import logging
import json
import boto3
from botocore.exceptions import ClientError
import iam_example

code_build_role_name = 'containerAppBuildProjectRolePython'
code_build_role_policy_name = 'containerAppBuildProjectRolePolicyPython'
code_build_project_name = "container-app-build-python"

code_pipeline_role_name = "appsCodepipelineRolePython"
code_pipeline_policy_name = "appsCodepipelineRolePolicy"
code_pipeline_project_name = "python-app-pipeline"
python_cicd_bucket = "python-cicd-example"
BranchName = "master"
RepositoryName = "pythonapp"
region_name = "us-west-2"
aws_ecs_cluster_name = "python-app-cluster"
aws_ecs_python_app_service_name = "python-api-service"
aws_ecs_python_app_continer_name = "pythonAppContainer"


codebuild_trust_relationship = {
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "codebuild.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}

codebuild_service_role_policy = {
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Resource": [
        "*"
      ],
      "Action": [
        "logs:CreateLogGroup",
        "logs:CreateLogStream",
        "logs:PutLogEvents"
      ]
    },
    {
      "Effect": "Allow",
      "Action": [
        "ec2:CreateNetworkInterface",
        "ec2:DescribeDhcpOptions",
        "ec2:DescribeNetworkInterfaces",
        "ec2:DeleteNetworkInterface",
        "ec2:DescribeSubnets",
        "ec2:DescribeSecurityGroups",
        "ec2:DescribeVpcs"
      ],
      "Resource": "*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "ec2:CreateNetworkInterfacePermission"
      ],
      "Resource": [
        "*"
      ]
    },
    {
      "Effect": "Allow",
      "Action": [
        "s3:*"
      ],
      "Resource": [
        "*"
      ]
    },
    {
            "Effect": "Allow",
            "Action": [
                "ecr:*"
            ],
            "Resource": "*"
    },
    {
            "Effect": "Allow",
            "Action": [
                "ecs:*"
            ],
            "Resource": "*"
    },
    {
            "Effect": "Allow",
            "Action": [
                "ssm:DescribeParameters"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "ssm:GetParameters"
            ],
            "Resource": "*"
        },
        {
         "Effect":"Allow",
         "Action":[
            "kms:Decrypt"
         ],
         "Resource":[
            "*"
         ]
      }
  ]
}

iam_example.create_role(code_build_role_name, codebuild_trust_relationship)
iam_example.create_iam_policy(code_build_role_policy_name, codebuild_service_role_policy)
iam_example.attach_custom_iam_policy_with_role(code_build_role_policy_name,code_build_role_name)
codebuild_client = boto3.client('codebuild')
try:
    codebuild_client.create_project(
    name=code_build_project_name,
    timeoutInMinutes = 60,
    queuedTimeoutInMinutes = 480,
    badgeEnabled = False,
    source={
        "type": "CODEPIPELINE",
        "gitCloneDepth":0,
        "insecureSsl": False,
        },
    artifacts={
        "type": "CODEPIPELINE",
        "encryptionDisabled": False,
        "packaging": "NONE"
        },
    environment={
    "type": "LINUX_CONTAINER",
    "image": "aws/codebuild/standard:5.0",
    "computeType": "BUILD_GENERAL1_MEDIUM",
    "environmentVariables": [],
    "imagePullCredentialsType": "CODEBUILD",
    "privilegedMode": True
    },
    logsConfig={
        'cloudWatchLogs': {
            'status': 'ENABLED',
        },
        's3Logs': {
            'status': 'DISABLED',
            'encryptionDisabled': False,
        }
    },
    serviceRole=code_build_role_name)
except ClientError as e:
        if e.response['Error']['Code'] == 'ResourceAlreadyExistsException':
            print("Error: %s" % e)


    # creating codepipeline project

codepipeline_trust_relationship = {
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "codepipeline.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}

codepipeline_service_role_policy = {
    "Statement": [
        {
            "Action": [
                "iam:PassRole"
            ],
            "Resource": "*",
            "Effect": "Allow",
            "Condition": {
                "StringEqualsIfExists": {
                    "iam:PassedToService": [
                        "cloudformation.amazonaws.com",
                        "elasticbeanstalk.amazonaws.com",
                        "ec2.amazonaws.com",
                        "ecs-tasks.amazonaws.com"
                    ]
                }
            }
        },
        {
            "Action": [
                "codecommit:CancelUploadArchive",
                "codecommit:GetBranch",
                "codecommit:GetCommit",
                "codecommit:GetRepository",
                "codecommit:GetUploadArchiveStatus",
                "codecommit:UploadArchive"
            ],
            "Resource": "*",
            "Effect": "Allow"
        },
        {
            "Action": [
                "codedeploy:CreateDeployment",
                "codedeploy:GetApplication",
                "codedeploy:GetApplicationRevision",
                "codedeploy:GetDeployment",
                "codedeploy:GetDeploymentConfig",
                "codedeploy:RegisterApplicationRevision"
            ],
            "Resource": "*",
            "Effect": "Allow"
        },
        {
            "Action": [
                "codestar-connections:UseConnection"
            ],
            "Resource": "*",
            "Effect": "Allow"
        },
        {
            "Action": [
                "elasticbeanstalk:*",
                "ec2:*",
                "elasticloadbalancing:*",
                "autoscaling:*",
                "cloudwatch:*",
                "s3:*",
                "sns:*",
                "cloudformation:*",
                "rds:*",
                "sqs:*",
                "ecs:*"
            ],
            "Resource": "*",
            "Effect": "Allow"
        },
        {
            "Action": [
                "lambda:InvokeFunction",
                "lambda:ListFunctions"
            ],
            "Resource": "*",
            "Effect": "Allow"
        },
        {
            "Action": [
                "opsworks:CreateDeployment",
                "opsworks:DescribeApps",
                "opsworks:DescribeCommands",
                "opsworks:DescribeDeployments",
                "opsworks:DescribeInstances",
                "opsworks:DescribeStacks",
                "opsworks:UpdateApp",
                "opsworks:UpdateStack"
            ],
            "Resource": "*",
            "Effect": "Allow"
        },
        {
            "Action": [
                "cloudformation:CreateStack",
                "cloudformation:DeleteStack",
                "cloudformation:DescribeStacks",
                "cloudformation:UpdateStack",
                "cloudformation:CreateChangeSet",
                "cloudformation:DeleteChangeSet",
                "cloudformation:DescribeChangeSet",
                "cloudformation:ExecuteChangeSet",
                "cloudformation:SetStackPolicy",
                "cloudformation:ValidateTemplate"
            ],
            "Resource": "*",
            "Effect": "Allow"
        },
        {
            "Action": [
                "codebuild:BatchGetBuilds",
                "codebuild:StartBuild",
                "codebuild:BatchGetBuildBatches",
                "codebuild:StartBuildBatch"
            ],
            "Resource": "*",
            "Effect": "Allow"
        },
        {
            "Effect": "Allow",
            "Action": [
                "devicefarm:ListProjects",
                "devicefarm:ListDevicePools",
                "devicefarm:GetRun",
                "devicefarm:GetUpload",
                "devicefarm:CreateUpload",
                "devicefarm:ScheduleRun"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "servicecatalog:ListProvisioningArtifacts",
                "servicecatalog:CreateProvisioningArtifact",
                "servicecatalog:DescribeProvisioningArtifact",
                "servicecatalog:DeleteProvisioningArtifact",
                "servicecatalog:UpdateProduct"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "cloudformation:ValidateTemplate"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "ecr:*"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "states:DescribeExecution",
                "states:DescribeStateMachine",
                "states:StartExecution"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "appconfig:StartDeployment",
                "appconfig:StopDeployment",
                "appconfig:GetDeployment"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "ssm:DescribeParameters"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "ssm:GetParameters"
            ],
            "Resource": "*"
        },
        {
         "Effect":"Allow",
         "Action":[
            "kms:Decrypt"
         ],
         "Resource":[
            "*"
         ]
      }
    ],
    "Version": "2012-10-17"
}

iam_example.create_role(code_pipeline_role_name, codepipeline_trust_relationship)
iam_example.create_iam_policy(code_pipeline_policy_name, codepipeline_service_role_policy)
iam_example.attach_custom_iam_policy_with_role(code_pipeline_policy_name,code_pipeline_role_name)
sts = boto3.client('sts')
account_id = sts.get_caller_identity()['Account']
EnvironmentVariables = [
            {
              "name"  : "AWS_DEFAULT_REGION",
              "type"  : "PLAINTEXT",
              "value" : region_name,
            },
            {
              "name"  : "AWS_ACCOUNT_ID",
              "type"  : "PLAINTEXT",
              "value" : account_id,
            },
            {
              "name"  : "IMAGE_REPO_NAME",
              "type"  : "PLAINTEXT",
              "value" : RepositoryName,
            },
            {
              "name"  : "IMAGE_TAG",
              "type"  : "PLAINTEXT",
              "value" : "latest",
            },
            {
              "name"  : "CONTAINER_NAME",
              "type"  : "PLAINTEXT",
              "value" : aws_ecs_python_app_continer_name,
            },
          ]
code_pipeline_config = {
    "name": code_pipeline_project_name,
    "roleArn": "arn:aws:iam::" + account_id + ":role/" + code_pipeline_role_name,
    "artifactStore": {
            "type": "S3",
            "location": python_cicd_bucket
        },
        "stages": [
            {
                "actions": [
                    {
                        "runOrder": 1,
                        "actionTypeId": {
                            "category": "Source",
                            "provider": "CodeCommit",
                            "version": "1",
                            "owner": "AWS"
                        },
                        "name": "Source",
                        "outputArtifacts": [
                            {
                                "name": "SourceArtifact"
                            }
                        ],
                        "configuration": {
                            "BranchName": BranchName,
                            "RepositoryName": RepositoryName,
                        },
                        "inputArtifacts": []
                    }
                ],
                "name": "Source"
            },
            {
                "actions": [
                    {
                        "runOrder": 1,
                        "actionTypeId": {
                            "category": "Build",
                            "provider": "CodeBuild",
                            "version": "1",
                            "owner": "AWS"
                        },
                        "name": "Build",
                        "outputArtifacts": [
                            {
                                "name": "BuildArtifact"
                            }
                        ],
                        "configuration": {
                            "ProjectName": code_build_project_name,
                             "EnvironmentVariables" : json.dumps(EnvironmentVariables)

                        },
                        "inputArtifacts": [
                            {
                                "name": "SourceArtifact"
                            }
                        ]
                    }
                ],
                "name": "Build"
            },
            {
                "name": "Deploy",
                "actions": [
                    {
                        "outputArtifacts": [],
                        "inputArtifacts": [
                            {
                                "name": "BuildArtifact"
                            } 
                            ],
                        "runOrder": 1,
                        "actionTypeId": {
                            "version": "1",
                            "category": "Deploy",
                            "provider": "ECS",
                            "owner": "AWS"
                        },
                        "name": "Deploy",
                        "configuration": {
                            "ClusterName" : aws_ecs_cluster_name,
                            "ServiceName" : aws_ecs_python_app_service_name,
                            "FileName"    : "imagedefinitions.json",
                        }
                    }
                ]
            }
        ],
    }

codepipeline_client = boto3.client('codepipeline')
try:
     codepipeline_client.create_pipeline(pipeline=code_pipeline_config)
except ClientError as e:
     if e.response['Error']['Code'] == 'PipelineNameInUseException':
        print("Object already exists")
        codepipeline_client.update_pipeline(pipeline=code_pipeline_config)
     else:
        print("Unexpected error: %s" % e)
