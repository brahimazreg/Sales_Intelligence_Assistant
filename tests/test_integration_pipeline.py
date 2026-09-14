from app.integration.pipeline import question_to_sql_with_rag


def test_chiffre_affaires_total():
    question = "Quel est le chiffre d'affaires total ?"

    result = question_to_sql_with_rag(question)

    assert result is not None
    assert len(result) > 0


def test_meilleur_produit():
    question = "Quel est le meilleur produit ?"

    result = question_to_sql_with_rag(question)

    assert result is not None
    assert len(result) > 0


def test_marge_totale():
    question = "Quelle est la marge totale ?"

    result = question_to_sql_with_rag(question)

    assert result is not None
    assert len(result) > 0


def test_produits_a_reapprovisionner():
    question = "Quels sont les produits à réapprovisionner ?"

    result = question_to_sql_with_rag(question)

    assert result is not None
    assert len(result) > 0


def test_chiffre_affaires_par_client():
    question = "Quel est le chiffre d'affaires par client ?"

    result = question_to_sql_with_rag(question)

    assert result is not None
    assert len(result) > 0