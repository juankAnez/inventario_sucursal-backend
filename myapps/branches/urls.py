from rest_framework.routers import DefaultRouter
from .views import BranchViewSet, WarehouseViewSet, LocationViewSet

router = DefaultRouter()
router.register(r'branches', BranchViewSet)
router.register(r'warehouses', WarehouseViewSet)
router.register(r'locations', LocationViewSet)

urlpatterns = router.urls