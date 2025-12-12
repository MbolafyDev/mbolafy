# mbolafy/portfolio/views.py

from django.shortcuts import render

# Import des modèles depuis chaque app
from accounts.models import Profile
from about.models import IntroItem
from skills.models import Quality, Language
from contact.models import ContactInfo
from hobbies.models import Hobby
from experience.models import Experience
from photos.models import Photo
from competence.models import Competence  # nouvelle app
from projet.models import Projet  # nouvelle app
from intro.models import About  # nouvelle app

def home(request):
    # Récupération des données
    profile = Profile.objects.first()  # 1 seul profil
    intro_items = IntroItem.objects.all()  # Liste des items intro
    about = About.objects.first()
    qualities = Quality.objects.all()  # Qualités personnelles
    languages = Language.objects.all()  # Compétences techniques / langages
    contact_info = ContactInfo.objects.first()  # 1 seul contact
    hobbies = Hobby.objects.all()  # Loisirs
    photos = Photo.objects.all().order_by('-uploaded_at')  # Photos récentes en premier
    skills = Competence.objects.all().order_by('-level')  # Compétences dynamiques
    projects = Projet.objects.all().order_by('-created_at')  # Projets dynamiques

    # Experiences et parcours (même modèle, différencié par type)
    experiences = Experience.objects.filter(type='experience').order_by('-year')
    parcours = Experience.objects.filter(type='parcours').order_by('-year')

    context = {
        "profile": profile,
        "intro_items": intro_items,
        "about": about,
        "qualities": qualities,
        "languages": languages,
        "contact_info": contact_info,
        "hobbies": hobbies,
        "photos": photos,
        "skills": skills,          # injection dans le template
        "projects": projects,      # injection dans le template
        "experiences": experiences,
        "parcours": parcours,
    }

    return render(request, "portfolio/index.html", context)
