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

def moyenne_tuples(notes,eleve,matiere):
  s=0
  i = 0
  for x in notes:
    if x[0] == eleve and x[1]== matiere:
      s+=x[2]
      i+=1
  moy = s / i
  return moy

print(moyenne_tuples(notes,'eleve1','math'))

#Que se passe-t-il si on fait une faute de frappe dans la saisie d'une matière ?
# Le shell ne trouve pas la matière et signale une erreur de syntaxe

#Que se passe-t-il si quelqu'un rentre une chaine de caractère au lieu d'une nombre '14' au lieu de 14 ?
#chaine de caractère pas définie

#Que se passe-t-il si on veut ajouter des coefficient aux notes et aux matières ?
#Ca ne marchera pas car on a pas rentré de paramètre pour les coefficients dans la fonction moyenne_tuples

#Que se passe-t-il si on a un triplet qui n'est pas du tout une note ?
#Problème d'integer car ce n'est pas possible de faire une moyenne sans une note

liste notes_enregistrées=[]

class Note:
  def __init__(self, eleve, matiere, valeur): #La méthode pour créer un objet
    self.eleve = eleve
    self.matiere = matiere
    self.valeur = valeur

  def __str__(self):
    return "La note est de {self.valeur} pour l'{self.eleve} en {self.matiere}.".format(self=self)

  def afficher(self):
    print('eleve', self.eleve, 'matiere', self.matiere, 'note', self.valeur)


onote = Note('eleve1', 'maths', 13)
print(onote.eleve)
print(onote.matiere)
print(onote.valeur)
Note.afficher(onote)

onotes=[]
for i in notes:
  onotes.append(Note(notes[0],notes[1],notes[2]))
print(onotes)

ma_note=Note('eleve1', 'math', 13)
print(ma_note)

def moyenne_Notes(notes,eleve,matiere):
  s=0
  for x in Note:
    if self.eleve == eleve and self.matiere== matiere:
      s+= self.valeur
  moy = s / i
  return moy