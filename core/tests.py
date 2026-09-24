from django.test import TestCase
from django.urls import reverse

from .models import Task


class TaskModelTests(TestCase):
    def test_str_returns_title(self):
        task = Task.objects.create(title='Write docs')
        self.assertEqual(str(task), 'Write docs')

    def test_default_not_done(self):
        task = Task.objects.create(title='New task')
        self.assertFalse(task.done)


class TaskViewTests(TestCase):
    def test_index_lists_tasks(self):
        Task.objects.create(title='Visible task')
        response = self.client.get(reverse('core:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Visible task')

    def test_add_task_creates_record(self):
        response = self.client.post(reverse('core:add_task'), {'title': 'Buy milk'})
        self.assertRedirects(response, reverse('core:index'))
        self.assertTrue(Task.objects.filter(title='Buy milk').exists())

    def test_add_task_ignores_blank_title(self):
        self.client.post(reverse('core:add_task'), {'title': '   '})
        self.assertEqual(Task.objects.count(), 0)

    def test_toggle_task_flips_done(self):
        task = Task.objects.create(title='Toggle me')
        self.client.post(reverse('core:toggle_task', args=[task.pk]))
        task.refresh_from_db()
        self.assertTrue(task.done)

    def test_delete_task_removes_record(self):
        task = Task.objects.create(title='Delete me')
        self.client.post(reverse('core:delete_task', args=[task.pk]))
        self.assertFalse(Task.objects.filter(pk=task.pk).exists())

    def test_healthz_returns_ok(self):
        response = self.client.get(reverse('core:healthz'))
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {'status': 'ok'})
