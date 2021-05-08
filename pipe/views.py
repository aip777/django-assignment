from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
# Create your views here.
from .forms import AddPipeForm, EditPipeForm, AddCoatingForm, AddContentsForm
from .models import Pipe, Contents, Coating
import math

def index(request):

    return render(request, 'pipe/add-pipe.html')



# @login_required()
def addPipeView(request):
    if request.method == 'POST':
        form = AddPipeForm(request.POST, request.FILES)
        coating_form = AddCoatingForm(request.POST, request.FILES)
        contents_form = AddContentsForm(request.POST, request.FILES)
        if form.is_valid() and coating_form.is_valid() and contents_form.is_valid():
            form.save()
            coating = coating_form.save(commit=False)
            coating.pipe = Pipe.objects.latest('id')
            coating.save() 

            content = contents_form.save(commit=False)
            content.pipe = Pipe.objects.latest('id')
            content.coating = Coating.objects.latest('id')
            content.save() 
             
            messages.success(request, 'Successfully added')
            return redirect('pipe-list')
        else:
            messages.error(request, form.errors)
            return HttpResponseRedirect("#")
    else:
        pipe_form = AddPipeForm()
        coating_form = AddCoatingForm()
        content_form = AddContentsForm()
        pipe_form.fields['pipe_od'].queryset = Pipe.objects.all()
    context = {
        'content_form':content_form,
        'coating_form': coating_form,
        'form': pipe_form,
    }
    return render(request, 'pipe/add-pipe.html', context)


# @login_required()
def pipelistView(request):
    pipe = Pipe.objects.all()
    context = {
        'pipe': pipe,
    }
    return render(request, 'pipe/pipe-list.html', context)

# @login_required()
def updatePipeView(request, id):
    pipe = get_object_or_404(Pipe, id=id)
    if request.method == 'POST':
        form = EditPipeForm(request.POST, request.FILES, instance=pipe)

        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated')
            return redirect('pipe-list')
        else:
            messages.error(request, waiter_form.errors)
            return HttpResponseRedirect("#")
    else:
        form = EditPipeForm(instance=pipe)
    context = {
        # 'form': form,
        'form': form,
    }
    return render(request, 'pipe/update-pipe.html', context)


# @login_required()
def contentslistView(request):
    content = Contents.objects.all()
    context = {
        'content': content,
    }
    return render(request, 'pipe/content-list.html', context)

# @login_required()
def coatinglistView(request):
    coating = Coating.objects.all()
    context = {
        'coating': coating,
    }
    return render(request, 'pipe/coating-list.html', context)

# @login_required()
def deletePipeView(request, id):
    pipe = get_object_or_404(Pipe, id=id)
    pipe.delete()
    messages.success(request, 'Successfully deleted')
    return redirect('pipe-list')




def detailsView(request, id):
    pipe = get_object_or_404(Pipe, id=id)
    
    coating = Coating.objects.filter(pipe=pipe)
    contents = Contents.objects.filter(pipe=pipe)

    # Pipe
    # B5 = pipe_od
    # B6 = pipe_wt
    # B7 = pipe_density
    # B8 = corrosion_allowance

    # Coating
    # C11 = thickness
    # D11 = density

    # contents
    # C15 = installation_empty
    # C16 = flooded
    # C17 = hydrotest

    # =($Input.B5-2*$Input.B6)/2
    pipe_inside_radius_r1 = round((pipe.pipe_od - 2 * pipe.pipe_wt) / 2, 2)

    # =$Input.B5/2
    pipe_outside_radius_r2 = round(pipe.pipe_od / 2, 4)


    for obj in coating:
        # =E4+$Input.C11/2
        outer_radius_coating_r3 = pipe_outside_radius_r2 + obj.thickness / 2
        # =E5*2
        total_pipeline_outside_diameter = round(outer_radius_coating_r3 * 2, 2)

        density = obj.density
    
    for contents_obj in contents:

        installation_empty = contents_obj.installation_empty
        hydrotest = contents_obj.hydrotest

    # =PI()*(E4^2-E3^2)/144*$Input.B7
    # round(answer, 2)
    pipe_weight_per_unit_length = round(math.pi * (math.pow(pipe_outside_radius_r2, 2) - math.pow(pipe_inside_radius_r1, 2)) /144 * pipe.pipe_density,2)
    # =PI()*(E5^2-E4^2)/144*$Input.D11
    coating_wt_per_unit_length = round(math.pi * (math.pow(outer_radius_coating_r3, 2) - math.pow(pipe_outside_radius_r2, 2)) /144 * density,2)
    #=PI()*$E$3^2/144*$Input.$C$15

    contents_wt_per_unit_length = round(math.pi * (math.pow(pipe_inside_radius_r1, 2)) /144 * installation_empty, 2)
    #=SUM(E9:E11)
    total_pipeline_outside_diameter_obj = round(pipe_weight_per_unit_length + coating_wt_per_unit_length + contents_wt_per_unit_length, 2)
    # =PI()*E5^2/144*$Input.C17
    buoyant_force_per_unit_length = round(math.pi * (math.pow(outer_radius_coating_r3, 2)) / 144 * hydrotest, 2)
    # =$Output.E12-$Output.$E$13
    submerged = round(total_pipeline_outside_diameter_obj - buoyant_force_per_unit_length, 2)

    # =$Output.E12/$Output.$E$13
    submerged_sw = round(total_pipeline_outside_diameter_obj / buoyant_force_per_unit_length, 2)

    context = { 
        'pipe_inside_radius_r1':pipe_inside_radius_r1,
        'pipe_outside_radius_r2':pipe_outside_radius_r2,
        'outer_radius_coating_r3':outer_radius_coating_r3, 
        'total_pipeline_outside_diameter': total_pipeline_outside_diameter, 

        'pipe_weight_per_unit_length':pipe_weight_per_unit_length,
        'contents_wt_per_unit_length': contents_wt_per_unit_length, 
        'coating_wt_per_unit_length':coating_wt_per_unit_length,
        'total_pipeline_outside_diameter_obj':total_pipeline_outside_diameter_obj,
        'buoyant_force_per_unit_length':buoyant_force_per_unit_length,

        'submerged':submerged,
        'submerged_sw':submerged_sw,

        'pipe': pipe,
    } 
 
    return render(request, 'pipe/details.html', context)
 