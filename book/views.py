from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer
from pymongo import MongoClient
from bson import ObjectId  # Import ObjectId để làm việc với MongoDB ID

client = MongoClient('mongodb://localhost:27017/')
db = client['book_db']
collection = db['book_db']
@api_view(['GET'])
def get_books(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_book(request):
    try:
        # Lấy dữ liệu từ request
        data = request.data
        title = data.get("title")
        author = data.get("author")
        price = data.get("price")

        if not title or not author or price is None:
            return Response({"error": "Thiếu dữ liệu"}, status=400)

        # Chèn dữ liệu vào MongoDB
        book = {"title": title, "author": author, "price": price}
        inserted_id = collection.insert_one(book).inserted_id

        return Response({"message": "Đã thêm sách", "id": str(inserted_id)}, status=201)
    except Exception as e:
        return Response({"error": str(e)}, status=500)

@api_view(['PUT'])
def update_book(request, pk):
    try:
        # Chuyển đổi pk sang ObjectId nếu hợp lệ
        if not ObjectId.is_valid(pk):
            return Response({"error": "ID không hợp lệ"}, status=status.HTTP_400_BAD_REQUEST)

        # Kiểm tra xem sách có tồn tại không
        book = collection.find_one({"_id": ObjectId(pk)})
        if not book:
            return Response({"error": "Không tìm thấy sách"}, status=status.HTTP_404_NOT_FOUND)

        # Lấy dữ liệu mới từ request
        data = request.data
        update_fields = {}

        if "title" in data:
            update_fields["title"] = data["title"]
        if "author" in data:
            update_fields["author"] = data["author"]
        if "price" in data:
            update_fields["price"] = data["price"]

        if not update_fields:
            return Response({"error": "Không có dữ liệu để cập nhật"}, status=status.HTTP_400_BAD_REQUEST)

        # Cập nhật dữ liệu trong MongoDB
        collection.update_one({"_id": ObjectId(pk)}, {"$set": update_fields})

        return Response({"message": "Cập nhật thành công"}, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['DELETE'])
def delete_book(request, pk):
    try:
        # Kiểm tra xem pk có hợp lệ không
        if not ObjectId.is_valid(pk):
            return Response({"error": "ID không hợp lệ"}, status=status.HTTP_400_BAD_REQUEST)

        # Kiểm tra xem sách có tồn tại không
        book = collection.find_one({"_id": ObjectId(pk)})
        if not book:
            return Response({"error": "Không tìm thấy sách"}, status=status.HTTP_404_NOT_FOUND)

        # Xóa sách khỏi MongoDB
        collection.delete_one({"_id": ObjectId(pk)})

        return Response({"message": "Xóa sách thành công"}, status=status.HTTP_204_NO_CONTENT)

    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)