from django.urls import path
from rest_framework.routers import DefaultRouter

from app.views import RentalViewSet, RentalItemViewSet, QueueViewSet, PenaltyViewSet, NotificationViewSet, CartViewSet, \
    OrderViewSet, BooksViewSet, AuthorViewSet, ChillZoneViewSet, ChillZoneBookingViewSet, PointTransactionViewSet, \
    BadgeViewSet, MyPointsView, ShelfViewSet, PublicShelfView, CountryViewSet, CityViewSet, GenreViewSet, \
    PublisherViewSet, ShiftViewSet, PositionViewSet, PaymentTypeViewSet, SupplierViewSet, LibraryViewSet, \
    LibraryBookViewSet, ProductCategoryViewSet, ProductViewSet, ChillOrderViewSet

router = DefaultRouter()
router.register('rentals', RentalViewSet, basename='rental')
router.register('rental_items', RentalItemViewSet, basename='rental-item')
router.register('queue', QueueViewSet, basename='queue')
router.register('penalties', PenaltyViewSet, basename='penalty')
router.register('notifications', NotificationViewSet, basename='notification')
router.register('cart', CartViewSet, basename='cart')
router.register('orders', OrderViewSet, basename='order')
router.register('books', BooksViewSet, basename='book')
router.register('authors', AuthorViewSet, basename='author')
router.register('chill_zones', ChillZoneViewSet, basename='chill-zone')
router.register('chill_zone_bookings', ChillZoneBookingViewSet, basename='chill-zone-booking')
router.register('point_transactions', PointTransactionViewSet, basename='point-transaction')
router.register('badges', BadgeViewSet, basename='badge')
router.register('shelf', ShelfViewSet, basename='shelf')
router.register('countries', CountryViewSet, basename='country')
router.register('cities', CityViewSet, basename='city')
router.register('genres', GenreViewSet, basename='genre')
router.register('publishers', PublisherViewSet, basename='publisher')
router.register('shifts', ShiftViewSet, basename='shift')
router.register('positions', PositionViewSet, basename='position')
router.register('payment_types', PaymentTypeViewSet, basename='payment-type')
router.register('suppliers', SupplierViewSet, basename='supplier')
router.register('libraries', LibraryViewSet, basename='library')
router.register('library_books', LibraryBookViewSet, basename='library-book')
router.register('product_categories', ProductCategoryViewSet, basename='product-category')
router.register('products', ProductViewSet, basename='product')
router.register('chill_orders', ChillOrderViewSet, basename='chill-order')

urlpatterns = [
    path('shelf/public/<uuid:token>/', PublicShelfView.as_view(), name='shelf-public'),
    path('points/me/', MyPointsView.as_view(), name='points-me'),
] + router.urls
