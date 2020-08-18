from django.db import models
from datetime import datetime, timedelta

# Create your models here.

class Note(models.Model):
    noteNumber = models.CharField(max_length=10, unique=True,error_messages={'unique':"Số phiếu này đã có"}, verbose_name="Số phiếu")
    customers = models.CharField(max_length=50, null=False, verbose_name="Khách hàng")
    receiveDay = models.DateField(null=False, verbose_name="Ngày tiếp nhận")
    note = models.TextField(blank=True, verbose_name="Ghi chú")

    def __str__(self):
        return f"{self.noteNumber} - {self.customers} - {self.receiveDay}"

class Item(models.Model):
    group = [
        ("TIDAU24", "TI dầu 24kV"),
        ("TUDAU24","TU dầu 24kV"),
        ("TIKHO24I", "TI khô 24kV trong nhà"),
        ("TIKHO24O", "TI khô 24kV ngoài trời"),
        ("TIHT", "TI hạ thế"),
    ]
    noteNumber = models.ForeignKey(Note, on_delete=models.CASCADE, related_name="item", verbose_name="Phiếu tiếp nhận")
    itemName = models.CharField(max_length=60, verbose_name="Tên sản phẩm")
    quantity = models.IntegerField(null=False, verbose_name="Số lượng")
    itemGroup = models.CharField(max_length=10, choices=group, verbose_name="Nhóm sản phẩm")
    status = models.CharField(max_length=128, blank=True, verbose_name="Tình trạng tiếp nhận")
    check = models.CharField(max_length=128, blank=True, verbose_name="Đánh giá")
    conclude = models.CharField(max_length=128, blank=True, verbose_name="Kết luận")
    deadline = models.DateField(verbose_name="Deadline")
    note = models.TextField(blank=True)
    done = models.BooleanField(choices=[(True, "Xong"), (False, "Chưa xong")], default=False)
    #null=False, default=(datetime.now() + timedelta(days=2)).date()

    def __str__(self):
        return f"{self.itemName} -> {self.noteNumber}"

class ItemLog(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="log", verbose_name="Sản phẩm")
    content = models.TextField(blank=False, verbose_name="Nội dung")
    date = models.DateField(null=False, verbose_name="Ngày thực hiện")
    note = models.TextField(blank=True, verbose_name="Ghi chú")

    def __str__(self):
        return f"{self.item} - {self.content} - {self.date}"