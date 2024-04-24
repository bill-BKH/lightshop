<<<<<<< HEAD
from django.db import models
from account.models import User
class AddAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    receiver_name =models.CharField(max_length=300)
    receiver_num=models.CharField(max_length=11)
    receiver_state=models.CharField(max_length=200)
    receiver_city=models.CharField(max_length=200)
    receiver_Postal_address=models.CharField(max_length=400)
    receiver_Postal_code=models.CharField(max_length=40)
    def __str__(self):
        return f'{self.receiver_name} | {self.receiver_num}'

   
=======
from django.db import models
>>>>>>> a6c731b (commit message)
