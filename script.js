/* =========================================================
   SOZO Tecnología: interacción (página principal y páginas
   de cada aplicación)
   ---------------------------------------------------------
   CONFIGURACIÓN: cambia aquí el número de WhatsApp (con código
   de país 502, sin espacios ni signos) y el correo corporativo.
   ========================================================= */
const CONFIG = {
  whatsapp: "50256907669",
  whatsappLabel: "+502 5690 7669",
  email: "sazosolucionesdigitales@gmail.com",
};

document.documentElement.classList.add("js");
const $ = (sel, root = document) => root.querySelector(sel);
const $$ = (sel, root = document) => [...root.querySelectorAll(sel)];
const reduceMotion = matchMedia("(prefers-reduced-motion: reduce)").matches;

/* Nombres de las aplicaciones (para mensajes y recomendaciones) */
const APPS = {
  inventario: { name: "SOZO Inventario", url: "aplicaciones/inventario/" },
  gestion: { name: "SOZO Gestión", url: "aplicaciones/gestion/" },
  reservas: { name: "SOZO Reservas", url: "aplicaciones/reservas/" },
};

/* ---------- Enlaces de contacto ---------- */
const waUrl = (text) => `https://wa.me/${CONFIG.whatsapp}${text ? `?text=${encodeURIComponent(text)}` : ""}`;
const mailUrl = (subject, body) => `mailto:${CONFIG.email}?subject=${encodeURIComponent(subject || "")}&body=${encodeURIComponent(body || "")}`;

const pageApp = document.body.dataset.app && APPS[document.body.dataset.app];
const waDefault = pageApp
  ? `Hola, SOZO Tecnología. Me interesa ${pageApp.name} y quisiera más información.`
  : "Hola, SOZO Tecnología. Me gustaría recibir información sobre sus aplicaciones web.";
$$(".js-wa, #wa-link").forEach((a) => (a.href = waUrl(waDefault)));
$$(".js-mail, #mail-link").forEach((a) => (a.href = mailUrl(pageApp ? `Información sobre ${pageApp.name}` : "Información sobre aplicaciones web")));
if ($("#wa-label")) $("#wa-label").textContent = CONFIG.whatsappLabel;
if ($("#mail-label")) $("#mail-label").textContent = CONFIG.email;
if ($("#year")) $("#year").textContent = new Date().getFullYear();

/* ---------- Encabezado y menú móvil ---------- */
const header = $(".site-header");
const nav = $("#main-nav");
const toggle = $(".nav-toggle");

const onScroll = () => header.classList.toggle("scrolled", window.scrollY > 8);
window.addEventListener("scroll", onScroll, { passive: true });
onScroll();

function setMenu(open) {
  if (!nav || !toggle) return;
  nav.classList.toggle("open", open);
  toggle.setAttribute("aria-expanded", String(open));
  toggle.setAttribute("aria-label", open ? "Cerrar menú" : "Abrir menú");
  $("use", toggle).setAttribute("href", open ? "#i-x" : "#i-menu");
}
if (toggle) toggle.addEventListener("click", () => setMenu(!nav.classList.contains("open")));
if (nav) nav.addEventListener("click", (e) => { if (e.target.closest("a")) setMenu(false); });
document.addEventListener("keydown", (e) => { if (e.key === "Escape" && nav && nav.classList.contains("open")) { setMenu(false); toggle.focus(); } });

/* Sección activa en el menú (solo enlaces internos de esta página) */
const navLinks = $$("#main-nav ul a").filter((a) => a.getAttribute("href").startsWith("#"));
const sections = navLinks.map((a) => document.getElementById(a.getAttribute("href").slice(1))).filter(Boolean);
if (sections.length && "IntersectionObserver" in window) {
  const spy = new IntersectionObserver((entries) => {
    entries.forEach((en) => {
      if (!en.isIntersecting) return;
      navLinks.forEach((a) => {
        const on = a.getAttribute("href") === `#${en.target.id}`;
        a.classList.toggle("active", on);
        if (on) a.setAttribute("aria-current", "true"); else a.removeAttribute("aria-current");
      });
    });
  }, { rootMargin: "-45% 0px -50% 0px" });
  sections.forEach((s) => spy.observe(s));
}

/* ---------- Aparición al desplazarse ---------- */
const reveals = $$(".reveal");
if ("IntersectionObserver" in window && !reduceMotion) {
  const io = new IntersectionObserver((entries) => {
    entries.forEach((en) => {
      if (en.isIntersecting) { en.target.classList.add("in"); io.unobserve(en.target); }
    });
  }, { rootMargin: "0px 0px -8% 0px", threshold: 0.08 });
  reveals.forEach((el) => {
    const siblings = $$(":scope > .reveal", el.parentElement);
    if (siblings.length > 1) el.style.transitionDelay = `${siblings.indexOf(el) * 70}ms`;
    io.observe(el);
  });
} else {
  reveals.forEach((el) => el.classList.add("in"));
}

/* ---------- Soluciones por necesidad (página principal) ---------- */
const NEEDS = {
  inventarios: { app: "inventario", text: "Registra productos, controla entradas y salidas y recibe alertas antes de quedarte sin existencias.", list: ["Existencias en tiempo real", "Alertas de existencias bajas", "Historial de movimientos"] },
  ventas: { app: "gestion", text: "Lleva el registro de tus ventas por cliente y consulta reportes para saber qué y a quién vendes más.", list: ["Historial de operaciones por cliente", "Reportes de ventas", "Usuarios por vendedor"] },
  clientes: { app: "gestion", text: "Toda la información de tus clientes en un solo lugar, con su historial de pedidos y solicitudes.", list: ["Ficha de cada cliente", "Búsqueda y filtros", "Historial completo"] },
  pedidos: { app: "gestion", text: "Sigue cada pedido desde que entra hasta que se entrega, con estados claros para todo tu equipo.", list: ["Estados de pedidos", "Seguimiento de solicitudes", "Reportes de pedidos"] },
  citas: { app: "reservas", text: "Organiza tu agenda, controla la disponibilidad y confirma las reservas de tus clientes.", list: ["Agenda de citas", "Configuración de horarios", "Confirmación de reservas"] },
  operaciones: { app: null, title: "Desarrollo a la medida", text: "Cada operación es distinta. Diseñamos una aplicación con los módulos, usuarios y reportes que tu proceso necesita.", list: ["Análisis de tu proceso", "Módulos según tu operación", "Roles y permisos"] },
  gastos: { app: null, title: "Control de gastos", text: "Registra gastos por categoría, adjunta comprobantes y compara mes a mes. Implementación desde Q2,000.", list: ["Gastos por categoría", "Reportes mensuales", "Usuarios con permisos"] },
  informacion: { app: null, title: "Desarrollo a la medida", text: "Centraliza documentos, registros y datos de tu empresa en una plataforma segura y fácil de consultar.", list: ["Base de datos propia", "Búsqueda de información", "Respaldos y seguridad"] },
};

const needButtons = $$(".need");
const result = $(".need-result");

function showNeed(key) {
  const n = NEEDS[key];
  const app = n.app ? APPS[n.app] : null;
  needButtons.forEach((b) => {
    const on = b.dataset.need === key;
    b.setAttribute("aria-checked", String(on));
    b.tabIndex = on ? 0 : -1;
  });
  $("#need-title").textContent = app ? app.name : n.title;
  $("#need-text").textContent = n.text;
  $("#need-list").innerHTML = n.list.map((t) => `<li>${t}</li>`).join("");
  const more = $("#need-more");
  const cta = $("#need-cta");
  if (app) {
    more.hidden = false;
    more.href = app.url;
    cta.textContent = "Solicitar demostración";
    cta.dataset.request = "demo";
    cta.dataset.topic = app.name;
  } else {
    more.hidden = true;
    cta.textContent = "Solicitar cotización";
    cta.dataset.request = "cotizacion";
    cta.dataset.topic = n.title;
  }
  result.classList.remove("swap");
  void result.offsetWidth;
  result.classList.add("swap");
}
if (needButtons.length && result) {
  needButtons.forEach((b, i) => {
    b.addEventListener("click", () => showNeed(b.dataset.need));
    b.addEventListener("keydown", (e) => {
      const keys = { ArrowRight: 1, ArrowDown: 1, ArrowLeft: -1, ArrowUp: -1 };
      if (!(e.key in keys)) return;
      e.preventDefault();
      const next = needButtons[(i + keys[e.key] + needButtons.length) % needButtons.length];
      next.focus();
      showNeed(next.dataset.need);
    });
  });
  showNeed("inventarios");
}

/* ---------- Formulario de contacto (página principal) ---------- */
const form = $("#contact-form");

if (form) {
  const needField = $("#f-necesidad");

  const prefill = (type, topic) => {
    const radio = $(`input[name="tipo"][value="${type}"]`, form);
    if (radio) radio.checked = true;
    if (topic && !needField.value.trim()) {
      needField.value = type === "demo" ? `Me interesa ver una demostración de ${topic}.` : `Me interesa una cotización: ${topic}.`;
    }
  };

  // Llegada desde una página de aplicación: ?solicitud=demo&app=inventario#contacto
  const params = new URLSearchParams(location.search);
  if (params.has("solicitud")) {
    const app = APPS[params.get("app")];
    prefill(params.get("solicitud"), app ? app.name : "");
  }

  document.addEventListener("click", (e) => {
    const link = e.target.closest("[data-request]");
    if (!link || link.getAttribute("href") !== "#contacto") return;
    let topic = link.dataset.topic || "";
    if (link.dataset.plan) topic = `Plan ${link.dataset.plan}`;
    prefill(link.dataset.request, topic);

    e.preventDefault();
    setMenu(false);
    const target = window.innerWidth < 900 ? form : $("#contacto");
    requestAnimationFrame(() => {
      target.scrollIntoView({ behavior: reduceMotion ? "auto" : "smooth" });
      history.replaceState(null, "", "#contacto");
    });
    setTimeout(() => $("#f-nombre").focus({ preventScroll: true }), 700);
  });

  const fields = {
    nombre: { el: $("#f-nombre"), err: $("#e-nombre"), ok: (v) => v.length >= 2 },
    negocio: { el: $("#f-negocio"), err: $("#e-negocio"), ok: (v) => v.length >= 2 },
    contacto: {
      el: $("#f-contacto"), err: $("#e-contacto"),
      ok: (v) => /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(v) || /^(\+?502)?\s?\d{4}[\s-]?\d{4}$/.test(v),
    },
    necesidad: { el: needField, err: $("#e-necesidad"), ok: (v) => v.length >= 5 },
  };

  const check = (name) => {
    const f = fields[name];
    const valid = f.ok(f.el.value.trim());
    f.el.setAttribute("aria-invalid", String(!valid));
    f.err.hidden = valid;
    const describedBy = [name === "contacto" ? "h-contacto" : "", valid ? "" : f.err.id].filter(Boolean).join(" ");
    if (describedBy) f.el.setAttribute("aria-describedby", describedBy); else f.el.removeAttribute("aria-describedby");
    return valid;
  };
  Object.keys(fields).forEach((name) => {
    fields[name].el.addEventListener("blur", () => { if (fields[name].el.value.trim()) check(name); });
    fields[name].el.addEventListener("input", () => { if (fields[name].el.getAttribute("aria-invalid") === "true") check(name); });
  });

  const TYPE_LABEL = { demo: "Solicitud de demostración", cotizacion: "Solicitud de cotización", consulta: "Consulta" };

  const buildMessage = () => {
    const tipo = $('input[name="tipo"]:checked', form).value;
    const v = (k) => fields[k].el.value.trim();
    return {
      subject: `${TYPE_LABEL[tipo]}: ${v("negocio")}`,
      body: `Hola, SOZO Tecnología.\n\n${TYPE_LABEL[tipo]}\nNombre: ${v("nombre")}\nNegocio: ${v("negocio")}\nContacto: ${v("contacto")}\n\nNecesidad:\n${v("necesidad")}`,
    };
  };

  const validateAll = () => {
    if ($("#f-web", form).value) return false; // spam
    const results = Object.keys(fields).map(check);
    const firstBad = Object.keys(fields).find((k, i) => !results[i]);
    if (firstBad) { fields[firstBad].el.focus(); return false; }
    return true;
  };

  const status = $("#form-status");
  form.addEventListener("submit", (e) => {
    e.preventDefault();
    if (!validateAll()) return;
    window.open(waUrl(buildMessage().body), "_blank", "noopener");
    status.textContent = "Abrimos WhatsApp con tu mensaje listo. Solo presiona enviar.";
  });
  $("#send-mail").addEventListener("click", () => {
    if (!validateAll()) return;
    const m = buildMessage();
    window.location.href = mailUrl(m.subject, m.body);
    status.textContent = "Abrimos tu correo con el mensaje listo para enviar.";
  });
}
