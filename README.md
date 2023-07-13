# Spaceship
![image](https://github.com/YanisARE/Spaceship/assets/99649037/d15d64f3-fd53-4f0b-9ea9-ea8dc38b2fbd)
# Projet SpaceApp

## Table des matières

1. [Introduction](#introduction)
2. [Cahier des charges](#cahier-des-charges)
3. [Installation](#installation)
4. [Utilisation](#utilisation)

## Introduction

Ce projet, baptisé SpaceApp, est une application backend que j'ai conçue pour être utilisée par les agences spatiales, passionnés d'exploration spatiale, enseignants ou chercheurs. Elle permet de suivre en temps réel les orbiteurs actuellement en espace et d'identifier leurs modules respectifs. L'application tire ses données de localisation d'une autre API, N2YO, et fournit des fonctionnalités supplémentaires pour une meilleure expérience utilisateur.

SpaceApp est construite sur Django et utilise le framework Django Rest pour créer des API REST. De plus, l'application utilise Docker pour l'isolation des processus, ce qui facilite le déploiement et l'échelle. L'application est divisée en deux conteneurs Docker : un pour la base de données PostgreSQL et l'autre pour l'application elle-même.

## Cahier des charges

### 1. Définition d'une API et du protocole REST

L'API, ou Interface de Programmation d'Application, est un ensemble de règles et de protocoles établis pour permettre à des applications de communiquer entre elles. Le protocole REST, ou REpresentational State Transfer, est un style d'architecture logicielle qui définit des règles pour la création de services web. Il se base sur le protocole HTTP et permet une communication entre le client et le serveur.

### 2. Initialisation du projet Django Rest Framework

J'ai utilisé PyCharm comme environnement de développement pour construire le projet et Postman pour tester les différentes commandes CRUD de l'API.

### 3. Implémentation de l'API

J'ai utilisé PostgreSQL pour la base de données de mon application. J'ai créé un modèle de données pour les voitures, avec un serializer et un viewset générique. 

Chaque voiture est représentée par un ID, une marque (parmi quatre marques possibles), un modèle, une couleur, un kilométrage, un prix et une date de parution. J'ai également configuré la page d'administration pour afficher la liste des voitures par marque et par prix.

### 4. Configuration de Swagger

J'ai utilisé Swagger pour la documentation et la visualisation de l'API. L'outil m'a permis de présenter de manière intuitive les différents endpoints et le format JSON des données.

## Installation

Pour installer et exécuter le projet, vous aurez besoin de Docker et de Docker Compose. Une fois ces outils installés, vous pouvez cloner le projet depuis le repository GitHub et lancer les conteneurs Docker avec la commande `docker-compose up --build`.

## Utilisation

Une fois l'application en cours d'exécution, vous pouvez accéder à l'API via l'URL `http://localhost:8000`. Les données sont présentées sous la forme d'une API REST, vous pouvez donc les récupérer en utilisant les méthodes HTTP standard (GET, POST, PUT, DELETE). Vous pouvez également utiliser Swagger pour explorer l'API en accédant à `http://localhost:8000/swagger`.

## Conclusion

SpaceApp est une application backend puissante et flexible qui fournit des informations précieuses sur les orbiteurs en espace et leurs modules. Elle peut être facilement déployée et mise à l'échelle grâce à l'utilisation de Docker, ce qui la rend parfaitement adaptée aux besoins des agences spatiales.

