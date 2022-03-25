from posts.models import Comment, Follow, Group, Post, User
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )
    post = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        fields = '__all__'
        model = Comment

class FollowSerializer(serializers.ModelSerializer):
    user = SlugRelatedField(
        queryset=User.objects.all(),
        default=serializers.CurrentUserDefault(),
        slug_field='username'
    )
    following = SlugRelatedField(queryset=User.objects.all(), slug_field='username')

    class Meta:
        fields = ('user', 'following')
        model = Follow
    
    def validate(self, data):
        if data["user"] == data["following"]:
            raise serializers.ValidationError("Нельзя подписываться на себя!")
        return data
