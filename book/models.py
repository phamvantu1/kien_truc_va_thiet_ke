
from djongo import models
from bson import ObjectId
class Book(models.Model):
    _id = models.AutoField(primary_key=True)  # Auto-incrementing primary key
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    price = models.FloatField()

    objects = models.DjongoManager()  # Đảm bảo có dòng này

    class Meta:
        db_table = "book_db"
