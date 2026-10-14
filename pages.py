# -*- coding: utf-8 -*-
"""Contenu de chaque page du site BAME PRÉVENTION.
Chaque entrée : slug -> (title, meta description, corps HTML).
"""

CONTACT_FORM_ACTION = "https://api.web3forms.com/submit"
WEB3FORMS_ACCESS_KEY = "0a1a4e74-3785-4056-9215-46690542ffb8"
NEWSLETTER_FORM_ACTION = "https://30d9b1be.sibforms.com/serve/MUIFAE7Bq2oiuqqEOznmQJ79DS0t1mcC2Rt_OOJfnLlq_fJReuIK0seKYTNrhKEnmaF-Hs2oY-IMTG-54NkeWGZMMGunjLmNlzFB5k6iQuBvmH6LR8KQwfyDnaVwGax4TcBpmiu2XKnnCRSy-8agnG-t-JvnqaMx6ASrMshQfzb3MrYc2XHpkDtIvHDBhHyEWSQTjroZJyAOePaRJQ=="

ICONS = {
    "shield": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M12 3l7 3v6c0 4.5-3 7.8-7 9-4-1.2-7-4.5-7-9V6l7-3z"/><path d="M9 12l2 2 4-4"/></svg>',
    "heart": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/></svg>',
    "users": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="9" cy="8" r="3.2"/><path d="M2.5 20c.6-3.6 3.3-6 6.5-6s5.9 2.4 6.5 6"/><circle cx="17.5" cy="8.5" r="2.6"/><path d="M15.5 14.3c2.5.2 4.6 2.3 5 5.7"/></svg>',
    "chevron-down": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" width="16" height="16"><path d="M6 9l6 6 6-6"/></svg>',
    "check": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 12.5l5 5L20 7"/></svg>',
    "award": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="12" cy="8" r="5.2"/><path d="M8.5 12.7L7 21l5-2.4L17 21l-1.5-8.3"/></svg>',
    "clock": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3.5 2"/></svg>',
    "phone": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M4 4.5c0 9.1 6.4 15.5 15.5 15.5l.8-3.6-4.4-1.6-1.6 1.6a12 12 0 01-6.2-6.2l1.6-1.6L8.1 3.7 4.5 4.5z"/></svg>',
    "mail": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3.5 6.5L12 13l8.5-6.5"/></svg>',
    "pin": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M12 21s7-6.5 7-12a7 7 0 10-14 0c0 5.5 7 12 7 12z"/><circle cx="12" cy="9" r="2.3"/></svg>',
    "book": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M4 4.5h7A2 2 0 0113 6.5V20a2 2 0 00-2-1.5H4V4.5z"/><path d="M20 4.5h-7a2 2 0 00-2 2V20a2 2 0 012-1.5h7V4.5z"/></svg>',
    "target": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="12" cy="12" r="8.5"/><circle cx="12" cy="12" r="4.5"/><circle cx="12" cy="12" r=".8" fill="currentColor"/></svg>',
    "scale": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M12 3v18M6 7l-3.5 7a3.5 3.5 0 007 0L6 7zm12 0l-3.5 7a3.5 3.5 0 007 0L18 7zM4 7h16M9 21h6"/></svg>',
}


def doc_links(items):
    out = []
    for href, label in items:
        out.append(
            f'<a class="doc-button" href="{href}" target="_blank" rel="noopener">{ICONS["book"]}{label}</a>'
        )
    return "\n          ".join(out)


# =================================================================
# ACCUEIL
# =================================================================
INDEX_BODY = f"""
<section class="hero">
  <div class="container">
    <div>
      <span class="eyebrow" style="background:rgba(255,255,255,.12);color:#fff;">Organisme de formation certifié INRS</span>
      <h1>Anticipez les risques avec BAME PRÉVENTION</h1>
      <p class="lede">Chez BAME PRÉVENTION, la prévention est au cœur de chaque action. Un accompagnement sur mesure pour anticiper les risques, préserver le bien-être et agir de manière responsable — avant que les situations ne deviennent critiques.</p>
      <div class="hero-actions">
        <a class="btn btn-primary" href="/contact.html">Construire mon projet de prévention</a>
        <a class="btn btn-ghost" href="#formations">Voir les formations</a>
      </div>
      <div class="hero-badges">
        <span class="hero-badge"><span class="badge-ico">{ICONS['award']}</span>SST certifiée INRS</span>
        <span class="hero-badge"><span class="badge-ico">{ICONS['clock']}</span>Disponibilité 2 à 4 semaines</span>
        <span class="hero-badge"><span class="badge-ico">{ICONS['users']}</span>Référente handicap</span>
      </div>
    </div>
    <div class="hero-card">
      <img src="/assets/images/laure-pipet.jpg" alt="Laure Pipet, formatrice BAME PRÉVENTION">
      <div class="role">Votre formatrice</div>
      <h3>Laure PIPET</h3>
      <p class="quote">« 98 % de satisfaction sur ma qualité pédagogique depuis que j'ai commencé en 2022, essentiellement en sous-traitance. »</p>
    </div>
  </div>
</section>

<section class="section" id="formations">
  <div class="container">
    <div class="center" style="max-width:640px;">
      <span class="eyebrow">Nos formations</span>
      <h2>Des formations sur mesure, ancrées dans vos risques réels</h2>
      <p class="lede center">Délai d'accès aux formations : 2 à 4 semaines. Accessibilité sur demande pour la réalisation d'un plan d'action.</p>
    </div>
    <div class="carousel">
      <div class="carousel-track">
        <div class="training-card">
          <div class="training-card__top"><h3 style="color:#fff;margin:0;">SST Initial</h3><div class="duration" style="margin-top:4px;">14h — 2 jours</div></div>
          <div class="training-card__body">
            <p>Sauveteur Secouriste du Travail. Protéger, examiner, faire alerter ou alerter, secourir — une formation complète pour réagir efficacement face à un accident.</p>
            <a class="btn btn-outline btn-sm" href="/sst.html">Découvrir la formation</a>
          </div>
        </div>
        <div class="training-card">
          <div class="training-card__top"><h3 style="color:#fff;margin:0;">MAC SST</h3><div class="duration" style="margin-top:4px;">7h</div></div>
          <div class="training-card__body">
            <p>Maintien et actualisation des compétences SST. Démontrez que rien n'a été oublié de votre formation initiale.</p>
            <a class="btn btn-outline btn-sm" href="/mac-sst.html">Découvrir la formation</a>
          </div>
        </div>
        <div class="training-card">
          <div class="training-card__top"><h3 style="color:#fff;margin:0;">Gestes qui sauvent</h3><div class="duration" style="margin-top:4px;">3h30 à 7h</div></div>
          <div class="training-card__body">
            <p>Les bonnes pratiques de secours, en initiation ou en sensibilisation — essentielles au quotidien, pour tous.</p>
            <a class="btn btn-outline btn-sm" href="/secours.html">Découvrir la formation</a>
          </div>
        </div>
        <div class="training-card">
          <div class="training-card__top"><h3 style="color:#fff;margin:0;">Gestes &amp; Postures</h3><div class="duration" style="margin-top:4px;">7h</div></div>
          <div class="training-card__body">
            <p>Prévention des TMS. Les bons gestes pour se protéger des maladies professionnelles, dans tous les secteurs d'activité.</p>
            <a class="btn btn-outline btn-sm" href="/gestes-et-postures.html">Découvrir la formation</a>
          </div>
        </div>
        <div class="training-card">
          <div class="training-card__top"><h3 style="color:#fff;margin:0;">DUERP</h3><div class="duration" style="margin-top:4px;">Conseil</div></div>
          <div class="training-card__body">
            <p>Document Unique d'Évaluation des Risques Professionnels. Un accompagnement pour évaluer et consigner les risques de votre entreprise.</p>
            <a class="btn btn-outline btn-sm" href="/duerp.html">Découvrir la prestation</a>
          </div>
        </div>
        <div class="training-card" style="background:linear-gradient(135deg,var(--orange),var(--orange-dark));">
          <div class="training-card__body" style="justify-content:center;color:#fff;">
            <h3 style="color:#fff;">Un besoin spécifique ?</h3>
            <p style="color:rgba(255,255,255,.9);">Chaque entreprise a ses propres risques. Parlons de votre contexte pour construire la formation la plus adaptée.</p>
            <a class="btn" style="background:#fff;color:var(--orange-dark);" href="/contact.html">Échanger avec Laure</a>
          </div>
        </div>
      </div>
      <div class="carousel-nav">
        <button class="carousel-btn prev" type="button" aria-label="Formation précédente">{ICONS['chevron-down']}</button>
        <button class="carousel-btn next" type="button" aria-label="Formation suivante">{ICONS['chevron-down']}</button>
      </div>
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="container">
    <div class="center" style="max-width:680px;margin-bottom:40px;">
      <span class="eyebrow">Sur mesure</span>
      <h2>Des ateliers personnalisés, construits avec vous</h2>
      <p class="lede center">Au-delà des formations certifiantes, Laure conçoit des ateliers de sensibilisation ciblés selon les besoins réels de votre équipe — un format court, concret, adapté à votre secteur.</p>
    </div>
    <div class="carousel" style="margin-top:0;">
      <div class="carousel-track">
        <div class="card">
          <div class="icon">{ICONS['heart']}</div>
          <h3>Malaise &amp; nutrition</h3>
          <p class="muted">Déjà animé en entreprise : reconnaître les signes d'un malaise, les bons réflexes, et les bases d'une alimentation qui soutient l'énergie au travail.</p>
        </div>
        <div class="card">
          <div class="icon">{ICONS['shield']}</div>
          <h3>Utilisation du défibrillateur</h3>
          <p class="muted">Un atelier pratique pour démystifier le DAE et gagner en confiance face à un arrêt cardiaque, en complément de la formation gestes qui sauvent.</p>
        </div>
        <div class="card">
          <div class="icon">{ICONS['target']}</div>
          <h3>Ergonomie &amp; télétravail</h3>
          <p class="muted">Dans le prolongement de la formation Gestes &amp; Postures : adapter son poste à la maison ou au bureau pour prévenir les TMS au quotidien.</p>
        </div>
        <div class="card">
          <div class="icon">{ICONS['clock']}</div>
          <h3>Échauffement &amp; réveil musculaire</h3>
          <p class="muted">Quelques minutes avant la prise de poste pour préparer le corps à l'effort physique — particulièrement utile en logistique et manutention.</p>
        </div>
        <div class="card">
          <div class="icon">{ICONS['users']}</div>
          <h3>Qualité de vie au travail</h3>
          <p class="muted">Charge mentale, sommeil, gestion du stress : des clés concrètes pour une équipe plus sereine, en complément d'une démarche de prévention globale.</p>
          <p class="muted" style="font-size:.8rem;font-style:italic;margin-top:8px;">Laure se forme à cet atelier en décembre 2026 — disponible pour vos équipes dès cette date.</p>
        </div>
      </div>
      <div class="carousel-nav">
        <button class="carousel-btn prev" type="button" aria-label="Atelier précédent">{ICONS['chevron-down']}</button>
        <button class="carousel-btn next" type="button" aria-label="Atelier suivant">{ICONS['chevron-down']}</button>
      </div>
    </div>
    <div class="text-center" style="margin-top:36px;">
      <p class="muted" style="font-size:.9rem;">Cette liste n'est pas exhaustive — chaque atelier est construit sur mesure selon vos enjeux.</p>
      <a class="btn btn-primary" href="/contact.html">Proposer un atelier à mon équipe</a>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="grid grid-2" style="align-items:center;gap:56px;">
      <div>
        <span class="eyebrow">Notre engagement</span>
        <h2>Ensemble pour l'avenir</h2>
        <p class="lede">La prévention des risques passe avant tout par la formation, pour protéger les équipes tout en améliorant la performance et le climat de travail.</p>
        <a class="btn btn-outline" href="/philosophie.html">Notre philosophie</a>
      </div>
      <details class="reveal-more" style="margin-top:0;">
        <summary>En savoir plus sur notre engagement <span class="chevron">{ICONS['chevron-down']}</span></summary>
        <div class="grid" style="gap:18px;">
          <p class="lede" style="margin-bottom:4px;">En donnant aux salariés les clés pour identifier et gérer les dangers, les entreprises renforcent la sécurité au quotidien. Intégrer ces enjeux dans la formation continue, c'est protéger les équipes tout en améliorant la performance et le climat de travail.</p>
          <span class="hero-badge" style="color:var(--navy);border-color:var(--line);background:var(--success-bg);justify-self:start;"><span class="badge-ico">{ICONS['award']}</span>Habilitation P123</span>
          <div class="card" style="display:flex;gap:16px;align-items:flex-start;padding:22px;">
            <div class="icon" style="margin:0;">{ICONS['target']}</div>
            <div><h3 style="margin-bottom:4px;">Conseil personnalisé</h3><p class="muted mb-0">Un accompagnement sur mesure selon vos besoins spécifiques.</p></div>
          </div>
          <div class="card" style="display:flex;gap:16px;align-items:flex-start;padding:22px;">
            <div class="icon" style="margin:0;">{ICONS['users']}</div>
            <div><h3 style="margin-bottom:4px;">Formation professionnelle</h3><p class="muted mb-0">Des formations adaptées pour sensibiliser et former vos équipes.</p></div>
          </div>
          <div class="card" style="display:flex;gap:16px;align-items:flex-start;padding:22px;">
            <div class="icon" style="margin:0;">{ICONS['shield']}</div>
            <div><h3 style="margin-bottom:4px;">Outils innovants</h3><p class="muted mb-0">Des solutions modernes pour une prévention efficace et durable.</p></div>
          </div>
        </div>
      </details>
    </div>
  </div>
</section>

<section class="section section--navy">
  <div class="container">
    <div class="center" style="max-width:640px;margin-bottom:36px;">
      <span class="eyebrow" style="background:rgba(255,255,255,.15);color:#fff;">Chiffres clés</span>
      <h2>Merci aux organismes de leur confiance</h2>
    </div>
    <div class="stats">
      <div class="stat">
        <div class="stat-number">260</div>
        <div class="stat-label">formations en prévention réalisées en sous-traitance depuis 2022</div>
      </div>
      <div class="stat">
        <div class="stat-number">1&nbsp;673</div>
        <div class="stat-label">salariés formés avec succès, toutes formations confondues</div>
      </div>
      <div class="stat">
        <div class="stat-number">98&nbsp;%</div>
        <div class="stat-label">de satisfaction sur la qualité pédagogique</div>
      </div>
      <div class="stat">
        <div class="stat-number">88</div>
        <div class="stat-label">salariés formés en une journée lors d'un atelier malaise &amp; nutrition</div>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="center" style="max-width:640px;margin-bottom:32px;">
      <span class="eyebrow">Ils nous font confiance</span>
      <h2>Des entreprises déjà accompagnées</h2>
      <p class="lede center">Des sociétés avec lesquelles BAME PRÉVENTION a déjà travaillé.</p>
    </div>
    <div class="partners">
      <a href="https://www.sofeca.com/" target="_blank" rel="noopener"><img src="/assets/images/partner-sofeca.png" alt="Sofeca" loading="lazy"></a>
      <img src="/assets/images/partner-haras-bouttemont.png" alt="Haras de Bouttemont" loading="lazy">
      <img src="/assets/images/partner-hp-elec.png" alt="HP Elec — Groupe Synelis" loading="lazy">
      <img src="/assets/images/partner-sethi-communication.png" alt="Sethi Communication" loading="lazy">
      <a href="https://www.lesjardinsdejo34.fr/" target="_blank" rel="noopener"><img src="/assets/images/partner-jardins-de-jo.jpg" alt="Les Jardins de Jo" loading="lazy"></a>
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="container">
    <div class="center" style="max-width:640px;margin-bottom:32px;">
      <span class="eyebrow">Nos certifications</span>
      <h2>Des références reconnues par la profession</h2>
    </div>
    <div class="partners" style="gap:48px;">
      <img src="/assets/images/logo-sst.png" alt="Sauveteur Secouriste du Travail" style="max-height:64px;filter:none;" loading="lazy">
      <img src="/assets/images/logo-qualiopi.jpg" alt="Qualiopi — processus certifié" style="width:calc(var(--logo-bame-size) * .85);height:auto;max-height:none;max-width:55vw;filter:none;" loading="lazy">
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="center" style="max-width:640px;margin-bottom:40px;">
      <span class="eyebrow">Nos partenaires</span>
      <h2>Nos entreprises partenaires</h2>
      <p class="lede center">Des fournisseurs et réseaux recommandés, pour une prévention toujours plus complète.</p>
    </div>
    <details class="reveal-more">
      <summary>En savoir plus sur nos partenaires équipement <span class="chevron">{ICONS['chevron-down']}</span></summary>
      <div class="grid grid-2" style="max-width:760px;margin:0 auto;">
        <div class="card text-center" style="padding:0;overflow:hidden;">
          <img src="/assets/images/product-lifeaz.jpg" alt="Défibrillateur Lifeaz" style="width:100%;">
          <div style="padding:22px;">
            <img src="/assets/images/qr-commander-lifeaz.png" alt="Lifeaz — QR code pour commander votre défibrillateur, code promo FPLPIPET" style="max-width:200px;margin:0 auto;">
          </div>
        </div>
        <div class="card text-center" style="padding:0;overflow:hidden;">
          <img src="/assets/images/badge-cardio-first-angel.png" alt="Dispositif Cardio First Angel" style="width:100%;background:#fff;">
          <div style="padding:22px;">
            <img src="/assets/images/qr-devis.png" alt="Cardio First Angel — QR code pour recevoir votre devis" style="max-width:200px;margin:0 auto;">
          </div>
        </div>
      </div>
    </details>
  </div>
</section>

<section class="section section--navy">
  <div class="container">
    <div class="newsletter">
      <div>
        <span class="eyebrow" style="background:rgba(255,255,255,.15);color:#fff;">Newsletter BAME PRÉVENTION</span>
        <h2>Restez informés, restez prêts</h2>
        <p>Chaque mois, recevez nos conseils prévention, nos actualités formations (SST, gestes et postures, secours) et les rappels réglementaires à connaître.</p>
        <p style="font-size:.85rem;opacity:.85;">Conforme RGPD · Désinscription en un clic</p>
      </div>
      <form method="POST" action="{NEWSLETTER_FORM_ACTION}" data-nocors-form>
        <div class="field mb-0">
          <label for="newsletter-email">Adresse email *</label>
          <input id="newsletter-email" name="EMAIL" type="email" required placeholder="vous@entreprise.fr">
        </div>
        <input type="text" name="email_address_check" value="" style="display:none !important" tabindex="-1" autocomplete="off">
        <input type="hidden" name="locale" value="fr">
        <label class="field-check">
          <input type="checkbox" required name="OPT_IN" value="1">
          <span>J'accepte de recevoir les emails de BAME PRÉVENTION et confirme avoir pris connaissance de la <a href="/rgpd.html" style="color:#fff;text-decoration:underline;">politique de confidentialité</a>.</span>
        </label>
        <button class="btn btn-primary" type="submit">S'inscrire</button>
        <p class="form-status"></p>
      </form>
    </div>
  </div>
</section>

"""

# =================================================================
# A PROPOS
# =================================================================
A_PROPOS_BODY = f"""
<section class="page-hero">
  <div class="container">
    <div class="breadcrumb"><a href="/index.html">Accueil</a> / À propos</div>
    <span class="eyebrow" style="background:rgba(255,255,255,.12);color:#fff;">Qui est BAME PRÉVENTION ?</span>
    <h1>L'engagement d'une professionnelle indépendante au service de votre sécurité</h1>
    <p class="lede">Fondée par Laure PIPET, issue du milieu paramédical et formatrice SST/PRAP certifiée INRS, BAME PRÉVENTION accompagne les entreprises dans une démarche globale de prévention.</p>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="grid grid-2" style="align-items:center;gap:56px;">
      <img src="/assets/images/laure-pipet.jpg" alt="Laure Pipet" style="border-radius:var(--radius-lg);box-shadow:var(--shadow-md);">
      <div>
        <h2>Du Document Unique à la formation des équipes</h2>
        <p class="lede">BAME PRÉVENTION accompagne les entreprises dans une démarche globale de prévention : du Document Unique à la formation des équipes.</p>
        <div class="quote-block" style="margin-top:24px;">
          Notre conviction : la prévention ne se résume pas à des obligations réglementaires. C'est une démarche humaine, concrète et durable qui protège les salariés au quotidien.
        </div>
        <p style="margin-top:24px;font-family:var(--font-head);font-size:1.2rem;color:var(--navy-dark);">Une formatrice. Un engagement.<br>Vos équipes formées aux gestes qui sauvent.</p>
        <a class="btn btn-primary" style="margin-top:10px;" href="/contact.html">Prendre contact</a>
      </div>
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="container">
    <div class="grid grid-3">
      <div class="card">
        <div class="icon">{ICONS['award']}</div>
        <h3>Formatrice certifiée INRS</h3>
        <p class="muted">Certification SST et PRAP reconnue, pour des formations conformes aux exigences réglementaires et pédagogiques.</p>
      </div>
      <div class="card">
        <div class="icon">{ICONS['heart']}</div>
        <h3>Issue du milieu paramédical</h3>
        <p class="muted">Une approche humaine et concrète de la prévention, nourrie par une expérience de terrain auprès des personnes.</p>
      </div>
      <div class="card">
        <div class="icon">{ICONS['shield']}</div>
        <h3>Référente handicap</h3>
        <p class="muted">Un accompagnement adapté à chaque stagiaire, en lien avec l'Agefiph pour les besoins spécifiques.</p>
      </div>
    </div>
  </div>
</section>
"""

# =================================================================
# PHILOSOPHIE
# =================================================================
PHILOSOPHIE_BODY = f"""
<section class="page-hero">
  <div class="container">
    <div class="breadcrumb"><a href="/index.html">Accueil</a> / Notre philosophie</div>
    <h1>Notre philosophie</h1>
    <p class="lede">Trois piliers guident chaque mission BAME PRÉVENTION : la qualité, l'efficacité, et des prix équitables.</p>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="grid grid-2" style="gap:24px;">
      <div class="card">
        <div class="icon">{ICONS['award']}</div>
        <h3>Qualité</h3>
        <p class="muted">Une démarche qualité au service de votre sécurité. Organisme de formation déclaré (NDA n° 11770808577), formatrice Sauveteur Secouriste du Travail habilitée par le réseau Assurance Maladie / INRS (habilitation n° ALC27016), démarche inspirée du référentiel Qualiopi : la rigueur au service de votre confiance.</p>
      </div>
      <div class="card">
        <div class="icon">{ICONS['users']}</div>
        <h3>Accessibilité</h3>
        <p class="muted">Référente handicap dédiée, en lien avec l'Agefiph pour adapter chaque formation aux besoins spécifiques.</p>
      </div>
      <div class="card" style="grid-column:1/-1;padding:0;overflow:hidden;">
        <img src="/assets/images/accessibilite-agefiph.png" alt="Politique d'accessibilité et d'accompagnement des personnes en situation de handicap — en lien avec l'Agefiph" style="width:100%;">
      </div>
      <div class="card">
        <div class="icon">{ICONS['shield']}</div>
        <h3>Efficacité</h3>
        <p class="muted">Une démarche globale de prévention. De l'évaluation des risques (DUERP) à la formation de vos équipes (SST, GQS, Gestes &amp; Postures), BAME PRÉVENTION vous accompagne dans la durée pour bâtir une vraie culture sécurité.</p>
      </div>
      <div class="card">
        <div class="icon">{ICONS['scale']}</div>
        <h3>Des prix équitables</h3>
        <p class="muted">Un juste prix, pour une prestation de qualité. Tarifs transparents, devis personnalisé selon vos besoins. Pas de surfacturation : juste le prix d'un accompagnement rigoureux par une professionnelle indépendante.</p>
      </div>
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="container">
    <div class="center" style="max-width:640px;margin-bottom:32px;">
      <span class="eyebrow">Nos engagements</span>
      <h2>Ce que BAME PRÉVENTION vous garantit</h2>
    </div>
    <ul class="check-list grid grid-2" style="max-width:860px;margin:0 auto;">
      <li>Analyse personnalisée du besoin</li>
      <li>Petits groupes pour un suivi de qualité</li>
      <li>Mémo pédagogique remis à chaque stagiaire</li>
      <li>Dispositif de rattrapage si nécessaire</li>
      <li>Évaluation systématique par les stagiaires</li>
      <li>Confidentialité RGPD garantie</li>
    </ul>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="center" style="max-width:640px;margin-bottom:32px;">
      <span class="eyebrow">Engagement accessibilité</span>
      <h2>Ressource Handicap Formation</h2>
      <p class="lede center">Laure PIPET est engagée dans la démarche d'accessibilité de ses formations, en lien avec l'Agefiph et son réseau de partenaires.</p>
    </div>
    <img src="/assets/images/ressource-handicap-formation.jpg" alt="Ressource Handicap Formation — Laure Pipet est engagée dans la démarche d'accessibilité de ses formations" style="max-width:520px;margin:0 auto;border-radius:var(--radius-lg);box-shadow:var(--shadow-md);">
  </div>
</section>
"""


def formation_page(
    slug,
    title,
    eyebrow,
    headline,
    law_text,
    outcome_text,
    docs,
    extra_html="",
):
    doc_block = doc_links(docs)
    return f"""
<section class="page-hero">
  <div class="container">
    <div class="breadcrumb"><a href="/index.html">Accueil</a> / <a href="/index.html#formations">Formations</a> / {title}</div>
    <span class="eyebrow" style="background:rgba(255,255,255,.12);color:#fff;">{eyebrow}</span>
    <h1>{headline}</h1>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="grid grid-2" style="gap:40px;align-items:flex-start;">
      <div>
        <h2>Cadre réglementaire</h2>
        <p class="lede">{law_text}</p>
        <div class="quote-block" style="margin-top:24px;">{outcome_text}</div>
        {extra_html}
      </div>
      <div class="card sticky-card">
        <h3>Documentation à télécharger</h3>
        <p class="muted">Plaquette de présentation, programme détaillé et livret d'accueil stagiaire.</p>
        <div class="doc-button-list">
          {doc_block}
        </div>
        <div class="divider" style="margin:24px 0;"></div>
        <p class="muted" style="font-size:.78rem;"><strong>Financement :</strong> formation facturée à l'entreprise, qui règle puis peut demander le remboursement à son OPCO (la subrogation n'est plus la règle). BAME PRÉVENTION ne propose pas de financement CPF.</p>
        <div class="divider" style="margin:24px 0;"></div>
        <p class="muted" style="font-size:.88rem;">Une question sur cette formation ?</p>
        <a class="btn btn-primary" style="width:100%;justify-content:center;" href="/contact.html">Demander un devis</a>
      </div>
    </div>
  </div>
</section>
"""


SST_BODY = formation_page(
    "sst",
    "SST — Sauveteur Secouriste du Travail",
    "Formation obligatoire — 14h sur 2 jours",
    "SST — Sauveteur Secouriste du Travail",
    "L'article R.4224-15 du Code du travail stipule que la présence d'un salarié formé est obligatoire dans chaque atelier où sont réalisés des travaux dangereux. Dans les chantiers de BTP occupant au moins 20 salariés pendant plus de 15 jours, un salarié formé doit également être présent s'il y a des travaux dangereux. Cette obligation s'applique en l'absence d'infirmier sur le lieu de travail.",
    "Grâce à cette formation, vous serez capable de <strong>PROTÉGER, EXAMINER, FAIRE ALERTER OU ALERTER, ET SECOURIR</strong> de manière efficace et structurée.",
    [
        ("/assets/documents/Plaquette_SST_Initial.pdf", "PLAQUETTE DE PRESENTATION"),
        ("/assets/documents/Programme_SST_Initial.pdf", "PROGRAMME"),
        ("/assets/documents/Livret_Accueil_Stagiaire.pdf", "LIVRET D'ACCUEIL STAGIAIRE"),
    ],
)

MAC_SST_BODY = formation_page(
    "mac-sst",
    "MAC SST — Maintien et actualisation des compétences",
    "Recyclage obligatoire — 7h",
    "SST MAC — Maintien des compétences acquises",
    "L'article R.4224-15 du Code du travail stipule que la présence d'un salarié formé est obligatoire dans chaque atelier où sont réalisés des travaux dangereux. Dans les chantiers de BTP occupant au moins 20 salariés pendant plus de 15 jours, un salarié formé doit également être présent s'il y a des travaux dangereux. Cette obligation s'applique en l'absence d'infirmier sur le lieu de travail.",
    "Grâce à cette actualisation, vous serez capable de <strong>démontrer que vous n'avez rien oublié de votre formation initiale</strong>.",
    [
        ("/assets/documents/Plaquette_MAC_SST.pdf", "PLAQUETTE DE PRESENTATION"),
        ("/assets/documents/Programme_MAC_SST.pdf", "PROGRAMME"),
        ("/assets/documents/Livret_Accueil_Stagiaire.pdf", "LIVRET D'ACCUEIL STAGIAIRE"),
    ],
)

SECOURS_BODY = f"""
<section class="page-hero">
  <div class="container">
    <div class="breadcrumb"><a href="/index.html">Accueil</a> / <a href="/index.html#formations">Formations</a> / Les gestes qui sauvent</div>
    <span class="eyebrow" style="background:rgba(255,255,255,.12);color:#fff;">Citoyen sauveteur — de 3h30 à 7h</span>
    <h1>Les gestes qui sauvent — les bonnes pratiques</h1>
  </div>
</section>

<section class="section">
  <div class="container">
    <h2>Cadre réglementaire</h2>
    <p class="lede">L'article L.721-1 du code de la sécurité intérieure a été modifié pour introduire le statut de citoyen sauveteur, défini comme toute personne portant assistance de manière bénévole à une personne en situation apparente de péril grave et imminent. Ce statut permet aux citoyens de bénéficier de la qualité de collaborateur occasionnel du service public et d'être exonérés de toute responsabilité civile lorsqu'il résulte un préjudice du fait de leur intervention, sauf en cas de faute lourde ou intentionnelle.</p>
    <div class="quote-block" style="margin-top:24px;">Mettre en œuvre les bonnes pratiques de secours, c'est essentiel au quotidien.</div>

    <div class="grid grid-2" style="gap:32px;margin-top:40px;align-items:start;">
      <div class="card">
        <span class="eyebrow">Sensibilisation — 3h30</span>
        <h3>Les bonnes pratiques pour secourir une victime</h3>
        <p class="muted">Les numéros d'urgence, les 3 étapes vitales et les bonnes pratiques au travail.</p>
        <div class="doc-button-list">
          {doc_links([
              ("/assets/documents/Plaquette_Secourir_3h30.pdf", "PLAQUETTE DE PRESENTATION"),
              ("/assets/documents/Programme_Secourir_Sensibilisation.pdf", "PROGRAMME"),
              ("/assets/documents/Livret_Accueil_Stagiaire.pdf", "LIVRET D'ACCUEIL STAGIAIRE"),
          ])}
        </div>
      </div>
      <div class="card">
        <span class="eyebrow">Initiation — 7h</span>
        <h3>Initiation aux gestes qui sauvent</h3>
        <p class="muted">Arrêt cardiaque, défibrillateur, PLS, étouffement, hémorragie — l'essentiel pour agir.</p>
        <div class="doc-button-list">
          {doc_links([
              ("/assets/documents/Plaquette_Secourir_7h.pdf", "PLAQUETTE DE PRESENTATION"),
              ("/assets/documents/Programme_Secourir_Initiation_7h.pdf", "PROGRAMME"),
              ("/assets/documents/Livret_Accueil_Stagiaire.pdf", "LIVRET D'ACCUEIL STAGIAIRE"),
          ])}
        </div>
      </div>
    </div>

    <div class="card" style="margin-top:32px;display:flex;gap:16px;align-items:center;">
      <div class="icon" style="margin:0;">{ICONS['award']}</div>
      <div><h3 style="margin-bottom:4px;">100 % de satisfaction</h3><p class="muted mb-0">Une formation réalisée à ce jour par mon organisme en direct en 2025.</p></div>
    </div>

    <p class="muted text-center" style="font-size:.78rem;max-width:600px;margin:24px auto 0;"><strong>Financement :</strong> formation facturée à l'entreprise, qui règle puis peut demander le remboursement à son OPCO (la subrogation n'est plus la règle). BAME PRÉVENTION ne propose pas de financement CPF.</p>

    <div class="text-center" style="margin-top:20px;">
      <a class="btn btn-primary" href="/contact.html">Demander un devis</a>
    </div>
  </div>
</section>
""" + f"""
<section class="section section--alt">
  <div class="container">
    <div class="card" style="max-width:780px;margin:0 auto 32px;text-align:center;">
      <div style="font-size:2rem;margin-bottom:8px;">🚨</div>
      <h2 style="margin-bottom:4px;">Aide-mémoires Secourisme</h2>
      <p style="color:var(--orange-dark);font-weight:600;font-style:italic;margin-bottom:14px;">Vos aide-mémoires de poche — Formations de secours</p>
      <p class="muted mb-0">Téléchargez gratuitement les aide-mémoires de vos formations de secourisme : Les bonnes pratiques pour secourir une victime (Sensibilisation 3h30 / Initiation 7h) et MAC SST. Format A5 à plier — pratique à glisser dans votre portefeuille.</p>
    </div>
    <div class="grid grid-2" style="max-width:780px;margin:0 auto;">
      <div class="card text-center" style="border-top:4px solid var(--navy);">
        <div style="font-size:1.6rem;margin-bottom:10px;">🚨</div>
        <h3 style="margin-bottom:2px;">Les bonnes pratiques pour secourir une victime</h3>
        <p style="font-style:italic;color:var(--ink-soft);font-size:.9rem;margin-bottom:10px;">Sensibilisation — 3h30</p>
        <p class="muted" style="font-size:.9rem;">Les numéros d'urgence, les 3 étapes vitales et les bonnes pratiques au travail.</p>
        <a class="pill-link" href="/assets/documents/Memo_Secourir_Sensibilisation.pdf" target="_blank" rel="noopener">{ICONS['book']}Télécharger</a>
      </div>
      <div class="card text-center" style="border-top:4px solid var(--orange-dark);">
        <div style="font-size:1.6rem;margin-bottom:10px;">❤️</div>
        <h3 style="margin-bottom:2px;">Les bonnes pratiques pour secourir une victime</h3>
        <p style="font-style:italic;color:var(--ink-soft);font-size:.9rem;margin-bottom:10px;">Initiation — 7h</p>
        <p class="muted" style="font-size:.9rem;">Arrêt cardiaque, défibrillateur, PLS, étouffement, hémorragie — l'essentiel pour agir.</p>
        <a class="pill-link" href="/assets/documents/Memo_Secourir_Initiation.pdf" target="_blank" rel="noopener">{ICONS['book']}Télécharger</a>
      </div>
    </div>
    <div class="card text-center" style="max-width:360px;margin:24px auto 0;border-top:4px solid var(--orange-dark);">
      <div style="font-size:1.6rem;margin-bottom:10px;">🔄</div>
      <h3 style="margin-bottom:2px;">MAC SST</h3>
      <p style="font-style:italic;color:var(--ink-soft);font-size:.9rem;margin-bottom:10px;">Dispositif INRS — 7h</p>
      <p class="muted" style="font-size:.9rem;">Rappel des compétences SST, méthode P-E-F-A-S, rôle d'acteur de prévention.</p>
      <a class="pill-link" href="/assets/documents/Memo_MAC_SST.pdf" target="_blank" rel="noopener">{ICONS['book']}Télécharger</a>
    </div>
    <div class="card" style="max-width:780px;margin:32px auto 0;">
      <h3 style="margin-bottom:14px;">💡 Comment utiliser ces aide-mémoires ?</h3>
      <ul class="check-list">
        <li><strong>Imprimer :</strong> en A4 paysage, recto seul</li>
        <li><strong>Plier :</strong> en deux verticalement pour obtenir un format A5</li>
        <li><strong>Garder à portée de main :</strong> dans votre portefeuille, dans une trousse de secours</li>
        <li><strong>Partager :</strong> avec vos collègues, votre famille</li>
      </ul>
      <p class="muted" style="font-size:.82rem;font-style:italic;margin-top:14px;">Ces aide-mémoires sont à utiliser en complément de la formation et ne remplacent pas un apprentissage pratique. En cas d'urgence, appelez toujours le 15, 18 ou 112.</p>
    </div>
  </div>
</section>
"""

GESTES_POSTURES_BODY = f"""
<section class="page-hero">
  <div class="container">
    <div class="breadcrumb"><a href="/index.html">Accueil</a> / <a href="/index.html#formations">Formations</a> / Gestes et Postures</div>
    <span class="eyebrow" style="background:rgba(255,255,255,.12);color:#fff;">Prévention des TMS — 7h</span>
    <h1>Gestes et Postures</h1>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="grid grid-2" style="gap:40px;align-items:flex-start;">
      <div>
        <h2>Cadre réglementaire</h2>
        <p class="lede">Les articles R.4541-8 et R.231-71 du Code du travail imposent à l'employeur de former les salariés aux gestes et postures adaptés à leur poste de travail. Cette formation est requise à l'embauche, au changement de poste, au retour d'arrêt long ou sur recommandation médicale. Elle concerne tous les secteurs, y compris manutention, tertiaire, santé, logistique, et plus encore.</p>
        <div class="quote-block" style="margin-top:24px;">Réaliser les bons gestes pour se protéger des maladies professionnelles.</div>
      </div>
      <div class="card sticky-card">
        <h3>Documentation à télécharger</h3>
        <p class="muted">Plaquette de présentation, programme détaillé et livret d'accueil stagiaire.</p>
        <div class="doc-button-list">
          {doc_links([
              ("/assets/documents/Plaquette_Gestes_Postures.pdf", "PLAQUETTE DE PRESENTATION"),
              ("/assets/documents/Programme_Gestes_Postures.pdf", "PROGRAMME"),
              ("/assets/documents/Livret_Accueil_Stagiaire.pdf", "LIVRET D'ACCUEIL STAGIAIRE"),
          ])}
        </div>
        <div class="divider" style="margin:24px 0;"></div>
        <p class="muted" style="font-size:.78rem;"><strong>Financement :</strong> formation facturée à l'entreprise, qui règle puis peut demander le remboursement à son OPCO (la subrogation n'est plus la règle). BAME PRÉVENTION ne propose pas de financement CPF.</p>
        <div class="divider" style="margin:24px 0;"></div>
        <a class="btn btn-primary" style="width:100%;justify-content:center;" href="/contact.html">Demander un devis</a>
      </div>
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="container">
    <div class="grid grid-2" style="gap:40px;align-items:center;">
      <div>
        <span class="eyebrow">Aide-mémoire Gestes et Postures</span>
        <h2>Votre aide-mémoire de poche — Prévention des TMS</h2>
        <p class="muted">Téléchargez gratuitement l'aide-mémoire de la formation Gestes et Postures : les 5 risques TMS, les 3 règles d'or, postures, manutention et échauffement. Format A5 à plier — pratique à glisser dans votre portefeuille pour garder les bons réflexes à portée de main.</p>
        <a class="btn btn-primary" href="/assets/documents/Aide_Memoire_Gestes_Postures.pdf" target="_blank" rel="noopener">Télécharger l'aide-mémoire</a>
      </div>
      <div class="card">
        <h3>Comment utiliser ces aide-mémoires ?</h3>
        <ul class="check-list" style="margin-top:14px;">
          <li>Imprimer en A4 paysage, recto seul</li>
          <li>Plier en deux verticalement pour obtenir un format A5</li>
          <li>Garder à portée de main — dans votre portefeuille, dans une trousse de secours</li>
          <li>Partager avec vos collègues, votre famille</li>
        </ul>
        <p class="muted" style="font-size:.82rem;margin-top:16px;">Ces aide-mémoires sont à utiliser en complément de la formation et ne remplacent pas un apprentissage pratique. En cas d'urgence, appelez toujours le 15, 18 ou 112.</p>
      </div>
    </div>
  </div>
</section>
"""

DUERP_BODY = f"""
<section class="page-hero">
  <div class="container">
    <div class="breadcrumb"><a href="/index.html">Accueil</a> / DUERP</div>
    <span class="eyebrow" style="background:rgba(255,255,255,.12);color:#fff;">Conseil &amp; accompagnement</span>
    <h1>Document Unique d'Évaluation des Risques Professionnels</h1>
    <p class="lede">Le DUERP est régi par les articles L.4121-3 et R.4121-1 du Code du travail, imposant à l'employeur d'évaluer et de consigner les risques professionnels.</p>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="grid grid-2" style="gap:40px;align-items:center;">
      <div>
        <h2>Un accompagnement méthodologique complet</h2>
        <p class="muted">BAME PRÉVENTION vous accompagne dans l'élaboration et la mise à jour de votre Document Unique : identification des unités de travail, évaluation et cotation des risques (y compris psychosociaux), et construction du plan d'actions de prévention annuel.</p>
        <p class="muted">Pour en savoir plus sur le cadre légal du DUERP, consultez la page officielle du ministère du Travail : <a href="https://travail-emploi.gouv.fr/le-document-unique-devaluation-des-risques-professionnels-duerp" target="_blank" rel="noopener" style="color:var(--teal-dark);font-weight:600;">travail-emploi.gouv.fr</a>.</p>
        <a class="btn btn-primary" href="/contact.html">Demander un accompagnement DUERP</a>
        <a class="btn btn-outline" style="margin-left:10px;" href="/cgv-duerp.html">Voir les CGV DUERP</a>
      </div>
      <div class="card">
        <div class="icon">{ICONS['scale']}</div>
        <h3>Cadre réglementaire</h3>
        <ul class="check-list" style="margin-top:14px;">
          <li>Art. L.4121-1 à L.4121-3 — obligation générale de prévention</li>
          <li>Art. R.4121-1 et R.4121-2 — obligation d'établir et de mettre à jour le DUERP</li>
          <li>Loi du 2 août 2021 — conservation du DUERP pendant au moins 40 ans et dépôt dématérialisé</li>
        </ul>
      </div>
    </div>
  </div>
</section>
"""

# =================================================================
# CONTACT
# =================================================================
CONTACT_BODY = f"""
<section class="page-hero">
  <div class="container">
    <div class="breadcrumb"><a href="/index.html">Accueil</a> / Contact</div>
    <h1>Construire votre projet de prévention — simple, rapide, sur mesure</h1>
    <p class="lede">De la demande à l'évaluation terrain, BAME PRÉVENTION vous accompagne à chaque étape.</p>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="grid grid-2" style="gap:48px;align-items:flex-start;">
      <div>
        <div class="timeline-group">
          <h4>Avant la formation</h4>
          <div class="timeline">
            <div class="timeline-step"><div class="dot">1</div><p class="mb-0">Téléchargez le programme de la formation souhaitée.</p></div>
            <div class="timeline-step"><div class="dot">2</div><p class="mb-0">Complétez le formulaire de contact ci-contre.</p></div>
            <div class="timeline-step"><div class="dot">3</div><p class="mb-0">Rendez-vous pour l'analyse de vos besoins spécifiques — si une prise en charge particulière d'un salarié est nécessaire, un rendez-vous complémentaire sera organisé.</p></div>
            <div class="timeline-step"><div class="dot">4</div><p class="mb-0">Convention transmise sous 48h pour signature — à retourner au plus tard 10 jours avant la formation.</p></div>
            <div class="timeline-step"><div class="dot">5</div><p class="mb-0">Bulletins d'inscription et attentes des salariés à retourner 48h avant la formation.</p></div>
            <div class="timeline-step"><div class="dot">6</div><p class="mb-0">Conception de votre formation sur mesure, adaptée à vos risques réels.</p></div>
          </div>
        </div>
        <div class="divider"></div>
        <div class="timeline-group">
          <h4>Pendant la formation</h4>
          <p class="muted">Formation réalisée sur votre site — feuille d'émargement, questionnaire de satisfaction, attestation de participation et certificat de réussite remis à chaque stagiaire.</p>
        </div>
        <div class="divider"></div>
        <div class="timeline-group">
          <h4>Après la formation</h4>
          <p class="muted">Rapport de formation avec bilan et recommandations personnalisées. Suivi à 6 mois : nous revenons vers vous avec un questionnaire pour faire le point sur la mise en place de la prévention au sein de votre établissement.</p>
        </div>

        <div class="divider"></div>
        <h2>Contactez-nous</h2>
        <div class="contact-info">
          <div class="row"><div class="icon">{ICONS['phone']}</div><div><strong>Téléphone</strong><br><a href="tel:+33667981471">+33 6 67 98 14 71</a></div></div>
          <div class="row"><div class="icon">{ICONS['mail']}</div><div><strong>Email</strong><br><a href="mailto:lp@sofeca.com">lp@sofeca.com</a></div></div>
          <div class="row"><div class="icon">{ICONS['pin']}</div><div><strong>Adresse</strong><br>2 bis rue du Parc, 77540 Bernay-Vilbert</div></div>
        </div>
      </div>

      <form class="form-card" data-ajax-form action="{CONTACT_FORM_ACTION}">
        <input type="hidden" name="access_key" value="{WEB3FORMS_ACCESS_KEY}">
        <input type="hidden" name="from_name" value="Formulaire de contact BAME PRÉVENTION">
        <h2 style="margin-top:0;">Envoyer un message</h2>
        <div class="field">
          <label for="contact-name">Nom et prénom *</label>
          <input id="contact-name" name="name" type="text" required placeholder="Jean Dupont">
        </div>
        <div class="field">
          <label for="contact-company">Entreprise</label>
          <input id="contact-company" name="company" type="text" placeholder="Nom de votre entreprise">
        </div>
        <div class="field">
          <label for="contact-email">E-mail *</label>
          <input id="contact-email" name="email" type="email" required placeholder="vous@entreprise.fr">
        </div>
        <div class="field">
          <label for="contact-subject">Objet *</label>
          <input id="contact-subject" name="subject" type="text" required placeholder="Formation SST, DUERP, devis…">
        </div>
        <div class="field">
          <label for="contact-message">Message *</label>
          <textarea id="contact-message" name="message" rows="6" required placeholder="Décrivez votre besoin, le nombre de salariés concernés, vos disponibilités…"></textarea>
        </div>
        <label class="field-check">
          <input type="checkbox" required name="consent">
          <span>J'accepte que ces données soient stockées et traitées dans le but d'établir un contact. Je suis conscient(e) que je peux révoquer mon consentement à tout moment.*</span>
        </label>
        <p class="form-note">* Indique les champs obligatoires</p>
        <button class="btn btn-primary" type="submit" style="margin-top:8px;">Envoyer</button>
        <p class="form-status"></p>
      </form>
    </div>
  </div>
</section>
"""

# =================================================================
# LEGAL PAGES
# =================================================================

MENTIONS_LEGALES_BODY = """
<section class="page-hero section--tight">
  <div class="container">
    <div class="breadcrumb"><a href="/index.html">Accueil</a> / Mentions légales</div>
    <h1>Mentions légales</h1>
  </div>
</section>
<section class="section">
  <div class="container legal">
    <p>Conformément aux dispositions de la loi n° 2004-575 du 21 juin 2004 pour la confiance en l'économie numérique, il est précisé aux utilisateurs du site bameprevention.fr l'identité des différents intervenants dans le cadre de sa réalisation et de son suivi.</p>

    <h2>1. Éditeur du site</h2>
    <p>Le site bameprevention.fr est édité par :</p>
    <p><strong>BAME PRÉVENTION</strong><br>
    Entreprise individuelle<br>
    Représentée par : Laure PIPET<br>
    Adresse : 2 bis Rue du Parc — 77540 Bernay-Vilbert, France<br>
    Téléphone : 06 67 98 14 71<br>
    Email : lp@sofeca.com</p>
    <p>SIRET : 91990879800011<br>
    Numéro de Déclaration d'Activité (NDA) : 11770808577<br>
    TVA non applicable, article 293 B du Code Général des Impôts</p>

    <h2>2. Directrice de la publication</h2>
    <p>Madame Laure PIPET — Email : lp@sofeca.com</p>

    <h2>3. Hébergeur du site</h2>
    <p><em>Section à finaliser avant mise en ligne, une fois l'hébergeur définitif choisi (ex. Vercel Inc. ou Netlify Inc.) — indiquer ici sa raison sociale et son adresse complète.</em></p>

    <h2>4. Propriété intellectuelle</h2>
    <p>L'ensemble du contenu présent sur le site bameprevention.fr (textes, images, photographies, logos, graphismes, vidéos, icônes, structure du site, etc.) est la propriété exclusive de BAME PRÉVENTION ou fait l'objet d'une autorisation d'utilisation.</p>
    <p>Toute reproduction, représentation, modification, publication, adaptation de tout ou partie des éléments du site, quel que soit le moyen ou le procédé utilisé, est interdite sans l'autorisation écrite préalable de BAME PRÉVENTION.</p>
    <p>Toute exploitation non autorisée du site ou de l'un quelconque des éléments qu'il contient sera considérée comme constitutive d'une contrefaçon et poursuivie conformément aux dispositions des articles L.335-2 et suivants du Code de la Propriété Intellectuelle.</p>

    <h2>5. Données personnelles — RGPD</h2>
    <p>Conformément au Règlement Général sur la Protection des Données (RGPD) n° 2016/679 et à la loi Informatique et Libertés modifiée, vous disposez d'un droit d'accès, de rectification, d'effacement, de portabilité et d'opposition concernant vos données personnelles.</p>
    <p>Les informations recueillies via le formulaire d'inscription du site sont nécessaires à la gestion de votre dossier de formation et au respect des obligations légales et réglementaires applicables aux organismes de formation professionnelle (article L.6353-1 du Code du Travail, référentiel Qualiopi).</p>
    <p>Vos données sont conservées pendant une durée de 5 ans à compter de la fin de la dernière formation suivie, puis détruites. Elles ne sont pas transmises à des tiers, à l'exception des organismes officiels (INRS, financeurs de formation) lorsque la formation l'exige.</p>
    <p>Pour exercer vos droits, vous pouvez nous contacter par email à lp@sofeca.com ou par courrier à l'adresse de l'entreprise indiquée ci-dessus.</p>
    <p>Vous disposez également du droit d'introduire une réclamation auprès de la Commission Nationale de l'Informatique et des Libertés (CNIL) : <a href="https://www.cnil.fr" target="_blank" rel="noopener">www.cnil.fr</a></p>

    <h2>6. Cookies</h2>
    <p>Le site bameprevention.fr peut utiliser des cookies à des fins de mesure d'audience et de bon fonctionnement. Vous pouvez à tout moment paramétrer votre navigateur pour refuser les cookies.</p>

    <h2>7. Responsabilité</h2>
    <p>BAME PRÉVENTION s'efforce d'assurer l'exactitude et la mise à jour des informations diffusées sur ce site. Toutefois, BAME PRÉVENTION ne peut garantir l'exactitude, la précision ou l'exhaustivité des informations mises à disposition sur le site.</p>
    <p>En conséquence, BAME PRÉVENTION décline toute responsabilité pour toute imprécision, inexactitude ou omission portant sur des informations disponibles sur le site.</p>
    <p>Les liens hypertextes mis en place sur le site en direction d'autres sites ne sauraient engager la responsabilité de BAME PRÉVENTION.</p>

    <h2>8. Contact</h2>
    <p>Pour toute question relative aux présentes mentions légales :<br>Email : lp@sofeca.com<br>Téléphone : 06 67 98 14 71</p>

    <p class="muted" style="margin-top:2.5em;font-size:.85rem;">Mentions légales mises à jour le : 5 mai 2026.</p>
  </div>
</section>
"""

RGPD_BODY = """
<section class="page-hero section--tight">
  <div class="container">
    <div class="breadcrumb"><a href="/index.html">Accueil</a> / RGPD</div>
    <h1>Politique de confidentialité</h1>
  </div>
</section>
<section class="section">
  <div class="container legal">
    <p>BAME PRÉVENTION s'engage à protéger la vie privée et les données personnelles des utilisateurs de son site et de ses services. La présente politique de confidentialité a pour objet d'informer les utilisateurs sur les modalités de collecte et de traitement de leurs données personnelles, conformément au Règlement Général sur la Protection des Données (RGPD) n° 2016/679 du 27 avril 2016 et à la loi Informatique et Libertés n° 78-17 du 6 janvier 1978 modifiée.</p>

    <h2>1. Identité du responsable de traitement</h2>
    <p>Le responsable du traitement des données personnelles est :</p>
    <p><strong>BAME PRÉVENTION — Laure PIPET</strong><br>
    2 bis Rue du Parc — 77540 Bernay-Vilbert<br>
    Email : lp@sofeca.com<br>
    Téléphone : 06 67 98 14 71</p>

    <h2>2. Données collectées</h2>
    <p>Les données personnelles collectées par BAME PRÉVENTION dans le cadre de ses activités de formation sont les suivantes :</p>
    <ul>
      <li>Nom et prénom</li>
      <li>Date de naissance</li>
      <li>Numéro de sécurité sociale (uniquement pour les formations éligibles au passeport prévention)</li>
      <li>Adresse email</li>
      <li>Numéro de téléphone</li>
      <li>Coordonnées professionnelles (entreprise, adresse, fonction)</li>
      <li>Informations sur les besoins spécifiques d'accompagnement (handicap éventuel)</li>
      <li>Réponses aux questions du formulaire d'inscription (attentes, expérience préalable)</li>
    </ul>

    <h2>3. Finalités du traitement et bases légales</h2>
    <p><strong>Gestion des inscriptions et des formations</strong><br>
    Base légale : exécution du contrat de formation (article 6.1.b du RGPD). Données nécessaires pour convoquer le stagiaire, établir la convention de formation, suivre la formation, délivrer l'attestation.</p>
    <p><strong>Respect des obligations légales</strong><br>
    Base légale : obligation légale (article 6.1.c du RGPD). Données nécessaires pour respecter les obligations imposées aux organismes de formation par le Code du Travail (article L.6353-1 et suivants), le référentiel Qualiopi, et les obligations comptables et fiscales.</p>
    <p><strong>Adaptation de la formation au handicap</strong><br>
    Base légale : obligation légale et intérêt légitime (articles 6.1.c et 6.1.f du RGPD). Les informations relatives au handicap ne sont collectées que sur déclaration volontaire du stagiaire et utilisées uniquement pour adapter la formation.</p>

    <h2>4. Destinataires des données</h2>
    <p>Les données collectées sont strictement réservées à BAME PRÉVENTION. Elles ne sont ni vendues, ni cédées à des tiers à des fins commerciales.</p>
    <p>Elles peuvent être transmises uniquement aux destinataires suivants, dans le cadre strict de la formation :</p>
    <ul>
      <li>L'INRS et la plateforme ForPrev (pour la délivrance des certificats SST)</li>
      <li>Les financeurs de formation (OPCO, FIFPL, CPF, Pôle Emploi, etc.) lorsqu'un financement est en jeu</li>
      <li>L'employeur du stagiaire (uniquement les documents nécessaires : convocation, convention)</li>
      <li>L'Agefiph ou organismes spécialisés (uniquement avec l'accord du stagiaire pour adapter la formation au handicap)</li>
    </ul>

    <h2>5. Durée de conservation</h2>
    <ul>
      <li>Données de formation (dossier complet) : 5 ans à compter de la fin de la formation, conformément aux exigences du référentiel Qualiopi et du Code du Travail, puis passées à la broyeuse avec certificat de destruction sur l'honneur sur demande.</li>
      <li>Données comptables et fiscales (factures) : 10 ans, conformément à l'article L.123-22 du Code de Commerce</li>
      <li>Données de prospect / contact non concrétisé : 3 ans à compter du dernier contact</li>
      <li>Numéro de sécurité sociale : non conservé, supprimé après l'inscription sur Net-entreprises</li>
    </ul>
    <p>À l'issue de ces durées, les données sont supprimées de manière sécurisée. Les emails sont supprimés automatiquement au bout d'un mois. Pour les inscriptions via Google Form, les réponses sont supprimées du Google Sheet une fois les informations récoltées.</p>

    <h2>6. Vos droits</h2>
    <ul>
      <li>Droit d'accès : obtenir la confirmation que vos données sont traitées et en obtenir une copie</li>
      <li>Droit de rectification : faire rectifier des données inexactes ou incomplètes</li>
      <li>Droit à l'effacement (« droit à l'oubli ») : faire supprimer vos données dans les conditions prévues par la loi</li>
      <li>Droit à la limitation : demander que le traitement soit suspendu temporairement</li>
      <li>Droit d'opposition : vous opposer au traitement de vos données pour des motifs légitimes</li>
      <li>Droit à la portabilité : recevoir vos données dans un format structuré pour les transmettre à un autre responsable de traitement</li>
      <li>Droit de définir des directives post-mortem concernant la conservation et la communication de vos données après votre décès</li>
    </ul>
    <p>Pour exercer ces droits, vous pouvez nous contacter à tout moment par email à lp@sofeca.com ou par courrier à BAME PRÉVENTION — 2 bis Rue du Parc — 77540 Bernay-Vilbert.</p>
    <p>Une réponse vous sera apportée dans un délai d'un mois maximum à compter de la réception de votre demande. Une preuve d'identité pourra être demandée pour s'assurer de la légitimité de la demande.</p>

    <h2>7. Réclamation auprès de la CNIL</h2>
    <p>Si vous estimez que le traitement de vos données personnelles n'est pas conforme à la réglementation, vous disposez du droit d'introduire une réclamation auprès de la Commission Nationale de l'Informatique et des Libertés (CNIL) :</p>
    <p>CNIL — 3 Place de Fontenoy — TSA 80715 — 75334 PARIS CEDEX 07<br>
    Téléphone : 01 53 73 22 22<br>
    Site web : <a href="https://www.cnil.fr" target="_blank" rel="noopener">www.cnil.fr</a></p>

    <h2>8. Sécurité des données</h2>
    <p>BAME PRÉVENTION met en œuvre les mesures techniques et organisationnelles appropriées pour garantir la sécurité et la confidentialité des données personnelles : accès restreint, mots de passe sécurisés, sauvegardes régulières, conservation locale sur poste protégé, transfert chiffré (HTTPS, SSL).</p>

    <h2>9. Modification de la politique</h2>
    <p>BAME PRÉVENTION se réserve le droit de modifier la présente politique de confidentialité à tout moment. La date de dernière mise à jour est indiquée ci-dessous.</p>

    <p class="muted" style="margin-top:2.5em;font-size:.85rem;">Politique de confidentialité mise à jour le : 5 mai 2026.</p>
  </div>
</section>
"""

CGV_FORMATION_BODY = """
<section class="page-hero section--tight">
  <div class="container">
    <div class="breadcrumb"><a href="/index.html">Accueil</a> / CGV Formation</div>
    <h1>Conditions générales de vente des formations</h1>
  </div>
</section>
<section class="section">
  <div class="container legal">
    <p>Les présentes Conditions Générales de Vente (« CGV ») régissent l'ensemble des prestations de formation professionnelle proposées par BAME PRÉVENTION. Elles font partie intégrante de la convention de formation signée entre les parties et s'appliquent à toute commande.</p>

    <h2>Article 1 — Objet</h2>
    <p>Les présentes CGV ont pour objet de définir les conditions dans lesquelles BAME PRÉVENTION fournit des prestations de formation professionnelle continue à ses clients, qu'ils soient entreprises, collectivités, associations ou particuliers.</p>
    <p>Toute commande implique l'acceptation sans réserve par le client des présentes CGV, qui prévalent sur tout autre document, à l'exception des dispositions particulières expressément acceptées par BAME PRÉVENTION.</p>

    <h2>Article 2 — Désignation du prestataire</h2>
    <p>BAME PRÉVENTION — entreprise individuelle représentée par Madame Laure PIPET<br>
    2 bis Rue du Parc — 77540 Bernay-Vilbert, France<br>
    SIRET : 91990879800011 — Numéro de Déclaration d'Activité : 11770808577<br>
    Téléphone : 06 67 98 14 71 — Email : lp@sofeca.com<br>
    Cet enregistrement ne vaut pas agrément de l'État.</p>

    <h2>Article 3 — Prestations proposées</h2>
    <p>BAME PRÉVENTION propose les formations suivantes :</p>
    <ul>
      <li>SST Initial (Sauveteur Secouriste du Travail) — 14 heures sur 2 jours</li>
      <li>MAC SST (Maintien et Actualisation des Compétences SST) — 7 heures</li>
      <li>Les bonnes pratiques pour secourir une victime — Initiation — 7 heures</li>
      <li>Les bonnes pratiques pour secourir une victime — Sensibilisation — 3 heures 30</li>
      <li>Gestes et Postures (prévention des TMS) — 7 heures</li>
    </ul>
    <p>Le contenu détaillé de chaque formation, ses objectifs pédagogiques et ses modalités d'évaluation sont décrits dans le programme de formation remis au client préalablement à toute commande.</p>

    <h2>Article 4 — Modalités de commande</h2>
    <p>Toute commande de formation fait l'objet d'un échange préalable (téléphonique ou par email) pour définir les besoins, d'un devis transmis par BAME PRÉVENTION, et d'une convention de formation professionnelle signée entre les parties (article L.6353-1 du Code du travail) avant le début de la formation.</p>
    <p>La signature de la convention de formation vaut acceptation pleine et entière des présentes CGV.</p>

    <h2>Article 5 — Tarifs</h2>
    <p>Les prestations de formation professionnelle continue dispensées par BAME PRÉVENTION sont exonérées de TVA en application de l'article 261-4-4°a du Code Général des Impôts ; à ce titre, la TVA n'est pas applicable et les prix sont indiqués nets de taxes.</p>
    <p>Tarif standard : 600 € net par jour de formation, pour un groupe de 4 à 10 stagiaires. Des tarifs spécifiques peuvent être appliqués selon le nombre de stagiaires, la durée totale de la prestation et les frais de déplacement éventuels. Tout devis est valable 30 jours à compter de sa date d'émission.</p>

    <h2>Article 6 — Modalités de paiement</h2>
    <p>Le règlement s'effectue à réception de la facture, par virement bancaire ou par chèque, dans un délai maximum de 30 jours.</p>
    <p><strong>Financement :</strong> les OPCO ne pratiquant plus la subrogation, il n'y a plus de paiement direct aux organismes de formation. Par conséquent, les règlements se font directement auprès de BAME PRÉVENTION ; il appartient au client de se rapprocher de son OPCO pour la prise en charge de tout ou partie de sa formation. BAME PRÉVENTION ne propose pas de financement par le CPF.</p>
    <p>Pénalités de retard : en cas de retard de paiement, des pénalités égales à trois fois le taux d'intérêt légal seront appliquées de plein droit, ainsi qu'une indemnité forfaitaire de 40 € pour frais de recouvrement (article L.441-10 du Code de commerce).</p>

    <h2>Article 7 — Annulation, report et rétractation</h2>
    <p><strong>7.1 — Annulation par le client :</strong></p>
    <ul>
      <li>Plus de 14 jours avant la formation : aucuns frais</li>
      <li>Entre 14 et 7 jours avant la formation : 30 % du montant total dû</li>
      <li>Moins de 7 jours avant la formation : 70 % du montant total dû</li>
      <li>Le jour même, absence non signalée ou abandon en cours : 100 % du montant total dû</li>
    </ul>
    <p><strong>7.2 — Annulation par BAME PRÉVENTION :</strong> BAME PRÉVENTION se réserve le droit d'annuler ou de reporter une formation en cas de force majeure, de maladie de la formatrice ou de nombre insuffisant de participants. Le client se voit alors proposer une nouvelle date sans frais supplémentaires ; aucune indemnité ne pourra être réclamée à BAME PRÉVENTION.</p>
    <p><strong>7.3 — Droit de rétractation :</strong> Lorsque le client est un consommateur (particulier), ou un professionnel employant cinq salariés au plus dont l'objet de la formation n'entre pas dans le champ de son activité principale, et que le contrat est conclu à distance ou hors établissement, il dispose d'un délai de rétractation de quatorze (14) jours à compter de la signature de la convention (articles L.221-3 et L.221-18 du Code de la consommation). Lorsque la formation doit débuter avant l'expiration de ce délai, le client demande expressément, en signant la convention, l'exécution anticipée de la prestation et reconnaît que son droit de rétractation s'éteint dès l'exécution complète de celle-ci (article L.221-25 du Code de la consommation). Dans les autres cas, la prestation n'est pas soumise au droit de rétractation.</p>

    <h2>Article 8 — Obligations de BAME PRÉVENTION</h2>
    <p>BAME PRÉVENTION s'engage à :</p>
    <ul>
      <li>réaliser les formations conformément au programme et aux objectifs définis</li>
      <li>mettre à disposition les moyens pédagogiques nécessaires (mannequins, défibrillateurs de formation, matériel de simulation, supports)</li>
      <li>remettre à chaque stagiaire un mémo pédagogique adapté à la formation suivie</li>
      <li>délivrer une attestation de fin de formation conformément à l'article L.6353-1 du Code du travail</li>
      <li>adapter la formation aux besoins spécifiques des stagiaires en situation de handicap (référente handicap : Laure PIPET, en lien avec l'Agefiph)</li>
    </ul>

    <h2>Article 9 — Obligations du client</h2>
    <p>Le client s'engage à :</p>
    <ul>
      <li>fournir tous les éléments nécessaires à la bonne réalisation de la formation (liste des stagiaires, dates, lieu)</li>
      <li>mettre à disposition une salle adaptée d'au moins 30 m², au sol propre et dégagé</li>
      <li>garantir des conditions matérielles satisfaisantes (chauffage, ventilation, prises électriques, sanitaires)</li>
      <li>régler le montant convenu dans les délais prévus</li>
    </ul>

    <h2>Article 10 — Propriété intellectuelle</h2>
    <p>Les supports pédagogiques, méthodes et contenus de formation utilisés ou remis par BAME PRÉVENTION sont la propriété exclusive de BAME PRÉVENTION ou de leurs ayants droit (notamment l'INRS pour les formations SST / MAC SST). Toute reproduction, diffusion ou utilisation à des fins autres que strictement personnelles est interdite sans accord écrit préalable.</p>

    <h2>Article 11 — Données personnelles</h2>
    <p>Les données personnelles collectées dans le cadre des formations sont traitées conformément à la <a href="/rgpd.html">Politique de Confidentialité</a> de BAME PRÉVENTION et au Règlement Général sur la Protection des Données (RGPD). Les stagiaires disposent d'un droit d'accès, de rectification, d'effacement, de portabilité et d'opposition concernant leurs données. Pour exercer ces droits : lp@sofeca.com.</p>

    <h2>Article 12 — Réclamation et médiation</h2>
    <p>En cas de réclamation, le client peut adresser sa demande à BAME PRÉVENTION par email (lp@sofeca.com) ou par courrier postal. Une réponse lui sera apportée dans un délai de 30 jours.</p>
    <p>Conformément à l'article L.612-1 du Code de la consommation, le client consommateur peut recourir gratuitement au médiateur de la consommation en cas de litige non résolu à l'amiable.</p>

    <h2>Article 13 — Loi applicable et juridiction</h2>
    <p>Les présentes CGV sont soumises au droit français. En cas de litige, et après échec de toute tentative de résolution amiable, les tribunaux compétents seront déterminés dans les conditions du droit commun.</p>

    <p class="muted" style="margin-top:2.5em;font-size:.85rem;">CGV mises à jour en juin 2026.</p>
    <a class="btn btn-outline" href="/assets/documents/CGV_Formations.pdf" target="_blank" rel="noopener">Télécharger les CGV (PDF)</a>
  </div>
</section>
"""

CGV_DUERP_BODY = """
<section class="page-hero section--tight">
  <div class="container">
    <div class="breadcrumb"><a href="/index.html">Accueil</a> / CGV DUERP</div>
    <h1>Conditions générales de vente — Prestation DUERP</h1>
  </div>
</section>
<section class="section">
  <div class="container legal">
    <p>Les présentes Conditions Générales de Vente (« CGV ») régissent les prestations de conseil et d'accompagnement en prévention des risques professionnels fournies par BAME PRÉVENTION, notamment l'élaboration et la mise à jour du Document Unique d'Évaluation des Risques Professionnels (DUERP). Elles font partie intégrante du contrat de prestation (devis ou lettre de mission) signé entre les parties.</p>

    <h2>Article 1 — Objet</h2>
    <p>Les présentes CGV définissent les conditions dans lesquelles BAME PRÉVENTION réalise, pour le compte de ses clients (entreprises, collectivités, associations), des prestations de conseil, d'audit et d'accompagnement en santé et sécurité au travail.</p>
    <p>Toute commande implique l'acceptation sans réserve des présentes CGV, qui prévalent sur tout autre document, sauf dispositions particulières expressément acceptées par BAME PRÉVENTION.</p>

    <h2>Article 2 — Désignation du prestataire</h2>
    <p>BAME PRÉVENTION — entreprise individuelle représentée par Madame Laure PIPET<br>
    2 bis Rue du Parc — 77540 Bernay-Vilbert, France<br>
    SIRET : 91990879800011<br>
    Téléphone : 06 67 98 14 71 — Email : lp@sofeca.com<br>
    Activité : conseil et accompagnement en prévention des risques professionnels.</p>

    <h2>Article 3 — Prestations proposées</h2>
    <ul>
      <li>Élaboration du Document Unique d'Évaluation des Risques Professionnels (DUERP)</li>
      <li>Mise à jour et révision du DUERP existant</li>
      <li>Évaluation des risques professionnels par unité de travail (identification, cotation, hiérarchisation)</li>
      <li>Évaluation des risques psychosociaux (RPS)</li>
      <li>Accompagnement à l'élaboration du plan d'actions de prévention (programme annuel / PAPRIPACT)</li>
      <li>Conseil et audit en santé et sécurité au travail</li>
    </ul>
    <p>Le périmètre précis de chaque mission est défini dans le devis ou la lettre de mission remis au client préalablement à toute intervention.</p>

    <h2>Article 4 — Cadre réglementaire et responsabilité de l'employeur</h2>
    <ul>
      <li>Code du travail — Art. L.4121-1 à L.4121-3 : obligation générale de prévention des risques professionnels à la charge de l'employeur</li>
      <li>Code du travail — Art. R.4121-1 et R.4121-2 : obligation d'établir et de mettre à jour le DUERP (au moins annuellement pour les entreprises d'au moins 11 salariés, et lors de toute décision d'aménagement important ou information nouvelle)</li>
      <li>Loi du 2 août 2021 : conservation du DUERP et de ses versions successives pendant au moins 40 ans et dépôt dématérialisé</li>
    </ul>
    <p><strong>Responsabilité de l'employeur :</strong> le DUERP relève de la responsabilité exclusive de l'employeur. BAME PRÉVENTION intervient en appui méthodologique et en conseil ; sa prestation ne transfère ni ne substitue la responsabilité légale de l'employeur en matière d'évaluation et de prévention des risques. Le client demeure seul responsable de la validation, de l'adoption et de la mise en œuvre du DUERP et du plan d'actions.</p>

    <h2>Article 5 — Modalités de commande</h2>
    <p>Toute prestation fait l'objet d'un échange préalable (téléphonique ou par email) pour cadrer le besoin, d'un devis ou d'une lettre de mission précisant le périmètre, les livrables et le tarif, et de la signature de ce document par le client avant le début de l'intervention. La signature du devis ou de la lettre de mission vaut acceptation pleine et entière des présentes CGV.</p>

    <h2>Article 6 — Tarifs</h2>
    <p>BAME PRÉVENTION bénéficie de la franchise en base de TVA prévue à l'article 293 B du Code Général des Impôts ; à ce titre, la TVA n'est pas applicable et les prix sont indiqués nets de taxes.</p>
    <p>Les prestations de conseil sont établies sur devis, en fonction de la taille de l'entreprise, du nombre d'unités de travail, du périmètre de la mission et des frais de déplacement éventuels. Tout devis est valable 30 jours à compter de sa date d'émission.</p>

    <h2>Article 7 — Modalités de paiement</h2>
    <p>Le règlement s'effectue à réception de la facture, par virement bancaire ou par chèque, dans un délai maximum de 30 jours. Un acompte peut être demandé à la commande pour les missions importantes ; il est alors précisé sur le devis.</p>
    <p>Pénalités de retard : en cas de retard de paiement, des pénalités égales à trois fois le taux d'intérêt légal seront appliquées de plein droit, ainsi qu'une indemnité forfaitaire de 40 € pour frais de recouvrement (article L.441-10 du Code de commerce).</p>

    <h2>Article 8 — Annulation, report et rétractation</h2>
    <p><strong>8.1 — Annulation par le client :</strong></p>
    <ul>
      <li>Plus de 14 jours avant l'intervention planifiée : aucuns frais</li>
      <li>Entre 14 et 7 jours : 30 % du montant de la mission</li>
      <li>Moins de 7 jours : 70 % du montant de la mission</li>
      <li>Mission entamée puis interrompue du fait du client : facturation au prorata des travaux déjà réalisés</li>
    </ul>
    <p><strong>8.2 — Annulation par BAME PRÉVENTION :</strong> en cas de force majeure ou d'indisponibilité, BAME PRÉVENTION propose une nouvelle date sans frais supplémentaires ; aucune indemnité ne pourra lui être réclamée.</p>
    <p><strong>8.3 — Droit de rétractation :</strong> lorsque le client est un professionnel employant cinq salariés au plus et que l'objet de la prestation n'entre pas dans le champ de son activité principale, et que le contrat est conclu à distance ou hors établissement, il dispose d'un délai de rétractation de quatorze (14) jours à compter de la signature (articles L.221-3 et L.221-18 du Code de la consommation). Lorsque la mission doit débuter avant l'expiration de ce délai, le client demande expressément, en signant le devis ou la lettre de mission, l'exécution anticipée et reconnaît que son droit de rétractation s'éteint dès l'exécution complète de la prestation (article L.221-25). Dans les autres cas, la prestation n'est pas soumise au droit de rétractation.</p>

    <h2>Article 9 — Obligations de BAME PRÉVENTION</h2>
    <ul>
      <li>réaliser la prestation conformément au périmètre défini dans le devis ou la lettre de mission</li>
      <li>mettre en œuvre une obligation de moyens, dans le respect des règles de l'art et de la méthodologie de prévention (notamment INRS)</li>
      <li>remettre les livrables convenus (DUERP, rapport d'évaluation, plan d'actions)</li>
      <li>respecter la confidentialité des informations recueillies au sein de l'entreprise</li>
    </ul>

    <h2>Article 10 — Obligations du client</h2>
    <ul>
      <li>désigner un interlocuteur référent pour la mission</li>
      <li>fournir les informations, documents et accès nécessaires (visite des locaux, entretiens avec les salariés, données d'activité)</li>
      <li>garantir des conditions d'intervention permettant la bonne réalisation de la prestation</li>
      <li>valider, adopter et mettre en œuvre le DUERP et le plan d'actions sous sa responsabilité</li>
      <li>régler le montant convenu dans les délais prévus</li>
    </ul>

    <h2>Article 11 — Confidentialité</h2>
    <p>BAME PRÉVENTION s'engage à conserver confidentielles l'ensemble des informations, documents et données auxquels elle a accès dans le cadre de la mission, et à ne les utiliser que pour les besoins de la prestation. Cette obligation perdure après la fin de la mission.</p>

    <h2>Article 12 — Propriété intellectuelle</h2>
    <p>Les méthodes, outils, trames et supports utilisés par BAME PRÉVENTION restent sa propriété exclusive. Les livrables personnalisés (DUERP, rapport, plan d'actions) deviennent la propriété du client après règlement intégral de la prestation.</p>

    <h2>Article 13 — Données personnelles (RGPD)</h2>
    <p>Les données personnelles traitées dans le cadre de la mission le sont conformément au Règlement Général sur la Protection des Données (RGPD). Les personnes concernées disposent d'un droit d'accès, de rectification, d'effacement et d'opposition, à exercer à l'adresse : lp@sofeca.com.</p>

    <h2>Article 14 — Responsabilité</h2>
    <p>BAME PRÉVENTION est tenue à une obligation de moyens et non de résultat. Sa responsabilité ne saurait être engagée pour les conséquences d'une mise en œuvre incomplète, tardive ou erronée du DUERP et du plan d'actions par le client, ni pour les informations inexactes ou incomplètes communiquées par ce dernier.</p>

    <h2>Article 15 — Réclamation, loi applicable et juridiction</h2>
    <p>Toute réclamation peut être adressée à BAME PRÉVENTION par email (lp@sofeca.com) ou par courrier ; une réponse sera apportée sous 30 jours. Les présentes CGV sont soumises au droit français. En cas de litige, et après échec de toute tentative de résolution amiable, les tribunaux compétents seront déterminés dans les conditions du droit commun.</p>

    <p class="muted" style="margin-top:2.5em;font-size:.85rem;">CGV DUERP mises à jour le 06/06/2026 — v2.</p>
    <a class="btn btn-outline" href="/assets/documents/CGV_DUERP.pdf" target="_blank" rel="noopener">Télécharger les CGV (PDF)</a>
  </div>
</section>
"""

PAGES = {
    "index": ("Accueil — BAME PRÉVENTION", "Organisme de formation en santé-sécurité au travail : SST, MAC SST, gestes qui sauvent, gestes et postures, DUERP. Prévenir aujourd'hui pour mieux vivre demain.", INDEX_BODY),
    "a-propos": ("À propos — BAME PRÉVENTION", "Laure PIPET, formatrice SST/PRAP certifiée INRS, fondatrice de BAME PRÉVENTION. Une démarche de prévention humaine, concrète et durable.", A_PROPOS_BODY),
    "philosophie": ("Notre philosophie — BAME PRÉVENTION", "Qualité, accessibilité, efficacité et prix équitables : les engagements de BAME PRÉVENTION pour une prévention durable.", PHILOSOPHIE_BODY),
    "sst": ("Formation SST — Sauveteur Secouriste du Travail", "Formation SST Initial, 14h sur 2 jours, par une formatrice certifiée INRS. Obligatoire dans les ateliers à travaux dangereux (article R.4224-15).", SST_BODY),
    "mac-sst": ("Formation MAC SST — Maintien des compétences", "Recyclage SST (MAC SST), 7h, pour actualiser vos compétences de sauveteur secouriste du travail.", MAC_SST_BODY),
    "secours": ("Les gestes qui sauvent — Bonnes pratiques de secours", "Formations citoyen sauveteur, de 3h30 à 7h : les bonnes pratiques pour secourir une victime au quotidien.", SECOURS_BODY),
    "gestes-et-postures": ("Formation Gestes et Postures — Prévention des TMS", "Formation Gestes et Postures, 7h, pour prévenir les troubles musculosquelettiques dans tous les secteurs d'activité.", GESTES_POSTURES_BODY),
    "duerp": ("DUERP — Document Unique d'Évaluation des Risques", "Accompagnement à l'élaboration et la mise à jour de votre Document Unique d'Évaluation des Risques Professionnels.", DUERP_BODY),
    "contact": ("Contact — BAME PRÉVENTION", "Contactez BAME PRÉVENTION pour construire votre projet de prévention : formulaire, téléphone, email et adresse.", CONTACT_BODY),
    "mentions-legales": ("Mentions légales — BAME PRÉVENTION", "Mentions légales du site bameprevention.fr : éditeur, hébergeur, propriété intellectuelle et données personnelles.", MENTIONS_LEGALES_BODY),
    "cgv-formation": ("CGV Formation — BAME PRÉVENTION", "Conditions générales de vente des prestations de formation professionnelle BAME PRÉVENTION.", CGV_FORMATION_BODY),
    "cgv-duerp": ("CGV DUERP — BAME PRÉVENTION", "Conditions générales de vente de la prestation de conseil et d'accompagnement DUERP BAME PRÉVENTION.", CGV_DUERP_BODY),
    "rgpd": ("Politique de confidentialité RGPD — BAME PRÉVENTION", "Politique de confidentialité et protection des données personnelles de BAME PRÉVENTION, conformément au RGPD.", RGPD_BODY),
}
