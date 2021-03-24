import statistics

note1 = ('eleve1', 'math', 13)
note2 = ('eleve1', 'physique', 15)
note3 = ('eleve1', 'math', 13)
note4 = ('eleve1', 'eco', 12)
note5 = ('eleve1', 'eco', 13)
note6 = ('eleve1', 'math', 12)
note7 = ('eleve2', 'math', 13)
note8 = ('eleve2', 'math', 14)

notes = [note1, note2, note3, note4, note5, note6,note7,note8]


#4
moy1 = (notes[0][2]+notes[1][2]+notes[2][2]+notes[3][2]+notes[4][2]+notes[5][2])/6
print("la moyenne de l'élève 1 = ",moy1)
y=(13,13,12)
print(statistics.mean(y))

notes_elv1 = [note for note in notes if note[0] == 'eleve1']
notes_elv1_maths = [n for n in notes_elv1 if n[1] == 'math']
print(notes_elv1_maths)
print(sum(n[2] for n in notes_elv1_maths)/len(notes_elv1_maths))

def moyenne_tuples(notes, eleve = None, matiere = None):
  notes_elv = [note for note in notes if note[0] == eleve] if eleve is not None else notes
  notes_elv_matiere = [n for n in notes_elv if n[1] == matiere] if matiere is not None else notes_elv

  return sum([n[2] for n in notes_elv_matiere])/len(notes_elv_matiere)

print(moyenne_tuples(notes,'eleve1','math'))

#Que se passe-t-il si on fait une faute de frappe dans la saisie d'une matière ?
# Le shell ne trouve pas la matière et signale une erreur de syntaxe

#Que se passe-t-il si quelqu'un rentre une chaine de caractère au lieu d'une nombre '14' au lieu de 14 ?
#chaine de caractère pas définie

#Que se passe-t-il si on veut ajouter des coefficient aux notes et aux matières ?
#Ca ne marchera pas car on a pas rentré de paramètre pour les coefficients dans la fonction moyenne_tuples

#Que se passe-t-il si on a un triplet qui n'est pas du tout une note ?
#Problème d'integer car ce n'est pas possible de faire une moyenne sans une note
notes_enregistrees = []

class Note:
  def __init__(self, eleve, matiere, valeur): #La méthode pour créer un objet
    self.eleve = eleve
    self.matiere = matiere
    self.valeur = valeur
    notes_enregistrees.append(self)
#Question 6
  def __str__(self):
    return "La note est de {self.valeur} pour l'{self.eleve} en {self.matiere}.".format(self=self)

  def afficher(self):
    print('eleve', self.eleve, 'matiere', self.matiere, 'note', self.valeur)


onote = Note('eleve1', 'maths', 13)
print(onote.eleve)
print(onote.matiere)
print(onote.valeur)
Note.afficher(onote)
print(onote)

#Question 5
onotes = [Note(elv, matiere,  valeur) for elv, matiere, valeur in notes]
for onote in onotes:
  onote.afficher()

#Question 7
for onote in notes_enregistrees:
  onote.afficher()

#Question 8

def moyenne_Notes(liste, eleve = None, matiere = None):
  liste_elv = [note for note in liste if note.eleve == eleve] if eleve is not None else liste
  liste_elv_matiere = [le for le in liste_elv if le.matiere == matiere] if matiere is not None else liste_elv

  return sum([n.valeur for n in liste_elv_matiere])/len(liste_elv_matiere)
  


print(moyenne_Notes(notes_enregistrees))