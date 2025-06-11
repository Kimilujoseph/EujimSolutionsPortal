from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    dependencies = [
        ('recruiter', '0006_alter_recruiter_user_alter_recruiterdoc_verifiedby_and_more'),
    ]

    operations = [
        # First remove the old varchar column
        migrations.RemoveField(
            model_name='recruiterdoc',  # Changed from recruiter_doc
            name='verifiedBy',
        ),
        
        # Then add the proper ForeignKey
        migrations.AddField(
            model_name='recruiterdoc',  # Changed from recruiter_doc
            name='verifiedBy',
            field=models.ForeignKey(
                null=True,
                blank=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name='verified_docs',
                to='auth.User',
                db_column='verifiedBy'
            ),
        ),
    ]