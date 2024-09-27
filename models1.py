# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Eoullimbalances(models.Model):
    id = models.BigAutoField(primary_key=True, db_comment='�ܰ� ���� ID')
    userid = models.OneToOneField('Users', models.DO_NOTHING, db_column='userId', blank=True, null=True, db_comment='����� ID')  # Field name made lowercase.
    boothid = models.OneToOneField('Eoullimbooths', models.DO_NOTHING, db_column='boothId', blank=True, null=True, db_comment='�ν� ID')  # Field name made lowercase.
    amount = models.PositiveBigIntegerField(db_comment='�ܰ� ���� �� �� �ܾ�')
    type = models.CharField(max_length=8, db_comment='�ܰ� �з�')
    comment = models.CharField(max_length=24, blank=True, null=True, db_comment='�ܰ� �޸�')

    class Meta:
        managed = False
        db_table = 'EoullimBalances'
        db_table_comment = '�Ѽ���︲�Ѹ��� �ܰ�'


class Eoullimbooths(models.Model):
    id = models.BigAutoField(primary_key=True, db_comment='�ν� ������ȣ')
    token = models.CharField(unique=True, max_length=16, db_comment='�ν�  ��ū')
    class_field = models.CharField(db_column='class', max_length=24, db_comment='�ν� ����')  # Field renamed because it was a Python reserved word.
    name = models.CharField(max_length=24, db_comment='�ν���')
    location = models.CharField(max_length=64, db_comment='�ν� ��ġ')
    createdat = models.DateTimeField(db_column='createdAt', db_comment='�ν� ���� ��¥')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt', blank=True, null=True, db_comment='�ν� ���� ��¥')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EoullimBooths'
        db_table_comment = '�Ѽ���︲�Ѹ��� �ν�'


class Eoullimpayments(models.Model):
    id = models.BigAutoField(primary_key=True, db_comment='����������ȣ')
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userId', db_comment='������')  # Field name made lowercase.
    boothid = models.ForeignKey(Eoullimbooths, models.DO_NOTHING, db_column='boothId', db_comment='�������')  # Field name made lowercase.
    userbalanceid = models.ForeignKey(Eoullimbalances, models.DO_NOTHING, db_column='userBalanceId', db_comment='�������ܰ������ȣ')  # Field name made lowercase.
    boothbalanceid = models.ForeignKey(Eoullimbalances, models.DO_NOTHING, db_column='boothBalanceId', related_name='eoullimpayments_boothbalanceid_set', db_comment='��������ܰ������ȣ')  # Field name made lowercase.
    paidamount = models.PositiveBigIntegerField(db_column='paidAmount', db_comment='�����ݾ�')  # Field name made lowercase.
    refundedamount = models.PositiveBigIntegerField(db_column='refundedAmount', blank=True, null=True, db_comment='������ұݾ�')  # Field name made lowercase.
    paymenttransactionid = models.PositiveBigIntegerField(db_column='paymentTransactionId', db_comment='����Ʈ����ǰ�����ȣ')  # Field name made lowercase.
    refundtransactionid = models.PositiveBigIntegerField(db_column='refundTransactionId', blank=True, null=True, db_comment='ȯ��Ʈ����ǰ�����ȣ')  # Field name made lowercase.
    paymentcomment = models.CharField(db_column='paymentComment', max_length=24, db_collation='utf8mb4_bin', blank=True, null=True, db_comment='�����޽���')  # Field name made lowercase.
    refundcomment = models.CharField(db_column='refundComment', max_length=24, db_collation='utf8mb4_bin', blank=True, null=True, db_comment='ȯ�Ҹ޽���')  # Field name made lowercase.
    status = models.CharField(max_length=8, db_collation='utf8mb4_bin', db_comment='��������')
    paidtime = models.DateTimeField(db_column='paidTime', db_comment='�����ð�')  # Field name made lowercase.
    refundedtime = models.DateTimeField(db_column='refundedTime', blank=True, null=True, db_comment='������ҽð�')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EoullimPayments'
        db_table_comment = '�Ѽ���︲�Ѹ��� ��������'


class Eoullimtransactions(models.Model):
    id = models.BigAutoField(primary_key=True, db_comment='Ʈ����� ���� ID')
    senderid = models.ForeignKey(Eoullimbalances, models.DO_NOTHING, db_column='senderId', blank=True, null=True, db_comment='�۱��� ID, ȯ������ ��� NULL�� ����')  # Field name made lowercase.
    receiverid = models.ForeignKey(Eoullimbalances, models.DO_NOTHING, db_column='receiverId', related_name='eoullimtransactions_receiverid_set', db_comment='������ ID')  # Field name made lowercase.
    amount = models.PositiveBigIntegerField(db_comment='�۱ݾ�')
    comment = models.CharField(max_length=24, blank=True, null=True, db_comment='�۱� �޸�')
    time = models.DateTimeField(db_comment='Ʈ����� �ð�')

    class Meta:
        managed = False
        db_table = 'EoullimTransactions'
        db_table_comment = '�Ѽ���︲�Ѹ��� ��ü ����'


class Votefields(models.Model):
    id = models.BigAutoField(primary_key=True)
    value = models.CharField(max_length=255)
    vote_table = models.ForeignKey('Votetables', models.DO_NOTHING)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'VoteFields'


class Votetables(models.Model):
    id = models.BigAutoField(primary_key=True)
    active = models.IntegerField()
    start_at = models.DateTimeField()
    end_at = models.DateTimeField()
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'VoteTables'


class Votes(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    vote_table = models.ForeignKey(Votetables, models.DO_NOTHING)
    vote_field = models.ForeignKey(Votefields, models.DO_NOTHING)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'Votes'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Fcmtokens(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    token = models.CharField(max_length=300)
    platform = models.CharField(max_length=7)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'fcmtokens'


class Luckynumbers(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'luckynumbers'


class Luckytokens(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    token = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    used_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'luckytokens'


class Notifications(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    is_announcement = models.IntegerField()
    title = models.CharField(max_length=1000, blank=True, null=True)
    body = models.CharField(max_length=1000, blank=True, null=True)
    link = models.CharField(max_length=1000, blank=True, null=True)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'notifications'


class UserSuspentions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    reason = models.CharField(max_length=100)
    created_at = models.DateTimeField()
    expiry = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user.suspentions'


class Users(models.Model):
    id = models.BigAutoField(primary_key=True)
    phone = models.CharField(unique=True, max_length=11)
    name = models.CharField(max_length=5)
    profile = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'users'


class VerificationKeys(models.Model):
    key = models.CharField(primary_key=True, max_length=6)
    user = models.ForeignKey(Users, models.DO_NOTHING, blank=True, null=True)
    type = models.CharField(max_length=7)
    department = models.CharField(max_length=16, blank=True, null=True)
    grade = models.PositiveIntegerField(blank=True, null=True)
    classroom = models.PositiveIntegerField(blank=True, null=True)
    number = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    valid_until = models.DateTimeField(blank=True, null=True)
    used_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'verification.keys'
