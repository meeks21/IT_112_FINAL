from django.test import TestCase
from .models import Artist, SongName, Review

# Create your tests here.
class ArtistTest(TestCase):
    def setUp(self):
        self.type=Artist(artistname='test artist')

    def test_typestring(self):
        self.assertEqual(str(self.type), 'test artist')
    
    
    def test_tablename(self):
        self.assertEqual(str(Artist._meta.db_table), 'songname')

class SongNameTest(TestCase):
    def setUp(self):
        self.type=SongName(songname='test song')

    def test_typestring(self):
        self.assertEqual(str(self.type), 'test song')
    
    
    def test_tablename(self):
        self.assertEqual(str(SongName._meta.db_table), 'artist')

class Title(TestCase):
    def setUp(self):
        self.type=Review(title='test review')

    def test_typestring(self):
        self.assertEqual(str(self.type), 'test review')
    
    
    def test_tablename(self):
        self.assertEqual(str(Review._meta.db_table), 'review')


