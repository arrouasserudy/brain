---
description: Shula — mon appli qui résume les groupes WhatsApp de parents en une page par classe ; feuille de route, infra, message aux parents pas encore envoyé
type: projet
statut: actif
tags: [side-project, revenus]
created: 2026-10-01
updated: 2026-10-10
---
# Shula (שולה)

**Objectif :** nouvelle source de revenus.
**Domaine :** [[Travail]]
**Repo :** arrouasserudy/shula
**Appli web :** smart-class-web.fly.dev (une URL par classe, protégée par un code)

## Ce que c'est
- L'appli lit les groupes WhatsApp de parents d'élèves et en fait une page simple par classe : quoi apporter aujourd'hui et demain, ce qui arrive bientôt, ce qu'il faut retenir (dates limites, paiements, qui récupère qui).
- On peut l'ajouter à l'écran d'accueil comme une app, et recevoir un petit rappel le matin seulement s'il faut apporter quelque chose.

## État (octobre 2026)
- L'appli tourne ; je l'utilise personnellement.
- Je ne l'ai encore montrée à personne : le message aux parents est rédigé (2026-09-01) mais **pas envoyé**.

## Prochaines étapes
- [ ] Envoyer le message au groupe des parents (ci-dessous), avec le lien de la classe et le code d'accès.
- [ ] Faire la QA avec un nouveau groupe et vérifier que tout marche.
- [ ] Acheter un nom de domaine ; travailler l'interface, le logo, le nom et le marketing.
- [ ] Gérer les réponses citées (reply quotes).
- [ ] Logs et analytics ; un admin pour voir ce qui se passe (nouvelles connexions…).
- [ ] Améliorer l'interface (police Rubik, freefonts.co.il), regrouper par catégorie.
- [ ] Ajouter une section devoirs ; intégrer Google Agenda ; un onglet contacts.
- [ ] Préparer une belle démo avec de vraies données.

## Plus tard
- Onboarding automatique, paywall, minuteur de fin d'essai gratuit, conditions d'utilisation.
- Gérer les images (classification + OCR) et les messages vocaux.
- Admin : alerte de budget OpenAI, alertes Telegram sur les nouvelles connexions, fenêtre de regroupement réglable par classe.
- Quelques parents qui peuvent ajouter, modifier ou supprimer des éléments (code ou OAuth).
- Peut-être une file SQS ; peut-être WasenderAPI à la place du serveur Baileys.

## Fait
- Nouvelle version du code (v2 seulement), mot de passe pour se connecter, URLs en /{uuid}, page d'accueil par défaut.
- Code gardé dans les cookies, plusieurs classes dans l'interface selon le code.
- Demande de feedback, gestion des sondages.
- Renommage automatique quand le nom du groupe change.
- Fenêtre de regroupement : 10 min minimum, 20 min maximum.

## Infra
- Une adresse Gmail dédiée au bot, une base Supabase, Fly.io.
- Un serveur toujours allumé avec Baileys (sur un numéro 055) : il enregistre les messages et gère les plannings par fenêtre.
- Un serveur qui traite les lots de messages et en sort les éléments (il peut s'endormir).
- L'appli web (Vercel).

## Message aux parents (rédigé le 2026-09-01, pas envoyé)
> היי לכולם 🙂
> בזמן האחרון בניתי כלי קטן בשם שולה, שנועד לפתור משהו שקורה לכולנו: הקבוצה פה עמוסה, ובתוך כל ההודעות הולכים לאיבוד הדברים שבאמת צריך לעשות — מה להביא מחר, מי אוסף, תשלומים, תאריכים אחרונים.
> שולה קוראת את מה שנכתב בקבוצה ומרכזת את זה לעמוד אחד פשוט לכיתה שלנו: מה צריך להביא היום ומחר, מה בקרוב, ומה חשוב לזכור באופן קבוע. אפשר גם להוסיף את זה למסך הבית כמו אפליקציה, ולקבל בבוקר תזכורת קצרה רק אם באמת צריך להביא משהו.
> הנה הקישור לכיתה שלנו: [lien de la classe + code]
> זה עדיין בהתחלה, ואשמח מאוד לשמוע מה אתם חושבים — מה עוזר, מה מיותר, ומה חסר. כל פידבק (גם ביקורת) יתקבל בשמחה 🙏

Note du 2026-09-07, pour un message de présentation : ne pas parler du produit, seulement du problème, avec une seule ligne sur la solution.

## Liens
- [[Mes idées de produits]] · [[Freemo]]
