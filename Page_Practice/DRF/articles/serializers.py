from rest_framework import serializers
from .models import Article, Comment


class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('article',)
       
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep.pop('article', None)
        return rep
   
        
class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'content')


class ArticleDetailSerializer(serializers.ModelSerializer):
    # comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True) 
    comment_set = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    class Meta(ArticleListSerializer.Meta):
        model = Article
        # fields = ('id', 'title', 'content')
        fields = ArticleListSerializer.Meta.fields + (
            'comment_set',
            'commnet_count',
        )

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['comments'] = rep.pop('comment_set', [])
        return rep