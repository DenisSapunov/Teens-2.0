from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_category_product_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(null=True, to='app.category'),
        ),
    ]
