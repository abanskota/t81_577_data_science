## Create user, group and policy


Go to the AWS console and type IAM on the search box 

![](../search-iam.png) 

Click on `users` under `Access Management`. You will see that there is no user associated with your new account. Click on `Add User` tab. 

![](../add-user.PNG) 

Type on a new username and check both access types as below. You can add as many users you wish. For this exercise, you will only add yourselves as a `user` to your personal account. 

Click on `Next:Permissions`. You need to add user to a group. Since there is no existing group, you need to create one. Click on `Create group`. 

![](../create-group.PNG) 


Type `Admin` as a group name and attach default `AdminstratorAccess` policy to the group. This provides the user with full access to all AWS services and resources. You are choosing this policy because it is for yourselves. In the future, if you want to add some other user to let them access to some of the services or resources from your account, you need to select other appropriate policy or create a custom one. 

![](../admin.PNG) 

 
Skip the next `Tagging` step, review your choice, and then `Create User`.  Download the .csv file with `access-keys` and `access-secret`. **Don’t share the credential with anyone**. Copy the one-time password, which you need to login to AWS console. The secret access keys are required to be authenticated when you access AWS resources and services programmatically.  

![](../access-key.PNG) 


Now you can see yourselves as a user within `Admin` group. In my cases, I also created another user `Student` and add it to `Students` group. I attached more restrictive  policy ` AmazonS3ReadOnlyAccess` to the group, which only gives read access to all the storage buckets (S3) created within my account. I intend to further limit the access to a single bucket or objects within a bucket by creating a custom policy.  

![](../group-policies.PNG) 

 
You successfully created an Admin user , a security group, and attach the most liberal Admin policy to the user. You are all set to create other other AWS resources and access them. 
