from MyVideoGames.models import Genre
from ClientIGDB import ClientIGDB


def add_genres():
    """
    Add the genres to database
    """
    # Get all genres from api
    genres = ClientIGDB.api_call("genres", ["name"], 50)

    Genre.objects.all().delete()
    for genre in genres:
        g = Genre.objects.create(name=genre["name"])
        g.save()
