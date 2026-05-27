---
layout: default
title: Programmation
parent: Notre travail
nav_order: 3
---

Afin de faire communiquer les différents composants ensemble, il est nécessaire d'écrire des programmes que nous allons charger sur la carte arduino.

Dans notre projet, nous utilisons plusieurs bibliothèques pour Arduino qui vont nous aider à simplifier le code et nous permettre une utilisation plus simple des composants.

Nous utilisons la bibliothèque [Accelstepper](https://www.airspayce.com/mikem/arduino/AccelStepper/) pour l'utilisation des moteurs pas-à-pas.

Les avantages de cette bibliothèque sont notamment:
* permet l'accélération/décélération et l'utilisation de vitesse très basse
* permet l'utilisation simultanné de plusieurs moteur indépendant
* la pluspart des fonctions ne sont pas bloquantes ce qui permet de réaliser des tâches en simultanné
---
Nous utilisons la bibliothèque [Servo](https://docs.arduino.cc/libraries/servo/) pour l'utilisation des servomoteurs.

Les avantages de cette bibliothèque sont notamment:
* la création d'un objet pour les servomoteurs ce qui permet une utilisation simplifié de ce dernier
* l'utilisation de plusieurs servomoteurs à la fois
* l'utilisation d'angle afin de donner des positions au moteur au lieu d'avoir à gérer les impulsions PWM

---
Choix des PINS 

<img src="../images/Choix_PINS.PNG" width="400" height="400"></img>

Pour faire communiquer la carte arduino avec les composants du Puzzle bot ( Servomoteurs, bouton fin de course, etc) il est necessaire de leur attribuer des PINS. 

Setup
---

<img src="../images/Setup.PNG" width="400" height="400"></img>

Cette partie du code sert à l'initialisation des composants. Elle est exécutée une seule fois lors de la mise sous tension de la carte.

Activation des Moteurs et Pompes 
---
<img src="../images/Moteur_Pompe.PNG" width="400" height="400"></img>

Ces fonctions ont pour objectif respectif l'activation des moteurs et de la pompe.

LimitPressed
---

<img src="../images/LimitPressed.PNG" width="400" height="400"></img>

Cette fonction permet à notre programme de détecter lorsque l'un des interrupteurs fin de course est actionné. Elle est notamment utilisé lors de la phase de HOMING qui permet de définir un systéme de coordonnée à nos moteurs stepper. Cette phase sera expliqué plus en détail dans la partie suivante du code. 

Homing
---
<img src="../images/Homing.PNG" width="400" height="400"></img>

L'algorithme de cette fonction est plutot simple: Il va donner comme instruction aux moteurs d'aller dans un sens en utilisant deux fonctions de la bibliothèque AcceLstepper  la fonction SetSpeed (il définit le sens en fonction du signe de la vitesse) couplée avec la fonction RunSpeed jusqu'a atteindre l'interrupteur fin de course de l'axe correspondant. Nous exécutons cette fonction dans la partie Setup du programme comme vous avez pu le voir précedemment. 

