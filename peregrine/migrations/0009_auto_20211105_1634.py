# Generated by Django 3.2.9 on 2021-11-05 16:34

from django.db import migrations, models
import wagtail.contrib.table_block.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('peregrine', '0008_peregrinesettings_revisions_to_keep'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='peregrinesettings',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='sitepage',
            name='body',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.TextBlock(icon='title', template='wagtailcontentstream/blocks/heading.html')), ('paragraph', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'link', 'ol', 'ul', 'monospace'], icon='pilcrow')), ('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='The image to display.')), ('caption', wagtail.core.blocks.TextBlock(help_text='The caption will appear under the image, if entered.', required=False)), ('credit', wagtail.core.blocks.TextBlock(help_text='The credit will appear under the image, if entered.', required=False)), ('align', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'Left'), ('right', 'Right'), ('center', 'Center'), ('full', 'Full Width')], help_text='How to align the image in the body of the page.'))])), ('document', wagtail.documents.blocks.DocumentChooserBlock()), ('embed', wagtail.embeds.blocks.EmbedBlock(icon='media')), ('table', wagtail.contrib.table_block.blocks.TableBlock(icon='table')), ('code', wagtail.core.blocks.StructBlock([('language', wagtail.core.blocks.ChoiceBlock(choices=[('bash', 'Bash/Shell'), ('css', 'CSS'), ('diff', 'diff'), ('html', 'HTML'), ('javascript', 'Javascript'), ('json', 'JSON'), ('python', 'Python'), ('scss', 'SCSS'), ('yaml', 'YAML')], help_text='Coding language', identifier='language', label='Language')), ('code', wagtail.core.blocks.TextBlock(identifier='code', label='Code'))], icon='code'))], blank=True),
        ),
    ]