# Generated by Django 3.1.7 on 2021-10-23 23:52

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('ClientID', models.AutoField(default=100000, primary_key=True, serialize=False)),
                ('ClientName', models.CharField(max_length=200)),
                ('ClientType', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Expertise',
            fields=[
                ('UserID', models.AutoField(default=100000, primary_key=True, serialize=False)),
                ('Test_Standard', models.CharField(max_length=50)),
                ('Certification', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Factory_Inspection',
            fields=[
                ('ID', models.AutoField(default=100000, primary_key=True, serialize=False)),
                ('LocationID', models.IntegerField(default=0)),
                ('Report', models.IntegerField(default=0)),
                ('Date', models.DateField(default=datetime.date.today)),
                ('Inspector', models.CharField(max_length=200)),
                ('Inspection_Sequence', models.IntegerField(default=0)),
                ('Certificate', models.CharField(max_length=200)),
                ('Findings', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('Model_Num', models.AutoField(default=100000, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('Cell_Technology', models.CharField(max_length=200)),
                ('Cell_Manufacturer', models.CharField(max_length=250)),
                ('Numberof_Cells', models.IntegerField(default=0)),
                ('Numberof_Cells_Series', models.IntegerField(default=0)),
                ('Numberof_Cells_Strings', models.IntegerField(default=0)),
                ('Numberof_Diodes', models.IntegerField(default=0)),
                ('Product_Length', models.IntegerField(default=0)),
                ('Product_Width', models.IntegerField(default=0)),
                ('Product_Weight', models.IntegerField(default=0)),
                ('Superstrate_type', models.CharField(max_length=200)),
                ('Superstrate_Manufacturer', models.CharField(max_length=200)),
                ('Frame_type', models.CharField(max_length=200)),
                ('Frame_adhesive', models.CharField(max_length=200)),
                ('encapsulate_type', models.CharField(max_length=200)),
                ('encapsulate_Manufacturer', models.CharField(max_length=200)),
                ('Junction_type', models.CharField(max_length=200)),
                ('Juntion_Box_Manufacturer', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Product_Factory',
            fields=[
                ('LocationID', models.AutoField(default=100000, primary_key=True, serialize=False)),
                ('ProductID', models.IntegerField(default=0)),
                ('Contact', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Test_Seqence',
            fields=[
                ('SequenceId', models.AutoField(default=100000, primary_key=True, serialize=False)),
                ('Sequence_Name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Test_Standard',
            fields=[
                ('StandardID', models.AutoField(default=100000, primary_key=True, serialize=False)),
                ('Standard_Name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=250)),
                ('Published_Date', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('UserID', models.AutoField(default=100000, primary_key=True, serialize=False)),
                ('firstName', models.CharField(max_length=200)),
                ('middlename', models.CharField(max_length=200)),
                ('lastname', models.CharField(max_length=200)),
                ('jobtitle', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('officephone', models.IntegerField(default=0)),
                ('cellphone', models.IntegerField(default=0)),
                ('prefix', models.CharField(choices=[('Mister', 'Mr.'), ('Miss', 'Miss'), ('Misses', 'Mrs.')], max_length=200)),
                ('ClientID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.client')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('ServiceID', models.AutoField(default=100000, primary_key=True, serialize=False)),
                ('ServiceName', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=250)),
                ('is_FI_required', models.CharField(max_length=200)),
                ('FI_frequency', models.CharField(max_length=200)),
                ('StandardID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.test_standard')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('LocationID', models.AutoField(default=100000, primary_key=True, serialize=False)),
                ('address1', models.CharField(max_length=200)),
                ('address2', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('postalcode', models.IntegerField(default=0)),
                ('country', models.CharField(max_length=50)),
                ('phonenumber', models.IntegerField(default=0)),
                ('faxnumber', models.IntegerField(default=0)),
                ('ClientID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.client')),
            ],
        ),
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('ID', models.AutoField(default=100000, primary_key=True, serialize=False)),
                ('Report_Number', models.IntegerField(default=0)),
                ('Cert_Issue_Date', models.DateField(default=datetime.date.today)),
                ('LocationID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.location')),
                ('Model_Num', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.product')),
                ('StandardID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.test_standard')),
                ('UserID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.user')),
            ],
        ),
        migrations.CreateModel(
            name='Performance_Data',
            fields=[
                ('Model_Num', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='backend.product')),
                ('Max_System_Voltage', models.IntegerField(default=0)),
                ('Open_Circuit_Voltage', models.IntegerField(default=0)),
                ('Short_Circuit_Current', models.IntegerField(default=0)),
                ('Voltage_at_Max_Power', models.IntegerField(default=0)),
                ('Current_at_Max_Power', models.IntegerField(default=0)),
                ('Max_Power_Output', models.IntegerField(default=0)),
                ('Fill_Factor', models.IntegerField(default=0)),
                ('SequenceId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.test_seqence')),
            ],
        ),
    ]
