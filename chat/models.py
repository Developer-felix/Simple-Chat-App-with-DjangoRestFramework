from django.contrib.auth.models import User
from django.db import models

# sender is used to identify the sender of the message
# receiver is used to identify the receiver of the message
# message is a CharField to store the text.
# timestamp stores the date and time of creation of message
# is_read keeps track if the message is read or not.

class Message(models.Model):
     sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')        
     receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')        
     message = models.CharField(max_length=1200)
     timestamp = models.DateTimeField(auto_now_add=True)
    #  is_read = models.BooleanFeild(default=False)
     def __str__(self):
           return self.message
     class Meta:
           ordering = ('timestamp',)