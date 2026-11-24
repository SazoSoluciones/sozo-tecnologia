"""
Genera las páginas de cada aplicación en /aplicaciones/<clave>/index.html

Uso (desde la carpeta del proyecto):
    python _build/generar_paginas.py

Edita el contenido en el diccionario APPS y vuelve a ejecutar.
La carpeta _build no se publica en GitHub Pages.
"""
import html
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://sazosoluciones.github.io/sozo-tecnologia/"
BASE = "../../"
PHONE = "+502 5690 7669"
EMAIL = "sazosolucionesdigitales@gmail.com"

# --------------------------------------------------------------------------
# Contenido de cada aplicación
# --------------------------------------------------------------------------
APPS = {
    "inventario": {
        "name": "SOZO Inventario",
        "icon": "i-package",
        "subtitle": "Sistema de control de inventarios para negocios en Guatemala",
        "title": "SOZO Inventario | Sistema de control de inventarios en Guatemala",
        "description": "Controla productos, existencias, entradas y salidas desde el navegador, con alertas de existencias bajas y reportes. Implementación desde Q3,500 en Guatemala.",
        "lead": "Registra tus productos, controla entradas y salidas y recibe alertas antes de quedarte sin existencias. Todo desde el navegador, en la computadora, la tableta o el teléfono.",
        "impl": ("Q3,500", "Q6,500", 3500, 6500),
        "pains_title": "Del cuaderno y el Excel a un inventario que cuadra",
        "pains": [
            ("Cuentas el inventario a mano y los números nunca cuadran.", "Cada entrada y salida queda registrada y las existencias se actualizan al momento."),
            ("Te enteras de que un producto se acabó cuando un cliente lo pide.", "Recibes una alerta cuando un producto llega a su mínimo, a tiempo para reabastecer."),
            ("No sabes quién movió qué ni cuándo.", "El historial de movimientos muestra cada cambio con su fecha y el usuario que lo hizo."),
        ],
        "features": [
            ("i-package", "Registro de productos", "Código, nombre, precio, unidad de medida y existencia de cada producto."),
            ("i-layers", "Clasificación por categorías", "Agrupa tus productos para encontrarlos y analizarlos más rápido."),
            ("i-database", "Control de existencias", "Existencias actualizadas con cada entrada y cada salida."),
            ("i-trending", "Entradas y salidas", "Registra compras, ventas, devoluciones y ajustes de inventario."),
            ("i-clock", "Historial de movimientos", "Consulta qué cambió, cuándo y quién lo hizo."),
            ("i-zap", "Alertas de existencias bajas", "Define un mínimo por producto y la aplicación te avisa al alcanzarlo."),
            ("i-chart", "Reportes de inventario", "Existencias, movimientos y productos con más rotación."),
            ("i-users", "Gestión de usuarios", "Cada persona de tu equipo entra con su propio usuario."),
            ("i-shield", "Control de permisos", "Decide quién puede consultar, registrar o modificar información."),
        ],
        "audience": [
            ("Tiendas", "Abarroterías, ferreterías, librerías y tiendas de barrio con muchos productos."),
            ("Comercios", "Negocios con mostrador y bodega que necesitan saber qué hay disponible."),
            ("Distribuidores", "Empresas que reciben y despachan mercadería todos los días."),
            ("Pequeñas empresas", "Negocios que hoy llevan el inventario en cuadernos o en Excel."),
            ("Negocios de productos", "Emprendimientos que venden productos propios o de terceros."),
        ],
        "faq": [
            ("¿Necesito instalar algún programa?", "No. SOZO Inventario funciona en el navegador. Solo necesitas una computadora, tableta o teléfono con conexión a internet."),
            ("¿Puedo usarla desde el celular?", "Sí. La aplicación se adapta a la pantalla del teléfono, así puedes consultar existencias o registrar movimientos desde la bodega o el mostrador."),
            ("Ya tengo mis productos en Excel, ¿tengo que escribirlos de nuevo?", "No es necesario. Ofrecemos el servicio de carga inicial de datos, desde Q500, para que empieces con tu inventario completo desde el primer día."),
            ("¿Cuántos usuarios puedo tener?", "Depende del plan. El plan Básico incluye un usuario administrador y los planes Estándar y Profesional permiten varios usuarios, cada uno con sus permisos."),
            ("¿Cómo se protege la información de mi negocio?", "Cada persona entra con su propio usuario y contraseña, los permisos limitan lo que cada quien puede hacer y la información cuenta con copias de seguridad."),
            ("¿Se puede adaptar a la forma en que trabajo?", "Sí. Podemos agregar campos, reportes o módulos adicionales como personalización, con precios desde Q500 según el alcance."),
        ],
        "mock": """
<div class="app-shot lg shot-inventory" aria-hidden="true">
  <div class="s-head"><b>Inventario · Productos</b><span class="s-btn">+ Nuevo producto</span></div>
  <div class="s-chips"><span><b>248</b> productos</span><span><b>12</b> categorías</span><span class="warn"><b>4</b> existencias bajas</span></div>
  <div class="s-table">
    <div class="s-row s-th"><span>Producto</span><span>Categoría</span><span>Exist.</span></div>
    <div class="s-row"><span>Café molido 1 lb</span><span>Abarrotes</span><span class="pill ok">48</span></div>
    <div class="s-row"><span>Aceite 900 ml</span><span>Abarrotes</span><span class="pill low">5</span></div>
    <div class="s-row"><span>Jabón líquido</span><span>Limpieza</span><span class="pill ok">27</span></div>
    <div class="s-row"><span>Papel toalla</span><span>Limpieza</span><span class="pill mid">12</span></div>
    <div class="s-row"><span>Arroz 5 lb</span><span>Abarrotes</span><span class="pill ok">36</span></div>
    <div class="s-row"><span>Cloro 1 galón</span><span>Limpieza</span><span class="pill low">3</span></div>
  </div>
</div>""",
    },
    "gestion": {
        "name": "SOZO Gestión",
        "icon": "i-users",
        "subtitle": "Gestión de clientes y control de pedidos para negocios en Guatemala",
        "title": "SOZO Gestión | Control de clientes y pedidos en Guatemala",
        "description": "Centraliza la información de tus clientes y da seguimiento a cada pedido, desde que entra hasta que se entrega. Implementación desde Q2,500 en Guatemala.",
        "lead": "Toda la información de tus clientes en un solo lugar y cada pedido con su estado, a la vista de todo tu equipo. Sin pedidos perdidos entre chats, llamadas y libretas.",
        "impl": ("Q2,500", "Q5,000", 2500, 5000),
        "pains_title": "Cada cliente y cada pedido, en un solo lugar",
        "pains": [
            ("Los pedidos llegan por WhatsApp, llamadas y en persona, y alguno siempre se pierde.", "Todos los pedidos se registran en un solo lugar, sin importar por dónde llegaron."),
            ("Para saber qué ha comprado un cliente tienes que buscar en chats y libretas.", "Cada cliente tiene su ficha con el historial completo de pedidos y operaciones."),
            ("Nadie sabe con certeza en qué estado está un pedido.", "Cada pedido tiene un estado (nuevo, en proceso, entregado) que todo el equipo puede consultar."),
        ],
        "features": [
            ("i-users", "Registro de clientes", "Datos de contacto, dirección y notas de cada cliente."),
            ("i-clock", "Historial de operaciones", "Todo lo que un cliente ha pedido o solicitado, en orden."),
            ("i-cart", "Registro de pedidos", "Productos o servicios, cantidades, montos y fecha de entrega."),
            ("i-clipboard", "Estados de pedidos", "Nuevo, en proceso, listo o entregado: siempre sabes en qué va."),
            ("i-chat", "Seguimiento de solicitudes", "Consultas y requerimientos de clientes con su respuesta."),
            ("i-sliders", "Búsqueda y filtros", "Encuentra un cliente o un pedido en segundos."),
            ("i-chart", "Reportes", "Pedidos por periodo, por estado y por cliente."),
            ("i-shield", "Administración de usuarios", "Accesos y permisos para cada persona del equipo."),
        ],
        "audience": [
            ("Comercios", "Negocios que toman pedidos por encargo o para entrega."),
            ("Empresas de servicios", "Talleres, imprentas, lavanderías y negocios que atienden solicitudes."),
            ("Emprendedores", "Negocios que venden por redes sociales y necesitan orden."),
            ("Distribuidores", "Empresas que surten a otros negocios con pedidos frecuentes."),
            ("Negocios con pedidos recurrentes", "Clientes que compran cada semana o cada mes."),
        ],
        "faq": [
            ("¿Puedo registrar pedidos que me llegan por WhatsApp?", "Sí. Cualquier persona de tu equipo registra el pedido en la aplicación, sin importar si llegó por WhatsApp, por teléfono o en persona. Así todos quedan en un solo lugar."),
            ("¿Sirve si vendo servicios y no productos?", "Sí. Puedes registrar solicitudes de servicio y darles seguimiento con sus estados, igual que un pedido."),
            ("¿Necesito instalar algún programa?", "No. SOZO Gestión funciona en el navegador de tu computadora, tableta o teléfono, con conexión a internet."),
            ("¿Varias personas pueden usarla al mismo tiempo?", "Sí, en los planes Estándar y Profesional. Cada persona tiene su usuario y sus permisos, y todos ven la misma información actualizada."),
            ("¿Puedo pasar mi lista de clientes actual?", "Sí. Con el servicio de carga inicial de datos, desde Q500, cargamos tus clientes para que empieces con la información completa."),
            ("¿Se puede adaptar a mi proceso de ventas?", "Sí. Podemos ajustar estados, campos y reportes, o agregar módulos como personalización, con precios desde Q500 según el alcance."),
        ],
        "mock": """
<div class="app-shot lg shot-orders" aria-hidden="true">
  <div class="s-head"><b>Pedidos</b><span class="s-search">Buscar cliente o pedido…</span></div>
  <div class="s-kanban">
    <div><small>Nuevos · 3</small><i>#1050 · Ferretería López<em>Q1,250</em></i><i>#1051 · Ana Pérez<em>Q480</em></i><i>#1052 · Hotel Lago<em>Q3,100</em></i></div>
    <div><small>En proceso · 2</small><i>#1047 · Distribuidora Maya<em>Q2,140</em></i><i>#1048 · Panadería Sol<em>Q760</em></i></div>
    <div><small>Entregados · 2</small><i class="done">#1046 · Café Antigua<em>Q890</em></i><i class="done">#1045 · Librería Central<em>Q1,520</em></i></div>
  </div>
</div>""",
    },
    "reservas": {
        "name": "SOZO Reservas",
        "icon": "i-calendar",
        "subtitle": "Sistema de reservas y agenda de citas para negocios en Guatemala",
        "title": "SOZO Reservas | Sistema de citas y reservas en Guatemala",
        "description": "Administra citas, horarios y disponibilidad de tu negocio desde el navegador. Para clínicas, consultorios, academias y profesionales. Implementación desde Q2,000.",
        "lead": "Organiza tu agenda, controla la disponibilidad de horarios y confirma las reservas de tus clientes, sin citas cruzadas ni olvidos.",
        "impl": ("Q2,000", "Q4,500", 2000, 4500),
        "pains_title": "Una agenda ordenada, sin citas cruzadas",
        "pains": [
            ("Las citas se anotan en una agenda de papel y a veces se cruzan.", "La agenda muestra los horarios disponibles y evita dar dos citas a la misma hora."),
            ("Los clientes olvidan su cita o no saben si quedó confirmada.", "Cada reserva tiene su confirmación y queda registrada con los datos del cliente."),
            ("No sabes cuántas citas atendiste ni qué servicios se piden más.", "El historial y los reportes muestran las citas atendidas y los servicios más solicitados."),
        ],
        "features": [
            ("i-briefcase", "Registro de servicios", "Cada servicio con su duración y su precio."),
            ("i-clock", "Configuración de horarios", "Días y horas de atención, descansos y días libres."),
            ("i-calendar", "Agenda de citas", "Vista por día y por semana de todas las citas."),
            ("i-users", "Registro de clientes", "Datos de contacto e historial de cada cliente."),
            ("i-check", "Confirmación de reservas", "Cada cita queda confirmada y registrada."),
            ("i-sliders", "Control de disponibilidad", "Solo se ofrecen los horarios libres; nada se cruza."),
            ("i-clipboard", "Historial de citas", "Citas atendidas, canceladas y reprogramadas."),
            ("i-chart", "Reportes", "Citas por periodo y servicios más solicitados."),
            ("i-shield", "Gestión de usuarios", "Accesos para recepción, profesionales y administración."),
        ],
        "audience": [
            ("Clínicas y consultorios", "Médicos, dentistas, psicólogos, fisioterapeutas y nutricionistas."),
            ("Profesionales independientes", "Abogados, contadores, asesores y consultores que trabajan con citas."),
            ("Centros de servicios", "Salones de belleza, barberías, spas y talleres."),
            ("Academias", "Clases, tutorías y cursos con horarios y cupos."),
            ("Negocios que trabajan con citas", "Cualquier negocio que necesite ordenar su agenda."),
        ],
        "faq": [
            ("¿Mis clientes pueden reservar en línea por su cuenta?", "La versión base está pensada para que tu equipo registre, confirme y administre las citas. Si quieres que tus clientes reserven en línea por su cuenta, lo evaluamos como personalización."),
            ("¿Puedo configurar mis propios horarios y servicios?", "Sí. Defines tus días y horas de atención, los servicios que ofreces y su duración, y la agenda solo muestra los horarios disponibles."),
            ("¿Necesito instalar algún programa?", "No. SOZO Reservas funciona en el navegador de tu computadora, tableta o teléfono, con conexión a internet."),
            ("¿Pueden usarla la recepción y los profesionales al mismo tiempo?", "Sí, en los planes Estándar y Profesional. Cada persona tiene su usuario y sus permisos, y todos ven la misma agenda actualizada."),
            ("¿Cómo se protege la información de mis clientes?", "Cada persona entra con su propio usuario y contraseña, los permisos limitan lo que cada quien puede ver y la información cuenta con copias de seguridad."),
            ("¿Se puede adaptar a mi negocio?", "Sí. Podemos ajustar campos, reportes o agregar módulos como personalización, con precios desde Q500 según el alcance."),
        ],
        "mock": """
<div class="app-shot lg shot-booking" aria-hidden="true">
  <div class="s-head"><b>Agenda · Martes 24</b><span class="s-btn">+ Nueva cita</span></div>
  <div class="s-chips"><span><b>7</b> citas hoy</span><span><b>2</b> horarios libres</span><span class="okc"><b>5</b> confirmadas</span></div>
  <div class="s-agenda">
    <div><time>8:00</time><i class="c2">Limpieza dental · J. Ruiz</i></div>
    <div><time>9:00</time><i class="c1">Consulta general · M. Gómez</i></div>
    <div><time>10:30</time><i class="c1">Ortodoncia · R. Méndez</i></div>
    <div><time>12:00</time><i class="free">Disponible</i></div>
    <div><time>14:00</time><i class="c2">Evaluación · S. Hernández</i></div>
    <div><time>15:30</time><i class="c1">Control · L. Castillo</i></div>
  </div>
</div>""",
    },
}

INCLUDES = [
    "Configuración inicial de la aplicación",
    "Creación de usuarios y permisos",
    "Personalización básica",
    "Capacitación para tu equipo",
    "Puesta en funcionamiento",
]

# --------------------------------------------------------------------------
# Plantilla
# --------------------------------------------------------------------------
e = html.escape


def icon(name, cls="icon"):
    return f'<svg class="{cls}" aria-hidden="true"><use href="#{name}"/></svg>'


def read_sprite():
    with open(os.path.join(ROOT, "index.html"), encoding="utf-8") as f:
        src = f.read()
    m = re.search(r'<svg width="0".*?\n</svg>', src, re.S)
    if not m:
        raise SystemExit("No se encontró el bloque de íconos en index.html")
    return m.group(0)


def jsonld(key, app):
    url = f"{SITE}aplicaciones/{key}/"
    lo, hi = app["impl"][2], app["impl"][3]
    data = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "SoftwareApplication",
                "@id": url + "#aplicacion",
                "name": app["name"],
                "description": app["description"],
                "url": url,
                "applicationCategory": "BusinessApplication",
                "operatingSystem": "Navegador web",
                "inLanguage": "es",
                "image": SITE + "assets/og-image.jpg",
                "featureList": [f[1] for f in app["features"]],
                "offers": {
                    "@type": "AggregateOffer",
                    "priceCurrency": "GTQ",
                    "lowPrice": lo,
                    "highPrice": hi,
                    "description": "Precio de implementación. También disponible por suscripción mensual desde Q150.",
                    "areaServed": "GT",
                },
                "provider": {"@id": SITE + "#empresa"},
            },
            {
                "@type": "ProfessionalService",
                "@id": SITE + "#empresa",
                "name": "SOZO Tecnología",
                "url": SITE,
                "telephone": PHONE,
                "email": EMAIL,
                "areaServed": {"@type": "Country", "name": "Guatemala"},
            },
            {
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "Inicio", "item": SITE},
                    {"@type": "ListItem", "position": 2, "name": "Aplicaciones web", "item": SITE + "#aplicaciones"},
                    {"@type": "ListItem", "position": 3, "name": app["name"], "item": url},
                ],
            },
            {
                "@type": "FAQPage",
                "mainEntity": [
                    {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
                    for q, a in app["faq"]
                ],
            },
        ],
    }
    return json.dumps(data, ensure_ascii=False, indent=2)


def page(key, app, sprite):
    url = f"{SITE}aplicaciones/{key}/"
    contact = f"{BASE}?solicitud=demo&amp;app={key}#contacto"
    quote = f"{BASE}?solicitud=cotizacion&amp;app={key}#contacto"
    impl_lo, impl_hi = app["impl"][0], app["impl"][1]

    pains = "\n".join(
        f"""        <li class="compare-row">
          <p class="before"><span class="tag-before">Antes</span>{e(a)}</p>
          <p class="after"><span class="tag-after">{icon("i-check")}Con {e(app["name"])}</span>{e(b)}</p>
        </li>"""
        for a, b in app["pains"]
    )
    features = "\n".join(
        f"""        <li class="service">{icon(ic)}<h3>{e(t)}</h3><p>{e(d)}</p></li>"""
        for ic, t, d in app["features"]
    )
    audience = "\n".join(
        f"""        <li><h3>{e(t)}</h3><p>{e(d)}</p></li>""" for t, d in app["audience"]
    )
    faq = "\n".join(
        f"""        <details class="faq-item">
          <summary>{e(q)}{icon("i-arrow", "icon faq-chev")}</summary>
          <p>{e(a)}</p>
        </details>"""
        for q, a in app["faq"]
    )
    includes = "\n".join(f"            <li>{e(i)}</li>" for i in INCLUDES)
    others = "\n".join(
        f"""        <a class="other-app" href="{BASE}aplicaciones/{k}/">
          <span class="icon-badge sm">{icon(o["icon"])}</span>
          <span><b>{e(o["name"])}</b><small>{e(o["subtitle"])}</small></span>
          {icon("i-arrow", "icon other-arrow")}
        </a>"""
        for k, o in APPS.items()
        if k != key
    )

    return f"""<!doctype html>
<html lang="es-GT">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{e(app["title"])}</title>
  <meta name="description" content="{e(app["description"])}">
  <link rel="canonical" href="{url}">
  <meta name="robots" content="index, follow">
  <meta name="theme-color" content="#FFFFFF">
  <meta property="og:type" content="website">
  <meta property="og:locale" content="es_GT">
  <meta property="og:site_name" content="SOZO Tecnología">
  <meta property="og:url" content="{url}">
  <meta property="og:title" content="{e(app["name"])}: {e(app["subtitle"])}">
  <meta property="og:description" content="{e(app["description"])}">
  <meta property="og:image" content="{SITE}assets/og-image.jpg">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:image:alt" content="Logo de SOZO Tecnología: aplicaciones web para negocios en Guatemala">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{e(app["title"])}">
  <meta name="twitter:description" content="{e(app["description"])}">
  <meta name="twitter:image" content="{SITE}assets/og-image.jpg">
  <link rel="icon" href="{BASE}assets/favicon.ico" sizes="any">
  <link rel="icon" type="image/png" sizes="32x32" href="{BASE}assets/favicon-32.png">
  <link rel="apple-touch-icon" href="{BASE}assets/apple-touch-icon.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@600;700;800&family=Open+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{BASE}styles.css">
  <script>document.documentElement.classList.add("js");</script>
  <script type="application/ld+json">
{jsonld(key, app)}
  </script>
</head>
<body data-app="{key}">

<!-- Página generada por _build/generar_paginas.py: edita el contenido allí -->
{sprite}

<a class="skip-link" href="#contenido">Saltar al contenido</a>

<header class="site-header" id="top">
  <div class="container header-inner">
    <a class="brand" href="{BASE}" aria-label="SOZO Tecnología, ir al inicio">
      <img src="{BASE}assets/sozo-mark-96.png" alt="" width="40" height="40">
      <span class="brand-text">
        <span class="brand-name">SOZO</span>
        <span class="brand-sub">Tecnología</span>
      </span>
    </a>

    <nav class="main-nav" id="main-nav" aria-label="Principal">
      <ul>
        <li><a href="{BASE}">Inicio</a></li>
        <li><a class="active" href="{BASE}#aplicaciones">Aplicaciones web</a></li>
        <li><a href="{BASE}#soluciones">Soluciones</a></li>
        <li><a href="{BASE}#personalizado">Desarrollo a la medida</a></li>
        <li><a href="{BASE}#servicios">Servicios</a></li>
        <li><a href="{BASE}#nosotros">Nosotros</a></li>
        <li><a href="{BASE}#contacto">Contacto</a></li>
      </ul>
      <a class="btn btn-primary nav-cta-mobile" href="{contact}">Solicitar demostración</a>
    </nav>

    <div class="header-actions">
      <a class="btn btn-primary btn-sm header-cta" href="{contact}">Solicitar demo</a>
      <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="main-nav" aria-label="Abrir menú">
        <svg class="icon"><use href="#i-menu"/></svg>
      </button>
    </div>
  </div>
</header>

<main id="contenido">
  <nav class="breadcrumb container" aria-label="Ruta de navegación">
    <ol>
      <li><a href="{BASE}">Inicio</a></li>
      <li><a href="{BASE}#aplicaciones">Aplicaciones web</a></li>
      <li aria-current="page">{e(app["name"])}</li>
    </ol>
  </nav>

  <section class="app-hero">
    <div class="hero-bg" aria-hidden="true"></div>
    <div class="container app-hero-grid">
      <div class="app-hero-copy">
        <h1><span class="h1-name">{e(app["name"])}</span> <span class="h1-sub">{e(app["subtitle"])}</span></h1>
        <p class="lead">{e(app["lead"])}</p>
        <div class="hero-ctas">
          <a class="btn btn-primary btn-lg" href="{contact}">Solicitar demostración {icon("i-arrow")}</a>
          <a class="btn btn-ghost btn-lg js-wa" href="https://wa.me/50256907669" target="_blank" rel="noopener">{icon("i-chat")} Escribir por WhatsApp</a>
        </div>
        <p class="price-line">Implementación desde <strong>{impl_lo}</strong> · Suscripción desde <strong>Q150 al mes</strong></p>
      </div>
      <div class="app-hero-visual">
{app["mock"].strip()}
      </div>
    </div>
  </section>

  <section class="section section-white" aria-labelledby="t-problema">
    <div class="container narrow">
      <h2 id="t-problema">{e(app["pains_title"])}</h2>
      <ul class="compare">
{pains}
      </ul>
    </div>
  </section>

  <section class="section" aria-labelledby="t-funciones">
    <div class="container">
      <div class="section-head">
        <h2 id="t-funciones">Funcionalidades de {e(app["name"])}</h2>
        <p>Todo lo que necesitas para el día a día, sin funciones que estorben.</p>
      </div>
      <ul class="service-grid">
{features}
      </ul>
    </div>
  </section>

  <section class="section section-white" aria-labelledby="t-para">
    <div class="container narrow">
      <h2 id="t-para">¿Para qué negocios es?</h2>
      <ul class="audience">
{audience}
      </ul>
    </div>
  </section>

  <section class="section" aria-labelledby="t-precio">
    <div class="container price-grid">
      <div>
        <h2 id="t-precio">Precio e implementación</h2>
        <p class="muted">Elige pagar una sola vez por la implementación o usar la aplicación con una suscripción mensual o anual. El precio final depende de la cantidad de usuarios y de las personalizaciones, y lo confirmamos en la cotización.</p>
        <div class="price-boxes">
          <div class="price-box">
            <span>Implementación (pago único)</span>
            <b>{impl_lo} – {impl_hi}</b>
          </div>
          <div class="price-box">
            <span>Suscripción</span>
            <b>Desde Q150<small>/mes</small></b>
            <a href="{BASE}#planes">Ver planes</a>
          </div>
        </div>
        <a class="btn btn-primary" href="{quote}">Solicitar cotización {icon("i-arrow")}</a>
      </div>
      <div class="price-details">
        <div>
          <h3>La implementación incluye</h3>
          <ul class="check-list">
{includes}
          </ul>
        </div>
        <div>
          <h3>Requisitos técnicos</h3>
          <p>Computadora, tableta o teléfono con un navegador actualizado y conexión a internet. No requiere instalación ni equipos especiales.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section section-white" aria-labelledby="t-faq">
    <div class="container narrow">
      <h2 id="t-faq">Preguntas frecuentes</h2>
      <div class="faq">
{faq}
      </div>
    </div>
  </section>

  <section class="section other-apps" aria-labelledby="t-otras">
    <div class="container narrow">
      <h2 id="t-otras">Otras aplicaciones</h2>
      <div class="other-list">
{others}
      </div>
    </div>
  </section>

  <section class="cta-band" aria-labelledby="t-cta">
    <div class="container cta-inner">
      <div>
        <h2 id="t-cta">Mira {e(app["name"])} funcionando antes de decidir</h2>
        <p>Agenda una demostración virtual sin compromiso.</p>
      </div>
      <a class="btn btn-light btn-lg" href="{contact}">Agendar demostración {icon("i-arrow")}</a>
    </div>
  </section>
</main>

<footer class="site-footer">
  <div class="container footer-grid">
    <div class="footer-brand">
      <a class="brand brand-light" href="{BASE}" aria-label="SOZO Tecnología, ir al inicio">
        <img src="{BASE}assets/sozo-mark-white-96.png" alt="" width="40" height="40" loading="lazy" decoding="async">
        <span class="brand-text"><span class="brand-name">SOZO</span><span class="brand-sub">Tecnología</span></span>
      </a>
      <p>Creamos soluciones que impulsan tu negocio.</p>
    </div>
    <nav aria-label="Aplicaciones">
      <h3>Aplicaciones</h3>
      <ul>
        <li><a href="{BASE}aplicaciones/inventario/">SOZO Inventario</a></li>
        <li><a href="{BASE}aplicaciones/gestion/">SOZO Gestión</a></li>
        <li><a href="{BASE}aplicaciones/reservas/">SOZO Reservas</a></li>
        <li><a href="{BASE}#personalizado">Desarrollo a la medida</a></li>
      </ul>
    </nav>
    <nav aria-label="Empresa">
      <h3>Empresa</h3>
      <ul>
        <li><a href="{BASE}#servicios">Servicios</a></li>
        <li><a href="{BASE}#planes">Planes</a></li>
        <li><a href="{BASE}#nosotros">Nosotros</a></li>
        <li><a href="{BASE}#contacto">Contacto</a></li>
      </ul>
    </nav>
    <div>
      <h3>Contacto</h3>
      <ul>
        <li><a class="js-wa" href="https://wa.me/50256907669" target="_blank" rel="noopener">WhatsApp</a></li>
        <li><a class="js-mail" href="mailto:{EMAIL}">Correo electrónico</a></li>
        <li>Guatemala</li>
      </ul>
    </div>
  </div>
  <div class="container footer-bottom">
    <p>© <span id="year">2026</span> SOZO Tecnología. Todos los derechos reservados.</p>
    <p lang="ja" class="footer-kanji">創造</p>
  </div>
</footer>

<a class="wa-float js-wa" href="https://wa.me/50256907669" target="_blank" rel="noopener" aria-label="Escríbenos por WhatsApp">
  <svg class="icon"><use href="#i-chat"/></svg>
</a>

<script src="{BASE}script.js"></script>
</body>
</html>
"""


def main():
    sprite = read_sprite()
    for key, app in APPS.items():
        out_dir = os.path.join(ROOT, "aplicaciones", key)
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "index.html")
        with open(path, "w", encoding="utf-8", newline="\n") as f:
            f.write(page(key, app, sprite))
        print("ok", os.path.relpath(path, ROOT))


if __name__ == "__main__":
    main()
