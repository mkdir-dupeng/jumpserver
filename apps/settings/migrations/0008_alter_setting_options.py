# Generated by Django 3.2.19 on 2023-06-30 10:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0007_migrate_ldap_sync_org_ids'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='setting',
            options={'permissions': [('change_email', 'Can change email setting'), ('change_auth', 'Can change auth setting'), ('change_vault', 'Can change vault setting'), ('change_systemmsgsubscription', 'Can change system msg sub setting'), ('change_sms', 'Can change sms setting'), ('change_security', 'Can change security setting'), ('change_clean', 'Can change clean setting'), ('change_interface', 'Can change interface setting'), ('change_license', 'Can change license setting'), ('change_terminal', 'Can change terminal setting'), ('change_other', 'Can change other setting')], 'verbose_name': 'System setting'},
        ),
    ]