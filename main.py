# Le Jeu de Math  # programme a developper 
import random

NB_MIN = 1
NB_MAX = 100
NB_QUESTIONS = 10

def poser_question():
      
    a = random.randint(NB_MIN, NB_MAX)
    b = random.randint(NB_MIN, NB_MAX)
    o = random.randint(0, 1)
    if o ==0:
        reponse_str = input(f"donner la reponse a l'equation suivante : {a} + {b} = " )
    else:
        reponse_str = input(f"donner la reponse a l'equation suivante : {a} * {b} = " )
    reponse_int = int(reponse_str)

    calcul = a + b
    if o == 1:
        calcul = (a)*(b)
    if (reponse_int) == calcul:    
        return True
    return False


nb_points = 0

for i in range(0,NB_QUESTIONS):
    print(f"question n° {i+1} sur {NB_QUESTIONS}")
    if poser_question():
        print("bravo vous avez gagné")
        nb_points +=1
        print(f"votre score est de : {nb_points}/{NB_QUESTIONS}")
    else:
        print("reponse incorrécte")
    print()
  
print(f"votre score final est de : {nb_points}/{NB_QUESTIONS}")

moyenne = int(NB_QUESTIONS/2)

if nb_points == NB_QUESTIONS:
    print(f"EXCELLENT")
elif nb_points == 0:
    print(f"Reviser vos leçons de maths !")
elif NB_QUESTIONS > nb_points > moyenne:
    print(f"pas mal")
elif 0 < nb_points < moyenne : 
    print(f"peut mieux faire")




    
