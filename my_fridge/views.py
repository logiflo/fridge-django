from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse

from django.contrib.auth.decorators import login_required

from .models import Food, Essencial
from .forms import FoodForm, QuantityForm, EssencialForm, QuantityEssencialForm

def home(request):
    """The home page for My Fridge
    """
    return render(request, 'my_fridge/home.html')


@login_required
def food(request):
    """Show food.
    """
    food = Food.objects.filter(owner=request.user).order_by('date_added')
    is_empty = True
    for f in food:
        if f.quantity > 0:
            is_empty = False
            break
    context = {'food': food, 'is_empty': is_empty}
    return render(request, 'my_fridge/food.html', context)


@login_required
def essencials(request):
    """Show essencials.
    """
    essencial = Essencial.objects.filter(owner=request.user).order_by('date_added')
    is_empty = True
    for e in essencial:
        is_empty = False
        break
    context = {'essencial': essencial, 'is_empty': is_empty}
    return render(request, 'my_fridge/essencials.html', context)


@login_required
def food_out(request):
    """Show food run out.
    """
    food = Food.objects.filter(owner=request.user).order_by('date_added')
    context = {'food': food}
    return render(request, 'my_fridge/food_out.html', context)


@login_required
def add_food(request):
    """Add food
    """
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = FoodForm()
    else:
        # POST data submitted; process data.
        form = FoodForm(request.POST)
        if form.is_valid():
            new_food = form.save(commit=False)
            new_food.owner = request.user
            new_food.save()

            return HttpResponseRedirect(reverse('my_fridge:food'))

    context = {'form': form}
    return render(request, 'my_fridge/add_food.html', context)


@login_required
def add_essencials(request):
    """Add essencials
    """
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = EssencialForm()
    else:
        # POST data submitted; process data.
        form = EssencialForm(request.POST)
        if form.is_valid():
            new_essencial = form.save(commit=False)
            new_essencial.owner = request.user
            new_essencial.save()

            return HttpResponseRedirect(reverse('my_fridge:essencials'))

    context = {'form': form}
    return render(request, 'my_fridge/add_essencials.html', context)


@login_required
def each_food(request, food_id):
    """Show food and its current quantity.
    """
    food = Food.objects.get(id=food_id)


    context = {'food': food}
    return render(request, 'my_fridge/each_food.html', context)


@login_required
def add_quantity(request, food_id):
    food = Food.objects.get(id=food_id)
    if food.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = FoodForm(instance=food)
        form.fields['text'].widget.attrs['readonly'] = True
    else:
        # POST data submitted; process data.
        form = FoodForm(request.POST, instance=food)
        form.fields['text'].widget.attrs['readonly'] = True
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('my_fridge:food'))

    context = {'food': food, 'form': form }
    return render(request, 'my_fridge/add_quantity.html', context)


@login_required
def add_quantity_essencials(request, essencials_id):
    essencials = Essencial.objects.get(id=essencials_id)
    if essencials.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = EssencialForm(instance=essencials)
        form.fields['text'].widget.attrs['readonly'] = True
    else:
        # POST data submitted; process data.
        form = EssencialForm(request.POST, instance=essencials)
        form.fields['text'].widget.attrs['readonly'] = True
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('my_fridge:essencials'))

    context = {'form': form, 'essencials': essencials}
    return render(request, 'my_fridge/add_quantity_essencials.html', context)


@login_required
def add_essencials_to_fridge(request):
    essencials = Essencial.objects.all()
    food = Food.objects.all()

    id_obj_error = list()
    id_essencial_error = list()
    is_error = 0

    for essencial in essencials:
        if essencial.owner != request.user:
            raise Http404

        obj, created = Food.objects.get_or_create(text__exact=essencial.text, defaults={'text': essencial.text, 'units': essencial.units, 'quantity': essencial.quantity, 'owner': essencial.owner})
        if not created:
            if obj.owner != request.user:
                raise Http404
            if obj.units == essencial.units:
                if obj.quantity < essencial.quantity:
                    obj.quantity = essencial.quantity
                    obj.save(update_fields=['quantity'])
            else:
                is_error += 1
                id_obj_error.append(obj.id)
                id_essencial_error.append(essencial.id)
    obj_error = Food.objects.filter(pk__in=id_obj_error)
    essencial_error = Essencial.objects.filter(pk__in=id_essencial_error)
    list_error = zip(obj_error, essencial_error)
    context = {'is_error':is_error, 'list_error': list_error}
    return render(request, 'my_fridge/add_essentials_to_fridge.html', context)


@login_required
def change_units(request, food_id):
    food = Food.objects.get(id=food_id)
    if food.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = FoodForm(instance=food)
        form.fields['text'].widget.attrs['readonly'] = True
    else:
        # POST data submitted; process data.
        form = EssencialForm(request.POST, instance=food)
        form.fields['text'].widget.attrs['readonly'] = True

        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('my_fridge:essencials'))

    context = {'form': form, 'food': food}
    return render(request, 'my_fridge/change_units.html', context)


@login_required
def remove_food(request, food_id):
    food = Food.objects.get(id=food_id)
    if food.owner != request.user:
        raise Http404

    food.delete()

    context = {'food': food}
    return render(request, 'my_fridge/remove_food.html', context)


@login_required
def remove_essencial(request, essencials_id):
    essencial = Essencial.objects.get(id=essencials_id)
    if essencials.owner != request.user:
        raise Http404

    essencial.delete()

    context = {'essencial': essencial}
    return render(request, 'my_fridge/remove_essencial.html', context)





