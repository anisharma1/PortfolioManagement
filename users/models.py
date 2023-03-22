# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class CurrentHoldings(models.Model):
    holdingid = models.IntegerField(db_column='holdingID', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userID')  # Field name made lowercase.
    quantity = models.IntegerField()
    investment_in_stock = models.IntegerField()
    stockholdid = models.ForeignKey('Stocks', models.DO_NOTHING, db_column='StockHoldID')  # Field name made lowercase.

    class Meta:
        
        db_table = 'current_holdings'


class Eps(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    date = models.TextField(blank=True, null=True)
    epscalculated = models.FloatField(db_column='epsCalculated', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'eps'


class Marketcap(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    year = models.IntegerField(blank=True, null=True)
    mccalculated = models.FloatField(db_column='mcCalculated', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'marketcap'


class PL(models.Model):
    userid = models.OneToOneField('Users', models.DO_NOTHING, db_column='userid', primary_key=True)
    stockid = models.ForeignKey('Stocks', models.DO_NOTHING, db_column='stockid')
    p_l = models.FloatField()

    class Meta:
        
        db_table = 'p_l'
        unique_together = (('userid', 'stockid'),)


class QuarterlyData(models.Model):
    stockid = models.IntegerField(db_column='stockID')  # Field name made lowercase.
    datemonthyear = models.TextField(db_column='dateMonthYear')  # Field name made lowercase.
    netincome = models.TextField(db_column='netIncome', blank=True, null=True)  # Field name made lowercase.
    sharesoutsanding = models.IntegerField(db_column='sharesOutsanding', blank=True, null=True)  # Field name made lowercase.
    quarterly_id = models.IntegerField(primary_key=True)

    class Meta:
        
        db_table = 'quarterly_data'


class Stocks(models.Model):
    stockinfoid = models.IntegerField(db_column='stockInfoID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=45)
    type = models.CharField(max_length=45)
    current_value = models.IntegerField()

    class Meta:
        
        db_table = 'stocks'


class Transaction(models.Model):
    transactionid = models.IntegerField(db_column='transactionID', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userID')  # Field name made lowercase.
    stockid = models.ForeignKey(Stocks, models.DO_NOTHING, db_column='stockID')  # Field name made lowercase.
    investment = models.IntegerField()
    quantity = models.IntegerField()

    class Meta:
        
        db_table = 'transaction'


class Users(models.Model):
    userid = models.AutoField(db_column='userID', primary_key=True)  # Field name made lowercase.
    password = models.CharField(max_length=45)
    name = models.CharField(max_length=45)
    email_id = models.CharField(unique=True, max_length=45)
    age = models.IntegerField()
    total_investment = models.IntegerField()
    total_current_value = models.IntegerField()
    total_pl = models.IntegerField()

    class Meta:
        
        db_table = 'users'


class ValuationStocks(models.Model):
    stockid = models.IntegerField(db_column='stockId')  # Field name made lowercase.
    date = models.TextField(blank=True, null=True)
    open = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    adj_close = models.FloatField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    valuation_id = models.IntegerField(primary_key=True)

    class Meta:
        
        db_table = 'valuation_stocks'


class YearlyData(models.Model):
    stockid = models.IntegerField(db_column='StockID')  # Field name made lowercase.
    year = models.IntegerField(db_column='Year', blank=True, null=True)  # Field name made lowercase.
    average_stock_value = models.FloatField(blank=True, null=True)
    outstanding_share = models.IntegerField(blank=True, null=True)
    yearly_id = models.IntegerField(primary_key=True)

    class Meta:
        
        db_table = 'yearly_data'
