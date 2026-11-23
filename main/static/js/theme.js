// Runs in <head> before first paint: picks the theme (dark by default) and
// flags that JS is available so reveal animations can hide content safely.
// The choice is stored in localStorage only (no cookies).
(function () {
  var root = document.documentElement;
  root.classList.add("js");
  try {
    var saved = localStorage.getItem("theme");
    if (saved === "light" || saved === "dark") root.setAttribute("data-theme", saved);
  } catch (e) {}
})();
