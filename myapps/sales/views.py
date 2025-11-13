from rest_framework import viewsets
from .models import Batch, BranchStock, InventoryMovement
from .serializers import BatchSerializer, BranchStockSerializer, InventoryMovementSerializer

class BatchViewSet(viewsets.ModelViewSet):
    queryset = Batch.objects.all()
    serializer_class = BatchSerializer

class BranchStockViewSet(viewsets.ModelViewSet):
    queryset = BranchStock.objects.all()
    serializer_class = BranchStockSerializer

class InventoryMovementViewSet(viewsets.ModelViewSet):
    queryset = InventoryMovement.objects.all()
    serializer_class = InventoryMovementSerializer