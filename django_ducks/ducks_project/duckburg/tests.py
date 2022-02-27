from django.test import SimpleTestCase
from django.urls import reverse

class DuckburgTest(SimpleTestCase):

  def test_duckburg_status_code(self):
    url = reverse('duckburg')
    response = self.client.get(url)
    assert response.status_code == 200

  def test_duckburg_template(self):
    url = reverse('duckburg')
    response = self.client.get(url)
    self.assertTemplateUsed(response, 'duckburg.html')
    self.assertTemplateUsed(response, 'base.html')
