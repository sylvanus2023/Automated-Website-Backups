# provider "aws" {
#   region = "us-east-1"
# }

variable "project_name" {
  type    = string
  default = "unamed-prj"
}

resource "aws_iam_user" "user" {
  name = "${var.project_name}-user"
}

resource "aws_iam_policy" "iam_policy" {
  name        = "${var.project_name}-iam-policy"
  description = "Policy giving allow, get, put, and delete permissions"
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Action = [
          "s3:GetObject",
          "s3:PutObject",
          "s3:ListBucket",
          "s3:ListObject",
          "s3:DeleteObject",
          "s3:DeleteBucket"
        ]
        Resource = "arn:aws:s3:::${var.project_name}/*"
      }
    ]
  })
}

resource "aws_iam_user_policy_attachment" "user_policy_attachment" {
  user       = aws_iam_user.user.name
  policy_arn = aws_iam_policy.iam_policy.arn
}

resource "aws_iam_access_key" "user_access_key" {
  user = aws_iam_user.user.name
}

output "user_access_key_id" {
  value     = aws_iam_access_key.user_access_key.id
  sensitive = true
}

output "user_secret_key" {
  value     = aws_iam_access_key.user_access_key.secret
  sensitive = true
}
