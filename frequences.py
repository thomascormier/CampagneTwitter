class Frequences :
    #def __init__(self):
        #self.ActivitesParHeure = self.calculActiviteHoraire()
        # Un tableau contenant 24 cases qui renseigne sur l'activité des followers sur chaque heure pendant 1 jour
        #self.ActivitesParHeure = [336]
        # Un tableau contenant 336 cases qui renseigne sur l'activité des followers sur chaque heure pendant 1 mois

    def getWeekday(self,YearTweet,MonthTweet,DayTweet):
        """
        :param YearTweet: L'année de publication du tweet
        :param MonthTweet: Le mois de publication du tweet
        :param DayTweet: Le jour de publication du tweet
        :return: Le jour de la semaine duquel le Tweet a été envoyé
        """
        return datetime.date(YearTweet, MonthTweet, DayTweet).strftime("%A")


    def calculActiviteHoraire(self):
        """
        On crée un tableau de taille 24 où chaque case représente une heure.
        On passe tous les tweets et on incrémente la case du tableau qui correspond à l'heure de publication du tweet
        :return: rien
        """
        ActivitesParHeure = []
        for follower in TwitterAPI.listFollowers:
            for tweet in follower.listTweets:
                heure = int(tweet.date[11:13])
                ActivitesParHeure [heure]+=1

    def setPeaksActivite(self,ExempleListeHeures):
        """
        On passe d'une liste d'heures de publications à une liste de nombre d'activité par heure
        :param ExempleListeHeures:
        :return:
        """
        ActiviteParHeure = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for h in ExempleListeHeures:
            ActiviteParHeure[h] += 1

    def nToWeekDay(self,numHour):
        numWeekday = numHour//24
        WeekdayDic = {0 :"lundi   ", 1 : "mardi   ",2: "mercredi",3: "jeudi   ",4: "vendredi",5: "samedi  ",6: "dimanche"}
        return WeekdayDic[numWeekday]

    def hBefore(self,numHour):
        return numHour%24

    def hAfter(self,numHour):
        return numHour%24+1

    def pourcentageActivite(self,hmax):
        return (ActiviteParHeure[hmax] / sommeActivite)*100

freq1= Frequences()

"""
On a une liste de date on cherche les pics:

On regarde les heures qui reviennent le plus 
"""

ListeDActivites = [[2, 19], [4, 18], [0, 3], [4, 12], [1, 17], [2, 18], [5, 19], [3, 20], [6, 12], [4, 22], [3, 17], [4, 22], [2, 1], [3, 2], [4, 11], [2, 14], [1, 16], [2, 19], [2, 18], [4, 19], [3, 17], [2, 19], [2, 16], [6, 20], [0, 20]]
ActiviteParHeure = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

#def setWeekActivite() :

for activite in ListeDActivites:
    a = activite[0]*24+activite[1]
    ActiviteParHeure[a]+=1

sommeActivite = float(sum(ActiviteParHeure))


for i in range(5):
    hmax = ActiviteParHeure.index(max(ActiviteParHeure))
    print(freq1.pourcentageActivite(hmax), "% :",freq1.nToWeekDay(hmax), "(", freq1.hBefore(hmax), "-", freq1.hAfter(hmax), "))")
    del ActiviteParHeure[hmax]


hmax1 = ActiviteParHeure.index(max(ActiviteParHeure))
print("\nLa période d'activité maximale est le", freq1.nToWeekDay(hmax1), "entre", freq1.hBefore(hmax1), "h et", freq1.hAfter(hmax1), "h.")
print("La semaine dernière, cette période représentait", freq1.pourcentageActivite(hmax1),"% de l'activité de vos Followers.")



del ActiviteParHeure[hmax1]
hmax2 = ActiviteParHeure.index(max(ActiviteParHeure))
print("\nLa période d'activité maximale est le", freq1.nToWeekDay(hmax2), "entre", freq1.hBefore(hmax2), "h et", freq1.hAfter(hmax2), "h.")
print("La semaine dernière, cette période représentait", freq1.pourcentageActivite(hmax2),"% de l'activité de vos Followers.")

del ActiviteParHeure[hmax2]
hmax3 = ActiviteParHeure.index(max(ActiviteParHeure))
print("\nLa période d'activité maximale est le", freq1.nToWeekDay(hmax3), "entre", freq1.hBefore(hmax3), "h et", freq1.hAfter(hmax3), "h.")
print("La semaine dernière, cette période représentait", freq1.pourcentageActivite(hmax3),"% de l'activité de vos Followers.")

del ActiviteParHeure[hmax3]
hmax4 = ActiviteParHeure.index(max(ActiviteParHeure))
print("\nLa période d'activité maximale est le", freq1.nToWeekDay(hmax4), "entre", freq1.hBefore(hmax4), "h et", freq1.hAfter(hmax4), "h.")
print("La semaine dernière, cette période représentait", freq1.pourcentageActivite(hmax4),"% de l'activité de vos Followers.")

del ActiviteParHeure[hmax4]
hmax5 = ActiviteParHeure.index(max(ActiviteParHeure))
print("\nLa période d'activité maximale est le", freq1.nToWeekDay(hmax5), "entre", freq1.hBefore(hmax5), "h et", freq1.hAfter(hmax5), "h.")
print("La semaine dernière, cette période représentait", freq1.pourcentageActivite(hmax5),"% de l'activité de vos Followers.")