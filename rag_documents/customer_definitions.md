# Définitions clients

## Client

Un client représente une entreprise ou une organisation ayant effectué des commandes.

Les clients sont stockés dans la table :

customers

---

## Identification d'un client

L'identifiant du client est :

customers.customer_id

Le nom du client est :

customers.customer_name

---

## Chiffre d'affaires par client

Le chiffre d'affaires d'un client correspond au montant total de ses commandes.

Formule :

SUM(
    order_items.quantity
    * order_items.unit_price
    * (1 - order_items.discount_percent / 100)
)

Les commandes annulées sont exclues.
---

## Meilleur client

Le meilleur client est celui qui possède le chiffre d'affaires le plus élevé.

Pour déterminer les meilleurs clients :

1. Regrouper les ventes par client.
2. Calculer le chiffre d'affaires de chaque client.
3. Trier le chiffre d'affaires par ordre décroissant.

---

## Client le plus actif

Le client le plus actif peut être déterminé en fonction du nombre de commandes réalisées.

Le nombre de commandes correspond au nombre de commandes associées au client.

---

## Analyse client

Les clients peuvent être classés selon :

- chiffre d'affaires
- nombre de commandes
- quantité totale achetée
- produits achetés