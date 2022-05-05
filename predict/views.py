from django.shortcuts import render
from keras.preprocessing.image import array_to_img, img_to_array, load_img

# Create your views here.

def predict(request):
    return render(request, 'predict.html')

def predict_changes(request):

    if request.POST.get('action') == 'post':

        image_input = request.POST.get('image_input')

        images_as_array=[]
        # Convert to Numpy Array
        images_as_array.append(img_to_array(load_img(image_input)))
        print(images_as_array)

    return