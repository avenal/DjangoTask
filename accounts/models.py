from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import now

import random
from datetime import date

def generate_random_number():
    return random.randint(1,100)

class CustomUser(AbstractUser):
    birth_date = models.DateField(default=now)
    number = models.PositiveSmallIntegerField(default=generate_random_number)
    def __str__(self):
        return self.username
    
    def calculateAge(self): 
        today = date.today() 
        try:  
            birthday = self.birth_date.replace(year = today.year) 
  
        except ValueError:  
            birthday = self.birth_date.replace(year = today.year, 
                      month = self.birth_date.month + 1, day = 1) 
    
        if birthday > today: 
            return today.year - self.birth_date.year - 1
        else: 
            return today.year - self.birth_date.year 
