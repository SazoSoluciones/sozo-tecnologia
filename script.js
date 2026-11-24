/* =========================================================
   SOZO Tecnología: interacción
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

/* ---------- Datos de las aplicaciones (fichas) ---------- */
const APPS = {
  inventario: {
    name: "SOZO Inventario",
    icon: "i-package",
    desc: "Aplicación para el registro, control y seguimiento de productos y existencias.",
    need: "Evita faltantes, pérdidas y conteos manuales. Sabes en todo momento qué tienes, qué entra, qué sale y qué debes reabastecer.",
    for: ["Tiendas", "Comercios", "Distribuidores", "Pequeñas empresas", "Negocios de productos"],
    features: ["Registro de productos", "Clasificación por categorías", "Control de existencias", "Entradas y salidas", "Historial de movimientos", "Alertas de existencias bajas", "Reportes de inventario", "Gestión de usuarios", "Control de permisos"],
    impl: "Q3,500 – Q6,500",
  },
  gestion: {
    name: "SOZO Gestión",
    icon: "i-users",
    desc: "Centraliza la información de tus clientes y facilita el seguimiento de pedidos y operaciones comerciales.",
    need: "Deja de buscar pedidos en chats y libretas. Cada cliente tiene su historial y cada pedido su estado, a la vista de todo tu equipo.",
    for: ["Comercios", "Empresas de servicios", "Emprendedores", "Distribuidores", "Pedidos recurrentes"],
    features: ["Registro de clientes", "Historial de operaciones", "Registro de pedidos", "Estados de pedidos", "Seguimiento de solicitudes", "Búsqueda y filtros", "Reportes", "Administración de usuarios"],
    impl: "Q2,500 – Q5,000",
  },
  reservas: {
    name: "SOZO Reservas",
    icon: "i-calendar",
    desc: "Facilita la administración de citas, horarios y disponibilidad de tu negocio.",
    need: "Termina con las citas duplicadas y los olvidos. Tu agenda se mantiene ordenada y tus clientes reciben confirmación de su reserva.",
    for: ["Clínicas y consultorios", "Profesionales independientes", "Centros de servicios", "Academias"],
    features: ["Registro de servicios", "Configuración de horarios", "Agenda de citas", "Registro de clientes", "Confirmación de reservas", "Control de disponibilidad", "Historial de citas", "Reportes", "Gestión de usuarios"],
    impl: "Q2,000 – Q4,500",
  },
};

/* ---------- Necesidades → recomendación ---------- */
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

/* ---------- Enlaces de contacto ---------- */
const waUrl = (text) => `https://wa.me/${CONFIG.whatsapp}${text ? `?text=${encodeURIComponent(text)}` : ""}`;
const mailUrl = (subject, body) => `mailto:${CONFIG.email}?subject=${encodeURIComponent(subject || "")}&body=${encodeURIComponent(body || "")}`;

const waDefault = "Hola, SOZO Tecnología. Me gustaría recibir información sobre sus aplicaciones web.";
document.querySelectorAll(".js-wa, #wa-link").forEach((a) => (a.href = waUrl(waDefault)));
document.querySelectorAll(".js-mail, #mail-link").forEach((a) => (a.href = mailUrl("Información sobre aplicaciones web")));
document.getElementById("wa-label").textContent = CONFIG.whatsappLabel;
document.getElementById("mail-label").textContent = CONFIG.email;
document.getElementById("year").textContent = new Date().getFullYear();

/* ---------- Encabezado y menú móvil ---------- */
const header = document.querySelector(".site-header");
const nav = document.getElementById("main-nav");
const toggle = document.querySelector(".nav-toggle");

const onScroll = () => header.classList.toggle("scrolled", window.scrollY > 8);
window.addEventListener("scroll", onScroll, { passive: true });
onScroll();

function setMenu(open) {
  nav.classList.toggle("open", open);
  toggle.setAttribute("aria-expanded", String(open));
  toggle.setAttribute("aria-label", open ? "Cerrar menú" : "Abrir menú");
  toggle.querySelector("use").setAttribute("href", open ? "#i-x" : "#i-menu");
}
toggle.addEventListener("click", () => setMenu(!nav.classList.contains("open")));
nav.addEventListener("click", (e) => { if (e.target.closest("a")) setMenu(false); });
document.addEventListener("keydown", (e) => { if (e.key === "Escape" && nav.classList.contains("open")) { setMenu(false); toggle.focus(); } });

/* Sección activa en el menú */
const navLinks = [...nav.querySelectorAll("ul a")];
const sections = navLinks.map((a) => document.querySelector(a.getAttribute("href"))).filter(Boolean);
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

/* ---------- Aparición al desplazarse ---------- */
const reveals = document.querySelectorAll(".reveal");
if ("IntersectionObserver" in window && !matchMedia("(prefers-reduced-motion: reduce)").matches) {
  const io = new IntersectionObserver((entries) => {
    entries.forEach((en) => {
      if (en.isIntersecting) { en.target.classList.add("in"); io.unobserve(en.target); }
    });
  }, { rootMargin: "0px 0px -8% 0px", threshold: 0.08 });
  reveals.forEach((el, i) => {
    const siblings = el.parentElement.querySelectorAll(":scope > .reveal");
    if (siblings.length > 1) el.style.transitionDelay = `${[...siblings].indexOf(el) * 70}ms`;
    io.observe(el);
  });
} else {
  reveals.forEach((el) => el.classList.add("in"));
}

/* ---------- Ficha de aplicación ---------- */
const dialog = document.getElementById("app-dialog");
let currentApp = null;
let lastFocus = null;

function openApp(key) {
  const app = APPS[key];
  if (!app) return;
  currentApp = key;
  lastFocus = document.activeElement;
  dialog.querySelector("#d-title").textContent = app.name;
  dialog.querySelector("#d-icon use").setAttribute("href", `#${app.icon}`);
  dialog.querySelector("#d-desc").textContent = app.desc;
  dialog.querySelector("#d-need").textContent = app.need;
  dialog.querySelector("#d-for").innerHTML = app.for.map((t) => `<li>${t}</li>`).join("");
  dialog.querySelector("#d-features").innerHTML = app.features.map((t) => `<li>${t}</li>`).join("");
  dialog.querySelector("#d-impl").textContent = app.impl;
  dialog.showModal();
  document.body.classList.add("dialog-open");
}
function closeApp() { dialog.close(); }
dialog.addEventListener("close", () => {
  document.body.classList.remove("dialog-open");
  if (lastFocus) lastFocus.focus({ preventScroll: true });
});
dialog.querySelector(".d-close").addEventListener("click", closeApp);
dialog.addEventListener("click", (e) => { if (e.target === dialog) closeApp(); });

document.addEventListener("click", (e) => {
  const trigger = e.target.closest("[data-app]");
  if (trigger) openApp(trigger.dataset.app);
});

/* ---------- Soluciones por necesidad ---------- */
const needButtons = [...document.querySelectorAll(".need")];
const result = document.querySelector(".need-result");

function showNeed(key) {
  const n = NEEDS[key];
  const app = n.app ? APPS[n.app] : null;
  needButtons.forEach((b) => {
    const on = b.dataset.need === key;
    b.setAttribute("aria-checked", String(on));
    b.tabIndex = on ? 0 : -1;
  });
  document.getElementById("need-title").textContent = app ? app.name : n.title;
  document.getElementById("need-text").textContent = n.text;
  document.getElementById("need-list").innerHTML = n.list.map((t) => `<li>${t}</li>`).join("");
  const more = document.getElementById("need-more");
  const cta = document.getElementById("need-cta");
  if (app) {
    more.hidden = false;
    more.dataset.app = n.app;
    cta.textContent = "Solicitar demostración";
    cta.dataset.request = "demo";
    cta.dataset.topic = app.name;
  } else {
    more.hidden = true;
    delete more.dataset.app;
    cta.textContent = "Solicitar cotización";
    cta.dataset.request = "cotizacion";
    cta.dataset.topic = n.title;
  }
  result.classList.remove("swap");
  void result.offsetWidth;
  result.classList.add("swap");
}
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

/* ---------- Botones que preseleccionan el formulario ---------- */
const form = document.getElementById("contact-form");
const needField = document.getElementById("f-necesidad");

document.addEventListener("click", (e) => {
  const link = e.target.closest("[data-request]");
  if (!link) return;
  const type = link.dataset.request;
  const radio = form.querySelector(`input[name="tipo"][value="${type}"]`);
  if (radio) radio.checked = true;

  let topic = link.dataset.topic || "";
  if (link.dataset.plan) topic = `Plan ${link.dataset.plan}`;
  if (link.closest("#app-dialog") && currentApp) topic = APPS[currentApp].name;
  if (topic && !needField.value.trim()) {
    needField.value = type === "demo" ? `Me interesa ver una demostración de ${topic}.` : `Me interesa una cotización: ${topic}.`;
  }
  e.preventDefault();
  if (dialog.open) { lastFocus = null; closeApp(); }
  setMenu(false);
  const target = window.innerWidth < 900 ? form : document.getElementById("contacto");
  requestAnimationFrame(() => {
    target.scrollIntoView({ behavior: matchMedia("(prefers-reduced-motion: reduce)").matches ? "auto" : "smooth" });
    history.replaceState(null, "", "#contacto");
  });
  setTimeout(() => document.getElementById("f-nombre").focus({ preventScroll: true }), 700);
});

/* ---------- Formulario ---------- */
const fields = {
  nombre: { el: document.getElementById("f-nombre"), err: document.getElementById("e-nombre"), ok: (v) => v.length >= 2 },
  negocio: { el: document.getElementById("f-negocio"), err: document.getElementById("e-negocio"), ok: (v) => v.length >= 2 },
  contacto: {
    el: document.getElementById("f-contacto"), err: document.getElementById("e-contacto"),
    ok: (v) => /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(v) || /^(\+?502)?\s?\d{4}[\s-]?\d{4}$/.test(v),
  },
  necesidad: { el: needField, err: document.getElementById("e-necesidad"), ok: (v) => v.length >= 5 },
};

function check(name) {
  const f = fields[name];
  const valid = f.ok(f.el.value.trim());
  f.el.setAttribute("aria-invalid", String(!valid));
  f.err.hidden = valid;
  const describedBy = [name === "contacto" ? "h-contacto" : "", valid ? "" : f.err.id].filter(Boolean).join(" ");
  if (describedBy) f.el.setAttribute("aria-describedby", describedBy); else f.el.removeAttribute("aria-describedby");
  return valid;
}
Object.keys(fields).forEach((name) => {
  fields[name].el.addEventListener("blur", () => { if (fields[name].el.value.trim()) check(name); });
  fields[name].el.addEventListener("input", () => { if (fields[name].el.getAttribute("aria-invalid") === "true") check(name); });
});

const TYPE_LABEL = { demo: "Solicitud de demostración", cotizacion: "Solicitud de cotización", consulta: "Consulta" };

function buildMessage() {
  const tipo = form.querySelector('input[name="tipo"]:checked').value;
  const v = (k) => fields[k].el.value.trim();
  return {
    subject: `${TYPE_LABEL[tipo]}: ${v("negocio")}`,
    body: `Hola, SOZO Tecnología.\n\n${TYPE_LABEL[tipo]}\nNombre: ${v("nombre")}\nNegocio: ${v("negocio")}\nContacto: ${v("contacto")}\n\nNecesidad:\n${v("necesidad")}`,
  };
}

function validateAll() {
  if (form.querySelector("#f-web").value) return false; // spam
  const results = Object.keys(fields).map(check);
  const firstBad = Object.keys(fields).find((k, i) => !results[i]);
  if (firstBad) { fields[firstBad].el.focus(); return false; }
  return true;
}

const status = document.getElementById("form-status");
form.addEventListener("submit", (e) => {
  e.preventDefault();
  if (!validateAll()) return;
  const m = buildMessage();
  window.open(waUrl(m.body), "_blank", "noopener");
  status.textContent = "Abrimos WhatsApp con tu mensaje listo. Solo presiona enviar.";
});
document.getElementById("send-mail").addEventListener("click", () => {
  if (!validateAll()) return;
  const m = buildMessage();
  window.location.href = mailUrl(m.subject, m.body);
  status.textContent = "Abrimos tu correo con el mensaje listo para enviar.";
});
