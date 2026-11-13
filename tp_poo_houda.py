from abc import ABC, abstractmethod


class Personne(ABC):

    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def nom_complet(self):
        return f"{self.prenom} {self.nom}"

    @abstractmethod
    def role(self):
        pass 

# Classe Etudiant : héritage et encapsulation

class Etudiant(Personne):

    def __init__(self, nom, prenom, matricule):
        super().__init__(nom, prenom)

        self.__matricule = matricule
        self._notes = []

    # Matricule en lecture seule
    @property
    def matricule(self):
        return self.__matricule

    # Ajouter une note
    def ajouter_note(self, note):
        if not 0 <= note <= 20:
            raise ValueError("La note doit être entre 0 et 20.")

        self._notes.append(note)

    # Calculer la moyenne
    def moyenne(self):
        if len(self._notes) == 0:
            return 0.0

        return sum(self._notes) / len(self._notes)

    # Nombre de notes
    @property
    def nombre_notes(self):
        return len(self._notes)

    # Role de l'etudiant
    def role(self):
        return "Étudiant"

    # Affichage de l'etudiant
    def __str__(self):
        return (
            f"{self.nom_complet()} "
            f"(matricule {self.matricule}) - "
            f"moyenne : {self.moyenne():.2f}"
        )
 # Classe Enseignant : heritage

class Enseignant(Personne):

    def __init__(self, nom, prenom, matiere, heures, taux_horaire):
        super().__init__(nom, prenom)

        self.matiere = matiere
        self.heures = heures
        self.taux_horaire = taux_horaire

    # Calculer le salaire
    def salaire(self):
        return self.heures * self.taux_horaire

    # Role de l'enseignant
    def role(self):
        return "Enseignant"

    # Affichage de l'enseignant
    def __str__(self):
        return (
            f"{self.nom_complet()} - "
            f"Matière : {self.matiere}"
        )
        # Tests du programme

if __name__ == "__main__":

    # Test Etudiant
    etu = Etudiant("Diop", "Awa", "M001")

    etu.ajouter_note(15)
    etu.ajouter_note(18)

    print("ETUDIANT")
    print(etu)
    print("Role :", etu.role())
    print("Nombre de notes :", etu.nombre_notes)

    # Test Enseignant
    prof = Enseignant("Sow", "Moussa", "Python", 20, 500)

    print("\nENSEIGNANT")
    print(prof)
    print("Role :", prof.role())
    print("Salaire :", prof.salaire())

    # Test Heritage
    print("\nHERITAGE")
    print(isinstance(etu, Personne))

    # Test Encapsulation
    try:
        etu.ajouter_note(25)
    except ValueError as e:
        print("Erreur :", e)

    try:
        etu.matricule = "M999"
    except AttributeError as e:
        print("Erreur :", e)

    # Test Abstraction
    try:
        p = Personne("Sow", "Moussa")
    except TypeError as e:
        print("Erreur :", e)