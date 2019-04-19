import json
from django.db import migrations



def load_minerals(apps, schema_editor):
  # fix <app_name> with your app name.
  Mineral = apps.get_model('minerals', 'Mineral')


# Now open your minerals.json file, read it in.
# Iterate over each item in the list of dicts
# use Mineral.objects.create() to create each mineral.
  with open('minerals/minerals.json', encoding="utf8") as file:
      minerals = json.load(file)
      for mineral in minerals:
          Mineral.objects.create(name=mineral.get('name', ''),
                                 img_file=mineral.get('image_filename', ''),
                                 img_caption=mineral.get('image_caption', ''),
                                 category=mineral.get('category', ''),
                                 formula=mineral.get('formula', ''),
                                 strunz=mineral.get('strunz_classification', ''),
                                 color=mineral.get('color', ''),
                                 crystal_sys=mineral.get('crystal_system', ''),
                                 unit=mineral.get('unit_cell', ''),
                                 crystal_sym=mineral.get('crystal_symmetry',''),
                                 cleavage=mineral.get('cleavage', ''),
                                 mohs=mineral.get('mohs_scale_hardness', ''),
                                 luster=mineral.get('luster', ''),
                                 streak=mineral.get('streak', ''),
                                 diaphaneity=mineral.get('diaphaneity', ''),
                                 optical=mineral.get('optical_properties', ''),
                                 refractive=mineral.get('refractive_index',''),
                                 crystal_habit=mineral.get('crystal_habit',''),
                                 specific_gravity=mineral.get('specific_gravity',''))


class Migration(migrations.Migration):
   dependencies = [
      # fix this <app_name> with your app name
      ('minerals', '0001_initial'),
   ]

   operations = [
      migrations.RunPython(load_minerals, reverse_code=migrations.RunPython.noop),
  ]
