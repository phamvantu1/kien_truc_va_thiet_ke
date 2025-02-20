import os
import django

# Thiết lập môi trường Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pvtu_project01.settings')
django.setup()

from customer.models import customerUser

# Thêm dữ liệu mẫu
users = [
    {"username": "john_doe", "email": "john@example.com", "first_name": "John", "last_name": "Doe", "phone": "0123456789"},
    {"username": "jane_smith", "email": "jane@example.com", "first_name": "Jane", "last_name": "Smith", "phone": "0987654321"},
    {"username": "alice_wonder", "email": "alice@example.com", "first_name": "Alice", "last_name": "Wonder", "phone": "0345678901"},
]

for user in users:
    customerUser.objects.create(**user)

print("Thêm dữ liệu thành công!")
