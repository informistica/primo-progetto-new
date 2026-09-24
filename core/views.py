from django.db.models import Count, Q
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.decorators.http import require_POST

from .models import Task


def index(request):
    tasks = Task.objects.all()
    stats = tasks.aggregate(
        total=Count('id'),
        done=Count('id', filter=Q(done=True)),
    )
    return render(request, 'core/index.html', {'tasks': tasks, 'stats': stats})


@require_POST
def add_task(request):
    title = (request.POST.get('title') or '').strip()
    if title:
        Task.objects.create(title=title)
    return redirect(reverse('core:index'))


@require_POST
def toggle_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.done = not task.done
    task.save(update_fields=['done'])
    return redirect(reverse('core:index'))


@require_POST
def delete_task(request, pk):
    get_object_or_404(Task, pk=pk).delete()
    return redirect(reverse('core:index'))


def healthz(request):
    return JsonResponse({'status': 'ok'})
