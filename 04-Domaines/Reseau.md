---
description: Graphe de mes contacts par cercle de vie, associés potentiels
type: domaine
tags: [reseau]
updated: 2026-10-06
---
# Réseau

Cartographie des personnes connues, par cercle de vie. Objectif initial (2026-09-25) : repérer des associés potentiels pour des projets micro-SaaS.

## Graphe

```mermaid
graph LR
  R((Rudy))
  R --> ECOLE[École — Nahalal ?]
  R --> ARMEE[Armée]
  R --> ASH[Amis d'Ashdod]
  R --> NET[Amis de Netanya]
  R --> RAA[Amis de Ra'anana]
  R --> GS[Amis de Givat Shmuel]
  R --> BI[Bar-Ilan]
  R --> MCC[McCann — agence de pub]
  R --> AUT[Autres boîtes — à nommer]
  R --> INF[Formation Infinity]
  R --> FAM[Famille]
  R --> NC[Cercle à préciser]

  BI --> Teddy[Teddy · avocat]
  BI --> Avigael[Avigaël · comptable]
  BI --> Simon[Simon · data analyst]
  BI --> Eli[Eli · psychologue]
  FAM --> Brigitte[Brigitte · budget / podcast]
  FAM --> Michaela[Michaela · ergothérapeute]
  GS --> Itzik[Itzik · ostéo/kiné]
  ECOLE --> Yoav[Yoav · développeur · meilleur ami]
  RAA --> Yoav
  Yoav -. beau-père .- Jonas[Jonas · artisan]
  Eli -. projet ergo .- Michaela
```

## Cercles
| Cercle | Personnes | Statut |
|---|---|---|
| École (Nahalal ?) | [[Yoav]] | commencé, nom de l'école à confirmer |
| Armée | — | à remplir |
| Amis d'Ashdod | — | à remplir |
| Amis de Netanya | — | à remplir |
| Amis de Ra'anana | [[Yoav]] (y habite) | commencé (jugé à fort potentiel) |
| Amis de Givat Shmuel | [[Itzik]] | commencé |
| Bar-Ilan | [[Teddy]], [[Avigaël]], [[Simon]], [[Eli]] | commencé (jugé à fort potentiel) |
| McCann | — | à remplir |
| Autres boîtes | — | noms à donner |
| Formation Infinity | — | à remplir |
| Famille | [[Brigitte]], [[Michaela]] | commencé |
| À préciser | [[Jonas]] (beau-père de Yoav) | rattacher à un cercle |

## Associés potentiels
- **Experts métier :** [[Teddy]], [[Avigaël]], [[Eli]], [[Brigitte]], [[Michaela]], [[Jonas]], [[Itzik]]
- **Partenaires techniques :** [[Simon]], [[Yoav]]
