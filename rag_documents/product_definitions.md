# Définitions produits

## Produit

Un produit représente un article vendu par l'entreprise.

Les produits sont stockés dans la table :

products

---

## Identification d'un produit

L'identifiant du produit est :

products.product_id

Le nom du produit est :

products.product_name

---

## Prix du produit

Le prix actuel du produit est stocké dans :

products.unit_price

Cependant, pour calculer le chiffre d'affaires historique d'une vente, le prix de la ligne de commande doit être utilisé :

order_items.unit_price

---

## Stock

La quantité actuellement disponible est stockée dans :

products.stock_quantity

---

## Niveau de réapprovisionnement

Le niveau de réapprovisionnement est stocké dans :

products.reorder_level

---

## Produit à réapprovisionner

Un produit doit être réapprovisionné lorsque :

products.stock_quantity < products.reorder_level

---

## Produit le plus vendu

Le produit le plus vendu est celui dont la quantité totale vendue est la plus importante.

La quantité vendue est calculée avec :

SUM(order_items.quantity)

Les commandes annulées sont exclues.

---

## Produit générant le plus de chiffre d'affaires

Le chiffre d'affaires généré par un produit est calculé avec :

SUM(
    order_items.quantity
    * order_items.unit_price
    * (1 - order_items.discount_percent / 100)
)

---

## Catégorie de produit

Chaque produit peut être associé à une catégorie.

Les catégories sont stockées dans la table :

categories

Les produits sont associés à leur catégorie via la relation entre les tables `products` et `categories`.