---
layout: default
title: Branchement
parent: Notre travail
nav_order: 2
---


-Branchement des 3 moteurs pas à pas:
<img src="../images/Branchement_stepper.jpeg" width="400" height="400">
Explications:
Chaque module contrôle un moteur pas à pas (X,Y,Z) sur la CNC Shield. Sachant que deux des moteurs sont placés sur l'axe X et un autre moteur sur l'axe Y 
L'ordre des fils dépend du moteur, mais:
. Si le moteur vibre sans tourner alors les fils sont mal placés,
. Si le sens est inversé il faudra inverser une paire
L'utilisation des jumpers nous permettent de dupliquer le movement d'un des moteurs pas à pas de l'axe X

