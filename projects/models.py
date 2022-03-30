from django.db import models

# Create your models here.

class Read(models.Model):
    title = models.CharField(null=True,blank=True,max_length=100)
    episode = models.IntegerField(null=True, blank=True)
    photos = models.ImageField(upload_to='images/',default='#')
    describe = models.TextField(null=True,blank=True)
    chapter = models.IntegerField(null=True, blank=True)
    season = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.title

class Choice(models.Model):
    plist = models.ForeignKey(Read, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(sef):
        return self.choice_text
