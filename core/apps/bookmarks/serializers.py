"""Bookmark serializer."""

# ruff: noqa: ANN001

from django.shortcuts import get_object_or_404
from rest_framework import serializers

from core.apps.articles.models import Article

from .models import ReadingCategory

PARTIAL_ARITCLE_BODY_LENGTH = 134


class BookmarkSerializer(serializers.ModelSerializer):
    """Bookmark Serializer."""

    claps_count = serializers.IntegerField(read_only=True)
    responses_count = serializers.IntegerField(read_only=True)
    partial_body = serializers.SerializerMethodField()
    created_at = serializers.DateTimeField(format="%b %d, %Y", read_only=True)

    class Meta:
        model = Article
        fields = [
            "id",
            "title",
            "partial_body",
            "banner_image",
            "created_at",
            "claps_count",
            "responses_count",
        ]
        read_only_fields = ["title"]

    def get_partial_body(self, obj):
        """Return certain length of article's body."""
        text = obj.description + obj.body

        return (
            text[:PARTIAL_ARITCLE_BODY_LENGTH]
            if len(text) >= PARTIAL_ARITCLE_BODY_LENGTH
            else text
        )


class ReadingCategorySerializer(serializers.ModelSerializer):
    """ReadingCategory Serializer."""

    bookmarks = BookmarkSerializer(many=True, read_only=True)
    bookmarks_count = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False)

    class Meta:
        model = ReadingCategory
        fields = [
            "id",
            "slug",
            "title",
            "description",
            "is_private",
            "updated_at",
            "bookmarks_count",
            "bookmarks",
        ]
        read_only_fields = ["id", "slug"]

    def update(self, instance, validated_data):
        """Allow only updating is_private and description for 'Reading list' category."""
        if instance.is_reading_list:
            validated_data.pop("title", None)
            for attr, value in validated_data.items():
                setattr(instance, attr, value)
                instance.save()
            return instance

        return super().update(instance, validated_data)

    def create(self, validated_data):
        """Get or create a bookmark categoyr and associate it with an article."""
        # Try to get exisitng category or create a new category
        title = validated_data.get("title", "Reading list")  # Default to "Reading list"
        user = validated_data.get("user")
        bookmark_category, _ = ReadingCategory.objects.get_or_create(
            user=user,
            title=title,
            defaults={
                "description": validated_data.get("description", ""),
                "is_private": validated_data.get("is_private", False),
            },
        )

        article_id = self.context.get("article_id", None)
        if article_id:
            article = get_object_or_404(Article, id=article_id)
            bookmark_category.bookmarks.add(article)

        return bookmark_category
