# from django.test import TestCase
# from rest_framework.test import APIClient
# from rest_framework import status
# from .models import Book
#
# class BookTests(TestCase):
#     def setUp(self):
#         self.client = APIClient()
#         self.book_data = {
#             'title': 'Test Book',
#             'author': 'Test Author',
#             'published_date': '2023-01-01',
#             'price': 9.99
#         }
#         self.book = Book.objects.create(**self.book_data)
#
#     def test_get_books(self):
#         response = self.client.get('/books/')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#     def test_add_book(self):
#         response = self.client.post('/books/add/', self.book_data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#
#     def test_update_book(self):
#         updated_data = self.book_data.copy()
#         updated_data['title'] = 'Updated Test Book'
#         response = self.client.put(f'/books/update/{self.book.pk}/', updated_data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#     def test_delete_book(self):
#         response = self.client.delete(f'/books/delete/{self.book.pk}/')
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)







from pymongo import MongoClient

# Kết nối tới MongoDB
client = MongoClient("mongodb://localhost:27017/")  # Thay đổi nếu có user/pass

# Chọn database và collection
db = client["book_db"]  # Tên database
collection = db["book_db"]  # Tên collection

# Dữ liệu cần thêm
book = {
    "title": "Django for Beginners",
    "author": "William S. Vincent phamtu",
    "price": 25.99
}

# Chèn vào MongoDB
inserted_id = collection.insert_one(book).inserted_id
print(f"Đã thêm sách với ID: {inserted_id}")



