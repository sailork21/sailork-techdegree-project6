from django.urls import reverse
from django.test import TestCase

from .models import Mineral



class MineralViewsTests(TestCase):
    def setUp(self):
        self.mineral1 = Mineral.objects.create(
            name='Test Mineral 1',
            category='Not a rock 1'
        )
        self.mineral2 = Mineral.objects.create(
            name='Test Mineral 2',
            category='Not a rock 2'
        )


    def test_mineral_list_view(self):
        """Mineral list view should return 200, have self.mineral in context
        and use the minerals/index.html template
        """
        resp = self.client.get(reverse('minerals:mineral_list'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.mineral1, resp.context['minerals'])
        self.assertIn(self.mineral2, resp.context['minerals'])
        self.assertTemplateUsed(resp, 'minerals/index.html')
        self.assertContains(resp, self.mineral1.name)


    def test_mineral_detail_view(self):
        """Mineral detail view should return 200, use the minerals/index.html
        template and show string version of self.mineral1.category
        """
        resp = self.client.get(reverse('minerals:detail',
            kwargs={'pk': self.mineral1.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'minerals/detail.html')
        self.assertContains(resp, self.mineral1.category)
