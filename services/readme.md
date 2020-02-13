
CI/CD INTEGRATION:

Create a new directory called ./circleci in the root of the folder
Create a config.yml within that directory.
We want to create a pipeline to deploy our service
A commit should be able to trigger a build which should be tagged with a version once the tst case passes
We want to create a release branch from the master branch so we can tract every release
Once a build is successful we can push an artifact to a central repo such as artifactory
