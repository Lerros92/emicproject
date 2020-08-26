from django.db import models
from datetime import datetime, timedelta
from django.core.validators import MinValueValidator

# Create your models here.

class Note(models.Model):
    customerGroup = [
        ('DAILY', 'Đại lý'),
        ('NPC', 'NPC'),
        ('SPC', 'SPC'),
    ]
    noteNumber = models.CharField(max_length=10, unique=True,error_messages={'unique':"Số phiếu này đã có"}, verbose_name="Số phiếu")
    customers = models.CharField(max_length=50, null=False, verbose_name="Khách hàng")
    customersObj = models.CharField(choices=customerGroup, max_length=50, verbose_name="Nhóm khách hàng", null=True)
    receiveDay = models.DateField(null=False, verbose_name="Ngày tiếp nhận")
    note = models.TextField(blank=True, verbose_name="Ghi chú")
    numOrder = models.IntegerField(verbose_name="Thứ tự", null=True)

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
    quantity = models.IntegerField(null=False, verbose_name="Số lượng", validators=[MinValueValidator(1)], )
    itemGroup = models.CharField(max_length=10, choices=group, verbose_name="Nhóm sản phẩm")
    status = models.CharField(max_length=128, blank=True, verbose_name="Tình trạng tiếp nhận")
    check = models.CharField(max_length=128, blank=True, verbose_name="Đánh giá")
    conclude = models.CharField(max_length=128, blank=True, verbose_name="Kết luận")
    deadline = models.DateField()
    note = models.TextField(blank=True, verbose_name="Ghi chú")
    numExport = models.CharField(max_length=10, verbose_name="Số phiếu xuất", blank=True)
    dayExport = models.DateField(verbose_name="Ngày xuất", null=True, blank=True)
    done = models.BooleanField(verbose_name="Xong/ Chưa xong:", choices=[(True, "Đã xong"), (False, "Chưa xong")], default=False)
    #null=False, default=(datetime.now() + timedelta(days=2)).date()

    def __str__(self):
        return f"{self.itemName} thuộc phiếu {self.noteNumber}"

class ItemLog(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="log", verbose_name="Sản phẩm")
    content = models.TextField(blank=False, verbose_name="Nội dung")
    date = models.DateField(null=False, verbose_name="Ngày thực hiện")
    note = models.TextField(blank=True, verbose_name="Ghi chú")

    def __str__(self):
        return f"{self.content} ngày {self.date} của sản phẩm {self.item}"