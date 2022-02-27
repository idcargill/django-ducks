from django.test import SimpleTestCase
from django.urls import reverse

class DuckTests(SimpleTestCase):

  def test_home_page_status_code(self):
    url = reverse('home')
    response = self.client.get(url)
    assert response.status_code == 200

  def test_home_template(self):
    url = reverse('home')
    response = self.client.get(url)
    self.assertTemplateUsed(response,'home.html')
    self.assertTemplateUsed(response,'base.html')

  def test_about_status_code(self):
    url = reverse('about')
    response = self.client.get(url)
    assert response.status_code == 200

  def test_about_template(self):
    url = reverse('about')
    response = self.client.get(url)
    self.assertTemplateUsed(response, 'about.html')
    self.assertTemplateUsed(response, 'base.html')
