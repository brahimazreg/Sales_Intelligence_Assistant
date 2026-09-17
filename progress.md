## Progress — 16/09/2026

### Tests fonctionnels réalisés

**SQL :**

* Commandes annulées → 1 commande, `order_id = 40` → ✅
* Total commandes → 39 affiché → ⚠️ cohérent avec les commandes `Delivered`, mais à surveiller car la base contient 40 commandes.
* Commandes > 1000 € → résultats obtenus → ✅ à confirmer plus tard
* Commandes par commercial → 20 / 10 / 6 / 3 = 39 → ⚠️ la commande 40 est `Cancelled`
* Commandes de décembre 2024 → commandes 36 à 40 → ✅
* Clients → colonnes correctes → ✅
* Clients Gold → 1, 5, 7 → ✅
* Clients Premium → 2, 3, 6 → ✅
* Clients par type → Gold 3 / Premium 3 / Standard 4 → ✅
* Montant total des commandes livrées → 85 270 € → ✅
* Montant moyen → 2 186,41 € → ⚠️ basé sur 39 commandes
* Commande 40 → montant `None`
* Commercial avec le plus de commandes → Sophie Martin, 20 → ⚠️ à confirmer avec les données
* Commandes annulées par commercial → commercial 4 : 1 → ✅
* Clients ayant une commande annulée → Retail Plus / Nathalie Simon → ✅ HYBRID

### RAG

* « Quelle est la politique de retour ? » → information non disponible → ⚠️
* « Que dit la documentation concernant les clients insatisfaits ? » → information non disponible → ⚠️
* Il faut tester le RAG avec une information dont on sait qu'elle existe réellement dans les documents.

### Vérification technique

La base MySQL utilisée par Docker est correcte :

* `DB_HOST = host.docker.internal`
* `DB_NAME = sales_rag`
* Total réel dans `orders` = **40**
* `Delivered` = **39**
* `Cancelled` = **1**
* Commande `40` = `sales_rep_id 4`, `Cancelled`
* `mysql.connector` fonctionne dans le container.

### État

**SQL :** globalement fonctionnel ✅
**HYBRID :** fonctionnel ✅
**RAG :** à approfondir ⚠️
**Base MySQL :** correcte ✅

### Reprendre demain

**NE PAS refaire le seed ni réinitialiser la base.**

Commencer par tester :

> Quels sont les clients qui n'ont jamais passé de commande ?

Puis poursuivre les tests fonctionnels SQL/RAG/HYBRID.

Le point à surveiller est la différence entre **40 commandes réelles** et certains résultats à **39**, sans modifier le code avant d'avoir identifié précisément la cause.
