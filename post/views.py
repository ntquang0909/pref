from django.shortcuts import render
from post.models import PostModel
from post.form import PostModelForm
from django.http import JsonResponse
from django.forms.models import model_to_dict

# Create your views here.
def post_index_view(request):
	if request.method == 'POST':
		if request.is_ajax():
			createpostform = PostModelForm(request.POST)
			if createpostform.is_valid():
				createpostform.cleaned_data
				createpostform.save()
				latest = PostModel.objects.latest('id').id
				post_object = model_to_dict(PostModel.objects.get(pk=latest))
				return JsonResponse({'error': False, 'data': post_object})
			else:
				print(createpostform.errors)
				return JsonResponse({'error': True, 'data': createpostform.errors})
		else:
			error = {
				'message': 'Error, must be an Ajax call.'
			}
			return JsonResponse(error, content_type="application/json")
	else:
		createpostform = PostModelForm()
		all_posts_object = PostModel.objects.all()
		data = {
			'createpostform_html': createpostform,
			'posts': all_posts_object,
		}
		return render(request, template_name='index.html', context=data)

def post_delete(request, id):
	if request.method == 'POST' and request.is_ajax():
		try:
			post_object = PostModel.objects.get(pk=id)
			post_object.delete()
			return JsonResponse({'status': 'Success', 'message': 'Recoard has been deleted.'})
		except PostModel.DoesNotExist:
			return JsonResponse({'status': 'Fail', 'message': 'Recoard does not exist.'})
	return JsonResponse({'status': 'Fail', 'message': 'Error, must be an Ajax call.'})
