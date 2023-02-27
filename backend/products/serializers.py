from rest_framework import serializers
from rest_framework.reverse import reverse

from api.serializers import UserPublicSerializer

from .models import Product
from .validators import validate_title_no_hello, unique_product_title

class ProductSerializer(serializers.ModelSerializer):
    owner = UserPublicSerializer(source='user', read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
            view_name='product-detail',
            lookup_field='pk',
        )
    title = serializers.CharField(validators=[validate_title_no_hello, unique_product_title])

    class Meta:
        model = Product
        fields = [
            'owner',
            'url',
            'edit_url',
            'pk',
            'title',
            'content',
            'price',
            'sale_price',
        ]


    def get_edit_url(self, obj):
        # return f"/api/products/{obj.pk}/"
        request = self.context.get('request') # not just self.request because Serializers may or may not have a .request
        if request is None:
            return None
        return reverse("product-edit", kwargs={'pk': obj.pk}, request=request)

    # def validate_title(self, value):
    #     request = self.context.get('request')
    #     user = request.user
    #     qs = Product.objects.filter(user=user, title__iexact=value)
    #     if qs.exists():
    #         raise serializers.ValidationError(f"{value} is already a product name.")
    #     return value

    # def create(self, validated_data):
    #     # email = validated_data.pop('email')
    #     obj = super().create(validated_data)
    #     # print(email, obj)
    #     return obj
    
    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get('title') # no need to invoke .save as it automatically invokes
    #     return instance