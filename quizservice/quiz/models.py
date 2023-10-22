from django.db import models


class Question(models.Model):
    question_id = models.IntegerField(primary_key=True)
    question_text = models.TextField()
    answer_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question_text
