#!/usr/bin/env python3
"""Générateur statique du site BAME PRÉVENTION.
Assemble chaque page HTML à partir d'un header/footer communs + d'un
bloc de contenu propre à la page. Relancer ce script après toute
modification dans PAGES pour régénérer les fichiers .html à la racine.
"""
import re
from datetime import date
from pathlib import Path

ROOT = Path(__file__).parent

# Domaine réellement en ligne actuellement. À remplacer par
# "https://www.bameprevention.fr" une fois le nom de domaine définitif
# connecté (sinon les aperçus de lien / og:image pointent dans le vide).
BASE_URL = "https://dev.bameprevention.workers.dev"

MOIS_FR = [
    "janvier", "février", "mars", "avril", "mai", "juin",
    "juillet", "août", "septembre", "octobre", "novembre", "décembre",
]
_today = date.today()
LAST_UPDATED = f"{_today.day} {MOIS_FR[_today.month - 1]} {_today.year}"

NAV_LINKS = [
    ("/index.html", "Accueil"),
]

FORMATIONS = [
    ("/sst.html", "SST Initial"),
    ("/mac-sst.html", "MAC SST"),
    ("/secours.html", "Gestes qui sauvent"),
    ("/gestes-et-postures.html", "Gestes &amp; Postures"),
]

SECONDARY_LINKS = [
    ("/duerp.html", "DUERP"),
    ("/a-propos.html", "À propos"),
    ("/philosophie.html", "Notre philosophie"),
]

FOOTER_FORMATIONS = FORMATIONS
FOOTER_ENTREPRISE = [
    ("/a-propos.html", "À propos de nous"),
    ("/philosophie.html", "Notre philosophie"),
    ("/duerp.html", "DUERP"),
    ("/contact.html", "Contact"),
]
FOOTER_LEGAL = [
    ("/mentions-legales.html", "Mentions légales"),
    ("/cgv-formation.html", "CGV Formation"),
    ("/cgv-duerp.html", "CGV DUERP"),
    ("/rgpd.html", "Politique de confidentialité (RGPD)"),
]


def nav_html(current):
    def cur(href):
        return ' aria-current="page"' if href == current else ""

    items = []
    for href, label in NAV_LINKS:
        items.append(f'<a href="{href}"{cur(href)}>{label}</a>')

    formation_active = any(href == current for href, _ in FORMATIONS)
    panel = "".join(f'<a href="{href}">{label}</a>' for href, label in FORMATIONS)
    items.append(
        f'<div class="nav-dropdown{" is-open" if formation_active else ""}">'
        f'<button type="button" aria-haspopup="true">Formations '
        f'<svg width="12" height="8" viewBox="0 0 12 8" fill="none" aria-hidden="true">'
        f'<path d="M1 1.5L6 6.5L11 1.5" stroke="currentColor" stroke-width="1.6" '
        f'stroke-linecap="round" stroke-linejoin="round"/></svg></button>'
        f'<div class="nav-dropdown-panel">{panel}</div></div>'
    )
    for href, label in SECONDARY_LINKS:
        items.append(f'<a href="{href}"{cur(href)}>{label}</a>')
    return "\n        ".join(items)


def footer_cols(href_list):
    return "\n          ".join(
        f'<li><a href="{href}">{label}</a></li>' for href, label in href_list
    )


def render_head(title, description, canonical):
    return f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{BASE_URL}{canonical}">
<link rel="icon" href="/assets/images/logo-bame.jpg">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:type" content="website">
<meta property="og:locale" content="fr_FR">
<meta property="og:url" content="{BASE_URL}{canonical}">
<meta property="og:image" content="{BASE_URL}/assets/images/logo-bame.jpg">
<meta name="twitter:card" content="summary">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{description}">
<meta name="twitter:image" content="{BASE_URL}/assets/images/logo-bame.jpg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:wght@500;600;700&family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/css/style.css">
</head>"""


def render_header(current):
    return f"""<a class="skip-link" href="#main">Aller au contenu</a>
<header class="site-header">
  <div class="container">
    <a class="brand" href="/index.html">
      <img class="brand-logo" src="/assets/images/logo-bame-cropped.jpg" alt="BAME PRÉVENTION">
    </a>
    <nav class="main-nav" aria-label="Navigation principale">
      {nav_html(current)}
    </nav>
    <div class="header-cta">
      <a class="btn btn-primary btn-sm" href="/contact.html"><span class="btn-label-full">Nous contacter</span><span class="btn-label-short">Contact</span></a>
      <button class="nav-toggle" aria-label="Ouvrir le menu" aria-expanded="false">
        <span></span>
      </button>
    </div>
    <div class="header-qualiopi">
      <img class="brand-qualiopi" src="/assets/images/logo-qualiopi.jpg" alt="Qualiopi — processus certifié">
    </div>
  </div>
</header>
<div class="nav-scrim"></div>"""


FOOTER = f"""<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div>
        <div class="footer-brand">
          <img src="/assets/images/logo-bame.jpg" alt="BAME PRÉVENTION">
          <span>BAME PRÉVENTION</span>
        </div>
        <p class="muted" style="color:#cfe0ea;font-size:.9rem;max-width:30ch;">Prévenir aujourd'hui pour mieux vivre demain. Formation et conseil en santé-sécurité au travail.</p>
        <ul class="stack-sm" style="margin-top:14px;">
          <li>2 bis Rue du Parc, 77540 Bernay-Vilbert</li>
          <li><a href="tel:+33667981471">06 67 98 14 71</a></li>
          <li><a href="mailto:lp@sofeca.com">lp@sofeca.com</a></li>
        </ul>
      </div>
      <div>
        <h4>Formations</h4>
        <ul>
          {footer_cols(FOOTER_FORMATIONS)}
        </ul>
      </div>
      <div>
        <h4>Entreprise</h4>
        <ul>
          {footer_cols(FOOTER_ENTREPRISE)}
        </ul>
      </div>
      <div>
        <h4>Informations légales</h4>
        <ul>
          {footer_cols(FOOTER_LEGAL)}
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>&copy; <span data-current-year>2026</span> BAME PRÉVENTION — Laure PIPET · SIRET 91990879800011 · NDA 11770808577</span>
      <span>Organisme de formation déclaré — formatrice SST certifiée INRS</span>
      <span>Dernière mise à jour du site : {LAST_UPDATED}</span>
    </div>
  </div>
</footer>
<div class="cookie-banner" role="dialog" aria-label="Gestion des cookies">
  <p>Ce site utilise uniquement des cookies techniques nécessaires à son fonctionnement (préférences d'affichage). Aucun cookie publicitaire ou de mesure d'audience tiers n'est déposé sans votre accord. Voir notre <a href="/rgpd.html">politique de confidentialité</a>.</p>
  <div class="actions">
    <button class="btn btn-primary btn-sm" data-cookie-choice="accepted">J'ai compris</button>
    <a class="btn btn-outline btn-sm" href="/rgpd.html">En savoir plus</a>
  </div>
</div>
<script src="/assets/js/main.js"></script>
</body>
</html>"""


WATERMARK_IMG = '<img class="hero-watermark" src="/assets/images/watermark-seal.png" alt="" aria-hidden="true">'
HERO_BG = ""


def inject_watermark(body):
    body = body.replace(
        '<section class="hero">', f'<section class="hero">\n{HERO_BG}', 1
    )
    body = re.sub(
        r'(<section class="page-hero[^"]*">)',
        lambda m: f"{m.group(1)}\n{WATERMARK_IMG}",
        body,
    )
    return body


def page(slug, title, description, body):
    canonical = "/" if slug == "index" else f"/{slug}.html"
    body = inject_watermark(body)
    html = (
        render_head(title, description, canonical)
        + "\n<body>\n"
        + render_header(f"/{slug}.html")
        + "\n<main id=\"main\">\n"
        + body
        + "\n</main>\n"
        + FOOTER
    )
    out = ROOT / f"{slug}.html"
    out.write_text(html, encoding="utf-8")
    print("wrote", out.name)


# ---------------------------------------------------------------
# Les blocs de contenu de chaque page sont importés depuis pages.py
# ---------------------------------------------------------------
from pages import PAGES  # noqa: E402

for slug, (title, description, body) in PAGES.items():
    page(slug, title, description, body)

print(f"\n{len(PAGES)} pages générées.")
