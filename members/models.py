from django.db import models
from django.contrib.auth.models import User

class Member(models.Model):
	user = models.OneToOneField(User, unique=True, null=True)
	name = models.CharField(max_length=200)
	email = models.EmailField(max_length=200)
	is_leader = models.BooleanField(default=False)
	is_department_leader = models.BooleanField(default=False)

	def __unicode__(self):
		return self.name