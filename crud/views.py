from django.shortcuts import render , redirect
from .models import Employer

#=============================================================

def home(request):
    context = {}
    context['workers'] = Employer.objects.all()

    return render(request, 'home.html', context=context)

def ajouter(request):
    
    return render(request, 'addpage.html')

def enregistrer(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        email = request.POST.get('email')
        numero = request.POST.get('numero')
        poste = request.POST.get('poste')
        Employer.objects.create(nom=nom, email=email, numero=numero, poste=poste)
        return redirect('/')
    
def supprimer(request, id):
    profil = Employer.objects.get(id=id)
    profil.delete()
    return redirect('/')

def modifier(request, id):
        worker = Employer.objects.get(id=id)
        return render(request, 'updatepage.html', {'worker':worker})

def valider(request, id):
     if request.method == 'POST':
        profil = Employer.objects.get(id=id)

        nouveau_nom = request.POST.get('nom')
        nouveau_email = request.POST.get('email')
        nouveau_numero = request.POST.get('numero')
        nouveau_poste = request.POST.get('poste')

        profil.nom = nouveau_nom
        profil.email = nouveau_email
        profil.numero = nouveau_numero
        profil.poste = nouveau_poste

        profil.save()
        return redirect('/')