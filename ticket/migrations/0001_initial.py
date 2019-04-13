# Generated by Django 2.1.7 on 2019-03-30 06:42

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import recurrence.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(max_length=1000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('before', models.TextField(null=True)),
                ('after', models.TextField(null=True)),
                ('fieldname', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Eine kurze Beschreibung der Aufgabe', max_length=255)),
                ('state', models.CharField(choices=[('done', 'done'), ('open', 'open')], default='open', help_text='Der aktuelle Status des Tickets', max_length=4, verbose_name='Status')),
                ('time_assign_user', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True)),
                ('accepted', models.BooleanField(default=False, verbose_name='Akzeptiert')),
                ('text', models.TextField(blank=True, help_text='Eine ausführlichere Beschreibung der Aufgabe', null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('priority', models.CharField(choices=[('high', 'high'), ('normal', 'normal'), ('low', 'low')], default='normal', help_text='Die Dringlichkeit des Tickets.', max_length=6, verbose_name='Priorität')),
                ('deadline', models.DateField(blank=True, null=True)),
                ('recurrences', recurrence.fields.RecurrenceField(blank=True, default='', verbose_name='wiederholungen')),
                ('rejected', models.BooleanField(default=False, verbose_name='abgelehnt')),
                ('assigned_group', models.ForeignKey(blank=True, help_text='Die Gruppe, für die das Ticket interessant ist.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assigned_group', to='auth.Group', verbose_name='gruppe')),
                ('assigned_user', models.ForeignKey(blank=True, help_text='Der Nutzer, der für diese Aufgabe verantwortlich ist. Er bekommt die Aufgabe in die Inbox und kann sie dann annehmen oder ablehnen.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assigned_tasks', to=settings.AUTH_USER_MODEL, verbose_name='zugewiesener Nutzer')),
                ('creator_user', models.ForeignKey(blank=True, help_text='Der Nutzer, der diese Aufgabe erstellt hat.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_tasks', to=settings.AUTH_USER_MODEL, verbose_name='ersteller')),
                ('dispatcher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dispatcher', to=settings.AUTH_USER_MODEL, verbose_name='zuteiler')),
                ('ignored_by', models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='ignoriert bei')),
            ],
        ),
        migrations.CreateModel(
            name='TicketLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('state', models.CharField(choices=[('add', 'ADD'), ('accepted', 'ACCEPTED'), ('rejected', 'REJECTED'), ('closed', 'CLOSED'), ('changed', 'CHANGED')], max_length=100)),
                ('message', models.TextField(blank=True)),
                ('changes', models.ManyToManyField(to='ticket.Log')),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticket.Ticket')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='ticket',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticket.Ticket'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]