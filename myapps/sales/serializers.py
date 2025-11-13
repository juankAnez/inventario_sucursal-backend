from rest_framework import serializers
from .models import Batch, BranchStock, InventoryMovement

class BatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Batch
        fields = '__all__'

class BranchStockSerializer(serializers.ModelSerializer):
    class Meta:
        model = BranchStock
        fields = '__all__'

class InventoryMovementSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryMovement
        fields = '__all__'