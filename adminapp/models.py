from django.db import models

# Create your models here.
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
        app_label = 'adminapp'
        managed = False
        db_table = 'article_comments'
        db_table_comment = '�Խñ� ���, ��� ���̺�'   
    def __str__(self):
        return self.content if self.content else "(None)"

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
        app_label = 'adminapp'
        managed = False
        db_table = 'articles'
        db_table_comment = '�Խñ� ���̺�'

    def __str__(self):
        return self.content if self.content else "(None)"

class UserBlocks(models.Model):
    id = models.BigAutoField(primary_key=True, db_comment='����� ���� ID')
    userid = models.PositiveBigIntegerField(db_column='userId', db_comment='������ ����� ID')  # Field name made lowercase.
    targetid = models.PositiveBigIntegerField(db_column='targetId', db_comment='���� ��� ����� ID')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='createdAt', db_comment='������ ��¥')  # Field name made lowercase.

    class Meta:
        app_label = 'adminapp'
        managed = False
        db_table = 'user_blocks'
        db_table_comment = '����� ���� ���̺�'

    def __str__(self):
        return self.userid if self.userid else "(None)"

