def get_data():
    return [
        # 0: remboursement
        ("Je veux un remboursement", 0),
        ("Je souhaite annuler ma commande et récupérer mon argent s'il vous plaît.", 0),
        ("Je veux me faire rembourser s'il vous plaît", 0),
        ("Remboursez-moi s'il vous plaît", 0),
        ("Demande de remboursement pour ma commande", 0),
        ("Je demande un remboursement pour ce produit défectueux", 0),
        ("Je veux être remboursé pour cet article", 0),

        # 1: problème technique
        ("Produit cassé", 1),
        ("Je n'arrive pas à me connecter", 1),
        ("Je veux signaler un bug", 1),
        ("L'application plante quand je clique sur le bouton de connexion", 1),
        ("Je n'arrive plus à me connecter à mon compte et le site affiche une erreur.", 1),
        ("Le site ne fonctionne pas et affiche une page blanche", 1),
        ("Un bug m'empêche de finaliser mon paiement", 1),
        ("mauvais service", 1),
        ("le service client ne répond pas", 1),
        ("très déçu du service client", 1),
        ("mauvaise expérience avec le produit", 1),

        # 2: positif
        ("Merci beaucoup", 2),
        ("Très satisfait du service", 2),
        ("bon travail", 2),
        ("Service client impeccable, je suis extrêmement satisfait de mon achat !", 2),
        ("Super service, merci beaucoup !", 2),
        ("Excellente expérience client, bravo", 2),
        ("Je suis très content de mon achat et de l'aide reçue", 2),

        # 3: livraison
        ("Problème de livraison", 3),
        ("Commande jamais arrivée", 3),
        ("Mon colis n'est toujours pas livré et le suivi n'affiche rien", 3),
        ("Retard de livraison pour ma commande", 3),
        ("Où est mon colis ?", 3),
        ("Je n'ai pas reçu mon colis après deux semaines", 3),

        # 4: achat / prise de commande
        ("Je veux faire une commande en ligne sur le produit", 4),
        ("Comment passer commande sur votre site ?", 4),
        ("Je voudrais acheter ce produit", 4),
        ("Comment je fais pour commander ?", 4),
        ("Je souhaite passer une commande", 4),
        ("Quels sont vos moyens de paiement ?", 4),
        ("Comment acheter en ligne ?", 4),
        ("Je veux commander un article sur votre site", 4),

        # 5: autre
        ("Bonjour", 5),
        ("Avez-vous des promotions en ce moment ?", 5),
        ("Quels sont vos horaires d'ouverture ?", 5),
        ("Pouvez-vous me donner plus d'informations sur vos produits ?", 5),
        ("Est-ce que vous livrez en Algérie ?", 5),
        ("Je voulais juste poser une question", 5),
        ("Avez-vous un magasin physique ?", 5),
    ]