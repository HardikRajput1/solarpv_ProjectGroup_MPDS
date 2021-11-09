from django.db import models
from datetime import date

# Create your models here.
class Client(models.Model):
    ClientID = models. AutoField(primary_key=True, default=100000)
    ClientName = models.CharField(max_length=200)
    ClientType = models.CharField(max_length=200)

    def __str__(self):
        return self.ClientName+' '+self.ClientType

class User(models.Model):
    UserID = models. AutoField(primary_key=True, default=100000)
    ClientID = models.ForeignKey(Client, on_delete=models.CASCADE)
    firstName = models.CharField(max_length=200)
    middlename = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    jobtitle = models.CharField(max_length=200)
    email = models.EmailField()
    officephone = models.IntegerField(default=0)
    cellphone = models.IntegerField(default=0)
    CHOICES = [('Mister', 'Mr.'),('Miss','Miss'),('Misses','Mrs.')]
    prefix = models.CharField(max_length=200, choices=CHOICES)

class Location(models.Model):
    LocationID = models. AutoField(primary_key=True, default=100000)
    ClientID = models.ForeignKey(Client, on_delete=models.CASCADE)
    address1 = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    postalcode = models.IntegerField(default=0)
    country = models.CharField(max_length=50)
    phonenumber = models.IntegerField(default=0)
    faxnumber = models.IntegerField(default=0)

class Test_Standard(models.Model):
    StandardID = models. AutoField(primary_key=True, default=100000)
    Standard_Name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    Published_Date = models.DateField(default=date.today)

class Service(models.Model):
    ServiceID = models. AutoField(primary_key=True, default=100000)
    ServiceName = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    is_FI_required = models.CharField(max_length=200)
    FI_frequency = models.CharField(max_length=200)
    StandardID = models.ForeignKey(Test_Standard, on_delete=models.CASCADE)


class Product(models.Model):
    Model_Num = models. AutoField(primary_key=True, default=100000)
    name = models.CharField(max_length=200)
    Cell_Technology = models.CharField(max_length=200)
    Cell_Manufacturer = models.CharField(max_length=250)
    Numberof_Cells = models.IntegerField(default=0)
    Numberof_Cells_Series = models.IntegerField(default=0)
    Numberof_Cells_Strings = models.IntegerField(default=0)
    Numberof_Diodes = models.IntegerField(default=0)
    Product_Length = models.IntegerField(default=0)
    Product_Width = models.IntegerField(default=0)
    Product_Weight = models.IntegerField(default=0)
    Superstrate_type = models.CharField(max_length=200)
    Superstrate_Manufacturer = models.CharField(max_length=200)
    Frame_type = models.CharField(max_length=200)
    Frame_adhesive = models.CharField(max_length=200)
    encapsulate_type = models.CharField(max_length=200)
    encapsulate_Manufacturer = models.CharField(max_length=200)
    Junction_type = models.CharField(max_length=200)
    Juntion_Box_Manufacturer = models.CharField(max_length=200)

class Test_Seqence(models.Model):
    SequenceId = models. AutoField(primary_key=True, default=100000)
    Sequence_Name = models.CharField(max_length=200)

class Performance_Data(models.Model):
    Model_Num = models.ForeignKey(Product, primary_key=True, on_delete=models.CASCADE)
    SequenceId = models.ForeignKey(Test_Seqence, on_delete=models.CASCADE)
    Max_System_Voltage = models.IntegerField(default=0)
    Open_Circuit_Voltage = models.IntegerField(default=0)
    Short_Circuit_Current = models.IntegerField(default=0)
    Voltage_at_Max_Power = models.IntegerField(default=0)
    Current_at_Max_Power = models.IntegerField(default=0)
    Max_Power_Output = models.IntegerField(default=0)
    Fill_Factor = models.IntegerField(default=0)


class Product_Factory(models.Model):
    LocationID = models. AutoField(primary_key=True, default=100000)
    ProductID = models.IntegerField(default=0)
    Contact = models.IntegerField(default=0)

class Certificate(models.Model):
    ID = models. AutoField(primary_key=True, default=100000)
    UserID = models.ForeignKey(User, on_delete=models.CASCADE)
    LocationID = models.ForeignKey(Location, on_delete=models.CASCADE)
    Report_Number = models.IntegerField(default=0)
    StandardID = models.ForeignKey(Test_Standard, on_delete=models.CASCADE)
    Cert_Issue_Date = models.DateField(default=date.today)
    Model_Num = models.ForeignKey(Product, on_delete=models.CASCADE)

class Factory_Inspection(models.Model):
    ID = models. AutoField(primary_key=True, default=100000)
    LocationID = models.IntegerField(default=0)
    Report = models.IntegerField(default=0)
    Date = models.DateField(default=date.today)
    Inspector = models.CharField(max_length=200)
    Inspection_Sequence = models.IntegerField(default=0)
    Certificate = models.CharField(max_length=200)
    Findings = models.CharField(max_length=200)

class Expertise(models.Model):
    UserID = models. AutoField(primary_key=True, default=100000)
    Test_Standard = models.CharField(max_length=50)
    Certification = models.CharField(max_length=50)