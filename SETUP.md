# BAME PRÉVENTION — nouveau site (statique)

Ce dossier contient le nouveau site, en remplacement du WordPress hébergé
chez IONOS. C'est un site 100 % statique (HTML/CSS/JS) : pas de base de
données, pas d'administration à maintenir, hébergement gratuit possible.

## Structure

- `index.html`, `a-propos.html`, … : les pages du site (générées, voir plus bas)
- `assets/css/style.css` : tout le design
- `assets/js/main.js` : menu mobile, bandeau cookies, envoi des formulaires
- `assets/images/` : logo, photo de Laure, logos partenaires
- `assets/documents/` : PDF (plaquettes, programmes, livrets, CGV) — rapatriés depuis l'ancien site
- `build.py` + `pages.py` : générateur du site. **Pour modifier un texte, éditez `pages.py` puis relancez `python3 build.py`** plutôt que d'éditer les `.html` directement (ils seront écrasés).

## À faire avant la mise en ligne

### 1. Choisir et brancher l'hébergeur (Vercel ou Netlify)

- Créer un compte sur [vercel.com](https://vercel.com) ou [netlify.com](https://netlify.com) (gratuit).
- Déployer ce dossier (glisser-déposer sur Netlify, ou `vercel` en CLI / import Git).
- Pointer le domaine `bameprevention.fr` vers le nouvel hébergeur (changement des serveurs DNS chez le registrar — à faire en dernier, une fois le site vérifié).

### 2. Connecter le formulaire de contact et la newsletter

Le site utilise [Formspree](https://formspree.io) (gratuit jusqu'à 50 emails/mois) :

1. Créer un compte Formspree avec l'email `lp@sofeca.com`.
2. Créer un formulaire "Contact" → copier son ID.
3. Créer un second formulaire "Newsletter" → copier son ID.
4. Dans `pages.py`, remplacer :
   - `CONTACT_FORM_ACTION = "https://formspree.io/f/VOTRE_ID_FORMSPREE"`
   - `NEWSLETTER_FORM_ACTION = "https://formspree.io/f/VOTRE_ID_FORMSPREE_NEWSLETTER"`
   par les vraies URLs fournies par Formspree.
5. Relancer `python3 build.py`.

Tant que ce n'est pas fait, les formulaires affichent un message clair au
lieu d'échouer silencieusement.

*(Alternative : Brevo, qui permet aussi de gérer une vraie liste de
diffusion pour la newsletter — plus de travail de mise en place, mais
mieux si l'audience grandit.)*

### 3. Mettre à jour les mentions légales

Dans `pages.py`, section `MENTIONS_LEGALES_BODY`, remplacer le paragraphe
"Hébergeur du site" par la raison sociale et l'adresse réelles de
l'hébergeur choisi (Vercel Inc. ou Netlify Inc.), puis relancer le build.

### 4. Vérifier

- Ouvrir chaque page, tester le formulaire de contact et la newsletter.
- Tester sur mobile (menu burger, lisibilité).
- Vérifier que tous les PDF s'ouvrent.

## Aperçu local

```bash
python3 -m http.server 8000
```

Puis ouvrir http://localhost:8000
