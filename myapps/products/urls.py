from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, SupplierViewSet, ProductViewSet, ProductSupplierViewSet, WarrantyViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'suppliers', SupplierViewSet)
router.register(r'products', ProductViewSet)
router.register(r'product-suppliers', ProductSupplierViewSet)
router.register(r'warranties', WarrantyViewSet)

urlpatterns = router.urls