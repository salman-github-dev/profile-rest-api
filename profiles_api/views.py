from rest_framework.views import APIView
from rest_framework.response import Response


class HelloAPIView(APIView):
    """test API View"""
    def get(self, request, format=None):
        """returns a list of APIView features"""
        an_apiview = [
            'Users HTTP methonds as function (get, post, patch, put ,delete)',
            'Is similar to a traditional Django view',
            'gives you te most control over your application logic',
            'is mapped manually to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
