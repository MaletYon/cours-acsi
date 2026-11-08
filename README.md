# Audit et Contrôle Interne des SI (ACSI)

[← Tous les cours de MaletYon](https://github.com/maletyon) · [Livre (PDF)](ACSI_main.pdf) · [Présentations](Présentation/) · [Fiches par chapitre](fiches/) · [Corrigés](correction/README.md)

**UE MSN-2S3-MSI05** · Master Professionnel en Management des Systèmes d'Information · Semestre 3
Chaire UNESCO d'Afrique Centrale ACCES-TIC, sous la tutelle académique de l'École Nationale Supérieure Polytechnique de l'Université de Yaoundé I
Auteur : MINKA MI NGUIDJOÏ Thierry Emmanuel, enseignant-chercheur (LIMSI, ENSPY) · contact : maletyon@proton.me · année académique 2026-2027

> *Méthode, normes et pratique de la mission d'audit : du métier à l'auditologie.*

Un rapport d'audit que personne n'a voulu signer : c'est le point de départ du cours. On y apprend à conduire une mission d'audit des systèmes d'information dont chaque conclusion peut être défendue devant un tiers. La méthode est celle de l'**auditologie**, science appliquée de la réduction de l'incertitude. Elle repose sur un instrument de réponse à trois modalités (OUI / NON / NEK, « connaissance insuffisante ») et sur trois mesures, μ, U et H. Trois cas forment le fil rouge : LiZbiZ (logistique, Douala), la BANQUE SANAGA et l'ANPP (paiements publics). Le cours s'appuie sur les normes de l'IIA, de l'ISACA, de l'ISO et de l'INTOSAI, et sur le droit camerounais et OHADA.

## Ce que contient ce dépôt

| Élément | Où | Description |
|---|---|---|
| Le livre du cours | [`ACSI_main.pdf`](ACSI_main.pdf) | Traité complet (prologue, 22 chapitres, annexes), compilé depuis [`ACSI_main.tex`](ACSI_main.tex) |
| Les présentations | [`Présentation/`](Présentation/) | 16 présentations PowerPoint : vision d'ensemble et 15 séances de 2 heures, avec notes du présentateur |
| Les fiches d'exercices | [`fiches/`](fiches/) | 23 fiches de 40 questions au format texte, à distribuer en attendant l'ouverture de NDAP SUKULU |
| Le livret de correction | [`correction/`](correction/) | Accès réservé : voir la page du dossier |
| Les sources LaTeX | `front/`, `partie0/` à `partie6/`, `annexes/`, `bibliographie/`, `figures/`, [`Style_ACSI.sty`](Style_ACSI.sty) | Sources du livre |

## Organisation du cours (30 heures, 15 séances de 2 heures)

| Partie | Chapitres | Fichiers |
|---|---|---|
| **Prologue** | 0. Quarante-cinq questions | [`partie0/`](partie0/) |
| **I. Fondements** | 1. Auditer, contrôler, donner une assurance · 2. Le contrôle interne et ses composantes · 3. Le risque, de la définition à la cartographie · 4. La fraude dans et par les SI | [`partie1/`](partie1/) |
| **II. Méthode de la mission** | 5. Principes et cycle · 6. Préparer et planifier · 7. Décomposer l'espace d'audit · 8. Collecter la preuve · 9. Conclure | [`partie2/`](partie2/) |
| **III. Cadre normatif et juridique** | 10. Les normes professionnelles · 11. Les référentiels de contrôle · 12. Le cadre juridique camerounais et africain | [`partie3/`](partie3/) |
| **IV. Pratique de l'audit des SI** | 13. Gouvernance et fonction informatique · 14. Application en service · 15. Projets · 16. Sécurité et infrastructure · 17. Production, continuité et tiers · 18. Études de cas intégratrices | [`partie4/`](partie4/) |
| **V. Défis avancés** | 19. Audit continu, analyse de données et outils · 20. Auditer l'IA, auditer avec elle | [`partie5/`](partie5/) |
| **VI. Recherche : l'auditologie** | 21. Objet, axiomes et piliers · 22. Mesurer l'incertitude, la stratégie et la trajectoire | [`partie6/`](partie6/) |
| **Annexes** | A. Glossaire · B. Outils · C. Modèles et grilles · D. Textes · E. Bibliographie commentée · F. Contacts | [`annexes/`](annexes/) |

## NDAP SUKULU, la salle de classe compagnon

*Ndap sukulu* signifie « la salle de classe » en bassa, et *Malet Yon* « ton enseignant ». NDAP SUKULU est l'environnement d'évaluation du cours : une fiche de 20 questions tirées d'une banque de 100 par chapitre, et dix laboratoires pratiques, minutés et en nombre de tentatives limité. Le code de cours est **MSN-2S3-MSI05**. La présentation complète figure au début du livre.

| Utilisation | Où |
|---|---|
| En ligne | `https://maletyon.github.io/cours-acsi/ndap-sukulu/` |
| Sur un ordinateur, sans Internet | archive téléchargeable dans [`ndap-sukulu/`](ndap-sukulu/) |
| Sur un téléphone (fiches seulement) | `https://maletyon.github.io/cours-acsi/ndap-sukulu/telephone/` |
| Si votre réseau bloque `github.io` | adresse de secours `https://raw.githack.com/MaletYon/cours-acsi/main/ndap-sukulu/`, ou [archive à télécharger](https://github.com/MaletYon/cours-acsi/raw/main/ndap-sukulu/NDAP_SUKULU_ACSI_ordinateur.zip) pour travailler hors ligne |

La connexion se fait avec le matricule et le mot de passe remis par l'enseignant. Les copies sont remises à l'enseignant sous forme d'un fichier chiffré ; il les corrige et publie les résultats, que chacun consulte dans l'application. Le mode d'emploi complet, pour l'étudiant et pour l'enseignant, est dans [`ndap-sukulu/README.md`](ndap-sukulu/README.md). Les fiches de 40 questions au format texte restent disponibles dans [`fiches/`](fiches/).

| Lab | Sujet | Chapitre |
|---|---|---|
| ACSI-LAB-01 | Construire la cartographie des risques de LiZbiZ | 3 |
| ACSI-LAB-02 | Analyser la matrice des droits de LiZbiZ | 2 |
| ACSI-LAB-03 | Coter les documents sollicités et dimensionner les échantillons | 6 |
| ACSI-LAB-04 | Contrôler une décomposition du domaine D | 7 |
| ACSI-LAB-05 | Mesurer, situer et comparer les domaines de LiZbiZ | 9 |
| ACSI-LAB-06 | Audit de conformité des paiements de l'ANPP | 12 |
| ACSI-LAB-07 | Tests substantifs sur les données de LiZbiZ | 14 |
| ACSI-LAB-08 | Audit d'infrastructure des quatre centres de LiZbiZ | 16 |
| ACSI-LAB-09 | Auditer la continuité du système central de la BANQUE SANAGA | 17 |
| ACSI-LAB-10 | Synthèse des trois cas | 18 |

## Sources de recherche

Le cours s'appuie sur deux prépublications de l'auteur, déposées sur HAL : *Vers l'auditologie* (`hal-05701007`) et *Modelling Epistemic Uncertainty in IS Audit* (`hal-05701270`). Les autres travaux cités comme « en préparation » ne sont pas encore publiés.

## Compiler le livre

Avec une distribution LaTeX : `pdflatex ACSI_main`, `biber ACSI_main`, `makeindex ACSI_main`, puis deux fois `pdflatex ACSI_main`.
Les présentations se régénèrent avec `python Présentation/_sources/run.py ACSI all` (Python 3 et python-pptx).

## Normes et documents sous licence

Les normes ISO, le référentiel COBIT et les autres documents sous licence cités dans le cours **ne sont pas fournis** dans ce dépôt.

## Licence

Contenu pédagogique : [CC BY-NC-SA 4.0](LICENSE.md). Code du générateur de présentations : MIT. Voir [`LICENSE.md`](LICENSE.md).
