# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AccessType(models.Model):
    id = models.CharField(primary_key=True, max_length=5)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'access_type'


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
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
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


class Bd(models.Model):
    unit = models.TextField(primary_key=True)  # The composite primary key (unit, date) found, that is not supported. The first column is selected. This field type is a guess.
    date = models.IntegerField()
    tank = models.TextField(blank=True, null=True)  # This field type is a guess.
    fdfqi = models.TextField(blank=True, null=True)  # This field type is a guess.
    prfqi = models.TextField(blank=True, null=True)  # This field type is a guess.
    capfqi = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'bd'
        unique_together = (('unit', 'date'),)


class Chemical(models.Model):
    chemical = models.CharField(primary_key=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'chemical'


class Comment(models.Model):
    date = models.IntegerField(primary_key=True)  # The composite primary key (date, comment) found, that is not supported. The first column is selected.
    comment = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'comment'
        unique_together = (('date', 'comment'),)


class Customer(models.Model):
    name = models.OneToOneField('Fl', models.DO_NOTHING, db_column='name', primary_key=True)  # The composite primary key (name, src, fluid, start_date) found, that is not supported. The first column is selected.
    pname = models.CharField(max_length=50, blank=True, null=True)
    src = models.ForeignKey('Fl', models.DO_NOTHING, db_column='src', related_name='customer_src_set')
    fluid = models.ForeignKey('Fluid', models.DO_NOTHING, db_column='fluid')
    start_date = models.IntegerField()
    end_date = models.IntegerField(blank=True, null=True)
    fqi = models.ForeignKey('Ttag', models.DO_NOTHING, db_column='fqi', blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    row = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer'
        unique_together = (('name', 'src', 'fluid', 'start_date'),)


class DailyProblemReason(models.Model):
    date = models.IntegerField(primary_key=True)
    reason = models.ForeignKey('FaultReason', models.DO_NOTHING, db_column='reason', blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'daily_problem_reason'


class DailyProductionOutage(models.Model):
    date = models.IntegerField(primary_key=True)  # The composite primary key (date, unit_list) found, that is not supported. The first column is selected.
    unit_list = models.TextField()  # This field type is a guess.
    outage_reason = models.ForeignKey('ProductionOutageReason', models.DO_NOTHING, db_column='outage_reason')
    outage_hours = models.IntegerField()
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'daily_production_outage'
        unique_together = (('date', 'unit_list'),)


class DbLog(models.Model):
    user = models.OneToOneField('Users', models.DO_NOTHING, primary_key=True)  # The composite primary key (user_id, user_no, activity_time, activity_date, activity) found, that is not supported. The first column is selected.
    user_no = models.IntegerField()
    activity_date = models.IntegerField()
    activity_time = models.IntegerField()
    version_no = models.ForeignKey('LogVersion', models.DO_NOTHING, db_column='version_no', blank=True, null=True)
    activity = models.CharField(max_length=50)
    data = models.TextField(blank=True, null=True)  # This field type is a guess.
    description = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'db_log'
        unique_together = (('user', 'user_no', 'activity_time', 'activity_date', 'activity'),)


class DbSession(models.Model):
    user = models.OneToOneField('Users', models.DO_NOTHING, primary_key=True)  # The composite primary key (user_id, user_no, variable_name) found, that is not supported. The first column is selected.
    user_no = models.IntegerField()
    variable_name = models.CharField(max_length=50)
    value = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'db_session'
        unique_together = (('user', 'user_no', 'variable_name'),)


class DbWarning(models.Model):
    date = models.IntegerField(blank=True, null=True)
    detail = models.CharField(max_length=50)
    description = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'db_warning'


class Dc(models.Model):
    date = models.IntegerField(primary_key=True)  # The composite primary key (date, unit, chemical) found, that is not supported. The first column is selected.
    unit = models.TextField()  # This field type is a guess.
    chemical = models.ForeignKey(Chemical, models.DO_NOTHING, db_column='chemical')
    value = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dc'
        unique_together = (('date', 'unit', 'chemical'),)


class Dcs(models.Model):
    tag = models.OneToOneField('Ttag', models.DO_NOTHING, db_column='tag', primary_key=True)  # The composite primary key (tag, date) found, that is not supported. The first column is selected.
    date = models.IntegerField()
    value = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dcs'
        unique_together = (('tag', 'date'),)


class Dcs1H(models.Model):
    tag = models.OneToOneField('Ttag', models.DO_NOTHING, db_column='tag', primary_key=True)  # The composite primary key (tag, date) found, that is not supported. The first column is selected.
    date = models.IntegerField()
    v01 = models.FloatField(blank=True, null=True)
    v02 = models.FloatField(blank=True, null=True)
    v03 = models.FloatField(blank=True, null=True)
    v04 = models.FloatField(blank=True, null=True)
    v05 = models.FloatField(blank=True, null=True)
    v06 = models.FloatField(blank=True, null=True)
    v07 = models.FloatField(blank=True, null=True)
    v08 = models.FloatField(blank=True, null=True)
    v09 = models.FloatField(blank=True, null=True)
    v10 = models.FloatField(blank=True, null=True)
    v11 = models.FloatField(blank=True, null=True)
    v12 = models.FloatField(blank=True, null=True)
    v13 = models.FloatField(blank=True, null=True)
    v14 = models.FloatField(blank=True, null=True)
    v15 = models.FloatField(blank=True, null=True)
    v16 = models.FloatField(blank=True, null=True)
    v17 = models.FloatField(blank=True, null=True)
    v18 = models.FloatField(blank=True, null=True)
    v19 = models.FloatField(blank=True, null=True)
    v20 = models.FloatField(blank=True, null=True)
    v21 = models.FloatField(blank=True, null=True)
    v22 = models.FloatField(blank=True, null=True)
    v23 = models.FloatField(blank=True, null=True)
    v24 = models.FloatField(blank=True, null=True)
    report = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dcs1h'
        unique_together = (('tag', 'date'),)


class Dcs1HFull(models.Model):
    tag = models.OneToOneField('TagFull', models.DO_NOTHING, db_column='tag', primary_key=True)  # The composite primary key (tag, parameter, date) found, that is not supported. The first column is selected.
    parameter = models.CharField(max_length=50)
    date = models.IntegerField()
    v01 = models.FloatField(blank=True, null=True)
    v02 = models.FloatField(blank=True, null=True)
    v03 = models.FloatField(blank=True, null=True)
    v04 = models.FloatField(blank=True, null=True)
    v05 = models.FloatField(blank=True, null=True)
    v06 = models.FloatField(blank=True, null=True)
    v07 = models.FloatField(blank=True, null=True)
    v08 = models.FloatField(blank=True, null=True)
    v09 = models.FloatField(blank=True, null=True)
    v10 = models.FloatField(blank=True, null=True)
    v11 = models.FloatField(blank=True, null=True)
    v12 = models.FloatField(blank=True, null=True)
    v13 = models.FloatField(blank=True, null=True)
    v14 = models.FloatField(blank=True, null=True)
    v15 = models.FloatField(blank=True, null=True)
    v16 = models.FloatField(blank=True, null=True)
    v17 = models.FloatField(blank=True, null=True)
    v18 = models.FloatField(blank=True, null=True)
    v19 = models.FloatField(blank=True, null=True)
    v20 = models.FloatField(blank=True, null=True)
    v21 = models.FloatField(blank=True, null=True)
    v22 = models.FloatField(blank=True, null=True)
    v23 = models.FloatField(blank=True, null=True)
    v24 = models.FloatField(blank=True, null=True)
    report = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dcs1h_full'
        unique_together = (('tag', 'parameter', 'date'),)


class Dcs1M(models.Model):
    tag = models.OneToOneField('Ttag', models.DO_NOTHING, db_column='tag', primary_key=True)  # The composite primary key (tag, date) found, that is not supported. The first column is selected.
    date = models.IntegerField()
    avg = models.FloatField(blank=True, null=True)
    min = models.FloatField(blank=True, null=True)
    max = models.FloatField(blank=True, null=True)
    tavg = models.FloatField(blank=True, null=True)
    tmin = models.FloatField(blank=True, null=True)
    tmax = models.FloatField(blank=True, null=True)
    tno = models.IntegerField(blank=True, null=True)
    report = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dcs1m'
        unique_together = (('tag', 'date'),)


class Dcs1MFull(models.Model):
    tag = models.OneToOneField('TagFull', models.DO_NOTHING, db_column='tag', primary_key=True)  # The composite primary key (tag, parameter, date, time) found, that is not supported. The first column is selected.
    parameter = models.CharField(max_length=50)
    date = models.IntegerField()
    time = models.IntegerField()
    value = models.FloatField(blank=True, null=True)
    report = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dcs1m_full'
        unique_together = (('tag', 'parameter', 'date', 'time'),)


class Dcs1MFullSummary(models.Model):
    tag = models.OneToOneField('TagFullReportMapping', models.DO_NOTHING, db_column='tag', primary_key=True)  # The composite primary key (tag, parameter, date) found, that is not supported. The first column is selected.
    parameter = models.CharField(max_length=50)
    date = models.IntegerField()
    avg = models.FloatField(blank=True, null=True)
    min = models.FloatField(blank=True, null=True)
    max = models.FloatField(blank=True, null=True)
    tavg = models.FloatField(blank=True, null=True)
    tmin = models.FloatField(blank=True, null=True)
    tmax = models.FloatField(blank=True, null=True)
    tno = models.IntegerField(blank=True, null=True)
    report = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dcs1m_full_summary'
        unique_together = (('tag', 'parameter', 'date'),)


class Dcs1Map(models.Model):
    tag = models.OneToOneField('Ttag', models.DO_NOTHING, db_column='tag', primary_key=True)  # The composite primary key (tag, date) found, that is not supported. The first column is selected.
    date = models.IntegerField()
    pno = models.IntegerField(blank=True, null=True)
    pnoto = models.IntegerField(blank=True, null=True)
    ap = models.FloatField(blank=True, null=True)
    nno = models.IntegerField(blank=True, null=True)
    nnoto = models.IntegerField(blank=True, null=True)
    report = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dcs1map'
        unique_together = (('tag', 'date'),)


class Dcs1Mlfl(models.Model):
    tag = models.OneToOneField('Ttag', models.DO_NOTHING, db_column='tag', primary_key=True)  # The composite primary key (tag, date) found, that is not supported. The first column is selected.
    date = models.IntegerField()
    negative = models.IntegerField(blank=True, null=True)
    tnegative = models.IntegerField(blank=True, null=True)
    report = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dcs1mlfl'
        unique_together = (('tag', 'date'),)


class Dcs1Mpsc(models.Model):
    tag = models.OneToOneField('Ttag', models.DO_NOTHING, db_column='tag', primary_key=True)  # The composite primary key (tag, date) found, that is not supported. The first column is selected.
    date = models.IntegerField()
    pno = models.IntegerField(blank=True, null=True)
    psum = models.FloatField(blank=True, null=True)
    pnoto = models.IntegerField(blank=True, null=True)
    psumto = models.FloatField(blank=True, null=True)
    nno = models.IntegerField(blank=True, null=True)
    nnoto = models.IntegerField(blank=True, null=True)
    report = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dcs1mpsc'
        unique_together = (('tag', 'date'),)


class Dcs1SFull(models.Model):
    tag = models.OneToOneField('TagFull', models.DO_NOTHING, db_column='tag', primary_key=True)  # The composite primary key (tag, parameter, date, time) found, that is not supported. The first column is selected.
    parameter = models.CharField(max_length=50)
    date = models.IntegerField()
    time = models.IntegerField()
    value = models.FloatField(blank=True, null=True)
    report = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dcs1s_full'
        unique_together = (('tag', 'parameter', 'date', 'time'),)


class Dcs1SFullSummary(models.Model):
    tag = models.OneToOneField('TagFullReportMapping', models.DO_NOTHING, db_column='tag', primary_key=True)  # The composite primary key (tag, parameter, date) found, that is not supported. The first column is selected.
    parameter = models.CharField(max_length=50)
    date = models.IntegerField()
    avg = models.FloatField(blank=True, null=True)
    min = models.FloatField(blank=True, null=True)
    max = models.FloatField(blank=True, null=True)
    tavg = models.FloatField(blank=True, null=True)
    tmin = models.FloatField(blank=True, null=True)
    tmax = models.FloatField(blank=True, null=True)
    tno = models.IntegerField(blank=True, null=True)
    report = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dcs1s_full_summary'
        unique_together = (('tag', 'parameter', 'date'),)


class Dcs24Havg(models.Model):
    tag = models.OneToOneField('Ttag', models.DO_NOTHING, db_column='tag', primary_key=True)  # The composite primary key (tag, date) found, that is not supported. The first column is selected.
    date = models.IntegerField()
    value = models.FloatField(blank=True, null=True)
    report = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dcs24havg'
        unique_together = (('tag', 'date'),)


class Dcs24HavgFull(models.Model):
    tag = models.OneToOneField('TagFull', models.DO_NOTHING, db_column='tag', primary_key=True)  # The composite primary key (tag, parameter, date) found, that is not supported. The first column is selected.
    parameter = models.CharField(max_length=50)
    date = models.IntegerField()
    value = models.FloatField(blank=True, null=True)
    report = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dcs24havg_full'
        unique_together = (('tag', 'parameter', 'date'),)


class DcsFileName(models.Model):
    id = models.IntegerField(primary_key=True)
    file_name = models.CharField(max_length=100, blank=True, null=True)
    ijdate = models.IntegerField(blank=True, null=True)
    creation_time = models.DateTimeField(blank=True, null=True)
    processing_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dcs_file_name'


class DcsStatusError(models.Model):
    id = models.BigIntegerField(primary_key=True)
    type = models.ForeignKey('DcsStatusErrorType', models.DO_NOTHING, blank=True, null=True)
    ijdate = models.IntegerField(blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    description = models.CharField(max_length=10000, blank=True, null=True)
    file = models.ForeignKey(DcsFileName, models.DO_NOTHING, blank=True, null=True)
    ext_i1 = models.IntegerField(blank=True, null=True)
    ext_i2 = models.IntegerField(blank=True, null=True)
    ext_i3 = models.IntegerField(blank=True, null=True)
    ext_d1 = models.FloatField(blank=True, null=True)
    ext_d2 = models.FloatField(blank=True, null=True)
    ext_d3 = models.FloatField(blank=True, null=True)
    more_info = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'dcs_status_error'


class DcsStatusErrorType(models.Model):
    id = models.IntegerField(primary_key=True)
    category = models.SmallIntegerField(blank=True, null=True)
    system_description = models.CharField(max_length=200, blank=True, null=True)
    user_description = models.CharField(max_length=200, blank=True, null=True)
    comment = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dcs_status_error_type'


class DefaultType(models.Model):
    id = models.CharField(primary_key=True, max_length=5)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'default_type'


class DeviceInTag(models.Model):
    name = models.CharField(primary_key=True, max_length=10)
    fname = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'device_in_tag'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
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


class FactoryTitle(models.Model):
    name = models.CharField(primary_key=True, max_length=50)  # The composite primary key (name, date) found, that is not supported. The first column is selected.
    date = models.IntegerField()
    pname = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'factory_title'
        unique_together = (('name', 'date'),)


class FaultReason(models.Model):
    name = models.CharField(primary_key=True, max_length=50)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fault_reason'


class Fdd(models.Model):
    fqi = models.OneToOneField('Ttag', models.DO_NOTHING, db_column='fqi', primary_key=True)  # The composite primary key (fqi, date) found, that is not supported. The first column is selected.
    date = models.IntegerField()
    fluid = models.ForeignKey('Fluid', models.DO_NOTHING, db_column='fluid', blank=True, null=True)
    dif = models.FloatField(blank=True, null=True)
    munit = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'fdd'
        unique_together = (('fqi', 'date'),)


class Fddp(models.Model):
    src = models.OneToOneField('Fl', models.DO_NOTHING, db_column='src', primary_key=True)  # The composite primary key (src, month) found, that is not supported. The first column is selected.
    month = models.IntegerField()
    plan = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fddp'
        unique_together = (('src', 'month'),)


class Fdmmscfdp(models.Model):
    src = models.OneToOneField('Fl', models.DO_NOTHING, db_column='src', primary_key=True)  # The composite primary key (src, month) found, that is not supported. The first column is selected.
    month = models.IntegerField()
    plan = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fdmmscfdp'
        unique_together = (('src', 'month'),)


class Fdyp(models.Model):
    src = models.OneToOneField('Fl', models.DO_NOTHING, db_column='src', primary_key=True)  # The composite primary key (src, month) found, that is not supported. The first column is selected.
    month = models.IntegerField()
    plan = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fdyp'
        unique_together = (('src', 'month'),)


class Fl(models.Model):
    name = models.CharField(primary_key=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'fl'


class Fluid(models.Model):
    name = models.CharField(primary_key=True, max_length=30)
    ename = models.CharField(max_length=50, blank=True, null=True)
    pname = models.CharField(max_length=50, blank=True, null=True)
    comment = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fluid'


class FluidType(models.Model):
    name = models.OneToOneField(Fluid, models.DO_NOTHING, db_column='name', primary_key=True)  # The composite primary key (name, date) found, that is not supported. The first column is selected.
    date = models.IntegerField()
    type = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'fluid_type'
        unique_together = (('name', 'date'),)


class FqiTemp(models.Model):
    fqi = models.OneToOneField('Ttag', models.DO_NOTHING, db_column='fqi', primary_key=True)  # The composite primary key (fqi, date) found, that is not supported. The first column is selected.
    date = models.IntegerField()
    fluid = models.ForeignKey(Fluid, models.DO_NOTHING, db_column='fluid', blank=True, null=True)
    dif = models.FloatField(blank=True, null=True)
    munit = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'fqi_temp'
        unique_together = (('fqi', 'date'),)


class GasAndOilCo(models.Model):
    meter = models.TextField(primary_key=True)  # The composite primary key (meter, date) found, that is not supported. The first column is selected. This field type is a guess.
    date = models.IntegerField()
    mass = models.FloatField(blank=True, null=True)
    mmscm = models.FloatField(blank=True, null=True)
    c1 = models.FloatField(blank=True, null=True)
    c2 = models.FloatField(blank=True, null=True)
    c3 = models.FloatField(blank=True, null=True)
    c4 = models.FloatField(blank=True, null=True)
    c5p = models.FloatField(blank=True, null=True)
    n2 = models.FloatField(blank=True, null=True)
    co2 = models.FloatField(blank=True, null=True)
    total_sulphur = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gas_and_oil_co'
        unique_together = (('meter', 'date'),)


class LastActivity(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    user_no = models.IntegerField(blank=True, null=True)
    login = models.BooleanField(blank=True, null=True)
    activity_date = models.CharField(max_length=30, blank=True, null=True)
    start_date = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'last_activity'


class LineStock(models.Model):
    date = models.IntegerField(primary_key=True)  # The composite primary key (date, title) found, that is not supported. The first column is selected.
    title = models.CharField(max_length=40)
    fluid = models.ForeignKey(Fluid, models.DO_NOTHING, db_column='fluid', blank=True, null=True)
    stock = models.FloatField()

    class Meta:
        managed = False
        db_table = 'line_stock'
        unique_together = (('date', 'title'),)


class LogVersion(models.Model):
    version_no = models.IntegerField(primary_key=True)  # The composite primary key (version_no, activity) found, that is not supported. The first column is selected.
    activity = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)  # This field type is a guess.
    persian = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log_version'
        unique_together = (('version_no', 'activity'),)


class LogsTb(models.Model):
    created = models.DateTimeField(blank=True, null=True)
    path_name = models.TextField(blank=True, null=True)
    file_name = models.TextField(blank=True, null=True)
    line_number = models.IntegerField(blank=True, null=True)
    log_level = models.TextField(blank=True, null=True)
    log_level_number = models.IntegerField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    report_name = models.TextField(blank=True, null=True)
    user_name = models.TextField(blank=True, null=True)
    db_name = models.TextField(blank=True, null=True)
    tb_name = models.TextField(blank=True, null=True)
    fa_tb_name = models.TextField(blank=True, null=True)
    fa_field_name = models.TextField(blank=True, null=True)
    field_name = models.TextField(blank=True, null=True)
    old_value = models.TextField(blank=True, null=True)
    new_value = models.TextField(blank=True, null=True)
    activity_date = models.TextField(blank=True, null=True)
    activity_time = models.TextField(blank=True, null=True)
    op = models.TextField(blank=True, null=True)
    exc_info = models.TextField(blank=True, null=True)
    computer_name = models.TextField(blank=True, null=True)
    ip = models.TextField(blank=True, null=True)
    browser_name = models.TextField(blank=True, null=True)
    inserted = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'logs_tb'


class Mc(models.Model):
    month = models.IntegerField(primary_key=True)  # The composite primary key (month, unit, chemical) found, that is not supported. The first column is selected.
    unit = models.CharField(max_length=10)
    chemical = models.ForeignKey(Chemical, models.DO_NOTHING, db_column='chemical')
    munit = models.TextField(blank=True, null=True)  # This field type is a guess.
    value = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mc'
        unique_together = (('month', 'unit', 'chemical'),)


class Mcd(models.Model):
    unit = models.CharField(primary_key=True, max_length=10)  # The composite primary key (unit, chemical) found, that is not supported. The first column is selected.
    chemical = models.ForeignKey(Chemical, models.DO_NOTHING, db_column='chemical')
    munit = models.TextField(blank=True, null=True)  # This field type is a guess.
    design = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mcd'
        unique_together = (('unit', 'chemical'),)


class MenuAccess(models.Model):
    menu_level = models.SmallIntegerField(primary_key=True)  # The composite primary key (menu_level, menu_name, role_name) found, that is not supported. The first column is selected.
    menu_name = models.CharField(max_length=256)
    role_name = models.ForeignKey('Roles', models.DO_NOTHING, db_column='role_name')

    class Meta:
        managed = False
        db_table = 'menu_access'
        unique_together = (('menu_level', 'menu_name', 'role_name'),)


class Message(models.Model):
    report = models.OneToOneField('MessageReport', models.DO_NOTHING, db_column='report', primary_key=True)  # The composite primary key (report, date, message) found, that is not supported. The first column is selected.
    date = models.IntegerField()
    message = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'message'
        unique_together = (('report', 'date', 'message'),)


class MessageReport(models.Model):
    report = models.CharField(primary_key=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'message_report'


class PcTitle(models.Model):
    ename = models.TextField(primary_key=True)  # The composite primary key (ename, date) found, that is not supported. The first column is selected. This field type is a guess.
    date = models.IntegerField()
    name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pc_title'
        unique_together = (('ename', 'date'),)


class Post(models.Model):
    name = models.CharField(primary_key=True, max_length=30)
    father_name = models.ForeignKey('self', models.DO_NOTHING, db_column='father_name', blank=True, null=True)
    max_personnel = models.IntegerField(blank=True, null=True)
    access = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'post'


class Prdp(models.Model):
    fluid = models.OneToOneField(Fluid, models.DO_NOTHING, db_column='fluid', primary_key=True)  # The composite primary key (fluid, month) found, that is not supported. The first column is selected.
    month = models.IntegerField()
    plan = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prdp'
        unique_together = (('fluid', 'month'),)


class ProcessUnits(models.Model):
    unit = models.CharField(primary_key=True, max_length=10)
    area = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'process_units'


class ProductionOutageReason(models.Model):
    reason = models.CharField(primary_key=True, max_length=100)
    reason_code = models.IntegerField(unique=True)

    class Meta:
        managed = False
        db_table = 'production_outage_reason'


class Pryp(models.Model):
    fluid = models.OneToOneField(Fluid, models.DO_NOTHING, db_column='fluid', primary_key=True)  # The composite primary key (fluid, month) found, that is not supported. The first column is selected.
    month = models.IntegerField()
    plan = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pryp'
        unique_together = (('fluid', 'month'),)


class ReportAccess(models.Model):
    owner = models.CharField(max_length=256)
    report_name = models.CharField(primary_key=True, max_length=256)  # The composite primary key (report_name, role_name, owner) found, that is not supported. The first column is selected.
    role_name = models.ForeignKey('Roles', models.DO_NOTHING, db_column='role_name')

    class Meta:
        managed = False
        db_table = 'report_access'
        unique_together = (('report_name', 'role_name', 'owner'),)


class ReportBuilderDcs1H(models.Model):
    id = models.BigAutoField(primary_key=True)
    tag = models.CharField(max_length=255)
    date = models.DateField()
    v01 = models.FloatField(blank=True, null=True)
    v02 = models.FloatField(blank=True, null=True)
    v03 = models.FloatField(blank=True, null=True)
    v04 = models.FloatField(blank=True, null=True)
    v05 = models.FloatField(blank=True, null=True)
    v06 = models.FloatField(blank=True, null=True)
    v07 = models.FloatField(blank=True, null=True)
    v08 = models.FloatField(blank=True, null=True)
    v09 = models.FloatField(blank=True, null=True)
    v10 = models.FloatField(blank=True, null=True)
    v11 = models.FloatField(blank=True, null=True)
    v12 = models.FloatField(blank=True, null=True)
    v13 = models.FloatField(blank=True, null=True)
    v14 = models.FloatField(blank=True, null=True)
    v15 = models.FloatField(blank=True, null=True)
    v16 = models.FloatField(blank=True, null=True)
    v17 = models.FloatField(blank=True, null=True)
    v18 = models.FloatField(blank=True, null=True)
    v19 = models.FloatField(blank=True, null=True)
    v20 = models.FloatField(blank=True, null=True)
    v21 = models.FloatField(blank=True, null=True)
    v22 = models.FloatField(blank=True, null=True)
    v23 = models.FloatField(blank=True, null=True)
    v24 = models.FloatField(blank=True, null=True)
    report = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'report_builder_dcs1h'


class Roles(models.Model):
    name = models.CharField(primary_key=True, max_length=30)
    parentrolename = models.ForeignKey('self', models.DO_NOTHING, db_column='parentrolename', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'roles'


class Settings(models.Model):
    active_2step = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'settings'


class Shutdown(models.Model):
    start_date = models.IntegerField(primary_key=True)  # The composite primary key (start_date, end_date, reason) found, that is not supported. The first column is selected.
    end_date = models.IntegerField()
    reason = models.TextField()

    class Meta:
        managed = False
        db_table = 'shutdown'
        unique_together = (('start_date', 'end_date', 'reason'),)


class TagFull(models.Model):
    tag = models.CharField(primary_key=True, max_length=50)  # The composite primary key (tag, parameter) found, that is not supported. The first column is selected.
    parameter = models.CharField(max_length=50)
    min = models.FloatField(blank=True, null=True)
    max = models.FloatField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tag_full'
        unique_together = (('tag', 'parameter'),)


class TagFullReportMapping(models.Model):
    tag = models.CharField(primary_key=True, max_length=50)  # The composite primary key (tag, parameter) found, that is not supported. The first column is selected.
    type = models.TextField(blank=True, null=True)  # This field type is a guess.
    parameter = models.CharField(max_length=50)
    report = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tag_full_report_mapping'
        unique_together = (('tag', 'parameter'),)


class Tanalysis(models.Model):
    meter = models.TextField(primary_key=True)  # The composite primary key (meter, date, type, fluid) found, that is not supported. The first column is selected. This field type is a guess.
    date = models.IntegerField()
    type = models.TextField()  # This field type is a guess.
    fluid = models.ForeignKey(Fluid, models.DO_NOTHING, db_column='fluid')
    percent = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tanalysis'
        unique_together = (('meter', 'date', 'type', 'fluid'),)


class Tdd(models.Model):
    tk = models.OneToOneField('Ttag', models.DO_NOTHING, db_column='tk', primary_key=True)  # The composite primary key (tk, date) found, that is not supported. The first column is selected.
    date = models.IntegerField()
    type = models.TextField(blank=True, null=True)  # This field type is a guess.
    fluid = models.ForeignKey(Fluid, models.DO_NOTHING, db_column='fluid', blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)
    tonage = models.FloatField(blank=True, null=True)
    dif = models.FloatField(blank=True, null=True)
    fqi = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tdd'
        unique_together = (('tk', 'date'),)


class Tfdd(models.Model):
    fqi = models.OneToOneField('Ttag', models.DO_NOTHING, db_column='fqi', primary_key=True)  # The composite primary key (fqi, date) found, that is not supported. The first column is selected.
    date = models.IntegerField()
    fluid = models.ForeignKey(Fluid, models.DO_NOTHING, db_column='fluid', blank=True, null=True)
    dif = models.FloatField(blank=True, null=True)
    munit = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'tfdd'
        unique_together = (('fqi', 'date'),)


class TfddDetail(models.Model):
    fqi = models.OneToOneField('Ttag', models.DO_NOTHING, db_column='fqi', primary_key=True)  # The composite primary key (fqi, date) found, that is not supported. The first column is selected.
    date = models.IntegerField()
    density = models.FloatField(blank=True, null=True)
    dcs = models.FloatField(blank=True, null=True)
    ydcs = models.FloatField(blank=True, null=True)
    cf = models.FloatField(blank=True, null=True)
    negative = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tfdd_detail'
        unique_together = (('fqi', 'date'),)


class Tfhd(models.Model):
    tag = models.OneToOneField('Ttag', models.DO_NOTHING, db_column='tag', primary_key=True)  # The composite primary key (tag, date) found, that is not supported. The first column is selected.
    date = models.IntegerField()
    v01 = models.FloatField(blank=True, null=True)
    v02 = models.FloatField(blank=True, null=True)
    v03 = models.FloatField(blank=True, null=True)
    v04 = models.FloatField(blank=True, null=True)
    v05 = models.FloatField(blank=True, null=True)
    v06 = models.FloatField(blank=True, null=True)
    v07 = models.FloatField(blank=True, null=True)
    v08 = models.FloatField(blank=True, null=True)
    v09 = models.FloatField(blank=True, null=True)
    v10 = models.FloatField(blank=True, null=True)
    v11 = models.FloatField(blank=True, null=True)
    v12 = models.FloatField(blank=True, null=True)
    v13 = models.FloatField(blank=True, null=True)
    v14 = models.FloatField(blank=True, null=True)
    v15 = models.FloatField(blank=True, null=True)
    v16 = models.FloatField(blank=True, null=True)
    v17 = models.FloatField(blank=True, null=True)
    v18 = models.FloatField(blank=True, null=True)
    v19 = models.FloatField(blank=True, null=True)
    v20 = models.FloatField(blank=True, null=True)
    v21 = models.FloatField(blank=True, null=True)
    v22 = models.FloatField(blank=True, null=True)
    v23 = models.FloatField(blank=True, null=True)
    v24 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tfhd'
        unique_together = (('tag', 'date'),)


class Tfqi(models.Model):
    fqi = models.OneToOneField('Ttag', models.DO_NOTHING, db_column='fqi', primary_key=True)  # The composite primary key (fqi, date) found, that is not supported. The first column is selected.
    date = models.IntegerField()
    munit = models.TextField(blank=True, null=True)  # This field type is a guess.
    fluid = models.ForeignKey(Fluid, models.DO_NOTHING, db_column='fluid', blank=True, null=True)
    density = models.FloatField(blank=True, null=True)
    fdn = models.FloatField(blank=True, null=True)
    min = models.FloatField(blank=True, null=True)
    max = models.FloatField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tfqi'
        unique_together = (('fqi', 'date'),)


class Tloss(models.Model):
    date = models.IntegerField(primary_key=True)  # The composite primary key (date, fluid, type, tk_type) found, that is not supported. The first column is selected.
    fluid = models.ForeignKey(Fluid, models.DO_NOTHING, db_column='fluid')
    type = models.TextField()  # This field type is a guess.
    tk_type = models.TextField()  # This field type is a guess.
    tonage = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tloss'
        unique_together = (('date', 'fluid', 'type', 'tk_type'),)


class Tpc(models.Model):
    type = models.TextField(primary_key=True)  # The composite primary key (type, date, fluid, fqi) found, that is not supported. The first column is selected. This field type is a guess.
    date = models.IntegerField()
    src = models.ForeignKey(Fl, models.DO_NOTHING, db_column='src', blank=True, null=True)
    dst = models.ForeignKey(Fl, models.DO_NOTHING, db_column='dst', related_name='tpc_dst_set', blank=True, null=True)
    fluid = models.ForeignKey(Fluid, models.DO_NOTHING, db_column='fluid')
    fqi = models.ForeignKey('Ttag', models.DO_NOTHING, db_column='fqi')
    title = models.CharField(max_length=50, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tpc'
        unique_together = (('type', 'date', 'fluid', 'fqi'),)


class Tplan(models.Model):
    fluid = models.OneToOneField(Fluid, models.DO_NOTHING, db_column='fluid', primary_key=True)  # The composite primary key (fluid, month, type) found, that is not supported. The first column is selected.
    month = models.IntegerField()
    type = models.TextField()  # This field type is a guess.
    value = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tplan'
        unique_together = (('fluid', 'month', 'type'),)


class Tship(models.Model):
    date = models.IntegerField(primary_key=True)  # The composite primary key (date, type, fluid) found, that is not supported. The first column is selected.
    type = models.TextField()  # This field type is a guess.
    fluid = models.ForeignKey(Fluid, models.DO_NOTHING, db_column='fluid')
    tonage = models.FloatField(blank=True, null=True)
    density = models.FloatField(blank=True, null=True)
    ship_figure = models.FloatField(blank=True, null=True)
    shore_figure = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tship'
        unique_together = (('date', 'type', 'fluid'),)


class Ttag(models.Model):
    tag = models.CharField(primary_key=True, max_length=50)
    parameter = models.CharField(max_length=50, blank=True, null=True)
    min = models.FloatField(blank=True, null=True)
    max = models.FloatField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)  # This field type is a guess.
    intype = models.TextField(blank=True, null=True)  # This field type is a guess.
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ttag'


class Ttdd(models.Model):
    tk = models.OneToOneField(Ttag, models.DO_NOTHING, db_column='tk', primary_key=True)  # The composite primary key (tk, date) found, that is not supported. The first column is selected.
    date = models.IntegerField()
    type = models.TextField(blank=True, null=True)  # This field type is a guess.
    fluid = models.ForeignKey(Fluid, models.DO_NOTHING, db_column='fluid', blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)
    tonage = models.FloatField(blank=True, null=True)
    fqi = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ttdd'
        unique_together = (('tk', 'date'),)


class TtddDetail(models.Model):
    tk = models.OneToOneField(Ttag, models.DO_NOTHING, db_column='tk', primary_key=True)  # The composite primary key (tk, date) found, that is not supported. The first column is selected.
    date = models.IntegerField()
    density = models.FloatField(blank=True, null=True)
    lic1 = models.FloatField(blank=True, null=True)
    lic2 = models.FloatField(blank=True, null=True)
    licp = models.FloatField(blank=True, null=True)
    tic = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ttdd_detail'
        unique_together = (('tk', 'date'),)


class Ttk(models.Model):
    tk = models.OneToOneField(Ttag, models.DO_NOTHING, db_column='tk', primary_key=True)  # The composite primary key (tk, date) found, that is not supported. The first column is selected.
    date = models.IntegerField()
    type = models.TextField(blank=True, null=True)  # This field type is a guess.
    fluid = models.ForeignKey(Fluid, models.DO_NOTHING, db_column='fluid', blank=True, null=True)
    licp = models.ForeignKey(Ttag, models.DO_NOTHING, db_column='licp', related_name='ttk_licp_set', blank=True, null=True)
    lic1 = models.ForeignKey(Ttag, models.DO_NOTHING, db_column='lic1', related_name='ttk_lic1_set', blank=True, null=True)
    lic2 = models.ForeignKey(Ttag, models.DO_NOTHING, db_column='lic2', related_name='ttk_lic2_set', blank=True, null=True)
    tic = models.ForeignKey(Ttag, models.DO_NOTHING, db_column='tic', related_name='ttk_tic_set', blank=True, null=True)
    dic = models.ForeignKey(Ttag, models.DO_NOTHING, db_column='dic', related_name='ttk_dic_set', blank=True, null=True)
    density = models.FloatField(blank=True, null=True)
    vic = models.ForeignKey(Ttag, models.DO_NOTHING, db_column='vic', related_name='ttk_vic_set', blank=True, null=True)
    fqi = models.ForeignKey(Ttag, models.DO_NOTHING, db_column='fqi', related_name='ttk_fqi_set', blank=True, null=True)
    min = models.FloatField(blank=True, null=True)
    max = models.FloatField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ttk'
        unique_together = (('tk', 'date'),)


class Ui(models.Model):
    name = models.CharField(primary_key=True, max_length=50)
    persian = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'ui'


class Users(models.Model):
    id = models.CharField(primary_key=True, max_length=30)
    firstname = models.CharField(max_length=30, blank=True, null=True)
    lastname = models.CharField(max_length=30, blank=True, null=True)
    password = models.CharField(max_length=1024, blank=True, null=True)
    role_name = models.ForeignKey(Roles, models.DO_NOTHING, db_column='role_name', blank=True, null=True)
    defaultaddress = models.TextField()  # This field type is a guess.
    defaulttimeing = models.IntegerField()
    phone = models.CharField(max_length=15)
    verify_code = models.CharField(max_length=6)
    err_verify_num = models.IntegerField()
    ui_name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'


class UtilityDesign(models.Model):
    utility = models.OneToOneField(Fluid, models.DO_NOTHING, db_column='utility', primary_key=True)  # The composite primary key (utility, month) found, that is not supported. The first column is selected.
    month = models.IntegerField()
    design = models.FloatField()

    class Meta:
        managed = False
        db_table = 'utility_design'
        unique_together = (('utility', 'month'),)


class UtilityOutage(models.Model):
    utility = models.OneToOneField(Fluid, models.DO_NOTHING, db_column='utility', primary_key=True)  # The composite primary key (utility, start_date, start_time) found, that is not supported. The first column is selected.
    start_time = models.IntegerField()
    start_date = models.IntegerField()
    end_time = models.IntegerField(blank=True, null=True)
    end_date = models.IntegerField(blank=True, null=True)
    unit_normal_time = models.IntegerField(blank=True, null=True)
    unit_shutdown_hours = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'utility_outage'
        unique_together = (('utility', 'start_date', 'start_time'),)
