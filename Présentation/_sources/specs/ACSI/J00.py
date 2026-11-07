import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from courses import ACSI

J = ACSI["jours"]
_cal1 = [[f"J{d:02d}", J[d][0], J[d][1]] for d in range(1, 9)]
_cal2 = [[f"J{d:02d}", J[d][0], J[d][1]] for d in range(9, 16)]
_mai = [[f"J{d:02d}", ", ".join(J[d][2]) or " · ", ", ".join(J[d][3]) or " · "] for d in range(1, 16)]

SPEC = [
    {"k": "title", "tag": "Vision globale du cours · 30 heures", "title": "Audit et contrôle interne\ndes systèmes d'information",
     "sub": "Méthode, normes et pratique de la mission d'audit : du métier à l'auditologie",
     "right": "UE MSN-2S3-MSI05 · 15 séances de 2 heures", "size": 38},
    {"k": "agenda", "title": "Sommaire", "kicker": "Ce document", "items": [
        ("", "**Pourquoi ce cours** : une grille qui déguise l'ignorance en certitude"),
        ("", "**Objectifs et compétences** : les métiers visés"),
        ("", "**Le plan** : un prologue, six parties, vingt-deux chapitres"),
        ("", "**L'organisation** : 30 heures en présentiel, travail personnel hors présentiel"),
        ("", "**Le calendrier** des quinze séances"),
        ("", "**Le fil rouge**, la méthode, les outils et l'évaluation"),
    ]},
    {"k": "quote", "kicker": "L'épigraphe du prologue", "text": "Une grille qui interdit de répondre « je ne sais pas » ne supprime pas l'ignorance : elle la déguise en certitude.",
     "author": "Prologue, « Quarante-cinq questions et aucune réponse fiable »", "size": 28},
    {"k": "compare", "title": "Pourquoi ce cours ?", "kicker": "Du métier à l'auditologie",
     "left": {"head": "Un métier sans socle scientifique", "items": ["L'audit des SI s'apprend par **compagnonnage**, se codifie dans des **référentiels**, se pratique par **jugement d'expert**", "Des grilles binaires OUI / NON **forcent l'ignorance** dans une case et produisent des conclusions **non opposables**"]},
     "right": {"head": "Une méthode fondée", "items": ["L'audit comme **réduction de l'incertitude** : la réponse **NEK**, trois mesures **μ, U, H**", "Une **décomposition** sous la borne cognitive, des **preuves** conservées, un **contradictoire** organisé", "Le tout ancré dans les **normes** (IIA, ISACA, ISO, INTOSAI) et le **droit camerounais et africain**"]}},
    {"k": "cards", "title": "Fondements, méthode, pratique", "kicker": "Trois ambitions", "cols": 3, "items": [
        {"head": "Les fondements", "badge": "1", "text": "Ce qu'est un **audit**, ce qu'il garantit et ne garantit pas ; le **contrôle interne** (COSO 2013), le **risque**, la **fraude**."},
        {"head": "La méthode", "badge": "2", "text": "Conduire une **mission** de bout en bout : préparer, **décomposer**, **collecter la preuve**, **conclure**, rapporter, suivre."},
        {"head": "La pratique", "badge": "3", "text": "Auditer la **gouvernance**, une **application**, un **projet**, la **sécurité**, la **continuité**, les **tiers**, puis l'**IA**."},
    ]},
    {"k": "table", "title": "Compétences visées par partie", "kicker": "Du niveau fondamental au niveau expert", "head": ["Partie", "Thème", "Compétences visées", "Niveau"], "widths": [1.6, 3.6, 4.8, 1.6], "rows": [
        ["Prologue", "Quarante-cinq questions", "Distinguer constatation, impression et opinion", "Base"],
        ["I", "Fondements de l'audit et du contrôle interne", "Situer l'audit, évaluer un contrôle, coter un risque, repérer la fraude", "Base"],
        ["II", "Méthode de la mission", "Planifier, décomposer, collecter la preuve, conclure avec μ, U et H", "Moyen"],
        ["III", "Cadre normatif, juridique et déontologique", "Choisir ses normes et ses critères ; connaître ses obligations", "Base"],
        ["IV", "Pratique de l'audit des SI", "Auditer gouvernance, application, projet, sécurité, continuité", "Moyen à expert"],
        ["V", "Défis avancés", "Audit continu, analyse de données, IA", "Expert"],
        ["VI", "Recherche : l'auditologie", "Lire et prolonger le programme de recherche", "Expert"],
    ]},
    {"k": "cards", "title": "Les métiers visés", "kicker": "Les fiches métier du cours", "cols": 3, "items": [
        {"head": "Auditeur SI", "badge": "1", "text": "Conduire la mission : mandat, décomposition, preuve, constat, rapport, suivi."},
        {"head": "Contrôleur interne", "badge": "2", "text": "Concevoir et évaluer les contrôles, séparer les tâches, prévenir la fraude, tenir le contrôle continu."},
        {"head": "Responsable GRC", "badge": "3", "text": "Cartographier les risques, tenir les registres, suivre les recommandations."},
        {"head": "Commissaire aux comptes", "badge": "4", "text": "S'appuyer sur des contrôles applicatifs fiables et sur les travaux de l'auditeur SI."},
        {"head": "RSSI", "badge": "5", "text": "Préparer les audits de sécurité, encadrer les tests techniques, répondre aux constats."},
    ]},
    {"k": "table", "title": "Le plan du cours", "kicker": "Un prologue, six parties, vingt-deux chapitres traités en présentiel", "head": ["Partie", "Thème", "Chapitres", "Séances"], "widths": [1.6, 6, 1.8, 1.8], "rows": [
        ["Prologue", "Quarante-cinq questions et aucune réponse fiable", "P00", "J01"],
        ["Partie I", "Fondements de l'audit et du contrôle interne", "C01 – C04", "J02 – J04"],
        ["Partie II", "Méthode de la mission d'audit", "C05 – C09", "J04 – J07"],
        ["Partie III", "Cadre normatif, juridique et déontologique", "C10 – C12", "J08 – J10"],
        ["Partie IV", "Pratique de l'audit des systèmes d'information", "C13 – C18", "J10 – J13"],
        ["Partie V", "Défis avancés : audit continu, données, IA", "C19 – C20", "J14"],
        ["Partie VI", "Recherche : l'auditologie", "C21 – C22", "J15"],
    ], "note": "Les séances commencent et finissent parfois au milieu d'un chapitre, pour équilibrer la charge des quinze séances."},
    {"k": "stats", "title": "L'organisation des enseignements", "kicker": "30 heures en présentiel, du travail personnel hors présentiel", "items": [
        ("15 × 2 h", "séances en présentiel, une par jour de cours, jamais plus de deux heures"),
        ("30 h", "tout le traité, du prologue à la Partie VI, réparti harmonieusement"),
        ("23", "ateliers de questions-réponses, un par chapitre, sur NDAP SUKULU"),
        ("10", "labs pratiques de 60 minutes sur NDAP SUKULU, corrigés automatiquement"),
    ], "bottom": "Ateliers et labs sont du **travail personnel**, **hors des 30 heures**. Leur répartition entre les séances est **indicative** ; chaque séance se termine par la liste de ce qu'il faut faire avant la suivante."},
    {"k": "steps", "title": "Le déroulé type d'une séance de deux heures", "kicker": "Une trame commune aux quinze séances", "items": [
        ("Ouvrir", "**Rappel** de la séance précédente, **déroulé**, **objectifs**."),
        ("Questionner", "La **question directrice** du chapitre, posée par un épisode du **fil rouge**."),
        ("Enseigner", "Définitions, tableaux, **lectures μ-U-H**, **fiches métier**, **exigences de contrôle**."),
        ("Pratiquer", "Un **exercice en séance**, corrigé dans les notes de l'orateur."),
        ("Conclure", "**Synthèse**, **travail à la maison** et **prochaine séance**."),
    ]},
    {"k": "table", "title": "Le calendrier des séances (1/2)", "kicker": "Jours 1 à 8", "head": ["Jour", "Thème de la séance", "Contenu du traité"], "widths": [1.1, 6.6, 3.7], "rows": _cal1},
    {"k": "table", "title": "Le calendrier des séances (2/2)", "kicker": "Jours 9 à 15", "head": ["Jour", "Thème de la séance", "Contenu du traité"], "widths": [1.1, 6.6, 3.7], "rows": _cal2},
    {"k": "table", "title": "Le travail personnel, séance par séance (1/2)", "kicker": "Ateliers de questions-réponses et labs de NDAP SUKULU · répartition indicative", "head": ["Après", "Ateliers (fiches ACSI-FICHE-…)", "Labs (ACSI-LAB-…)"], "widths": [1.4, 5.4, 4.6], "rows": _mai[:8]},
    {"k": "table", "title": "Le travail personnel, séance par séance (2/2)", "kicker": "Hors des 30 heures de présentiel", "head": ["Après", "Ateliers (fiches ACSI-FICHE-…)", "Labs (ACSI-LAB-…)"], "widths": [1.4, 5.4, 4.6], "rows": _mai[8:]},
    {"k": "table", "title": "Les dix labs de NDAP SUKULU", "kicker": "60 minutes chacun, sur les pièces des trois organisations", "head": ["Lab", "Intitulé", "Chap.", "Cas"], "widths": [1.5, 6.6, 1.4, 1.9], "rows": [
        ["LAB-01", "Construire la cartographie des risques", "C03", "LIZBIZ"],
        ["LAB-02", "Analyser la matrice des droits", "C02", "LIZBIZ"],
        ["LAB-03", "Coter les documents sollicités, dimensionner les échantillons", "C06", "LIZBIZ"],
        ["LAB-04", "Contrôler une décomposition du domaine D", "C07", "LIZBIZ"],
        ["LAB-05", "Mesurer, situer et comparer les domaines", "C09", "LIZBIZ"],
        ["LAB-06", "Audit de conformité des paiements", "C12", "MEFOU"],
        ["LAB-07", "Tests substantifs sur les données", "C14", "LIZBIZ"],
        ["LAB-08", "Audit d'infrastructure des quatre centres", "C16", "LIZBIZ"],
        ["LAB-09", "Auditer la continuité du système central", "C17", "SANAGA"],
        ["LAB-10", "Synthèse des trois cas", "C18", "Les trois"],
    ]},
    {"k": "cards", "title": "Trois organisations fictives, un fil rouge", "kicker": "Des cas ancrés dans la réalité camerounaise", "cols": 3, "items": [
        {"head": "Opération LIZBIZ", "badge": "L", "text": "**LiZbiZ SA**, Douala : logistique, quatre centres de données, douze agences ; écart de stock de 186 M FCFA, réserve du commissaire aux comptes."},
        {"head": "Opération SANAGA", "badge": "S", "text": "La **BANQUE SANAGA**, après une panne de trois jours : contrôle interne bancaire (COBAC), changements, continuité, IA."},
        {"head": "Opération MEFOU", "badge": "M", "text": "L'**ANPP**, Yaoundé, auditée par la **Chambre des comptes** : audit public, paiements, projets."},
    ], "notes": "SANAGA et MEFOU viennent du cours MSN-2S3-MSI03 (IT Governance, COBIT et ITIL) : les mêmes organisations, vues depuis la position de l'auditeur."},
    {"k": "cards", "title": "Les outils de la méthode", "kicker": "Ce que vous retrouverez à chaque séance", "cols": 3, "items": [
        {"head": "Les cinq réflexes", "badge": "5", "text": "Mandat écrit, critère avant constat, preuve avant conclusion, droit au NEK, contradictoire avant le rapport."},
        {"head": "OUI / NON / NEK", "badge": "?", "text": "L'instrument trichotomique, et les trois mesures **μ, U, H** qui lisent un domaine."},
        {"head": "Le gabarit canonique", "badge": "8", "text": "Huit niveaux, du domaine à la trace ; une **fiche d'assertion** par contrôle."},
        {"head": "Le quadrant", "badge": "4", "text": "Conformité × incertitude : quatre régions, quatre types de recommandation."},
        {"head": "L'observation en sept éléments", "badge": "7", "text": "Norme, constatation, risques, contradictoire, analyse, conclusion, recommandations."},
        {"head": "Les outils O0 à O9", "badge": "O4", "text": "Du plan d'audit aux projets d'observation ; le **classeur O4** au centre."},
    ]},
    {"k": "points", "title": "L'évaluation", "kicker": "Hors des 30 heures de présentiel", "items": [
        "Les modalités d'évaluation suivent le **règlement des études** de l'ENSPY pour l'UE MSN-2S3-MSI05",
        "La **simulation d'examen** du chapitre C18 (séance J13) donne le **format type** : un cas, quatre questions, trois heures, calculatrice",
        "Ce qui est attendu : **calculs justes et commentés**, quadrant lu avec **U d'abord**, fiches **atomiques**, constats **séparés** des analyses, recommandations sur les **causes**",
        "Les ateliers et les labs, faits régulièrement, sont la meilleure **préparation**",
    ], "side": {"head": "Les ressources", "text": ["Le traité **ACSI** (PDF) et son livret de correction.", "**NDAP SUKULU**, code MSN-2S3-MSI05 : fiches d'auto-évaluation et labs.", "Le dossier **Normes** : IIA, ITAF, ISO, COSO, INTOSAI, textes de loi."], "tone": "green"}},
    {"k": "fin", "next": "Jour 1 · Ouverture du cours et Quarante-cinq questions", "label": "PREMIÈRE SÉANCE", "items": [
        "Douala, mardi 14 avril 2026 : un rapport que personne n'a voulu signer",
        "Impression, constatation, opinion ; la réponse NEK",
        "Les cinq réflexes de l'auditeur",
    ], "foot": "Bienvenue dans le cours · questions ?"},
]
