print("mon premier projet que je doit presente sur github ")
class Gestion :
    def __init__( self,nom,age):
        self.nom=nom
        self.age=age
    def afficher(self):
        print("nom : ",self.nom,"\nage: ",self.age)
        print("je suis un etudiant")
def ajouter():
    nom= input("donner le nom de l'etudiant ")
    age=input("donner l'age de l'age ")
    e=Gestion(nom,age)
    return e
def chercher(liste):
    nom_rhc=input("donner le nom de l'etudiant que vous rechercher")
    for i in range(len(liste)):
        if nom_rhc==liste[i].nom:
            print("trouver\n infos")
            liste[i].afficher()
            return
    print(nom_rhc,"nest pas dans la liste")
def supprimer(liste):
    n_sup=input("nom de l'etudiant a supprimer")
    for i in range(len(liste)):
        if n_sup==liste[i].nom:
            print('menu de suppression \n  a pour le nom \nb pour l age')
            choix=input("faites votre choix")
            if choix=='a':
                del liste[i].nom
            else:
                del liste[i].age    
            return
    print("suppression impossible")
liste=[]
for i in range(1):
    liste.append(ajouter())
for i in range(1):
    liste[i].afficher()
chercher(liste)
supprimer(liste)




            