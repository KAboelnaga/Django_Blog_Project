from django.db import models
from forbidden.models import ForbiddenWord



from django.contrib.auth import get_user_model

User = get_user_model()

class Comment(models.Model):
    ID=models.AutoField(primary_key=True,editable=False)
    USER_ID = models.ForeignKey(User, on_delete=models.CASCADE)
    POST_ID = models.ForeignKey('blogs.Post', on_delete=models.CASCADE, related_name='comments')
    PARENT_COMMENT_ID = models.ForeignKey('self',null=True,blank=True,related_name='replies',on_delete=models.CASCADE)
    CONTENT = models.TextField()
    CREATED_AT = models.DateTimeField(auto_now_add=True)


    def filtered_content(self):
        words = self.CONTENT.split()
        forbidden = ForbiddenWord.objects.values_list('word', flat=True)
        return ' '.join([
            '*' * len(word) if word.lower() in forbidden else word
            for word in words
        ])


    def is_reply(self):
        return self.parent is not None
    
    def __str__(self):
        return f"Comment by {self.user.username} on {self.post.title} ({'Reply' if self.parent else 'Comment'})"

