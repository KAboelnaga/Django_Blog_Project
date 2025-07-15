from rest_framework import serializers
from .models import Comment
from forbidden.models import ForbiddenWord

class CommentSerializer(serializers.ModelSerializer):
    filtered_content = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ['ID', 'POST_ID', 'PARENT_COMMENT_ID', 'CONTENT', 'filtered_content', 'CREATED_AT']

    def get_filtered_content(self, obj):
        return obj.filtered_content()
