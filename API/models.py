from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

class FriendRequest(models.Model):
    UserModel = get_user_model()
    from_user = models.ForeignKey(UserModel, related_name='from_user', on_delete=models.CASCADE)
    to_user = models.ForeignKey(UserModel, related_name='to_user', on_delete=models.CASCADE)
    is_complete = models.BooleanField(default = False)
    accepted = models.BooleanField(default=False)

    def __str__(self):
        return f'friend request from {self.from_user.first_name} {self.from_user.last_name} to {self.to_user.first_name} {self.to_user.last_name}'
    