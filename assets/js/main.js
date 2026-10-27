// BAME PRÉVENTION — comportements partagés
(function () {
  "use strict";

  // --- Rétrécissement du logo au scroll ---
  var header = document.querySelector(".site-header");
  if (header) {
    var ticking = false;
    var applyScrollState = function () {
      var y = window.pageYOffset || document.documentElement.scrollTop || document.body.scrollTop || 0;
      // Hystérésis pour éviter le clignotement du logo pendant le
      // rebond élastique (rubber-band) en haut de page sur trackpad/mobile.
      if (y > 60) {
        header.classList.add("is-scrolled");
      } else if (y < 10) {
        header.classList.remove("is-scrolled");
      }
      ticking = false;
    };
    applyScrollState();
    window.addEventListener(
      "scroll",
      function () {
        if (!ticking) {
          ticking = true;
          requestAnimationFrame(applyScrollState);
        }
      },
      { passive: true }
    );
  }

  // --- Navigation mobile ---
  var toggle = document.querySelector(".nav-toggle");
  var nav = document.querySelector(".main-nav");
  var scrim = document.querySelector(".nav-scrim");

  function closeNav() {
    nav && nav.classList.remove("is-open");
    scrim && scrim.classList.remove("is-open");
    toggle && toggle.setAttribute("aria-expanded", "false");
  }

  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = nav.classList.toggle("is-open");
      scrim && scrim.classList.toggle("is-open", open);
      toggle.setAttribute("aria-expanded", String(open));
    });
  }
  scrim && scrim.addEventListener("click", closeNav);

  document.querySelectorAll(".nav-dropdown > button").forEach(function (btn) {
    btn.addEventListener("click", function (e) {
      if (window.innerWidth > 980) return;
      e.preventDefault();
      btn.closest(".nav-dropdown").classList.toggle("is-open");
    });
  });

  document.querySelectorAll(".main-nav a").forEach(function (a) {
    a.addEventListener("click", function () {
      if (window.innerWidth <= 980) closeNav();
    });
  });

  // --- Bandeau cookies (choix stocké en local, pas de tracking tiers) ---
  var COOKIE_KEY = "bame-cookie-choice";
  var banner = document.querySelector(".cookie-banner");
  if (banner) {
    try {
      if (!localStorage.getItem(COOKIE_KEY)) {
        banner.classList.add("is-visible");
      }
    } catch (e) {}
    banner.querySelectorAll("[data-cookie-choice]").forEach(function (btn) {
      btn.addEventListener("click", function () {
        try {
          localStorage.setItem(COOKIE_KEY, btn.getAttribute("data-cookie-choice"));
        } catch (e) {}
        banner.classList.remove("is-visible");
      });
    });
  }

  // --- Envoi des formulaires (Formspree) en AJAX avec message de statut ---
  document.querySelectorAll("form[data-ajax-form]").forEach(function (form) {
    var status = form.querySelector(".form-status");
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      if (status) {
        status.className = "form-status is-visible";
        status.textContent = "Envoi en cours…";
      }
      var action = form.getAttribute("action") || "";
      if (!action || action.indexOf("VOTRE_ID_FORMSPREE") !== -1) {
        if (status) {
          status.className = "form-status is-visible err";
          status.textContent =
            "Formulaire non encore connecté — contactez-nous directement par téléphone ou email en attendant.";
        }
        return;
      }
      fetch(action, {
        method: "POST",
        body: new FormData(form),
        headers: { Accept: "application/json" },
      })
        .then(function (res) {
          if (res.ok) {
            form.reset();
            if (status) {
              status.className = "form-status is-visible ok";
              status.textContent = "Merci ! Nous revenons très vite vers vous pour vous proposer un plan adapté à votre demande. Cordialement. Laure PIPET";
            }
          } else {
            throw new Error("send-failed");
          }
        })
        .catch(function () {
          if (status) {
            status.className = "form-status is-visible err";
            status.textContent =
              "Une erreur est survenue. Merci de nous contacter par téléphone au 06 67 98 14 71.";
          }
        });
    });
  });

  // --- Newsletter (Brevo) : envoi en arrière-plan, sans ouvrir d'onglet ---
  document.querySelectorAll("form[data-nocors-form]").forEach(function (form) {
    var status = form.querySelector(".form-status");
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      if (status) {
        status.className = "form-status is-visible";
        status.textContent = "Envoi en cours…";
      }
      var action = form.getAttribute("action") || "";
      fetch(action, {
        method: "POST",
        mode: "no-cors",
        body: new FormData(form),
      })
        .then(function () {
          form.reset();
          if (status) {
            status.className = "form-status is-visible ok";
            status.textContent = "Merci, votre inscription est confirmée !";
          }
        })
        .catch(function () {
          if (status) {
            status.className = "form-status is-visible err";
            status.textContent =
              "Une erreur est survenue. Merci de réessayer ou de nous contacter directement.";
          }
        });
    });
  });

  // --- Carrousel (formations / ateliers) ---
  document.querySelectorAll(".carousel").forEach(function (carousel) {
    var track = carousel.querySelector(".carousel-track");
    if (!track) return;
    function scrollByCard(dir) {
      var card = track.querySelector(":scope > *");
      var amount = card ? card.getBoundingClientRect().width + 20 : 300;
      track.scrollBy({ left: dir * amount, behavior: "smooth" });
    }
    var prev = carousel.querySelector(".carousel-btn.prev");
    var next = carousel.querySelector(".carousel-btn.next");
    prev && prev.addEventListener("click", function () { scrollByCard(-1); });
    next && next.addEventListener("click", function () { scrollByCard(1); });
  });

  // --- Chiffres clés : effet compteur animé au scroll ---
  var counters = document.querySelectorAll(".stat-number[data-count]");
  if (counters.length) {
    var animateCount = function (el) {
      var target = parseInt(el.getAttribute("data-count"), 10) || 0;
      var suffix = el.getAttribute("data-suffix") || "";
      var duration = 1400;
      var start = null;
      el.textContent = "0";
      var step = function (timestamp) {
        if (start === null) start = timestamp;
        var progress = Math.min((timestamp - start) / duration, 1);
        var eased = 1 - Math.pow(1 - progress, 3);
        var value = Math.round(eased * target);
        el.textContent = value.toLocaleString("fr-FR") + suffix.replace("&nbsp;", " ");
        if (progress < 1) {
          requestAnimationFrame(step);
        } else {
          el.textContent = target.toLocaleString("fr-FR") + suffix.replace("&nbsp;", " ");
        }
      };
      requestAnimationFrame(step);
    };
    if ("IntersectionObserver" in window) {
      var counterObserver = new IntersectionObserver(
        function (entries) {
          entries.forEach(function (entry) {
            if (entry.isIntersecting) {
              animateCount(entry.target);
              counterObserver.unobserve(entry.target);
            }
          });
        },
        { threshold: 0.4 }
      );
      counters.forEach(function (el) {
        counterObserver.observe(el);
      });
    } else {
      counters.forEach(animateCount);
    }
  }

  // --- Année courante dans le footer ---
  document.querySelectorAll("[data-current-year]").forEach(function (el) {
    el.textContent = new Date().getFullYear();
  });
})();
