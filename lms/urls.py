from lms.views import CuratorViewSet

curator_router = DefaultRouter()
curator_router.register(r'curator',CuratorViewSet,basename='curator')