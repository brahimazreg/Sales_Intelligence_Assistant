# Règles métier

## Chiffre d'affaires

Le chiffre d'affaires d'une ligne de commande est calculé comme suit :

quantity * unit_price * (1 - discount_percent / 100)

Le chiffre d'affaires total est :

SUM(
    quantity * unit_price * (1 - discount_percent / 100)
)

Les commandes annulées sont exclues.

---

## Meilleur client

Le meilleur client est le client ayant généré le chiffre d'affaires le plus élevé.

Le chiffre d'affaires d'un client correspond à la somme des montants de ses commandes.

Les commandes annulées sont exclues.

---

## Meilleur commercial

Le meilleur commercial est le commercial ayant généré le chiffre d'affaires le plus élevé pour les commandes qui lui sont attribuées.

Les commandes annulées sont exclues.

---

## Produit le plus vendu

Un produit est considéré comme le plus vendu lorsqu'il possède la quantité totale vendue la plus élevée.

La quantité vendue correspond à :

SUM(order_items.quantity)

Les commandes annulées sont exclues.

---

## Produit générant le plus de chiffre d'affaires

Un produit génère du chiffre d'affaires selon :

SUM(order_items.quantity * order_items.unit_price)

Les commandes annulées sont exclues.

---

## Réapprovisionnement

Un produit doit être réapprovisionné lorsque la quantité actuellement disponible en stock est inférieure au niveau de réapprovisionnement.

Condition :

stock_quantity < reorder_level