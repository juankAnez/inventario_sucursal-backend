from rest_framework.routers import DefaultRouter
from .views import BatchViewSet, BranchStockViewSet, InventoryMovementViewSet

router = DefaultRouter()
router.register(r'batches', BatchViewSet)
router.register(r'stocks', BranchStockViewSet)
router.register(r'movements', InventoryMovementViewSet)

urlpatterns = router.urls