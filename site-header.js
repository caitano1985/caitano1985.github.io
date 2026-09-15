/*!
 * site-header.js — cabecalho canonico das paginas estaticas
 * caitano1985.github.io
 *
 * USO — coloque no <body>, antes de qualquer conteudo:
 *
 *   <div id="jc-header"
 *        data-title="Perspective"
 *        data-sub-en="— Capital Markets Technology"
 *        data-sub-es="— Tecnología de Mercados de Capitales"
 *        data-sub-pt="— Tecnologia de Mercado de Capitais"></div>
 *   <script src="/_shared/site-header.js"></script>
 *
 * Para paginas que precisam do seletor de lente (ULL Arena), acrescente:
 *        data-lens="true"
 *
 * EVENTOS emitidos em window:
 *   "jc:lang"  -> detail: { lang: "en" | "es" | "pt" }
 *   "jc:lens"  -> detail: { lens: "eng" | "board" }
 *
 * O idioma persiste em localStorage sob a chave "jc-lang",
 * compartilhada com o restante do site.
 */
(function () {
  "use strict";

  var MOUNT = document.getElementById("jc-header");
  if (!MOUNT) return;

  /* ---------------------------------------------------------- menu unico */
  var NAV = [
    ["about",       { en: "About",    es: "Sobre mí",     pt: "Sobre" }],
    ["academia",    { en: "Academy",  es: "Academia",     pt: "Academia" }],
    ["projetos",    { en: "Projects", es: "Proyectos",    pt: "Projetos" }],
    ["perspective", { en: "Perspective", es: "Perspectiva", pt: "Perspectiva" }],
    ["contato",     { en: "Contact",  es: "Contacto",     pt: "Contato" }]
  ];

  var LANGS = [
    { code: "en", flag: "\uD83C\uDDFA\uD83C\uDDF8", label: "English (US)" },
    { code: "es", flag: "\uD83C\uDDEA\uD83C\uDDF8", label: "Español (ES)" },
    { code: "pt", flag: "\uD83C\uDDE7\uD83C\uDDF7", label: "Português (BR)" }
  ];

  var LENS = {
    eng:   { en: "Engineering", es: "Ingeniería", pt: "Engenharia" },
    board: { en: "Board",       es: "Directorio", pt: "Board" }
  };

  var HOME = { en: "Home", es: "Inicio", pt: "Início" };

  /* ----------------------------------------------------------------- CSS */
  var CSS = [
    '#jc-header{display:block}',
    '.jc-nav{position:sticky;top:0;z-index:999;background:rgba(255,255,255,.92);',
    ' backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);',
    ' border-bottom:1px solid var(--ln,#DCE7F1);font-family:"DM Sans",system-ui,sans-serif}',
    '.jc-nav-in{max-width:var(--mw,1220px);margin:0 auto;display:flex;align-items:center;',
    ' gap:1.5rem;padding:.65rem 1.5rem}',
    '.jc-brand{display:flex;align-items:baseline;gap:.5rem;text-decoration:none;flex-shrink:0}',
    '.jc-brand b{font-family:"IBM Plex Mono",ui-monospace,monospace;font-weight:700;',
    ' font-size:.9rem;color:var(--bl,#0B5CD5)}',
    '.jc-brand i{font-style:normal;font-size:.75rem;color:var(--mu2,#93A6BB)}',
    '.jc-links{display:flex;align-items:center;gap:1.25rem;flex:1}',
    '.jc-links a{font-size:.82rem;color:var(--tx2,#4A5E78);text-decoration:none;',
    ' transition:color .15s;white-space:nowrap}',
    '.jc-links a:hover{color:var(--bl,#0B5CD5)}',
    '.jc-home{font-family:"IBM Plex Mono",ui-monospace,monospace;font-size:.8rem;',
    ' color:var(--bl,#0B5CD5);text-decoration:none;white-space:nowrap}',
    '.jc-home:hover{text-decoration:underline}',
    '@media(max-width:900px){.jc-links{display:none}.jc-home{margin-left:auto}}',

    '.jc-tb{background:rgba(255,255,255,.96);backdrop-filter:blur(10px);',
    ' border-bottom:1px solid var(--ln,#DCE7F1);position:sticky;top:45px;z-index:60}',
    '.jc-tb-in{max-width:var(--mw,1220px);margin:0 auto;padding:10px 24px;display:flex;',
    ' align-items:center;gap:12px;flex-wrap:wrap}',
    '.jc-badge{display:flex;align-items:center;gap:10px;font-weight:700;',
    ' color:var(--ink,#08213E);font-size:15px;font-family:"DM Sans",system-ui,sans-serif}',
    '.jc-badge span.s{color:var(--mu,#63768E);font-weight:400}',
    '.jc-sp{flex:1}',
    '.jc-seg{display:inline-flex;background:var(--t2,#E5F1FA);border:1px solid var(--sf,#D2E7F5);',
    ' border-radius:999px;padding:3px;gap:2px}',
    '.jc-seg button{appearance:none;border:0;cursor:pointer;font-family:inherit;font-weight:600;',
    ' font-size:12.5px;padding:6px 13px;border-radius:999px;background:transparent;',
    ' color:var(--mu,#63768E);white-space:nowrap;transition:.14s}',
    '.jc-seg button[aria-pressed="true"]{background:var(--ink,#08213E);color:#fff;',
    ' box-shadow:0 1px 2px rgba(8,33,62,.05)}',
    '.jc-seg button:hover:not([aria-pressed="true"]){color:var(--ink,#08213E)}',
    '.jc-seg.flags button{font-size:15px;padding:5px 10px;line-height:1}',
    '.jc-seg button:focus-visible{outline:2px solid var(--bl,#0B5CD5);outline-offset:2px}'
  ].join("");

  /* --------------------------------------------------------------- estado */
  function readLang() {
    try {
      var v = localStorage.getItem("jc-lang");
      if (v === "en" || v === "es" || v === "pt") return v;
    } catch (e) {}
    return "en";
  }

  function saveLang(v) {
    try { localStorage.setItem("jc-lang", v); } catch (e) {}
  }

  var lang = readLang();
  var lens = "eng";
  var wantLens = MOUNT.dataset.lens === "true";

  var title = MOUNT.dataset.title || "";
  var subs = {
    en: MOUNT.dataset.subEn || "",
    es: MOUNT.dataset.subEs || MOUNT.dataset.subEn || "",
    pt: MOUNT.dataset.subPt || MOUNT.dataset.subEn || ""
  };

  /* ---------------------------------------------------------------- build */
  var style = document.createElement("style");
  style.textContent = CSS;
  document.head.appendChild(style);

  function el(tag, attrs, html) {
    var n = document.createElement(tag);
    if (attrs) for (var k in attrs) n.setAttribute(k, attrs[k]);
    if (html != null) n.innerHTML = html;
    return n;
  }

  var LOGO =
    '<svg width="26" height="22" viewBox="0 0 26 22" aria-hidden="true">' +
    '<g stroke-linecap="round">' +
    '<line x1="3" y1="15" x2="3" y2="9" stroke="#00BCEB" stroke-width="3"/>' +
    '<line x1="8" y1="15" x2="8" y2="5" stroke="#0B5CD5" stroke-width="3"/>' +
    '<line x1="13" y1="15" x2="13" y2="2" stroke="#08213E" stroke-width="3"/>' +
    '<line x1="18" y1="15" x2="18" y2="5" stroke="#0B5CD5" stroke-width="3"/>' +
    '<line x1="23" y1="15" x2="23" y2="9" stroke="#00BCEB" stroke-width="3"/>' +
    '</g></svg>';

  MOUNT.innerHTML =
    '<nav class="jc-nav"><div class="jc-nav-in">' +
      '<a href="/" class="jc-brand"><b>Josimar Caitano</b><i>\u3058\u3087\u3057\u307E\u308B</i></a>' +
      '<div class="jc-links" id="jc-links"></div>' +
      '<a href="/" class="jc-home" id="jc-home">\u2190 Home</a>' +
    '</div></nav>' +
    (title
      ? '<div class="jc-tb"><div class="jc-tb-in">' +
          '<span class="jc-badge">' + LOGO +
            '<span id="jc-title"></span> <span class="s" id="jc-sub"></span>' +
          '</span>' +
          '<span class="jc-sp"></span>' +
          '<div class="jc-seg flags" id="jc-flags" role="group" aria-label="Language"></div>' +
          (wantLens
            ? '<div class="jc-seg" id="jc-lens" role="group" aria-label="Lens"></div>'
            : '') +
        '</div></div>'
      : '');

  /* flags */
  var flagsBox = document.getElementById("jc-flags");
  if (flagsBox) {
    LANGS.forEach(function (L) {
      var b = el("button", { type: "button", title: L.label, "aria-label": L.label });
      b.dataset.lang = L.code;
      b.textContent = L.flag;
      b.addEventListener("click", function () { setLang(L.code); });
      flagsBox.appendChild(b);
    });
  }

  /* lens */
  var lensBox = document.getElementById("jc-lens");
  if (lensBox) {
    ["eng", "board"].forEach(function (k) {
      var b = el("button", { type: "button" });
      b.dataset.lens = k;
      b.addEventListener("click", function () { setLens(k); });
      lensBox.appendChild(b);
    });
  }

  /* --------------------------------------------------------------- render */
  function render() {
    var links = document.getElementById("jc-links");
    links.innerHTML = "";
    NAV.forEach(function (item) {
      var a = el("a", { href: "/#" + item[0] });
      a.textContent = item[1][lang];
      links.appendChild(a);
    });

    document.getElementById("jc-home").textContent = "\u2190 " + HOME[lang];

    var tEl = document.getElementById("jc-title");
    if (tEl) {
      tEl.textContent = title;
      document.getElementById("jc-sub").textContent = subs[lang];
    }

    if (flagsBox) {
      Array.prototype.forEach.call(flagsBox.children, function (b) {
        b.setAttribute("aria-pressed", String(b.dataset.lang === lang));
      });
    }
    if (lensBox) {
      Array.prototype.forEach.call(lensBox.children, function (b) {
        b.textContent = LENS[b.dataset.lens][lang];
        b.setAttribute("aria-pressed", String(b.dataset.lens === lens));
      });
    }
  }

  /* --------------------------------------------------------------- acoes */
  function setLang(v) {
    lang = v;
    saveLang(v);
    document.body.dataset.lang = v;
    document.documentElement.lang = v === "pt" ? "pt-BR" : v;
    render();
    window.dispatchEvent(new CustomEvent("jc:lang", { detail: { lang: v } }));
  }

  function setLens(v) {
    lens = v;
    document.body.dataset.lens = v;
    render();
    window.dispatchEvent(new CustomEvent("jc:lens", { detail: { lens: v } }));
  }

  /* expoe para a pagina consultar o estado inicial */
  window.jcHeader = {
    get lang() { return lang; },
    get lens() { return lens; },
    setLang: setLang,
    setLens: setLens
  };

  /* boot */
  document.body.dataset.lang = lang;
  document.documentElement.lang = lang === "pt" ? "pt-BR" : lang;
  if (wantLens) document.body.dataset.lens = lens;
  render();

  /* dispara uma vez para a pagina aplicar o idioma inicial */
  window.dispatchEvent(new CustomEvent("jc:lang", { detail: { lang: lang } }));
  if (wantLens) {
    window.dispatchEvent(new CustomEvent("jc:lens", { detail: { lens: lens } }));
  }
})();
