(function () {
  var root = document.documentElement;
  var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  // ---- Theme toggle
  var themeBtn = document.querySelector(".theme-toggle");
  if (themeBtn) {
    themeBtn.addEventListener("click", function () {
      var next = root.getAttribute("data-theme") === "light" ? "dark" : "light";
      root.setAttribute("data-theme", next);
      try { localStorage.setItem("theme", next); } catch (e) {}
    });
  }

  // ---- Mobile menu
  var toggle = document.querySelector(".nav-toggle");
  var panel = document.getElementById("nav-links");
  if (toggle && panel) {
    var close = function () {
      panel.classList.remove("open");
      toggle.setAttribute("aria-expanded", "false");
    };
    toggle.addEventListener("click", function () {
      var open = panel.classList.toggle("open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
    panel.addEventListener("click", function (e) { if (e.target.closest("a")) close(); });
    document.addEventListener("keydown", function (e) { if (e.key === "Escape") close(); });
  }

  // ---- Header becomes solid after scrolling
  var header = document.querySelector(".site-header");
  var onScroll = function () {
    if (header) header.classList.toggle("is-scrolled", window.scrollY > 24);
  };
  onScroll();
  window.addEventListener("scroll", onScroll, { passive: true });

  // ---- Reveal on scroll (with a small stagger between siblings)
  var items = document.querySelectorAll("[data-reveal]");
  if (!("IntersectionObserver" in window) || reduceMotion) {
    items.forEach(function (el) { el.classList.add("is-visible"); });
  } else {
    var groups = new Map();
    items.forEach(function (el) {
      var parent = el.parentElement;
      var i = groups.get(parent) || 0;
      groups.set(parent, i + 1);
      el.style.setProperty("--delay", Math.min(i, 5) * 0.08 + "s");
    });
    var revealer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-visible");
          revealer.unobserve(entry.target);
        }
      });
    }, { rootMargin: "0px 0px -8% 0px", threshold: 0.08 });
    items.forEach(function (el) { revealer.observe(el); });
  }

  // ---- Active section in the nav
  var navLinks = document.querySelectorAll("[data-nav]");
  if (navLinks.length && "IntersectionObserver" in window) {
    var byId = {};
    navLinks.forEach(function (a) { byId[a.getAttribute("data-nav")] = a; });
    var spy = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        var link = byId[entry.target.id];
        if (!link) return;
        if (entry.isIntersecting) {
          navLinks.forEach(function (a) { a.classList.remove("is-active"); });
          link.classList.add("is-active");
        }
      });
    }, { rootMargin: "-45% 0px -50% 0px" });
    Object.keys(byId).forEach(function (id) {
      var section = document.getElementById(id);
      if (section) spy.observe(section);
    });
  }

  // ---- Spotlight that follows the pointer in hero areas.
  // Moved with a GPU transform (the CSS transition smooths it), so it never repaints.
  if (!reduceMotion && window.matchMedia("(pointer: fine)").matches) {
    document.querySelectorAll(".hero, .project-hero").forEach(function (hero) {
      var spot = hero.querySelector(".hero-spot");
      if (!spot) return;
      var half = spot.offsetWidth / 2;
      var x = 0, y = 0, frame = null, rect = null;
      // Read the hero position only when it can change, never inside pointermove
      // (reading layout there would force a style recalculation on every event).
      var measure = function () { rect = hero.getBoundingClientRect(); };
      hero.addEventListener("pointerenter", measure, { passive: true });
      window.addEventListener("scroll", function () { rect = null; }, { passive: true });
      window.addEventListener("resize", function () { rect = null; }, { passive: true });
      hero.addEventListener("pointermove", function (e) {
        if (!rect) measure();
        x = e.clientX - rect.left - half;
        y = e.clientY - rect.top - half;
        if (frame) return;
        frame = requestAnimationFrame(function () {
          spot.style.transform = "translate3d(" + x + "px," + y + "px,0)";
          frame = null;
        });
      }, { passive: true });
    });
  }
})();
