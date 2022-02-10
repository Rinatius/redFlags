from abc import ABCMeta, abstractmethod

from rest_access_policy import AccessPolicy

from users.models import CustomUser


class StaffOnlyCreateAccessPolicy(AccessPolicy):
    __metaclass__ = ABCMeta
    statements = [
        {
            "action": ["list", "retrieve"],
            "principal": "authenticated",
            "effect": "allow",
        },
        {
            "action": ["create"],
            "principal": "authenticated",
            "effect": "allow",
            "condition": "can_create"

        },
        {
            "action": ["partial_update", "update"],
            "principal": "authenticated",
            "effect": "allow",
            "condition": "can_create"

        },
        {
            "action": ["destroy"],
            "principal": "authenticated",
            "effect": "can_create"
        }
    ]

    @classmethod
    @abstractmethod
    def scope_queryset(cls, request, qs):
        pass

    def can_create(self, request, view, action) -> bool:
        # is_stuff = CustomUser.objects.get(user)
        return bool(request.user.is_staff)


class MainAccessPolicy(StaffOnlyCreateAccessPolicy):
    @classmethod
    def scope_queryset(cls, request, queryset):
        return queryset
