/* ===========================================================
   BAME PRÉVENTION — Quiz du jour et test de réflexe
   Contenus tirés de sources officielles (ameli, INRS, Légifrance).
   Aucun cookie, aucun stockage : rien n'est enregistré sur l'appareil.
   =========================================================== */
(function () {
  "use strict";

  var SRC = {
    ed4085: { nom: "INRS — Aide-mémoire du sauveteur secouriste du travail (ED 4085, 6e édition)", url: "https://www.inrs.fr/media.html?refINRS=ED%204085" },
    infarctus: { nom: "ameli — Infarctus et arrêt cardiaque", url: "https://www.ameli.fr/assure/sante/urgence/pathologies/infarctus-myocarde-reagir" },
    malaise: { nom: "ameli — Perte de connaissance", url: "https://www.ameli.fr/assure/sante/urgence/pathologies/perte-connaissance" },
    brulure: { nom: "ameli — Brûlures de la peau", url: "https://www.ameli.fr/assure/sante/urgence/accidents-domestiques/brulures-peau" },
    etouffement: { nom: "ameli — Corps étranger inhalé", url: "https://www.ameli.fr/assure/sante/urgence/corps-etrangers/inhale" },
    plaie: { nom: "ameli — Coupure cutanée", url: "https://www.ameli.fr/assure/sante/urgence/accidents-domestiques/coupure-cutanee" },
    chimique: { nom: "INRS — Mesures d'urgence face au risque chimique", url: "https://www.inrs.fr/risques/chimiques/mesures-urgence.html" },
    sst: { nom: "INRS — Sauvetage secourisme du travail", url: "https://www.inrs.fr/services/formation/publics/sauveteur-secouriste.html" },
    tms: { nom: "INRS — Les TMS, ce qu'il faut retenir", url: "https://www.inrs.fr/risques/tms-troubles-musculosquelettiques/ce-qu-il-faut-retenir.html" },
    r4224: { nom: "Légifrance — Article R4224-15 du Code du travail", url: "https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000018532203" }
  };

  /* ---------- Quiz du jour : une question par jour, 14 en rotation ---------- */
  var QUIZ = [
    { q: "Quel numéro compose-t-on pour joindre le Samu ?",
      o: ["Le 15", "Le 17", "Le 19"], a: 0,
      e: "Le 15 est le numéro du Samu. Devant un arrêt cardiaque ou une urgence vitale, on appelle le 15 ou le 112, le numéro d'urgence européen.",
      s: "infarctus" },
    { q: "Vous vous brûlez la main. Quel est le premier geste ?",
      o: ["Appliquer de la glace directement sur la brûlure",
          "Arroser à l'eau à température ambiante, 20 minutes idéalement",
          "Passer une crème ou du beurre"], a: 1,
      e: "On arrose immédiatement la zone brûlée à l'eau à température ambiante, au moins 10 minutes et idéalement 20 minutes, en retirant les vêtements s'ils n'adhèrent pas à la peau. On évite la glace, les crèmes, le beurre et l'huile, qui peuvent aggraver la lésion.",
      s: ["ed4085", "brulure"] },
    { q: "Une personne s'étouffe : elle ne peut plus parler, tousser ni respirer. Que faites-vous en premier ?",
      o: ["Lui donner un verre d'eau",
          "Lui donner de 1 à 5 claques dans le dos",
          "L'allonger sur le dos"], a: 1,
      e: "Si la personne ne peut plus parler, tousser ni émettre un son, on donne de 1 à 5 claques dans le dos. Si c'est inefficace : compressions abdominales (méthode de Heimlich) chez l'adulte, compressions thoraciques chez la femme enceinte ou la personne obèse.",
      s: ["ed4085", "etouffement"] },
    { q: "Faut-il avoir suivi une formation pour utiliser un défibrillateur automatisé externe (DAE) ?",
      o: ["Oui, il faut être secouriste diplômé",
          "Non : il guide l'utilisateur par la voix, pas à pas",
          "Oui, il faut être professionnel de santé"], a: 1,
      e: "Le défibrillateur vous guide vocalement : il indique où placer les électrodes et quand s'écarter avant le choc. On peut s'en servir sans être formé, et il vaut mieux le faire que de ne rien faire.",
      s: "infarctus" },
    { q: "Pour un massage cardiaque chez l'adulte, où placez-vous vos mains ?",
      o: ["Sur le haut du ventre", "Au centre de la poitrine, l'une sur l'autre", "Sur le côté gauche du thorax"], a: 1,
      e: "Les mains se placent l'une sur l'autre au centre de la poitrine. On réalise 30 compressions à un rythme de 100 à 120 par minute, puis 2 insufflations, et on répète les cycles jusqu'à l'arrivée des secours. Le défibrillateur est mis en œuvre le plus tôt possible.",
      s: ["ed4085", "infarctus"] },
    { q: "Vous êtes seul face à une personne qui ne répond pas et ne respire pas. Que faites-vous d'abord ?",
      o: ["Je commence le massage pendant 10 minutes avant d'appeler",
          "J'appelle le 15 ou le 112, puis je commence le massage",
          "Je vais chercher un voisin"], a: 1,
      e: "Si vous êtes seul, vous appelez d'abord le 15 ou le 112, puis vous commencez le massage cardiaque sans vous arrêter jusqu'à l'arrivée des secours. Si quelqu'un est là, il peut aller chercher un défibrillateur.",
      s: "infarctus" },
    { q: "Une personne ne répond pas mais respire. Son état résulte d'un événement non traumatique (un malaise, par exemple). Quelle position lui donnez-vous ?",
      o: ["Allongée sur le dos, jambes surélevées", "Assise contre un mur", "Sur le côté, en position latérale de sécurité (PLS)"], a: 2,
      e: "On allonge la victime sur le dos, on libère les voies respiratoires, puis, si son état résulte d'un événement non traumatique, on la met sur le côté en position latérale de sécurité. On la couvre et on surveille sa respiration en permanence.",
      s: ["ed4085", "malaise"] },
    { q: "Une personne a chuté d'une échelle. Elle ne répond pas mais respire. Que faites-vous ?",
      o: ["Je la mets systématiquement en PLS", "Je la laisse sur le dos et je maintiens la liberté de ses voies aériennes", "Je la fais s'asseoir"], a: 1,
      e: "Si l'état de la victime résulte d'un événement traumatique, ou d'un événement dont on ne connaît pas l'origine, on la laisse sur le dos et on maintient la liberté des voies aériennes. La PLS n'est donc pas automatique. On la couvre et on surveille sa respiration en permanence.",
      s: "ed4085" },
    { q: "Une personne saigne abondamment. Quels sont les premiers gestes ?",
      o: ["Lui donner à boire et la laisser debout", "Comprimer l'endroit qui saigne avec la paume de la main et l'allonger", "Retirer ce qui recouvre la plaie pour mieux voir"], a: 1,
      e: "On fait comprimer ou on comprime l'endroit qui saigne avec la paume de la main, protégée si possible, et on allonge la victime. On surveille l'efficacité de la compression, on couvre et on réconforte.",
      s: "ed4085" },
    { q: "Vous comprimez une plaie qui saigne abondamment, mais le saignement continue malgré la compression manuelle. Que faites-vous ?",
      o: ["Je pose un garrot", "Je relâche pour laisser la plaie respirer", "J'attends que cela s'arrête"], a: 0,
      e: "Si la compression manuelle est inefficace, on pose un garrot. Si elle est efficace, un pansement compressif peut la relayer si besoin. Si le saignement continue malgré le pansement compressif, on pose aussi un garrot, et on le laisse visible.",
      s: "ed4085" },
    { q: "Un produit chimique est projeté sur la peau. Combien de temps faut-il rincer à l'eau ?",
      o: ["Une trentaine de secondes", "Au moins 15 minutes", "Jusqu'à ce que la peau soit sèche"], a: 1,
      e: "On rince abondamment, au moins 15 minutes, en déshabillant la victime si nécessaire. Pour une projection importante, on la conduit sous une douche de sécurité. Un avis médical reste nécessaire, même sans symptôme visible.",
      s: "chimique" },
    { q: "Où trouver la conduite à tenir de premiers secours propre à un produit chimique ?",
      o: ["Sur le bon de livraison",
          "Dans la rubrique 4 « Premiers secours » de la fiche de données de sécurité (FDS)",
          "Uniquement en appelant le fabricant"], a: 1,
      e: "La rubrique 4 de la fiche de données de sécurité est consacrée aux premiers secours. En cas de brûlure par un produit chimique, on consulte et on conserve les informations de la fiche de données de sécurité du produit. Mieux vaut les repérer avant l'accident.",
      s: ["ed4085", "chimique"] },
    { q: "Quelle est la durée de validité du certificat de sauveteur secouriste du travail (SST) ?",
      o: ["6 mois", "24 mois, à prolonger par un stage de maintien et d'actualisation des compétences (MAC)", "À vie"], a: 1,
      e: "Le certificat SST est valable 24 mois. Il se prolonge en suivant, avant la fin de validité, un stage MAC de 7 heures, et en réussissant les épreuves certificatives.",
      s: "sst" },
    { q: "Quelle part des maladies professionnelles reconnues en France représentent les troubles musculosquelettiques (TMS) ?",
      o: ["Environ 10 %", "Environ 30 %", "Plus de 80 %"], a: 2,
      e: "Les TMS représentent plus de 80 % des maladies professionnelles reconnues. Ils touchent les muscles, les tendons et les nerfs, surtout au cou, aux épaules, aux coudes et aux poignets.",
      s: "tms" },
    { q: "Selon l'article R.4224-15 du Code du travail, que faut-il dans chaque atelier où sont réalisés des travaux dangereux ?",
      o: ["Un médecin sur place", "Un salarié formé aux premiers secours", "Un défibrillateur obligatoire"], a: 1,
      e: "La présence d'un salarié formé aux premiers secours est obligatoire dans chaque atelier où sont réalisés des travaux dangereux. C'est le rôle du sauveteur secouriste du travail.",
      s: "r4224" }
  ];

  /* ---------- Test de réflexe : 6 situations ---------- */
  var REFLEXE = [
    { t: "Un collègue s'étouffe en mangeant. Il se tient la gorge, ne peut plus parler ni tousser.",
      o: ["Lui donner de l'eau pour faire passer", "Lui donner de 1 à 5 claques dans le dos", "Attendre en observant"], a: 1,
      e: "Les claques dans le dos (de 1 à 5) sont le premier geste. Si elles sont inefficaces, on passe aux compressions abdominales (méthode de Heimlich) chez l'adulte, et on fait alerter les secours.", s: ["ed4085", "etouffement"] },
    { t: "Une personne s'effondre devant vous. Elle ne répond pas et ne respire pas.",
      o: ["La mettre en position latérale de sécurité", "Appeler le 15 ou le 112, puis faire un massage cardiaque en faisant chercher un défibrillateur", "Lui faire boire un peu d'eau"], a: 1,
      e: "C'est un arrêt cardiaque. On fait alerter, on réalise 30 compressions (100 à 120 par minute) puis 2 insufflations, et on utilise le défibrillateur le plus tôt possible : il vous guide par la voix.", s: ["ed4085", "infarctus"] },
    { t: "Un produit chimique a éclaboussé l'avant-bras d'un collègue.",
      o: ["Essuyer avec un chiffon et reprendre le travail", "Rincer abondamment à l'eau, au moins 15 minutes, en déshabillant la zone si besoin", "Appliquer une crème apaisante"], a: 1,
      e: "On rince longtemps et abondamment, sans s'arrêter avant 15 minutes. Un avis médical reste nécessaire, même sans symptôme visible. Pensez à la rubrique 4 de la fiche de données de sécurité.", s: "chimique" },
    { t: "Un collègue a fait un malaise sous vos yeux, sans chute ni choc. Il ne répond pas mais sa poitrine se soulève : il respire.",
      o: ["Le laisser sur le dos et attendre", "Le placer en position latérale de sécurité et surveiller sa respiration", "Le faire asseoir pour qu'il reprenne ses esprits"], a: 1,
      e: "L'état de ce collègue résulte d'un événement non traumatique : on l'allonge sur le dos, on libère les voies respiratoires, puis on le met en position latérale de sécurité. On le couvre et on surveille sa respiration en permanence.", s: ["ed4085", "malaise"] },
    { t: "Un collègue vient de tomber d'un escabeau. Il ne répond pas mais il respire.",
      o: ["Le mettre systématiquement en position latérale de sécurité", "Le laisser sur le dos et maintenir la liberté de ses voies aériennes", "Le relever pour le faire asseoir"], a: 1,
      e: "L'état de la victime résulte d'un événement traumatique : on ne la met pas en PLS automatiquement. On la laisse sur le dos, on maintient la liberté des voies aériennes, on la couvre et on surveille sa respiration en permanence, en faisant alerter les secours.", s: "ed4085" },
    { t: "Vous vous brûlez la main sur une plaque chauffante.",
      o: ["Mettre de la glace sur la brûlure", "Passer la main sous l'eau à température ambiante, 20 minutes idéalement", "Appliquer du beurre ou une crème"], a: 1,
      e: "On arrose immédiatement la brûlure à l'eau à température ambiante, au moins 10 minutes et idéalement 20, en retirant les vêtements s'ils n'adhèrent pas à la peau. La glace, les crèmes, le beurre et l'huile peuvent aggraver la lésion.", s: ["ed4085", "brulure"] },
    { t: "Un collègue s'est blessé : la plaie saigne abondamment.",
      o: ["Comprimer l'endroit qui saigne avec la paume de la main, et l'allonger", "Lui donner à boire pour qu'il reste conscient", "Retirer le linge régulièrement pour vérifier"], a: 0,
      e: "On comprime avec la paume de la main, protégée si possible, et on allonge le blessé. Si la compression manuelle est inefficace, on pose un garrot. Dans tous les cas, on fait alerter les secours.", s: ["ed4085", "plaie"] }
  ];

  /* ---------- Outils ---------- */
  function el(tag, cls, text) {
    var n = document.createElement(tag);
    if (cls) n.className = cls;
    if (text !== undefined) n.textContent = text;
    return n;
  }
  function shuffle(list) {
    var a = list.slice(), i, j, t;
    for (i = a.length - 1; i > 0; i--) {
      j = Math.floor(Math.random() * (i + 1)); t = a[i]; a[i] = a[j]; a[j] = t;
    }
    return a;
  }
  function sourceLink(keys) {
    var list = [].concat(keys), p = el("p", "jeu-source");
    p.appendChild(document.createTextNode(list.length > 1 ? "Sources : " : "Source : "));
    list.forEach(function (key, i) {
      var s = SRC[key];
      var a = el("a", null, s.nom);
      a.href = s.url; a.target = "_blank"; a.rel = "noopener";
      if (i) p.appendChild(document.createTextNode(" ; "));
      p.appendChild(a);
    });
    return p;
  }
  /* Construit les boutons de réponse ; rappelle onPick(indexChoisi, indexBonneReponse). */
  function buildOptions(q, onPick) {
    var wrap = el("div", "jeu-options");
    var order = shuffle(q.o.map(function (_, i) { return i; }));
    var buttons = [];
    order.forEach(function (origIdx) {
      var b = el("button", "jeu-option", q.o[origIdx]);
      b.type = "button";
      b.addEventListener("click", function () {
        buttons.forEach(function (x, k) {
          x.disabled = true;
          if (order[k] === q.a) x.classList.add("is-correct");
        });
        if (origIdx !== q.a) b.classList.add("is-wrong");
        onPick(origIdx === q.a);
      });
      buttons.push(b); wrap.appendChild(b);
    });
    return wrap;
  }

  /* ---------- Quiz du jour ---------- */
  function initQuiz(root) {
    var d = new Date();
    var dayNumber = Math.floor(Date.UTC(d.getFullYear(), d.getMonth(), d.getDate()) / 86400000);
    var q = QUIZ[dayNumber % QUIZ.length];
    var live = el("div", "jeu-feedback");
    live.setAttribute("aria-live", "polite");
    root.appendChild(el("h3", "jeu-question", q.q));
    root.appendChild(buildOptions(q, function (ok) {
      live.appendChild(el("p", "jeu-verdict " + (ok ? "ok" : "ko"), ok ? "Bonne réponse !" : "Pas tout à fait."));
      live.appendChild(el("p", "jeu-explication", q.e));
      live.appendChild(sourceLink(q.s));
      var cta = el("p", "jeu-cta");
      cta.appendChild(document.createTextNode("Une nouvelle question vous attend demain. En attendant, "));
      var a = el("a", null, "testez vos réflexes en 7 situations");
      a.href = "/test-reflexe.html";
      cta.appendChild(a); cta.appendChild(document.createTextNode("."));
      live.appendChild(cta);
    }));
    root.appendChild(live);
  }

  /* ---------- Test de réflexe ---------- */
  function initReflexe(root) {
    var idx = 0, score = 0;

    function showScenario() {
      root.textContent = "";
      var q = REFLEXE[idx];
      root.appendChild(el("p", "jeu-progress", "Situation " + (idx + 1) + " sur " + REFLEXE.length));
      root.appendChild(el("h3", "jeu-question", q.t));
      var live = el("div", "jeu-feedback");
      live.setAttribute("aria-live", "polite");
      root.appendChild(buildOptions(q, function (ok) {
        if (ok) score++;
        live.appendChild(el("p", "jeu-verdict " + (ok ? "ok" : "ko"), ok ? "Bon réflexe !" : "Ce n'est pas le bon geste."));
        live.appendChild(el("p", "jeu-explication", q.e));
        live.appendChild(sourceLink(q.s));
        var last = idx === REFLEXE.length - 1;
        var next = el("button", "btn btn-primary", last ? "Voir mon résultat" : "Situation suivante");
        next.type = "button";
        next.addEventListener("click", function () { idx++; last ? showResult() : showScenario(); });
        live.appendChild(next);
        next.focus();
      }));
      root.appendChild(live);
    }

    function showResult() {
      root.textContent = "";
      var total = REFLEXE.length;
      var msg = score === total ? "Excellent : vous avez les bons réflexes !"
        : score >= 4 ? "Bien joué : vous connaissez l'essentiel."
        : "Un bon début : une formation vous donnera les bons gestes.";
      root.appendChild(el("p", "jeu-score", score + " / " + total));
      root.appendChild(el("h3", "jeu-question", msg));
      root.appendChild(el("p", "jeu-explication",
        "Ce jeu est un rappel : il ne remplace pas une formation. Seule la pratique, avec un mannequin et un formateur, permet d'acquérir les bons gestes."));
      var actions = el("div", "jeu-actions");
      var a1 = el("a", "btn btn-primary", "Découvrir la formation SST"); a1.href = "/sst.html";
      var a2 = el("a", "btn btn-outline", "Demander un devis"); a2.href = "/contact.html";
      var again = el("button", "btn btn-outline", "Rejouer"); again.type = "button";
      again.addEventListener("click", function () { idx = 0; score = 0; showScenario(); });
      actions.appendChild(a1); actions.appendChild(a2); actions.appendChild(again);
      root.appendChild(actions);
    }

    showScenario();
  }

  var quiz = document.getElementById("quiz-jour");
  if (quiz) initQuiz(quiz);
  var reflexe = document.getElementById("test-reflexe");
  if (reflexe) initReflexe(reflexe);
})();
