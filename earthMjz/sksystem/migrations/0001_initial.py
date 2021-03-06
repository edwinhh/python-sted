# Generated by Django 2.1 on 2020-03-01 18:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_delete', models.SmallIntegerField(choices=[(0, '删除'), (1, '正常')], default=1, verbose_name='是否被删除')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('title', models.CharField(max_length=100, verbose_name='用例标题')),
                ('method', models.SmallIntegerField(choices=[(1, 'POST'), (2, 'GET'), (3, 'DELETE'), (4, 'PUT')], verbose_name='请求方式')),
                ('cache_field', models.CharField(blank=True, max_length=128, null=True, verbose_name='缓存字段')),
                ('check', models.CharField(max_length=512, verbose_name='校验点')),
                ('params', models.CharField(blank=True, max_length=2048, null=True, verbose_name='请求参数')),
                ('headers', models.CharField(blank=True, max_length=2048, null=True, verbose_name='请求头信息')),
                ('is_json', models.BooleanField(default=False, verbose_name='参数是否是json')),
                ('json', models.CharField(blank=True, max_length=2048, null=True, verbose_name='json类型参数')),
                ('status', models.SmallIntegerField(choices=[(1, '通过'), (2, '未运行'), (3, '运行中'), (999, '失败')], default=2, verbose_name='用例状态')),
                ('report_batch', models.CharField(blank=True, max_length=512, null=True, verbose_name='最后一次执行的批次号')),
            ],
            options={
                'verbose_name': '用例表',
                'verbose_name_plural': '用例表',
                'db_table': 'case',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='CaseCollection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_delete', models.SmallIntegerField(choices=[(0, '删除'), (1, '正常')], default=1, verbose_name='是否被删除')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='集合名')),
                ('desc', models.CharField(max_length=200, null=True, verbose_name='描述')),
                ('report_batch', models.CharField(blank=True, max_length=512, null=True, verbose_name='最后一次执行的批次号')),
                ('status', models.SmallIntegerField(choices=[(2, '未运行'), (3, '运行中'), (4, '执行完毕')], default=2, verbose_name='用例状态')),
                ('case', models.ManyToManyField(to='sksystem.Case', verbose_name='集合下的用例')),
            ],
            options={
                'verbose_name': '用例集合表',
                'verbose_name_plural': '用例集合表',
                'db_table': 'case_collection',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='CasePremise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_delete', models.SmallIntegerField(choices=[(0, '删除'), (1, '正常')], default=1, verbose_name='是否被删除')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('case', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, related_name='case', to='sksystem.Case', verbose_name='用例id')),
                ('premise_case', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, related_name='premise_case', to='sksystem.Case', verbose_name='被依赖用例的id')),
            ],
            options={
                'verbose_name': '依赖关系表',
                'verbose_name_plural': '依赖关系表',
                'db_table': 'case_premise',
            },
        ),
        migrations.CreateModel(
            name='HomeData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_delete', models.SmallIntegerField(choices=[(0, '删除'), (1, '正常')], default=1, verbose_name='是否被删除')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('date', models.DateField(unique=True, verbose_name='统计时间')),
                ('pass_count', models.IntegerField(default=0, verbose_name='成功次数')),
                ('all_count', models.IntegerField(default=0, verbose_name='执行次数')),
                ('fail_count', models.IntegerField(default=0, verbose_name='失败次数')),
            ],
            options={
                'verbose_name': '首页数据统计',
                'verbose_name_plural': '首页数据统计',
                'db_table': 'home_data',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Interface',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_delete', models.SmallIntegerField(choices=[(0, '删除'), (1, '正常')], default=1, verbose_name='是否被删除')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='接口名称')),
                ('uri', models.CharField(max_length=1024, verbose_name='接口路径')),
                ('params', models.CharField(blank=True, max_length=2048, null=True, verbose_name='默认参数')),
                ('headers', models.CharField(blank=True, max_length=2048, null=True, verbose_name='默认Headers')),
            ],
            options={
                'verbose_name': '接口表',
                'verbose_name_plural': '接口表',
                'db_table': 'interface',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Parameter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_delete', models.SmallIntegerField(choices=[(0, '删除'), (1, '正常')], default=1, verbose_name='是否被删除')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='参数名')),
                ('desc', models.CharField(max_length=200, null=True, verbose_name='描述')),
                ('value', models.CharField(max_length=100, verbose_name='参数值')),
            ],
            options={
                'verbose_name': '全局参数',
                'verbose_name_plural': '全局参数',
                'db_table': 'parameter',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_delete', models.SmallIntegerField(choices=[(0, '删除'), (1, '正常')], default=1, verbose_name='是否被删除')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='项目名')),
                ('desc', models.CharField(max_length=200, null=True, verbose_name='描述')),
                ('host', models.CharField(max_length=1024, verbose_name='域名')),
            ],
            options={
                'verbose_name': '项目表',
                'verbose_name_plural': '项目表',
                'db_table': 'project',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_delete', models.SmallIntegerField(choices=[(0, '删除'), (1, '正常')], default=1, verbose_name='是否被删除')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('url', models.CharField(max_length=1024, verbose_name='请求URL')),
                ('title', models.CharField(max_length=100, verbose_name='用例名称')),
                ('params', models.CharField(max_length=2048, verbose_name='请求参数')),
                ('response', models.CharField(max_length=2048, verbose_name='接口返回值结果')),
                ('batch', models.CharField(max_length=128, null=True, verbose_name='批次')),
                ('reason', models.CharField(blank=True, max_length=128, null=True, verbose_name='失败原因')),
                ('duration', models.IntegerField(verbose_name='用例耗时')),
                ('status', models.SmallIntegerField(choices=[(1, '通过'), (999, '失败')], verbose_name='用例结果状态')),
                ('case', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, to='sksystem.Case', verbose_name='结果所属用例')),
                ('case_collection', models.ForeignKey(db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='sksystem.CaseCollection', verbose_name='结果所属集合')),
                ('project', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, to='sksystem.Project', verbose_name='项目')),
            ],
            options={
                'verbose_name': '用例报告表',
                'verbose_name_plural': '用例报告表',
                'db_table': 'report',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_delete', models.SmallIntegerField(choices=[(0, '删除'), (1, '正常')], default=1, verbose_name='是否被删除')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('phone', models.CharField(max_length=11, unique=True, verbose_name='手机号')),
                ('email', models.EmailField(max_length=25, unique=True, verbose_name='邮箱')),
                ('password', models.CharField(max_length=32, verbose_name='密码')),
                ('username', models.CharField(max_length=20, verbose_name='账号')),
            ],
            options={
                'verbose_name': '用户表',
                'verbose_name_plural': '用户表',
                'db_table': 'user',
            },
        ),
        migrations.AddField(
            model_name='report',
            name='user',
            field=models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, to='sksystem.User', verbose_name='运行用户'),
        ),
        migrations.AddField(
            model_name='project',
            name='user',
            field=models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, to='sksystem.User', verbose_name='创建者'),
        ),
        migrations.AddField(
            model_name='interface',
            name='project',
            field=models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, to='sksystem.Project', verbose_name='归属项目'),
        ),
        migrations.AddField(
            model_name='interface',
            name='user',
            field=models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, to='sksystem.User', verbose_name='创建者'),
        ),
        migrations.AddField(
            model_name='casecollection',
            name='project',
            field=models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, to='sksystem.Project', verbose_name='归属项目'),
        ),
        migrations.AddField(
            model_name='casecollection',
            name='user',
            field=models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, to='sksystem.User', verbose_name='创建者'),
        ),
        migrations.AddField(
            model_name='case',
            name='interface',
            field=models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, to='sksystem.Interface', verbose_name='接口'),
        ),
        migrations.AddField(
            model_name='case',
            name='project',
            field=models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, to='sksystem.Project', verbose_name='归属项目'),
        ),
        migrations.AddField(
            model_name='case',
            name='user',
            field=models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, to='sksystem.User', verbose_name='创建用户'),
        ),
        migrations.AlterUniqueTogether(
            name='casepremise',
            unique_together={('case', 'premise_case')},
        ),
    ]
