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
