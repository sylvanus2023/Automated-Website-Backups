# Automated-Website-Backups
.tf modules to create AWS resources necessary for website backups
Edit the main.tf the set arguments such as project_name
Open VS Code
Navigate to the directory of the module
open new terminal
run the following commands one at a time
```terraform init```
```terraform validate``` #You can skip this one
```terraform plan```
```terraform apply```
type ```yes``` to approve resource creation.

This creates 
  -an iam user
  -iam policy that gives the following s3 permissions:
                "GetObject",
                "PutObject",
                "ListBucket",
                "ListObject",
                "DeleteBucket",
                "DeleteObject"
  -ataches the iam policy to the user
  -Outputs the bucket arn, bucket name in your CLI
  -The user access key and secret keys are sensitive so will not be displayed in CLI. 
      open the .tfstate file to find them,

Use the access key, secret key and bucket arn to give permission to the back-up/Restore plugin such as UpDraftPlus.
 running ```terraform destroy -auto-approve``` will destroy the whole infrastructure.

