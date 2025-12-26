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
    profile = Profile.objects.first()
    intro_items = IntroItem.objects.all()
    about = About.objects.first()
    qualities = Quality.objects.all()
    languages = Language.objects.all()  # récupère les niveaux textuels
    contact_info = ContactInfo.objects.first()
    hobbies = Hobby.objects.all()
    photos = Photo.objects.all().order_by('-uploaded_at')
    skills = Competence.objects.all().order_by('-level')
    projects = Projet.objects.all().order_by('-created_at')

    experiences = Experience.objects.filter(type='experience').order_by('-year')
    parcours = Experience.objects.filter(type='parcours').order_by('-year')

    context = {
        "profile": profile,
        "intro_items": intro_items,
        "about": about,
        "qualities": qualities,
        "languages": languages,  # injection pour template
        "contact_info": contact_info,
        "hobbies": hobbies,
        "photos": photos,
        "skills": skills,
        "projects": projects,
        "experiences": experiences,
        "parcours": parcours,
    }

    return render(request, "portfolio/index.html", context)
