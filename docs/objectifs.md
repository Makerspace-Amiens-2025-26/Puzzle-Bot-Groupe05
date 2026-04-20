---
layout: default
nav_order: 3
title: Objectifs du projet
---

# Introduction

Dans le cadre de nos études à Unilasalle Amiens, nous sommes ammenés à réaliser différents projets de conception robotique afin de nous enseigner différentes compétences qui nous seront utiles dans nos futurs métiers. C'est donc le cas de ce projet qui va nous apporter de nouvelles connaissances autour de plusieurs domaines (conception assisté par ordinateur, manipulation de composant divers, algorithmie et autres). Bien entendu, il nous a confronté à un bon nombre d'épreuve et difficulté que nous vous présenterons dans les autres parties de ce site.

## Objectifs du Projet

En soit, ce projet a pour but de nous mettre en contact avec différents enjeux actuels (contrôle de robot, automatisation, intéraction avec l’environnement) et de développer nos compétences, à la fois technique et nos soft skills (travail en équipe, présentation technique).

Il passe par plusieurs pallier de réalisation: 
* Puzzle "simple":
    position et orientation des pièces connues,
    constitué de 4 à 6 pièces de formes carrées (sans encoches),
    a pour but de vérifier que notre robot puisse déplacer les pièces d'un point A à un point B

* Puzzle "simple" avec orientation variable:
    idem qu'au dessus mais l'orientation des pièces est dorénavant variable,
    a pour but de vérifier que notre robot puisse réorienter les pièces afin de les mettre dans le bon sens

* Détection des pièces avec des marqueurs ArUco:
    l'emplacement des pièces n'est plus connues au préalable,
    nous rajoutons donc une caméra qui va détecter les marqueurs ArUco afin de déterminer la position et l'orientation des pièces

* Assemblage du puzzle avec les marqueurs précédemment introduits:
    maintenant que le robot peut détecter les pièces,
    nous pouvons commencer l'assemblage du puzzle

* Etape finale:
    nous retirons les marqueurs et nous effectuons l'assemblage du puzzle,
    la détection ne se fait donc plus qu'avec la forme ou la couleur des pièces.
  
# Existant

Ce projet s'inspire des robots conçu par [Mark Rober](https://www.youtube.com/watch?v=Sqr-PdVYhY4) et [Stuff Made Here](https://www.youtube.com/watch?v=WsPHBD5NsS0).

# Cahier des Charges

Pour réaliser ce projet, nous avons dû respecter certaines consignes. 
Tout d'abord, nous avons eu une contrainte de temps: 
* En effet, après les 25 premières heures de travail en classe, nous avons effectué une présentation technique de notre projet afin de faire valider nos choix et de montrer l'état d'avancement des recherches et des réalisations. 
* Après cette présentation, nous avons 50 autres heures afin de finaliser notre projet. Cette finalisation inclus: la rédaction de la documentation technique, la vidéo de présentation, le rendu OnShape et le fonctionnement complet du robot.

Sinon du point de vue matériel et technique, nous avons été plutôt libre quand à nos choix du moment que nous ne demandions pas trop d'argent.

En outre, nous avons également eu pour consignes de répartir les tâches en plusieurs sous-groupes autour de thèmes bien précis (conception, electronique, programmation). Les tâches de ces sous-équipes sont détaillé dans une autre section.
