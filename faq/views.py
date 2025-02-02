from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django.core.cache import cache
from .models import FAQ
from .serializers import FAQSerializer

class FAQViewSet(viewsets.ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

    def list(self, request, *args, **kwargs):
        lang = request.GET.get("lang", "en")
        cached_faqs = cache.get(f"faqs_{lang}")
        
        if cached_faqs:
            return Response(cached_faqs)
        
        faqs = FAQ.objects.all()
        response_data = [{"id": faq.id, **faq.get_translated(lang)} for faq in faqs]
        
        cache.set(f"faqs_{lang}", response_data, timeout=3600)  # Cache for 1 hour
        return Response(response_data)
