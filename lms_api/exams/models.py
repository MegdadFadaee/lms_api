from django.db import models


class Question(models.Model):
    # right_choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    created_at = models.DateTimeField("date created", auto_now_add=True)
    updated_at = models.DateTimeField("date updated", auto_now=True)

    def __str__(self):
        return self.text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    created_at = models.DateTimeField("date created", auto_now_add=True)
    updated_at = models.DateTimeField("date updated", auto_now=True)

    def __str__(self):
        return self.text
