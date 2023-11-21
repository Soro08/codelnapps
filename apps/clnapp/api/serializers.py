from django.contrib.auth.models import (
    User,
)
from rest_framework import (
    serializers,
)
from clnapp.models import (
    Model3d,
    UserBadge,
    Badge,
)
from django.contrib.auth.password_validation import (
    validate_password,
)


class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(
        write_only=True,
        required=True,
    )

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "password",
            "password2",
        ]
        extra_kwargs = {
            "password": {
                "write_only": True,
                "validators": [validate_password],
            }
        }

    def validate(self, data):
        if data["password"] != data["password2"]:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        del data["password2"]
        return data


class UserBadgeSerializer(serializers.ModelSerializer):
    class EmbeddedBadgeSerializer(serializers.ModelSerializer):
        class Meta:
            model = Badge
            exclude = ["id"]

    badge = EmbeddedBadgeSerializer()
    delivred_at = serializers.DateTimeField(source="created_at")

    class Meta:
        model = UserBadge
        exclude = [
            "id",
            "user",
            "created_at",
        ]


class UserDetailSerializer(serializers.ModelSerializer):
    badges = UserBadgeSerializer(
        many=True,
        source="userbadge_set",
    )

    class Meta:
        model = User
        fields = [
            "id",
            "first_name",
            "last_name",
            "badges",
            "date_joined",
        ]


class Model3dSerializer(serializers.ModelSerializer):
    class Meta:
        model = Model3d
        fields = "__all__"
        extra_kwargs = {
            "author": {"read_only": True},
            "nb_views": {"read_only": True},
        }


class Model3dDetailSerializer(Model3dSerializer):
    class EmbeddedUserSerilizer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = [
                "first_name",
                "last_name",
            ]

    author = EmbeddedUserSerilizer()
