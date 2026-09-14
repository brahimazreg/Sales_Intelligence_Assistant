# Progress — Sales Intelligence Assistant

## Architecture actuelle

Le projet est organisé en 3 parties distinctes :

1. **Projet 1 — Text-to-SQL original**

   * Génération SQL avec Qwen 3 8B via Ollama
   * Validation avec SQLGlot
   * Exécution MySQL
   * Projet original conservé et fonctionnel

2. **Projet 2 — RAG**

   * Documents Markdown dans `rag_documents/`
   * Chunking par titres
   * Embeddings avec `nomic-embed-text`
   * ChromaDB persistant
   * Retrieval fonctionnel
   * Projet RAG conservé indépendamment

3. **Projet 3 — Intégration RAG + Text-to-SQL**

   * Code dans `app/integration/`
   * Le RAG récupère le contexte métier
   * Le contexte RAG est envoyé à Qwen avec la question et le schéma
   * Qwen génère le SQL
   * SQLGlot valide le SQL
   * MySQL exécute la requête

Le Router SQL/RAG/HYBRID et MCP sont prévus plus tard. Ils ne sont PAS encore implémentés.

---

## Structure importante

```text
app/
├── config.py
├── connection.py
├── schema.py
├── llm.py
├── generator.py              # Projet Text-to-SQL original — NE PAS MODIFIER
├── validator.py
├── executor.py
├── rag/
│   ├── documents.py
│   ├── embeddings.py
│   ├── vectorstore.py
│   └── retriever.py
└── integration/
    ├── generator_with_rag.py
    └── pipeline.py
```

Tests :

```text
tests/
├── test_schema.py
├── test_llm.py
├── test_generator.py
├── test_validator.py
├── test_documents.py
├── test_splitter.py
├── test_embeddings.py
├── test_vector_store.py
├── test_generator_with_rag.py
└── test_integration_pipeline.py
```

---

## Règle de développement

Développement incrémental obligatoire :

1. Implement
2. Test
3. Verify
4. Validate
5. Seulement ensuite passer à l'étape suivante

Ne pas modifier plusieurs composants simultanément.

Préserver les projets originaux.

---

# État actuel — Intégration RAG + Text-to-SQL

L'intégration fonctionne.

Pipeline actuel :

```text
Question
   ↓
RAG Retriever
   ↓
Contexte métier
   ↓
Qwen 3 8B
   ↓
SQL
   ↓
SQLGlot
   ↓
Validation tables/colonnes
   ↓
MySQL
   ↓
Résultat
```

Fichiers principaux :

* `app/integration/generator_with_rag.py`
* `app/integration/pipeline.py`
* `tests/test_integration_pipeline.py`

---

## Correction importante effectuée

Un problème a été découvert avec la génération de CTE.

Qwen pouvait générer une structure du type :

```sql
SELECT ...
FROM ...
...
),
product_margin AS (
...
)
SELECT ...
```

sans générer le `WITH` initial.

SQLGlot rejetait correctement cette requête.

### Correction

Le prompt de `app/integration/generator_with_rag.py` a été renforcé avec :

```text
- uniquement SELECT / WITH SELECT
- Si tu utilises des CTE (WITH), le mot-clé WITH doit obligatoirement
  être placé au tout début de la requête.
- La requête générée doit être une requête SQL complète et syntaxiquement
  valide en MySQL.
```

Ne pas modifier `validator.py` pour corriger ce problème : le problème venait de la génération Qwen.

---

# Tests d'intégration

Fichier :

```text
tests/test_integration_pipeline.py
```

Tests présents :

```text
test_chiffre_affaires_total
test_meilleur_produit
test_marge_totale
test_produits_a_reapprovisionner
test_chiffre_affaires_par_client
```

### Résultats connus

Les quatre premiers tests avaient déjà été validés.

Le test `test_meilleur_produit` avait initialement échoué à cause du problème de CTE décrit ci-dessus.

Après modification du prompt, le test ciblé a été relancé :

```powershell
uv run pytest tests/test_integration_pipeline.py::test_meilleur_produit -v
```

Résultat :

```text
tests/test_integration_pipeline.py::test_meilleur_produit PASSED

1 passed in 505.71s (0:08:25)
```

Donc le problème de CTE est maintenant corrigé et vérifié.

---

# Dernière étape effectuée

Le test ciblé `test_meilleur_produit` vient de passer.

La suite complète n'a PAS encore été relancée après cette correction.

## PROCHAINE ACTION EXACTE

À la prochaine session, NE PAS modifier le code immédiatement.

Commencer par lancer :

```powershell
uv run pytest tests/test_integration_pipeline.py -v
```

Objectif :

```text
5 tests passed
```

Si les 5 tests passent :

1. Verify
2. Validate l'intégration complète
3. Vérifier qu'aucun ancien composant n'a été modifié inutilement
4. Nettoyer le `print` de debug présent actuellement dans `app/integration/pipeline.py` :

```python
print("\n--- SQL GÉNÉRÉ ---")
print(sql_generated)
print("--- FIN SQL ---\n")
```

Puis relancer les tests concernés après ce nettoyage.

Ne pas commencer le Router, MCP ou une nouvelle fonctionnalité avant d'avoir terminé cette validation.

---

# Commande uv importante

Le projet utilise `uv`.

Utiliser :

```powershell
uv run pytest ...
```

et non :

```powershell
pytest ...
```

car `pytest` seul peut utiliser le Python global au lieu de `.venv`.

---

# État de la base de données

Les statuts actuels de `orders.status` sont :

```text
delivred
shipped
confirmed
pending
```

Il n'existe actuellement aucune commande avec le statut `canceled` ou `cancelled`.

La règle métier concernant l'exclusion des commandes annulées reste présente dans le prompt, mais elle ne peut pas être réellement testée avec les données actuelles.

Ne pas modifier les données ou le code uniquement pour cette raison.

---

# Business rules importantes

Le prompt doit conserver les règles métier du Text-to-SQL original :

### Revenue

```text
quantity * unit_price * (1 - discount_percent / 100)
```

### Cost

```text
quantity * products.cost_price
```

### Margin

```text
revenue - cost
```

Autres règles :

* uniquement SELECT ou WITH SELECT
* aucune écriture/modification de données
* ne pas inventer de tables ou colonnes
* utiliser les JOIN appropriés
* `order_date` pour les périodes temporelles
* `order_items.unit_price` = prix de vente
* `products.cost_price` = prix de revient
* TOP N → `ORDER BY` + `LIMIT`
* exclusion des commandes annulées sauf demande explicite
* si CTE utilisé : `WITH` doit être au début
* SQL complet et syntaxiquement valide MySQL

---

# Objectif immédiat

Finir et valider complètement :

```text
Projet 3 — Intégration RAG + Text-to-SQL
```

avant de commencer une nouvelle architecture.

Dernier point confirmé :

```text
test_meilleur_produit → PASSED
```

Prochaine commande :

```powershell
uv run pytest tests/test_integration_pipeline.py -v
```
Avec ça, si tu reviens plus tard et me dis simplement “on reprend le projet”, je pourrai repartir de cette étape : la correction CTE est validée, et il reste à lancer la suite complète des 5 tests avant le nettoyage/validation finale.