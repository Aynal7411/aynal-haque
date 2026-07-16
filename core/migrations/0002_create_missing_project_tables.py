from django.db import migrations


def create_missing_project_tables(apps, schema_editor):
    ProjectCategory = apps.get_model("core", "ProjectCategory")
    Technology = apps.get_model("core", "Technology")
    ProjectImage = apps.get_model("core", "ProjectImage")
    ProjectFeature = apps.get_model("core", "ProjectFeature")
    Project = apps.get_model("core", "Project")

    existing_tables = set(schema_editor.connection.introspection.table_names())

    models_to_create = [
        ProjectCategory,
        Technology,
        ProjectImage,
        ProjectFeature,
    ]

    for model in models_to_create:
        if model._meta.db_table not in existing_tables:
            schema_editor.create_model(model)

    through_model = Project._meta.get_field("technologies").remote_field.through
    if through_model._meta.db_table not in existing_tables:
        schema_editor.create_model(through_model)


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(create_missing_project_tables, reverse_code=migrations.RunPython.noop),
    ]
