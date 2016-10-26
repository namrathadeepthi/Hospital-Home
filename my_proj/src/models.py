# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Disease(models.Model):
    id = models.IntegerField(db_column='ID')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=20)  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=20)  # Field name made lowercase.
    symptoms = models.CharField(db_column='Symptoms', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Disease'
        unique_together = (('name', 'category'),)


class Diseasesymptoms(models.Model):
    diseaseid = models.IntegerField(db_column='DiseaseID')  # Field name made lowercase.
    bodylocation = models.CharField(db_column='BodyLocation', max_length=200, blank=True, null=True)  # Field name made lowercase.
    disease = models.CharField(db_column='Disease', max_length=200, blank=True, null=True)  # Field name made lowercase.
    symptoms = models.CharField(db_column='Symptoms', max_length=10000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DiseaseSymptoms'


class Doctors(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=20, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=20, blank=True, null=True)  # Field name made lowercase.
    specialisation = models.CharField(db_column='Specialisation', max_length=20, blank=True, null=True)  # Field name made lowercase.
    hospital = models.CharField(db_column='Hospital', max_length=20, blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Doctors'


class Healthtips(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tip = models.CharField(db_column='Tip', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HealthTips'


class Hospital(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=55, blank=True, null=True)  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=100, blank=True, null=True)  # Field name made lowercase.
    doctorid = models.ForeignKey(Doctors, models.DO_NOTHING, db_column='DoctorID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Hospital'


class Medicine(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=20, blank=True, null=True)  # Field name made lowercase.
    composition = models.CharField(db_column='Composition', max_length=20, blank=True, null=True)  # Field name made lowercase.
    disease = models.CharField(db_column='Disease', max_length=25, blank=True, null=True)  # Field name made lowercase.
    dosage = models.CharField(db_column='Dosage', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Medicine'


class Users(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=25, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=20, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Users'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
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


class AuthtoolsUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    email = models.CharField(unique=True, max_length=255)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'authtools_user'


class AuthtoolsUserGroups(models.Model):
    user = models.ForeignKey(AuthtoolsUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'authtools_user_groups'
        unique_together = (('user', 'group'),)


class AuthtoolsUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthtoolsUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'authtools_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthtoolsUser, models.DO_NOTHING)

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


class EasyThumbnailsSource(models.Model):
    storage_hash = models.CharField(max_length=40)
    name = models.CharField(max_length=255)
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'easy_thumbnails_source'
        unique_together = (('storage_hash', 'name'),)


class EasyThumbnailsThumbnail(models.Model):
    storage_hash = models.CharField(max_length=40)
    name = models.CharField(max_length=255)
    modified = models.DateTimeField()
    source = models.ForeignKey(EasyThumbnailsSource, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'easy_thumbnails_thumbnail'
        unique_together = (('storage_hash', 'name', 'source'),)


class EasyThumbnailsThumbnaildimensions(models.Model):
    thumbnail = models.ForeignKey(EasyThumbnailsThumbnail, models.DO_NOTHING, unique=True)
    width = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'easy_thumbnails_thumbnaildimensions'


class ProfilesProfile(models.Model):
    user = models.ForeignKey(AuthtoolsUser, models.DO_NOTHING, primary_key=True)
    slug = models.CharField(max_length=32)
    picture = models.CharField(max_length=100, blank=True, null=True)
    bio = models.CharField(max_length=200, blank=True, null=True)
    email_verified = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'profiles_profile'


class SymptomsTfidf(models.Model):
    disease_id = models.IntegerField()
    term = models.CharField(max_length=200, blank=True, null=True)
    term_freq = models.IntegerField(blank=True, null=True)
    norm_tfidf = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'symptoms_tfidf'
