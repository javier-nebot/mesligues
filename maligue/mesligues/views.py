from django.http import HttpResponse
from django.template import loader

from .models import Participant, Ligue, Match

import operator

def index(request):
    template = loader.get_template('mesligues/index.html')
    context = {
        'liste_participants' : liste_participants(request),
        'liste_matchs' : liste_matchs(request),
        'classement' : classement(request)
    }
    return HttpResponse(template.render(context, request))


##  Participants -----------------------------------------------------------

def liste_participants(request):
    list_parti = Participant.objects.all()
    template = loader.get_template('mesligues/liste_participants.html')
    context = {
        'liste_participants':list_parti,
    }
    return HttpResponse(template.render(context, request))

def participant(request, participant_id): # a developper
    return HttpResponse("Tu est en train de regarder le participant %s" % participant_id)

###  Matchs -------------------------------------------------------------------

def liste_matchs(request):
    list_match = Match.objects.all()
    template = loader.get_template('mesligues/liste_matchs.html')
    context = {
        'liste_matchs':list_match,
    }
    return HttpResponse(template.render(context, request))

def match(request, match_id): # a developper
    #template = loader.get_template('mesligues/match.html')
    return HttpResponse("Tu est en train de regarder le match %s" % match_id)

###  Classement ----------------------------------------------------------------

def points_classement():
    mon_dict = {}
    mes_participants = Participant.objects.filter()
    for participant in mes_participants:
        mon_dict[str(participant)]=0
    
    mes_matchs = Match.objects.filter()
    for match in mes_matchs:
        if match.score_locaux > match.score_visiteur:
            mon_dict[str(match.locaux)] += 3
        elif match.score_locaux < match.score_visiteur:
            mon_dict[str(match.visiteur)] += 3
        else:
            mon_dict[str(match.locaux)] += 1
            mon_dict[str(match.visiteur)] += 1

    mon_dict_ord = sorted(mon_dict.items(), key=operator.itemgetter(1), reverse=True)

    return mon_dict_ord

def classement(request):
    points_clas = points_classement()
    template = loader.get_template('mesligues/classement.html')
    context = {
         'points_classement':points_clas
    }
    return HttpResponse(template.render(context, request))


    