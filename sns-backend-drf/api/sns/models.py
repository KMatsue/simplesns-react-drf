from django.db import models
from django.conf import settings


class FriendRequest(models.Model):
    askFrom = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='askFrom',
        on_delete=models.CASCADE
    )
    askTo = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='askTo',
        on_delete=models.CASCADE
    )
    approved = models.BooleanField('承認状態', default=False)

    class Meta:
        # ('askFrom', 'askTo')の組み合わせがユニークになる
        unique_together = (('askFrom', 'askTo'),)

    def __str__(self):
        return str(self.askFrom) + '----->' + str(self.askTo)


class Message(models.Model):

    message = models.CharField(max_length=140)
    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='sender',
        on_delete=models.CASCADE
    )
    receiver = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='receiver',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return str(self.sender)
