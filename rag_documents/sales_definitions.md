# Définitions commerciales

## Commande

Une commande représente une vente enregistrée dans le système.

Les commandes sont stockées dans la table `orders`.

---

## Ligne de commande

Une ligne de commande représente un produit vendu dans une commande.

Les lignes de commande sont stockées dans la table `order_items`.

---

## Quantité vendue

La quantité vendue correspond à la colonne :

order_items.quantity

Pour connaître la quantité totale vendue d'un produit :

SUM(order_items.quantity)

---

## Prix unitaire

Le prix unitaire appliqué lors de la vente est stocké dans :

order_items.unit_price

Le prix utilisé pour calculer le chiffre d'affaires doit être celui de la ligne de commande.

---

## Chiffre d'affaires

Le chiffre d'affaires d'une ligne de commande est calculé avec :

order_items.quantity * order_items.unit_price

Le chiffre d'affaires total est :

SUM(order_items.quantity * order_items.unit_price)

Les commandes annulées doivent être exclues.

---

## Statut d'une commande

Le statut d'une commande est stocké dans :

orders.status

Une commande dont le statut est `Cancelled` est considérée comme annulée.

Les commandes annulées ne doivent normalement pas être incluses dans les indicateurs commerciaux.

---

## Performance commerciale

Les performances commerciales peuvent être analysées par :

- client
- commercial
- produit
- catégorie
- période