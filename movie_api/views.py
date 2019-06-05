from .models import Movie
from .models import Comment
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter, SearchFilter
from .serializers import MoviesSerializer, CommentSerializer, CreateMovieSerializer
from rest_framework.views import APIView
from django.db.models import Count, Q
from rest_framework.response import Response





class MoviesViewSet(viewsets.ModelViewSet):
     #Viewset dla dodowania filmow i wyświetlania #
    queryset = Movie.objects.all()
    serializer_class = MoviesSerializer
    filter_backends = (OrderingFilter, SearchFilter)
    search_fields = ('title', 'year')
    ordering = ('title',)

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateMovieSerializer
        else:
            return MoviesSerializer


class CommentsViewSet(viewsets.ModelViewSet):
    #Viewset dla dodawania komentarzy i wyświetlania #
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = (OrderingFilter, SearchFilter)
    search_fields = ('author',)
    ordering_fields = ('date', 'author', 'movie')
    ordering = ('date',)





class TopMoviesView(APIView):
    def get(self, request, format=None):
        date_from = request.query_params.get("from")
        date_to = request.query_params.get("to")
        qs = Movie.objects.prefetch_related("Comments")
        filters = []
        if date_from:
            filters.append(Q(comments__created_at__gte=date_from))
        if date_to:
            filters.append(Q(comments__created_at__lte=date_to))
        qs = (
            qs.filter(*filters)
            .annotate(total_comments=Count("Comments"))
            .values("id", "total_comments")
            .order_by("-total_comments")
        )
        response = []
        last_count = 0
        last_rank = 0
        for element in qs.all():
            if not last_rank or element["total_comments"] < last_count:
                last_rank += 1
            last_count = element["total_comments"]
            element["rank"] = last_rank
            element["movie_id"] = element.pop("id")  # rename the key
            response.append(element)
        return Response(response, status=200)
