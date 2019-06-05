from rest_framework import serializers
from .models import Movie, Comment, Rating
from . import omdb


class CreateMovieSerializer(serializers.ModelSerializer):
     #serializer do zapisywania filmu do dany bazych po tytule #

    def create(self, data):
         #zapisywanie filmu po tytule do bazy danych z omdbapi. #
        omdb_data = omdb.collect_movie(data.get('title', ''))
        movie_serializer = MoviesSerializer(data=omdb_data)
        if omdb_data.get('response') == 'False':
            raise serializers.ValidationError(omdb_data)
        movie_serializer.is_valid(raise_exception=True)
        movie_serializer.save()
        print('Dodano film')
        return movie_serializer.data

    class Meta:
        model = Movie
        fields = ('title',)



class RatingSerializer(serializers.ModelSerializer):
     #serializer dla ratingu filmów #
    Source = serializers.CharField(source='source')
    Value = serializers.CharField(source='value')

    class Meta:
        model = Rating
        fields = ('Source','Value')



class MoviesSerializer(serializers.ModelSerializer):
    # serializuje dane z omdb. Wszystkie pola są serializowane #

    ratings = RatingSerializer(many=True, required=False)

    def create(self, validated_data):
        ratings_data = validated_data.pop('ratings', '')
        movie = Movie.objects.create(**validated_data)
        for rating in ratings_data:
            Rating.objects.create(movie=movie, **rating)
        return movie

    class Meta:
        model = Movie
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
     #serializer dla komentarzy #

    class Meta:
        model = Comment
        fields = '__all__'
