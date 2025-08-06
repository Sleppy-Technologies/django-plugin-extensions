from django.test import TestCase

from tests.test_app.models import TestModel


class TestDjangoPluginExtensions(TestCase):
    def test_model_extensions_available(self):
        self.assertEqual(TestModel.objects.count(), 0)
        TestModel.objects.create(title="Test Title", description="Test Description")
        instance = TestModel.objects.first()
        self.assertEqual(instance.title, "Test Title")
        self.assertEqual(instance.description, "Test Description")
