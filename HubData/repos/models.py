from django.db import models


REPO, BRANCH, COMMIT, USER = 'repo', 'branch', 'commit', 'user'


class Organization(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, unique=True)

    def __str__(self) -> str:
        return self.name

class Repository(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    org = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name=REPO)

    def __str__(self) -> str:
        return f'{self.org}/{self.name}'

class Branch(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    repo = models.ForeignKey(Repository, on_delete=models.CASCADE, related_name=BRANCH)
    create_at = models.DateTimeField()

    def __str__(self) -> str:
        return f'{self.repo}/{self.name}'

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, default="noname")
    email = models.CharField(max_length=50, unique=True)

    def __str__(self) -> str:
        return self.name

class Commit(models.Model):
    id = models.AutoField(primary_key=True)
    repo = models.ForeignKey(Repository, on_delete=models.CASCADE, related_name=COMMIT)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name=COMMIT)
    sha = models.CharField(max_length=40, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name=USER)
    date = models.DateTimeField()
    additions = models.PositiveIntegerField(default=0)
    deletions = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return self.sha