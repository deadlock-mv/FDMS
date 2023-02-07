# Generated by Django 4.1.3 on 2023-01-12 08:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Categorylist',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('categoryname', models.CharField(blank=True, db_column='CategoryName', max_length=255, null=True)),
            ],
            options={
                'db_table': 'CategoryList',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Deliveryagents',
            fields=[
                ('name', models.CharField(blank=True, db_column='Name', max_length=255, null=True)),
                ('username', models.CharField(blank=True, db_column='UserName', max_length=255, null=True)),
                ('address', models.CharField(blank=True, db_column='Address', max_length=300, null=True)),
                ('pincode', models.CharField(blank=True, db_column='Pincode', max_length=10, null=True)),
                ('phone', models.CharField(blank=True, db_column='Phone', max_length=10, null=True)),
                ('agentid', models.AutoField(db_column='AgentID', primary_key=True, serialize=False)),
                ('password', models.CharField(blank=True, db_column='Password', max_length=255, null=True)),
            ],
            options={
                'db_table': 'DeliveryAgents',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, db_column='Description', max_length=500, null=True)),
            ],
            options={
                'db_table': 'Feedback',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Foodorder',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('totalamount', models.IntegerField(blank=True, db_column='TotalAmount', null=True)),
                ('orderdate', models.DateTimeField(blank=True, db_column='OrderDate', null=True)),
            ],
            options={
                'db_table': 'FoodOrder',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemid', models.IntegerField(blank=True, db_column='ItemID', null=True)),
                ('itemname', models.CharField(blank=True, db_column='ItemName', max_length=255, null=True)),
                ('price', models.IntegerField(blank=True, db_column='Price', null=True)),
            ],
            options={
                'db_table': 'Menu',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Orderstatus',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('status_value', models.CharField(blank=True, db_column='Status_value', max_length=200, null=True)),
            ],
            options={
                'db_table': 'OrderStatus',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('name', models.CharField(blank=True, db_column='Name', max_length=255, null=True)),
                ('username', models.CharField(blank=True, db_column='UserName', max_length=255, null=True)),
                ('address', models.CharField(blank=True, db_column='Address', max_length=300, null=True)),
                ('pincode', models.CharField(blank=True, db_column='Pincode', max_length=10, null=True)),
                ('phone', models.CharField(blank=True, db_column='Phone', max_length=10, null=True)),
                ('userid', models.AutoField(db_column='UserID', primary_key=True, serialize=False)),
                ('password', models.CharField(blank=True, db_column='Password', max_length=255, null=True)),
            ],
            options={
                'db_table': 'Users',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Foodorderitems',
            fields=[
                ('foodorderid', models.OneToOneField(db_column='FooDOrderID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='app.foodorder')),
            ],
            options={
                'db_table': 'FoodOrderItems',
                'managed': False,
            },
        ),
    ]