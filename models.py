from django.db import models


class User(models.Model):
    userId = models.AutoField(primary_key=True)
    password = models.CharField(max_length=45)
    name = models.CharField(max_length=45)
    email_id = models.CharField(max_length=45)
    age = models.IntegerField()
    total_investment = models.DecimalField(max_digits=2, decimal_places=0)
    total_current_value = models.DecimalField(max_digits=2, decimal_places=0)
    total_pl = models.DecimalField(max_digits=2, decimal_places=0)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        # ⭐ To make this human readable
        return f"[{self.userId}] {self.name}"


# Stonks 📈
class Stocks(models.Model):

    class StockType(models.TextChoices):
        FD = 'FD', _('FDs')
        STOCK = 'STOCK', _('Stocks')
        REALESTATE = 'REALESTATE', _('Real Estate')
        MUTUALFUNDS = 'MUTUALFUNDS', _('Mutual Funds')
        COMMODITY = 'COMMODITY', _('Commodities')
        BOND = 'BOND', _('Bonds')

    stockInfoID = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45)
    type = models.CharField(max_length=45)
    type = models.CharField(max_length=45, choices=StockType.choices)
    current_value = models.CharField(max_length=45)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return f"[{self.stockInfoID}] {self.name}"


class CurrentHoldings(models.Model):

    holdingID = models.IntegerField(primary_key=True)
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    investment_in_stock = models.DecimalField(max_digits=2, decimal_places=0)
    profit_loss_ifSoldNow = models.DecimalField(max_digits=2, decimal_places=0)
    StockHoldID = models.ForeignKey(Stocks, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return f"[{self.holdingID}] {self.userID} {self.quantity}"


class Transaction(models.Model):
    transactionID = models.IntegerField(primary_key=True)
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    stockID = models.ForeignKey(Stocks, on_delete=models.CASCADE)
    bought_sold = models.BinaryField(max_length=2)
    dateTime = models.DateTimeField()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return f"[{self.transactionID}] {self.userID} {self.bought_sold} {self.stockID}"


class QuarterlyData:
    stockID = models.IntegerField(primary_key=True)
    dateMonthYear = models.DateField(primary_key=True)
    netIncome = models.DecimalField(max_digits=2, decimal_places=0)
    sharesOutstanding = models.DecimalField(max_digits=2, decimal_places=0)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class YearlyData:
    stockID = models.IntegerField(primary_key=True)
    Year = models.IntegerField(primary_key=True)
    average_stock_value = models.DecimalField(max_digits=2, decimal_places=0)
    outstanding_share = models.DecimalField(max_digits=2, decimal_places=0)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class ValuationStocks:
    stockID = models.IntegerField(primary_key=True)
    date = models.DateField(primary_key=True)
    open = models.DecimalField(max_digits=6, decimal_places=0)
    high = models.DecimalField(max_digits=6, decimal_places=0)
    low = models.DecimalField(max_digits=6, decimal_places=0)
    close = models.DecimalField(max_digits=6, decimal_places=0)
    adj_close = models.DecimalField(max_digits=6, decimal_places=0)
    volume = models.IntegerField()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)