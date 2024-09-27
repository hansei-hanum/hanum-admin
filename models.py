# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Efmigrationshistory(models.Model):
    migrationid = models.CharField(db_column='MigrationId', primary_key=True, max_length=150)  # Field name made lowercase.
    productversion = models.CharField(db_column='ProductVersion', max_length=32)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '__EFMigrationsHistory'


class ArticleComments(models.Model):
    id = models.BigAutoField(primary_key=True, db_comment='��� ID')
    articleid = models.ForeignKey('Articles', models.DO_NOTHING, db_column='articleId', db_comment='�Խñ� ID')  # Field name made lowercase.
    parentid = models.ForeignKey('self', models.DO_NOTHING, db_column='parentId', blank=True, null=True, db_comment='�θ� ��� ID')  # Field name made lowercase.
    authorid = models.PositiveBigIntegerField(db_column='authorId', db_comment='�ۼ��� ID')  # Field name made lowercase.
    isanonymous = models.IntegerField(db_column='isAnonymous', db_comment='�͸� ����')  # Field name made lowercase.
    content = models.CharField(max_length=1000, blank=True, null=True, db_comment='��� ����')
    createdat = models.DateTimeField(db_column='createdAt', db_comment='��� ���� ��¥')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt', blank=True, null=True, db_comment='��� ���� ��¥')  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='deletedAt', blank=True, null=True, db_comment='��� ���� ��¥')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'article_comments'
        db_table_comment = '�Խñ� ���, ��� ���̺�'


class ArticleImages(models.Model):
    id = models.BigAutoField(primary_key=True, db_comment='�Խñ� ���� ID')
    articleid = models.ForeignKey('Articles', models.DO_NOTHING, db_column='articleId', db_comment='�Խñ� ID')  # Field name made lowercase.
    commentid = models.ForeignKey(ArticleComments, models.DO_NOTHING, db_column='commentId', blank=True, null=True, db_comment='��� ID')  # Field name made lowercase.
    imageid = models.ForeignKey('Images', models.DO_NOTHING, db_column='imageId', db_comment='���� ID')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='createdAt', db_comment='�Խñ� ���� �߰� ��¥')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'article_images'
        db_table_comment = '�Խñ�, ��� ��� ���� ���̺�'


class ArticleReactions(models.Model):
    id = models.BigAutoField(primary_key=True, db_comment='�Խñ� ���� ID')
    articleid = models.ForeignKey('Articles', models.DO_NOTHING, db_column='articleId', db_comment='�Խñ� ID')  # Field name made lowercase.
    commentid = models.ForeignKey(ArticleComments, models.DO_NOTHING, db_column='commentId', blank=True, null=True, db_comment='��� ID')  # Field name made lowercase.
    authorid = models.PositiveBigIntegerField(db_column='authorId', db_comment='�ۼ��� ID')  # Field name made lowercase.
    reaction = models.CharField(max_length=50, blank=True, null=True, db_comment='����')
    createdat = models.DateTimeField(db_column='createdAt', db_comment='���� ��¥')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt', blank=True, null=True, db_comment='���� ���� ��¥')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'article_reactions'
        db_table_comment = '�Խñ� �� ���, ��� ���� ���̺�'


class Articles(models.Model):
    id = models.BigAutoField(primary_key=True, db_comment='�Խñ� ID')
    authorid = models.PositiveBigIntegerField(db_column='authorId', db_comment='�ۼ��� ID')  # Field name made lowercase.
    authernickname = models.CharField(db_column='autherNickname', max_length=50, blank=True, null=True, db_comment='�͸� �ۼ��� �̸�')  # Field name made lowercase.
    isanonymous = models.IntegerField(db_column='isAnonymous', db_comment='�͸� ����')  # Field name made lowercase.
    scope = models.PositiveIntegerField(blank=True, null=True, db_comment='���� ����')
    cluster = models.PositiveIntegerField(blank=True, null=True, db_comment='���� �׷�')
    content = models.CharField(max_length=10000, db_comment='�Խñ� ����')
    createdat = models.DateTimeField(db_column='createdAt', db_comment='�Խñ� ���� ��¥')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt', blank=True, null=True, db_comment='�Խñ� ���� ��¥')  # Field name made lowercase.
    deletedat = models.DateTimeField(db_column='deletedAt', blank=True, null=True, db_comment='�Խñ� ���� ��¥')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'articles'
        db_table_comment = '�Խñ� ���̺�'


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


class Images(models.Model):
    id = models.BigAutoField(primary_key=True, db_comment='���� ID')
    filename = models.CharField(max_length=256, db_comment='���� ���ϸ�')
    thumbnail = models.CharField(max_length=256, db_comment='����� ����')
    original = models.CharField(max_length=256, db_comment='���� ����')
    createdat = models.DateTimeField(db_column='createdAt', db_comment='���� ���� ��¥')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'images'
        db_table_comment = 'Ŀ�´�Ƽ �̹��� ���̺�'


class UserBlocks(models.Model):
    id = models.BigAutoField(primary_key=True, db_comment='����� ���� ID')
    userid = models.PositiveBigIntegerField(db_column='userId', db_comment='������ ����� ID')  # Field name made lowercase.
    targetid = models.PositiveBigIntegerField(db_column='targetId', db_comment='���� ��� ����� ID')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='createdAt', db_comment='������ ��¥')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user_blocks'
        db_table_comment = '����� ���� ���̺�'
