from rest_framework import serializers
from watchlist_app.models import Movie

""" 
Validation is called when serializer.is_valid() is called. We have three types of validation
1. field validation 
2. object validation
3. validators
"""

class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = "__all__"

    def validate_name(self, value):
        """
        This is a field validation. it starts with the KEYWORD validate_<Field_name>
        """
        if len(value) < 2:
            raise serializers.ValidationError("Name is too short")
        else:
            return value

    def validate(self, data):
        """
        This ia an object validation. it starts with the KEYWORD validate
        """
        if data["name"] == data["description"]:
            raise serializers.ValidationError("The name and description should be different")
        else:
            return data 



# def name_length(value):
#     """
#     When using the validator to validate, you declare the KEYWORD 'validators' 
#     in the field to be validate and also calling the function the functions that runs the validation.
#     """
#     if len(value) < 4:
#         raise serializers.ValidationError("The characters are less the 4 ")
#     # else:
#     #     return value


# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField()
#     description = serializers.CharField(validators=[name_length])
#     active = serializers.BooleanField()

#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance

#     def validate_name(self, value):
#         """
#         This is a field validation. it starts with the KEYWORD validate_<Field_name>
#         """
#         if len(value) < 2:
#             raise serializers.ValidationError("Name is too short")
#         else:
#             return value

#     def validate(self, data):
#         """
#         This ia an object validation. it starts with the KEYWORD validate
#         """
#         if data["name"] == data["description"]:
#             raise serializers.ValidationError("The name and description should be different")
#         else:
#             return data 


