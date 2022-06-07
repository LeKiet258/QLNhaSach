# Generated by Django 4.0.3 on 2022-06-06 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0014_alter_hoadon_da_tra_alter_hoadon_tong_tien'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chitiethoadon',
            name='sach',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='book.sach', verbose_name='Sách mua'),
        ),
        migrations.AlterField(
            model_name='chitiethoadon',
            name='so_luong',
            field=models.PositiveIntegerField(default=0, null=True, verbose_name='Số lượng'),
        ),
        migrations.AlterField(
            model_name='hoadon',
            name='da_tra',
            field=models.FloatField(default=0, null=True, verbose_name='Đã trả'),
        ),
        migrations.AlterField(
            model_name='hoadon',
            name='ngay_lap_HD',
            field=models.DateTimeField(null=True, verbose_name='Ngày lập hóa đơn'),
        ),
        migrations.AlterField(
            model_name='hoadon',
            name='tong_tien',
            field=models.FloatField(default=0, null=True, verbose_name='Tổng tiền'),
        ),
        migrations.AlterField(
            model_name='person',
            name='profile_pic',
            field=models.ImageField(blank=True, default='profile1.png', null=True, upload_to='', verbose_name='Ảnh đại diện'),
        ),
        migrations.AlterField(
            model_name='sach',
            name='don_gia',
            field=models.PositiveBigIntegerField(null=True, verbose_name='Đơn giá'),
        ),
        migrations.AlterField(
            model_name='sach',
            name='gia_ban',
            field=models.PositiveBigIntegerField(null=True, verbose_name='Giá bán'),
        ),
        migrations.AlterField(
            model_name='sach',
            name='nam_xuat_ban',
            field=models.PositiveIntegerField(null=True, verbose_name='Năm xuất bản'),
        ),
        migrations.AlterField(
            model_name='sach',
            name='ngay_nhap',
            field=models.DateField(null=True, verbose_name='Ngày nhập'),
        ),
        migrations.AlterField(
            model_name='sach',
            name='nguoi_nhap',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='book.person', verbose_name='Người nhập'),
        ),
        migrations.AlterField(
            model_name='sach',
            name='nha_xuat_ban',
            field=models.CharField(max_length=100, null=True, verbose_name='Nhà xuất bản'),
        ),
        migrations.AlterField(
            model_name='sach',
            name='so_luong',
            field=models.PositiveIntegerField(null=True, verbose_name='Số lượng'),
        ),
        migrations.AlterField(
            model_name='sach',
            name='tac_gia',
            field=models.CharField(max_length=100, null=True, verbose_name='Tác giả'),
        ),
        migrations.AlterField(
            model_name='sach',
            name='ten_sach',
            field=models.CharField(max_length=100, null=True, verbose_name='Tên sách'),
        ),
        migrations.AlterField(
            model_name='sach',
            name='the_loai',
            field=models.CharField(max_length=100, null=True, verbose_name='Thể loại'),
        ),
    ]
