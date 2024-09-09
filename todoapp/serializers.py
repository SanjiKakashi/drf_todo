from datetime import date, datetime, timedelta

from django.contrib.auth import get_user_model
from django.utils import timezone
from django.views.generic.dates import timezone_today
from pytz import timezone as pytz_timezone
from rest_framework import serializers

from .models import TodoModel
from .utils import make_aware, now

User = get_user_model()

priorityItems = ["high", "medium", "low"]


class ToDoSerializers(serializers.ModelSerializer):
    taskStatus = serializers.CharField(required=False, allow_blank=True)
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), required=False, allow_null=True
    )

    class Meta:
        model = TodoModel
        fields = "__all__"

    def create(self, validated_data):
        user = self.context["request"].user
        validated_data["user"] = user
        validated_data["taskStatus"] = "Todo"
        validated_data["priority"] = validated_data["priority"].lower()
        return super().create(validated_data)

    def validate(self, attrs):
        if not attrs["priority"]:
            raise serializers.ValidationError("Priority can not be Empty")
        if not attrs["priority"].lower() in priorityItems:
            raise serializers.ValidationError("Invalid Priority Value")
        if not attrs["dueDate"]:
            raise serializers.ValidationError("DueDate can not be Empty")
        return super().validate(attrs)

    # def validate_priority(self, value):
    #     if not value:
    #         raise serializers.ValidationError("Priority can not be Empty")
    #     if not value in priorityItems:
    #         raise serializers.ValidationError("Invalid Priority Value")
    #     return value

    # def validate_dueDate(self, value):
    #     if not value:
    #         raise serializers.ValidationError("DueDate can not be Empty")

    # print(value)
    # value = make_aware(value)
    # current_time = now()
    # print("Local time:", timezone.now().astimezone(pytz_timezone("Asia/Kolkata")))
    # now = timezone.now().astimezone(pytz_timezone("Asia/Kolkata"))
    # print(current_time)
    # TODO Need to add the Validation for the Due Date
    # if value <= current_time:
    #     raise serializers.ValidationError(
    #         "DueDate should be Greater than the Current Time"
    #     )
    # min_due_date = current_time + timedelta(minutes=30)
    # print(min_due_date)
    # if value < min_due_date:
    #     raise serializers.ValidationError(
    #         "DueDate should be atleast 30 minutes Greater than Current time"
    #     )
    # return value
