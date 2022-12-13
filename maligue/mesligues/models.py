from django.db import models



class Participant(models.Model):
    nom_participant = models.CharField(max_length = 50)
    prenom_participant = models.CharField(max_length = 50)
    

    def __str__(self):
        return f"{self.prenom_participant} {self.nom_participant}" 

class Ligue(models.Model):
    nom_ligue = models.CharField(max_length = 50)

    def __str__(self):
        return self.nom_ligue

class Match(models.Model):
    nom_match = models.CharField(max_length = 50)
    date_match = models.DateTimeField('Match date')
    locaux = models.ForeignKey(Participant, on_delete=models.CASCADE, related_name='locaux')
    visiteur = models.ForeignKey(Participant, on_delete=models.CASCADE, related_name='visiteur')
    ligue= models.ForeignKey(Ligue, on_delete=models.CASCADE, related_name='ligue')
    score_locaux = models.IntegerField(default=0)
    score_visiteur = models.IntegerField(default=0)
    

    def __str__(self):
        return f"{self.nom_match}, {self.date_match}, {self.locaux}, {self.visiteur}, {self.ligue}, {self.score_locaux}, {self.score_visiteur} "

