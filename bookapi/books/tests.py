from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Book

# Create your tests here.
class BookAPITests(APITestCase):
    def setUp(self):
        self.book_data = {
            "title": "Test Book",
            "author": "Jane Doe",
            "isbn": "1234567890123",
            "published_date": "2022-01-01"
        }
        self.book = Book.objects.create(**self.book_data)
        self.list_url = reverse('book-list')  # from DRF router
        self.detail_url = reverse('book-detail', args=[self.book.id])

    def test_create_book(self):
        """✅ Test creating a new book (POST /api/books/)"""
        new_data = {
            "title": "New Book",
            "author": "John Smith",
            "isbn": "9876543210123",
            "published_date": "2021-12-31"
        }
        response = self.client.post(self.list_url, new_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_get_book_list(self):
        """✅ Test retrieving list of books (GET /api/books/)"""
        response = self.client.get(self.list_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], self.book.title)

    def test_delete_book(self):
        """✅ Test deleting a book (DELETE /api/books/{id}/)"""
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)
