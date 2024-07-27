# Automated-Website-Backups
.tf modules to create AWS resources necessary for website backups <br>
Edit the main.tf the set arguments such as project_name <br><br>
Open VS Code<br>
Navigate to the directory of the module<br>
open new terminal<br>
run the following commands one at a time<br>
```terraform init```<br>
```terraform validate``` #You can skip this one<br>
```terraform plan```<br>
```terraform apply```<br>
type ```yes``` to approve resource creation.<br>
<br>
This creates <br>
  -an iam user<br>
  -iam policy that gives the following s3 permissions:<br>
                "GetObject",<br>
                "PutObject",<br>
                "ListBucket",<br>
                "ListObject",<br>
                "DeleteBucket",<br>
                "DeleteObject"<br>
  -ataches the iam policy to the user<br>
  -Outputs the bucket arn, bucket name in your CLI<br>
  -The user access key and secret keys are sensitive so will not be displayed in CLI. <br>
      open the .tfstate file to find them,<br>

Use the access key, secret key and bucket arn to give permission to the back-up/Restore plugin such as UpDraftPlus.<br>
 running ```terraform destroy -auto-approve``` will destroy the whole infrastructure.<br>
