# mbolafy/portfolio/views.py

from django.shortcuts import render
from accueil.models import Hero
from parcour.models import Parcours
from experience.models import Experience
from competence.models import Competence
from projet.models import Projet
from contact.models import ContactInfo

def home(request):
    # Récupérer le profil actif (le plus récent si plusieurs)
    hero = Hero.objects.filter(is_active=True).order_by('-created_at').first()
    # recupérer les parcours actifs
    parcours = Parcours.objects.filter(is_active=True).order_by('ordre', '-annee_debut')
    # recupérer les expériences actives
    experiences = Experience.objects.filter(is_active=True).order_by('-created_at')
    # recupere les compétences actives
    competences = Competence.objects.all().order_by('ordre')
    # recuperer les projets actifs
    projets = Projet.objects.filter(is_active=True).order_by('-created_at')
    # Récuperation des infos de contact actives
    contact_info = ContactInfo.objects.filter(is_active=True).order_by('-created_at').first()

    context = {
        'hero': hero,
        'parcours': parcours,
        'experiences': experiences,
        'competences': competences,
        'projets': projets,
        'contact_info': contact_info,
    }

    return render(request, "portfolio/index.html", context)
