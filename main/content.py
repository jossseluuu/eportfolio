"""
All the content of the e-portfolio, in English and Spanish.

Any translatable text is written as ``T("English", "Español")``.
``localize(data, lang)`` turns those pairs into plain strings for a language,
so templates never have to care about translations.

To update the site, edit this file and push: GitHub Actions rebuilds it.
"""

LANGS = ("en", "es")


class T(dict):
    """A bilingual string."""

    def __init__(self, en, es):
        super().__init__(en=en, es=es)


def localize(data, lang):
    if isinstance(data, T):
        return data[lang]
    if isinstance(data, dict):
        return {k: localize(v, lang) for k, v in data.items()}
    if isinstance(data, (list, tuple)):
        return [localize(v, lang) for v in data]
    return data


# --------------------------------------------------------------------------
# Profile
# --------------------------------------------------------------------------

PROFILE = {
    "name": "José Luis López López",
    "short_name": "José Luis",
    "name_lines": ["José Luis", "López López"],
    "availability": T("Open to internships & junior roles", "Abierto a prácticas y puestos junior"),
    "role": T("Computer Engineering student", "Estudiante de Ingeniería Informática"),
    "tagline": T(
        "Applied AI, cybersecurity and backend systems",
        "IA aplicada, ciberseguridad y sistemas backend",
    ),
    "intro": T(
        "Almost everything I build starts with a question I can't let go of. "
        "I answer it by building something, measuring how well it works and "
        "writing down what I learned along the way.",
        "Casi todo lo que construyo empieza con una pregunta que no consigo "
        "quitarme de la cabeza. La respondo construyendo algo, midiendo lo bien "
        "que funciona y dejando por escrito lo que aprendo por el camino.",
    ),
    "location": T("Granada, Spain", "Granada, España"),
    "email": "jossseluuu@gmail.com",
    "github": "https://github.com/jossseluuu",
    "github_label": "github.com/jossseluuu",
    "linkedin": "https://www.linkedin.com/in/joseluislop",
    "linkedin_label": "linkedin.com/in/joseluislop",
    "newsletter": "https://jossseluuu.github.io/ZeroTrace",
    "newsletter_label": "jossseluuu.github.io/ZeroTrace",
    "ms_learn": "https://learn.microsoft.com/es-es/users/joseluislopezlopez/transcript/71wx2hew1onyx98",
}

HIGHLIGHTS = [
    {"value": "7", "label": T("Honours with Distinction · UGR", "Matrículas de Honor · UGR")},
    {"value": T("3.68", "3,68"), "label": T("GPA · Univ. of Montana", "GPA · Univ. of Montana")},
    {"value": "900+", "label": T("students represented", "estudiantes representados")},
    {"value": "5", "label": T("featured projects", "proyectos destacados")},
]

# --------------------------------------------------------------------------
# About
# --------------------------------------------------------------------------

ABOUT = {
    "title": T("Understanding in depth how systems work",
               "Comprender a fondo cómo funcionan los sistemas"),
    "paragraphs": [
        T(
            "I'm a fourth-year Computer Engineering student at the University of Granada. "
            "I spent a full academic year at the University of Montana (USA) on an exchange "
            "programme and worked there during that time, which taught me a lot about landing "
            "in an unfamiliar place and figuring things out quickly. From January 2027, only "
            "my Final Degree Project (thesis) will remain.",
            "Soy estudiante de cuarto curso de Ingeniería Informática en la Universidad de "
            "Granada. Pasé un curso académico completo en la University of Montana (EE. UU.) "
            "con un programa de intercambio y trabajé allí durante ese tiempo, lo que me enseñó "
            "mucho sobre llegar a un sitio desconocido y resolver las cosas rápido. A partir de "
            "enero de 2027 solo tendré pendiente el Trabajo Fin de Grado.",
        ),
        T(
            "The areas I keep coming back to are backend systems, applied AI, security and "
            "optimisation, and above all the places where they overlap.",
            "Las áreas a las que siempre vuelvo son los sistemas backend, la IA aplicada, la "
            "seguridad y la optimización, y sobre todo los puntos donde se cruzan.",
        ),
    ],
    "principles": [
        {
            "icon": "✍",
            "title": T("I write the design down first", "Primero escribo el diseño"),
            "text": T(
                "Specifications, requirements and architecture decision records (ADRs) come "
                "before the code. CompanyAgentsHQ has 161 functional requirements and 10 ADRs; "
                "I-CPU has nine ADRs.",
                "Especificaciones, requisitos y registros de decisiones de arquitectura (ADR) "
                "van antes que el código. CompanyAgentsHQ tiene 161 requisitos funcionales y "
                "10 ADR; I-CPU tiene nueve.",
            ),
        },
        {
            "icon": "📏",
            "title": T("Numbers, not impressions", "Números, no impresiones"),
            "text": T(
                "I-CPU runs steganalysis against its own output; the openScope bots are scored "
                "on separation losses and runway throughput.",
                "I-CPU ejecuta estegoanálisis contra su propia salida; los bots de openScope se "
                "evalúan por pérdidas de separación y capacidad de pista.",
            ),
        },
        {
            "icon": "🛡",
            "title": T("Safety is part of the design", "La seguridad es parte del diseño"),
            "text": T(
                "Approval steps, audit logs, safety shields and strict content policies are "
                "there from the first commit, not added later.",
                "Pasos de aprobación, registros de auditoría, escudos de seguridad y políticas "
                "de contenido estrictas están desde el primer commit, no se añaden después.",
            ),
        },
        {
            "icon": "🗣",
            "title": T("I like explaining things", "Me gusta explicar las cosas"),
            "text": T(
                "I write technical content in English and Spanish, aiming for something a "
                "beginner can follow and an expert won't wince at.",
                "Escribo contenido técnico en inglés y en español, buscando que un principiante "
                "pueda seguirlo y que a un experto no le chirríe.",
            ),
        },
    ],
}

# --------------------------------------------------------------------------
# Projects
# --------------------------------------------------------------------------

FEATURED_PROJECTS = [
    {
        "slug": "openscope",
        "visual": "radar",
        "terminal": [],
        "icon": "🛫",
        "name": "openScope",
        "subtitle": T("AI air traffic controllers", "Controladores aéreos con IA"),
        "status": T("Bot A working · Bot B implemented, not yet trained",
                    "Bot A funcionando · Bot B implementado, aún sin entrenar"),
        "repo": "https://github.com/jossseluuu/openScope",
        "stack": ["JavaScript", "Python", "PyTorch", "ONNX", "PPO · DAgger", "CMA-ES", "Gymnasium"],
        "summary": T(
            "Two programs that act as the air traffic controller for an entire airport, "
            "restricted to the same commands a human controller can give, under real ICAO, "
            "EASA and FAA separation rules.",
            "Dos programas que hacen de controlador aéreo de un aeropuerto entero, limitados a "
            "los mismos comandos que puede dar un controlador humano y bajo normas de separación "
            "reales de OACI, EASA y FAA.",
        ),
        "description": [
            T(
                "Two programs that act as the air traffic controller for an entire airport: "
                "arrivals, departures and every conflict between them. The rule I set myself is "
                "that they may only do what a human controller can, giving the same commands "
                "through the same command line, under real ICAO, EASA and FAA separation rules.",
                "Dos programas que hacen de controlador aéreo de un aeropuerto entero: llegadas, "
                "salidas y todos los conflictos entre ellas. La regla que me impuse es que solo "
                "pueden hacer lo que haría un controlador humano, dando los mismos comandos por "
                "la misma línea de comandos y bajo normas de separación reales de OACI, EASA y FAA.",
            ),
            T(
                "Fork of the open-source openScope ATC simulator. The bots, realism layer, "
                "headless simulator, Python tooling and the two new airports are my additions.",
                "Es un fork del simulador ATC de código abierto openScope. Los bots, la capa de "
                "realismo, el simulador headless, las herramientas en Python y los dos aeropuertos "
                "nuevos son aportaciones mías.",
            ),
        ],
        "metrics": [
            {"value": "0", "label": T("collisions or runway incursions", "colisiones o incursiones en pista")},
            {"value": "20–22", "label": T("landings per hour", "aterrizajes por hora")},
            {"value": "21–25", "label": T("departures per hour", "despegues por hora")},
            {"value": "4–11", "label": T("separation losses per hour", "pérdidas de separación por hora")},
        ],
        "metrics_note": T(
            "Untuned Bot A results · 60-minute sessions · seeds 1–3 · Madrid-Barajas and Munich.",
            "Resultados del Bot A sin ajustar · sesiones de 60 minutos · semillas 1–3 · "
            "Madrid-Barajas y Múnich.",
        ),
        "cards": [
            {
                "title": T("Bot A · expert rules", "Bot A · reglas expertas"),
                "text": T(
                    "Arrival and departure sequencing (AMAN/DMAN), vectors, holds and conflict "
                    "resolution. Every command carries its reason, and its parameters can be "
                    "tuned with CMA-ES.",
                    "Secuenciación de llegadas y salidas (AMAN/DMAN), vectores, esperas y "
                    "resolución de conflictos. Cada comando lleva su motivo y sus parámetros se "
                    "pueden ajustar con CMA-ES.",
                ),
            },
            {
                "title": T("Bot B · reinforcement learning", "Bot B · aprendizaje por refuerzo"),
                "text": T(
                    "A PPO agent in PyTorch with a curriculum, designed to start by imitating "
                    "Bot A (DAgger) and export to ONNX to play in the browser.",
                    "Un agente PPO en PyTorch con currículo, diseñado para empezar imitando al "
                    "Bot A (DAgger) y exportarse a ONNX para jugar en el navegador.",
                ),
            },
            {
                "title": T("Safety shield", "Escudo de seguridad"),
                "text": T(
                    "Blocks unsafe commands from either bot. Rules ranked by priority: "
                    "safety → separation → procedure → efficiency.",
                    "Bloquea los comandos inseguros de cualquiera de los dos bots. Reglas por "
                    "prioridad: seguridad → separación → procedimiento → eficiencia.",
                ),
            },
        ],
        "sections": [
            {
                "title": T("What I built", "Lo que he construido"),
                "items": [
                    T("Headless simulator with seeded randomness, a Bot API and a Python bridge "
                      "exposed as a Gymnasium-style environment.",
                      "Simulador headless con aleatoriedad con semilla, una Bot API y un puente "
                      "con Python expuesto como entorno estilo Gymnasium."),
                    T("Realism layer: a regulatory profile per airport (EASA with RECAT-EU, FAA "
                      "or ICAO), wake turbulence separation, runway wind limits, terrain "
                      "clearance and minimum vectoring altitudes.",
                      "Capa de realismo: un perfil normativo por aeropuerto (EASA con RECAT-EU, "
                      "FAA u OACI), separación por estela turbulenta, límites de viento en pista, "
                      "franqueamiento de terreno y altitudes mínimas de vectorización."),
                    T("Two new airports: Madrid-Barajas (LEMD) and Málaga (LEMG), with "
                      "procedures and terrain data.",
                      "Dos aeropuertos nuevos: Madrid-Barajas (LEMD) y Málaga (LEMG), con "
                      "procedimientos y datos de terreno."),
                ],
            },
            {
                "title": T("Training pipeline", "Pipeline de entrenamiento"),
                "items": [
                    T("Bot A plays and every decision is recorded on an audit page.",
                      "El Bot A juega y cada decisión queda registrada en una página de auditoría."),
                    T("Bot B learns to imitate it (DAgger), then improves with PPO behind the "
                      "same shield.",
                      "El Bot B aprende a imitarlo (DAgger) y después mejora con PPO detrás del "
                      "mismo escudo."),
                ],
            },
            {
                "title": T("Known limitations", "Limitaciones conocidas"),
                "items": [
                    T("Bot A still loses separation a few times per hour, mostly with aircraft "
                      "bunching on the downwind or leaving holds. Taxiing is modelled as a "
                      "waiting time.",
                      "El Bot A todavía pierde la separación unas pocas veces por hora, sobre todo "
                      "con aviones que se agrupan en el tramo de viento en cola o al salir de las "
                      "esperas. El rodaje se modela como un tiempo de espera."),
                ],
            },
        ],
        "images": [],
    },
    {
        "slug": "icpu",
        "visual": "image",
        "terminal": [],
        "icon": "🔐",
        "name": "I-CPU",
        "subtitle": T("Hide data in images, then try to find it",
                      "Esconder datos en imágenes y después intentar encontrarlos"),
        "status": T("v2.0.0 released", "v2.0.0 publicada"),
        "repo": "https://github.com/jossseluuu/I-CPU",
        "stack": ["C++20", "CMake", "Argon2id", "XChaCha20-Poly1305", "libjpeg-turbo",
                  "doctest · libFuzzer", "CI Windows/Linux"],
        "summary": T(
            "Steganography tool that hides encrypted data inside images and then attacks its "
            "own output with standard steganalysis, so configurations are compared by numbers.",
            "Herramienta de esteganografía que esconde datos cifrados en imágenes y después "
            "ataca su propia salida con estegoanálisis, para comparar configuraciones con números.",
        ),
        "description": [
            T(
                "I-CPU hides an encrypted message or file inside an image so that it can't be "
                "read without the password, and tries to make it hard to tell anything is there "
                "at all. Most steganography tools stop at hiding the data; I-CPU also attacks its "
                "own output with standard steganalysis, so configurations can be compared by "
                "numbers instead of guesses.",
                "I-CPU esconde un mensaje o un fichero cifrado dentro de una imagen para que no "
                "se pueda leer sin la contraseña, e intenta que sea difícil notar que hay algo "
                "escondido. La mayoría de herramientas de esteganografía se quedan en ocultar los "
                "datos; I-CPU además ataca su propia salida con estegoanálisis estándar, así que "
                "las configuraciones se comparan con números en lugar de a ojo.",
            ),
        ],
        "metrics": [],
        "metrics_note": "",
        "cards": [],
        "sections": [
            {
                "title": T("Features", "Funcionalidades"),
                "items": [
                    T("Three hiding domains picked from the output format: pixel bits (PNG, BMP, "
                      "TGA, QOI, PNM), JPEG DCT coefficients without recompression, and GIF "
                      "palette indices, animated GIFs included.",
                      "Tres dominios de ocultación según el formato de salida: bits de píxel "
                      "(PNG, BMP, TGA, QOI, PNM), coeficientes DCT de JPEG sin recompresión e "
                      "índices de paleta GIF, incluidos GIF animados."),
                    T("Adaptive embedding with Syndrome-Trellis Codes: changes few samples and "
                      "prefers textured areas.",
                      "Incrustación adaptativa con Syndrome-Trellis Codes: cambia pocas muestras "
                      "y prefiere las zonas con textura."),
                    T("Modern cryptography: Argon2id, XChaCha20-Poly1305, a random salt per "
                      "embedding and an encrypted header.",
                      "Criptografía moderna: Argon2id, XChaCha20-Poly1305, una sal aleatoria por "
                      "incrustación y una cabecera cifrada."),
                    T("Built-in evaluation: chi-square, RS analysis, DCT chi-square, PSNR and SSIM.",
                      "Evaluación integrada: chi-cuadrado, análisis RS, chi-cuadrado DCT, PSNR y SSIM."),
                ],
            },
            {
                "title": T("Engineering", "Ingeniería"),
                "items": [
                    T("Own codecs for PNG, QOI, PNM and GIF/LZW.",
                      "Códecs propios para PNG, QOI, PNM y GIF/LZW."),
                    T("CLI with a guided mode and a local web GUI served only on 127.0.0.1, fully "
                      "offline.",
                      "CLI con modo guiado y una interfaz web local servida solo en 127.0.0.1, "
                      "totalmente offline."),
                    T("doctest test suite, a libFuzzer target for the decoders, CI on Windows "
                      "and Linux.",
                      "Batería de tests con doctest, un objetivo de libFuzzer para los "
                      "decodificadores y CI en Windows y Linux."),
                    T("Nine ADRs and a threat model documenting what it protects against and "
                      "what it doesn't.",
                      "Nueve ADR y un modelo de amenazas que documenta contra qué protege y "
                      "contra qué no."),
                ],
            },
        ],
        "images": [
            {"src": "img/projects/icpu-gui.webp", "w": 1096, "h": 960,
             "caption": T("Local web GUI: message hidden and verified, with a before/after slider.",
                          "Interfaz web local: mensaje oculto y verificado, con comparador antes/después.")},
            {"src": "img/projects/icpu-experiment.webp", "w": 1096, "h": 950,
             "caption": T("Experiment mode: distortion (PSNR, SSIM) and detection (RS, chi-square) by payload.",
                          "Modo experimento: distorsión (PSNR, SSIM) y detección (RS, chi-cuadrado) según la carga.")},
        ],
    },
    {
        "slug": "companyagentshq",
        "visual": "image",
        "terminal": [],
        "icon": "🏢",
        "name": "CompanyAgentsHQ",
        "subtitle": T("A company of AI agents you can actually manage",
                      "Una empresa de agentes de IA que de verdad puedes gestionar"),
        "status": T("In development", "En desarrollo"),
        "repo": "https://github.com/jossseluuu/CompanyAgentsHQ",
        "stack": ["Python · FastAPI", "React + TypeScript", "Three.js / R3F",
                  "PostgreSQL + pgvector", "Redis", "WebSockets", "Docker Compose"],
        "summary": T(
            "A multi-agent system made visible: you give the CEO agent a goal, approve its plan "
            "and watch the agents work in an isometric office, with everything audited and costed.",
            "Un sistema multiagente hecho visible: das un objetivo al agente CEO, apruebas su "
            "plan y ves a los agentes trabajar en una oficina isométrica, con todo auditado y costeado.",
        ),
        "description": [
            T(
                "Multi-agent systems are usually black boxes. CompanyAgentsHQ makes the company "
                "visible: you give a goal to the CEO agent and approve its plan, managers review "
                "their team's work, and everything is archived, audited and costed while you "
                "watch the agents move between rooms of an isometric office.",
                "Los sistemas multiagente suelen ser cajas negras. CompanyAgentsHQ hace visible "
                "la empresa: das un objetivo al agente CEO y apruebas su plan, los responsables "
                "revisan el trabajo de su equipo y todo queda archivado, auditado y costeado "
                "mientras ves a los agentes moverse entre las salas de una oficina isométrica.",
            ),
            T(
                "Architecturally it is a modular monolith with clear domains (agents, tasks, "
                "knowledge, files, approvals, audit, finance, office and real-time events), "
                "designed so that every agent action can be traced.",
                "A nivel de arquitectura es un monolito modular con dominios claros (agentes, "
                "tareas, conocimiento, ficheros, aprobaciones, auditoría, finanzas, oficina y "
                "eventos en tiempo real), diseñado para que cada acción de un agente sea trazable.",
            ),
        ],
        "metrics": [
            {"value": "161 + 66", "label": T("functional and measurable non-functional requirements (MoSCoW)",
                                             "requisitos funcionales y no funcionales medibles (MoSCoW)")},
            {"value": "646", "label": T("hireable roles across 25 areas", "roles contratables en 25 áreas")},
            {"value": "10", "label": T("ADRs · ruff, mypy, pytest, Vitest and Playwright in CI",
                                       "ADR · ruff, mypy, pytest, Vitest y Playwright en CI")},
        ],
        "metrics_note": "",
        "cards": [
            {
                "title": T("A real org chart", "Un organigrama real"),
                "text": T("Supervisors, escalation to the owner and an approval inbox for "
                          "sensitive actions such as deleting files.",
                          "Supervisores, escalado al propietario y una bandeja de aprobaciones "
                          "para acciones sensibles como borrar ficheros."),
            },
            {
                "title": T("Accountable by design", "Responsable por diseño"),
                "text": T("A hash-chained audit log, an Auditor agent that pauses others when it "
                          "detects loops, and daily AI budgets per agent.",
                          "Un registro de auditoría encadenado con hashes, un agente Auditor que "
                          "pausa a los demás si detecta bucles y presupuestos diarios de IA por agente."),
            },
            {
                "title": T("Zero cost by default", "Coste cero por defecto"),
                "text": T("A scripted fake model for development, local models through Ollama, "
                          "any OpenAI-compatible server, or the Claude API.",
                          "Un modelo simulado para desarrollo, modelos locales con Ollama, "
                          "cualquier servidor compatible con OpenAI o la API de Claude."),
            },
        ],
        "sections": [
            {
                "title": T("Architecture", "Arquitectura"),
                "items": [
                    T("Rooms as plugins (task board, file cabinet, knowledge base, finance, "
                      "audit…): each adds furniture to the map, a tab in the UI and tools for "
                      "the agents in that room.",
                      "Salas como plugins (tablero de tareas, archivo, base de conocimiento, "
                      "finanzas, auditoría…): cada una añade mobiliario al mapa, una pestaña en "
                      "la interfaz y herramientas para los agentes de esa sala."),
                    T("Agent work runs in a separate worker queued through Redis, with events "
                      "streamed to the browser over WebSockets.",
                      "El trabajo de los agentes se ejecuta en un worker aparte, encolado con "
                      "Redis, y los eventos llegan al navegador por WebSockets."),
                    T("PostgreSQL + pgvector for data and embeddings; MinIO/S3 for files. "
                      "Knowledge answers cite their sources.",
                      "PostgreSQL + pgvector para datos y embeddings; MinIO/S3 para ficheros. "
                      "Las respuestas de conocimiento citan sus fuentes."),
                ],
            },
            {
                "title": T("Agent safety", "Seguridad de los agentes"),
                "items": [
                    T("File and web content is handed to agents as data, never as instructions "
                      "(prompt-injection-aware design).",
                      "El contenido de ficheros y webs se entrega a los agentes como datos, nunca "
                      "como instrucciones (diseño consciente de la inyección de prompts)."),
                    T("Human approval for sensitive actions and a global pause button.",
                      "Aprobación humana para acciones sensibles y un botón de pausa general."),
                    T("Tested end-to-end with local models on an 8 GB laptop GPU, with results "
                      "and limitations written down.",
                      "Probado de extremo a extremo con modelos locales en la GPU de 8 GB de un "
                      "portátil, con resultados y limitaciones documentados."),
                ],
            },
        ],
        "images": [
            {"src": "img/projects/cahq-office.webp", "w": 1400, "h": 875,
             "caption": T("The isometric office with the default company's eight agents in their rooms.",
                          "La oficina isométrica con los ocho agentes de la empresa por defecto en sus salas.")},
            {"src": "img/projects/cahq-audit.webp", "w": 1400, "h": 875,
             "caption": T("Audit panel: a verifiable event chain and traceability for every action.",
                          "Panel de auditoría: una cadena de eventos verificable y trazabilidad de cada acción.")},
        ],
    },
    {
        "slug": "howthingstalk",
        "visual": "terminal",
        "terminal": [
            {"kind": "cmd", "text": "howthingstalk ask \"how does GPS compute your position?\""},
            {"kind": "out", "text": T("1 · question & prerequisites", "1 · pregunta y requisitos previos")},
            {"kind": "out", "text": T("2 · one-sentence answer", "2 · respuesta en una frase")},
            {"kind": "out", "text": T("3 · everyday mental model (and where it breaks)",
                                     "3 · modelo mental cotidiano (y dónde falla)")},
            {"kind": "out", "text": T("4 · mechanism: protocols & real numbers",
                                     "4 · mecanismo: protocolos y números reales")},
            {"kind": "ok", "text": T("EN · ES — written twice, not translated once",
                                    "EN · ES — escrito dos veces, no traducido una")},
        ],
        "icon": "📡",
        "name": "HowThingsTalk",
        "subtitle": T("Explaining the technology we use without thinking",
                      "Explicar la tecnología que usamos sin pensar"),
        "status": T("Ongoing", "En curso"),
        "repo": "https://github.com/jossseluuu/HowThingsTalk",
        "stack": ["EN · ES", "Markdown", "CC BY-SA"],
        "summary": T(
            "A bilingual library of explanations about everyday devices. Each article answers "
            "one concrete question, such as how GPS computes your position.",
            "Una biblioteca bilingüe de explicaciones sobre dispositivos cotidianos. Cada "
            "artículo responde a una pregunta concreta, como cómo calcula el GPS tu posición.",
        ),
        "description": [
            T(
                "A library of explanations about phones, laptops, earbuds, watches, cards, light "
                "bulbs and cars. Each article answers one concrete question, such as how GPS "
                "computes your position or why phones randomise their MAC address.",
                "Una biblioteca de explicaciones sobre móviles, portátiles, auriculares, relojes, "
                "tarjetas, bombillas y coches. Cada artículo responde a una pregunta concreta, "
                "como cómo calcula el GPS tu posición o por qué los móviles aleatorizan su "
                "dirección MAC.",
            ),
        ],
        "metrics": [],
        "metrics_note": "",
        "cards": [],
        "sections": [
            {
                "title": T("How it is written", "Cómo está escrito"),
                "items": [
                    T("Four layers of depth: the question and its prerequisites, a one-sentence "
                      "answer, an everyday mental model (and where it breaks), and the technical "
                      "mechanism with protocols and real numbers.",
                      "Cuatro niveles de profundidad: la pregunta y sus requisitos previos, una "
                      "respuesta en una frase, un modelo mental cotidiano (y dónde falla) y el "
                      "mecanismo técnico con protocolos y números reales."),
                    T("Written twice, not translated once: the same structure in both languages, "
                      "with a shared style guide and glossary.",
                      "Escrito dos veces, no traducido una: la misma estructura en los dos "
                      "idiomas, con una guía de estilo y un glosario compartidos."),
                    T("12 topic areas: Wi-Fi, cellular networks, short-range radio, positioning, "
                      "storage, IoT, cryptography, privacy…",
                      "12 áreas temáticas: Wi-Fi, redes móviles, radio de corto alcance, "
                      "posicionamiento, almacenamiento, IoT, criptografía, privacidad…"),
                ],
            },
        ],
        "images": [],
    },
    {
        "slug": "zerotrace",
        "visual": "terminal",
        "terminal": [
            {"kind": "cmd", "text": "python build.py --lang en,es"},
            {"kind": "ok", "text": T("edition generated · markdown + html", "edición generada · markdown + html")},
            {"kind": "ok", "text": T("rss feeds updated (en, es)", "feeds rss actualizados (en, es)")},
            {"kind": "ok", "text": T("0 duplicated alerts or CVEs", "0 alertas o CVE duplicados")},
            {"kind": "ok", "text": T("no cookies · no analytics · strict CSP",
                                    "sin cookies · sin analítica · CSP estricta")},
        ],
        "icon": "🚦",
        "name": "ZeroTrace",
        "subtitle": T("A daily cybersecurity newsletter for everyone",
                      "Un boletín diario de ciberseguridad para todo el mundo"),
        "status": T("Daily editions", "Ediciones diarias"),
        "repo": "https://github.com/jossseluuu/ZeroTrace",
        "site": "https://jossseluuu.github.io/ZeroTrace",
        "stack": ["Python (stdlib only)", "HTML · RSS", "Strict CSP", "EN · ES"],
        "summary": T(
            "A bilingual daily newsletter: each edition explains one concrete security concept "
            "about the devices people actually use, built by a dependency-free generator.",
            "Un boletín diario bilingüe: cada edición explica un concepto concreto de seguridad "
            "sobre los dispositivos que usamos, generado sin dependencias externas.",
        ),
        "description": [
            T(
                "A daily cybersecurity newsletter for everyone. Each edition covers one concrete "
                "concept about the devices people actually use, like what someone can do if they "
                "steal your phone after watching you type the passcode.",
                "Un boletín diario de ciberseguridad para todo el mundo. Cada edición trata un "
                "concepto concreto sobre los dispositivos que usamos de verdad, como qué puede "
                "hacer alguien si te roba el móvil después de verte teclear el código.",
            ),
        ],
        "metrics": [],
        "metrics_note": "",
        "cards": [],
        "sections": [
            {
                "title": T("Content", "Contenido"),
                "items": [
                    T("Two reading levels: Basic and Deep dive, with the mechanism and what an "
                      "attack looks like.",
                      "Dos niveles de lectura: Básico y A fondo, con el mecanismo y cómo es un ataque."),
                    T("Right-sized advice: impact, effort and audience for every action, plus "
                      "what you don't need to do.",
                      "Consejos a medida: impacto, esfuerzo y público de cada acción, y también lo "
                      "que no hace falta hacer."),
                    T("Primary sources (INCIBE, CCN-CERT, CISA, NIST or the vendor) for every "
                      "fact or CVE.",
                      "Fuentes primarias (INCIBE, CCN-CERT, CISA, NIST o el fabricante) para cada "
                      "dato o CVE."),
                ],
            },
            {
                "title": T("Engineering", "Ingeniería"),
                "items": [
                    T("Dependency-free generator producing Markdown and HTML editions, indexes, "
                      "an alert log and RSS feeds in both languages.",
                      "Generador sin dependencias que produce ediciones en Markdown y HTML, "
                      "índices, un registro de alertas y feeds RSS en los dos idiomas."),
                    T("The build fails if an already-published alert or CVE shows up again.",
                      "La compilación falla si vuelve a aparecer una alerta o un CVE ya publicado."),
                    T("No cookies, analytics, third-party scripts or external fonts.",
                      "Sin cookies, analítica, scripts de terceros ni fuentes externas."),
                ],
            },
        ],
        "images": [],
    },
]

OTHER_PROJECTS = [
    {
        "icon": "📈",
        "name": "InvestDashboard",
        "repo": "https://github.com/jossseluuu/InvestDashboard",
        "text": T(
            "A personal portfolio dashboard: live prices converted into seven currencies, "
            "per-asset and portfolio P&L, historical charts, fundamentals, news per ticker and a "
            "weekly Telegram summary. Includes a Railway + Vercel deployment guide.",
            "Un panel de inversiones personal: precios en directo convertidos a siete divisas, "
            "rentabilidad por activo y de la cartera, gráficos históricos, fundamentales, noticias "
            "por ticker y un resumen semanal por Telegram. Incluye guía de despliegue en Railway + Vercel.",
        ),
        "stack": ["Flask", "React", "Vite", "SQLite", "Chart.js", "APScheduler"],
    },
    {
        "icon": "🧮",
        "name": "DataStructures-Algorithms",
        "repo": "https://github.com/jossseluuu/DataStructures-Algorithms",
        "text": T(
            "Classic data structures written from scratch, starting with static and dynamic "
            "linear structures, with a test program and a roadmap.",
            "Estructuras de datos clásicas escritas desde cero, empezando por las estructuras "
            "lineales estáticas y dinámicas, con un programa de pruebas y una hoja de ruta.",
        ),
        "stack": ["C"],
    },
    {
        "icon": "✈",
        "name": "airline-database-project",
        "repo": "https://github.com/jossseluuu/airline-database-project",
        "text": T(
            "Relational database design for airline operations (pilots, crew, flights, flight "
            "plans, aircraft, hangars and maintenance), with a work breakdown structure, a "
            "data-quality risk analysis and a small web front end.",
            "Diseño de una base de datos relacional para operaciones de aerolínea (pilotos, "
            "tripulación, vuelos, planes de vuelo, aviones, hangares y mantenimiento), con "
            "estructura de desglose del trabajo, análisis de riesgos de calidad de datos y un "
            "pequeño front end web.",
        ),
        "stack": ["MySQL", "Flask", "JavaScript"],
    },
    {
        "icon": "🎓",
        "name": "eportfolio",
        "repo": "https://github.com/jossseluuu/eportfolio",
        "text": T(
            "This site. Started in Django during the exchange year in Montana; now Django "
            "renders it and GitHub Actions publishes it as a static, bilingual site.",
            "Esta web. Empezó en Django durante el año de intercambio en Montana; ahora Django la "
            "renderiza y GitHub Actions la publica como web estática y bilingüe.",
        ),
        "stack": ["Python", "Django", "GitHub Actions", "GitHub Pages"],
    },
]

TECH_STACK = [
    {"area": T("Languages", "Lenguajes"),
     "items": "Python · C++20 · TypeScript · JavaScript · SQL · C · Java · PHP · Bash"},
    {"area": T("Backend & data", "Backend y datos"),
     "items": "FastAPI · Flask · Django · SQLAlchemy · Node.js · PostgreSQL · MySQL · SQLite · "
              "Oracle · Redis · pgvector"},
    {"area": "Frontend",
     "items": "React · Vite · Three.js / React Three Fiber · Tailwind CSS · Chart.js · Figma · WCAG"},
    {"area": T("AI & ML", "IA y ML"),
     "items": "PyTorch · ONNX · PPO · DAgger · CMA-ES · RAG · embeddings · LLM agents · "
              "Claude API · Ollama · scikit-learn · pandas"},
    {"area": T("Security", "Seguridad"),
     "items": "Argon2id · XChaCha20-Poly1305 · steganography/steganalysis · fuzzing · CSP · "
              "Microsoft Defender XDR · Wireshark · Nmap · Burp Suite · Kali Linux"},
    {"area": T("Tooling & quality", "Herramientas y calidad"),
     "items": "Git · GitHub Actions · Docker · CMake · pytest · Vitest · Playwright · doctest · "
              "ruff · mypy · Linux"},
]

# --------------------------------------------------------------------------
# Education
# --------------------------------------------------------------------------

EDUCATION = [
    {
        "period": T("2023 – Present", "2023 – Actualidad"),
        "title": T("Bachelor's Degree in Computer Engineering", "Grado en Ingeniería Informática"),
        "place": T("University of Granada, Spain", "Universidad de Granada, España"),
        "stats": [
            {"value": T("4th", "4.º"), "label": T("year", "curso")},
            {"value": T("7.744", "7,744"), "label": T("grade average / 10", "nota media / 10")},
            {"value": "7", "label": T("Honours with Distinction", "Matrículas de Honor")},
            {"value": "174/240", "label": T("ECTS completed", "ECTS superados")},
        ],
        "items": [
            T("From January 2027, only the Final Degree Project (thesis) will remain.",
              "A partir de enero de 2027 únicamente tendré pendiente el Trabajo Fin de Grado."),
            T("“Honours with Distinction” (Matrícula de Honor) is the highest grade in the "
              "Spanish university system, awarded to a limited number of top students per course.",
              "La Matrícula de Honor es la máxima calificación del sistema universitario "
              "español y se concede a un número limitado de estudiantes por asignatura."),
        ],
    },
    {
        "period": T("Aug 2025 – May 2026", "Ago. 2025 – May. 2026"),
        "title": T("International Mobility Program", "Programa de Movilidad Internacional"),
        "place": T("University of Montana · Missoula, Montana, United States",
                   "University of Montana · Missoula, Montana, Estados Unidos"),
        "stats": [
            {"value": T("3.64", "3,64"), "label": T("GPA Fall 2025", "GPA otoño 2025")},
            {"value": T("3.74", "3,74"), "label": T("GPA Spring 2026", "GPA primavera 2026")},
            {"value": T("3.68", "3,68"), "label": T("cumulative GPA / 4.0", "GPA acumulado / 4,0")},
        ],
        "items": [
            T("Dean's List in both semesters (semester average of 3.50 or higher and no grade "
              "below B).",
              "Dean's List en los dos semestres (media semestral igual o superior a 3,50 y "
              "ninguna calificación inferior a B, equivalente a un notable)."),
            T("Full two-semester academic year with all teaching, coursework and exams entirely "
              "in English.",
              "Curso académico completo de dos semestres con docencia, trabajos y exámenes "
              "íntegramente en inglés."),
            T("Advanced coursework in software engineering, algorithms, databases and SQL, data "
              "analytics, web development and UI design.",
              "Asignaturas de nivel avanzado en ingeniería del software, algoritmia, bases de "
              "datos y SQL, analítica de datos, desarrollo web y diseño de interfaces."),
        ],
    },
    {
        "period": "2021 – 2023",
        "title": T("Spanish Baccalaureate in Science · Health Sciences track",
                   "Bachillerato de Ciencias · Itinerario de Ciencias de la Salud"),
        "place": T("IES La Madraza · Granada", "IES La Madraza · Granada"),
        "stats": [],
        "items": [
            T("Passed the Spanish university entrance examination (PEvAU) in 2023.",
              "Prueba de acceso a la universidad (PEvAU) superada en 2023."),
        ],
    },
]

TRAINING = [
    {
        "title": "Microsoft Learn",
        "meta": T("30 learning paths · 95 modules · 69 h · 2026",
                  "30 rutas de aprendizaje · 95 módulos · 69 h · 2026"),
        "text": T(
            "Cybersecurity (SC-200 preparation, Defender XDR, Security Copilot) and AI and data "
            "(ML with Python, AI agents on Azure, generative and responsible AI).",
            "Ciberseguridad (preparación del SC-200, Defender XDR, Security Copilot) e IA y datos "
            "(ML con Python, agentes de IA en Azure, IA generativa y responsable).",
        ),
        "link": PROFILE["ms_learn"],
        "link_label": T("Verifiable transcript", "Expediente verificable"),
    },
    {
        "title": "TOEFL · B2",
        "meta": T("ETS · December 2024", "ETS · diciembre de 2024"),
        "text": T("English certificate issued by ETS (Educational Testing Service).",
                  "Certificado de inglés emitido por ETS (Educational Testing Service)."),
    },
    {
        "title": T("Ángel Barrios Conservatory", "Conservatorio Ángel Barrios"),
        "meta": "2013 – 2018",
        "text": T("Elementary Music Diploma, transverse flute, completed alongside compulsory "
                  "schooling.",
                  "Título de Enseñanzas Elementales de Música, flauta travesera, compaginado con "
                  "la educación obligatoria."),
    },
]

# --------------------------------------------------------------------------
# Experience
# --------------------------------------------------------------------------

EXPERIENCE_INTRO = T(
    "During my year in Montana I made the Dean's List in both semesters while working on "
    "campus and building my personal projects. It's the clearest proof that I perform well "
    "under pressure and adapt quickly to new environments.",
    "Durante mi año en Montana entré en la Dean's List los dos semestres mientras trabajaba en "
    "el campus y desarrollaba mis proyectos personales. Es la prueba más clara de que rindo bien "
    "bajo presión y me adapto rápido a entornos nuevos.",
)

EXPERIENCE = [
    {
        "period": T("Dec 2024 – May 2026", "Dic. 2024 – May. 2026"),
        "title": T("Faculty Student Delegate and Student Representative",
                   "Delegado de Facultad y Representante Estudiantil"),
        "place": T("University of Granada", "Universidad de Granada"),
        "stats": [
            {"value": "900+", "label": T("students represented", "estudiantes representados")},
            {"value": "11", "label": T("roles in the team I built", "cargos en el equipo que formé")},
            {"value": "3", "label": T("Faculty governing bodies", "órganos de gobierno de la Facultad")},
        ],
        "items": [
            T("Revived the Student Council, which had been inactive for some time, and built an "
              "eleven-person team: delegate, deputy, treasury, secretariat and coordinators for "
              "academic affairs, activities, communication, finance and infrastructure.",
              "Reactivé la Delegación de Estudiantes, que llevaba tiempo inactiva, y formé un "
              "equipo de once cargos: delegación, subdelegación, tesorería, secretaría y "
              "coordinadores de asuntos académicos, actividades, comunicación, economía e "
              "infraestructuras."),
            T("Represented students on the Faculty Board, the Governing Committee and the "
              "Committee for Outreach, Students and Inclusion, and in meetings with the Dean's team.",
              "Representé al estudiantado en la Junta de Facultad, la Comisión de Gobierno y la "
              "Comisión de Extensión Universitaria, Estudiantes e Inclusión, y en reuniones con el "
              "equipo decanal."),
            T("Co-organised the Rector's Trophy basketball and volleyball tournaments, the 3rd "
              "University League and a visit to Telefónica's 42 Málaga coding campus.",
              "Coorganizamos los torneos de baloncesto y voleibol del Trofeo Rector, la III Liga "
              "Universitaria y la visita al Campus 42 de Telefónica en Málaga."),
            T("Proposed biannual meetings between each degree's coordinators and its class "
              "delegates to speed up communication.",
              "Propuse reuniones semestrales entre la coordinación de cada grado y sus delegados "
              "para agilizar la comunicación."),
            T("Represented the Faculty at national forums such as AEALCEE and RITSI.",
              "Representé a la Facultad en foros nacionales como AEALCEE y RITSI."),
        ],
    },
    {
        "period": T("Jan 2026 – May 2026", "Ene. 2026 – May. 2026"),
        "title": "UM Catering",
        "place": T("University of Montana · Missoula, United States",
                   "University of Montana · Missoula, Estados Unidos"),
        "stats": [],
        "items": [
            T("Worked in the kitchen of the university's catering service to learn first-hand "
              "how work is organised in the US: shifts, team coordination, service pace and "
              "quality standards, all in English.",
              "Trabajé en la cocina del servicio de catering de la universidad para conocer de "
              "primera mano cómo se organiza el trabajo en Estados Unidos: turnos, coordinación, "
              "ritmo de servicio y estándares de calidad, todo en inglés."),
            T("An excellent, highly diverse work environment where I made great friends.",
              "Un ambiente excelente y muy diverso, del que me llevo grandes amistades."),
        ],
    },
]

# --------------------------------------------------------------------------
# Skills
# --------------------------------------------------------------------------

SKILLS = [
    {"area": T("Programming", "Programación"),
     "text": T("C++ (STL, dynamic memory), Java, Python (NumPy, pandas, Matplotlib, "
               "scikit-learn), JavaScript, PHP, SQL; OOP; data structures; algorithm design "
               "(divide and conquer, greedy, dynamic programming, backtracking).",
               "C++ (STL, memoria dinámica), Java, Python (NumPy, pandas, Matplotlib, "
               "scikit-learn), JavaScript, PHP, SQL; POO; estructuras de datos; diseño de "
               "algoritmos (divide y vencerás, voraces, programación dinámica, vuelta atrás).")},
    {"area": T("Databases & BI", "Bases de datos y BI"),
     "text": T("MySQL, Oracle, PostgreSQL; ER modelling and normalisation; database "
               "administration; distributed databases; data warehousing and OLAP; Power BI, Tableau.",
               "MySQL, Oracle, PostgreSQL; modelado entidad-relación y normalización; "
               "administración de bases de datos; bases de datos distribuidas; data warehousing "
               "y OLAP; Power BI, Tableau.")},
    {"area": T("Web development", "Desarrollo web"),
     "text": T("HTML5, CSS3, JavaScript, PHP, Node.js; interface and UX design (Figma); web "
               "accessibility (WCAG).",
               "HTML5, CSS3, JavaScript, PHP, Node.js; diseño de interfaces y experiencia de "
               "usuario (Figma); accesibilidad web (WCAG).")},
    {"area": T("AI & data science", "IA y ciencia de datos"),
     "text": T("Supervised and unsupervised learning; deep learning fundamentals; heuristic "
               "search and intelligent agents; generative AI, RAG and prompt engineering; Azure "
               "AI services; Jupyter.",
               "Aprendizaje supervisado y no supervisado; fundamentos de deep learning; búsqueda "
               "heurística y agentes inteligentes; IA generativa, RAG e ingeniería de prompts; "
               "servicios de IA en Azure; Jupyter.")},
    {"area": T("Systems", "Sistemas"),
     "text": T("Linux (Bash), Windows; processes and system calls; concurrent programming "
               "(threads, semaphores, monitors); computer architecture; assembly language.",
               "Linux (Bash), Windows; procesos y llamadas al sistema; programación concurrente "
               "(hebras, semáforos, monitores); arquitectura de computadores; ensamblador.")},
    {"area": T("Software engineering", "Ingeniería del software"),
     "text": T("Requirements analysis, UML, information systems analysis and design, ADRs, "
               "automata theory and formal languages.",
               "Análisis de requisitos, UML, análisis y diseño de sistemas de información, ADR, "
               "teoría de autómatas y lenguajes formales.")},
    {"area": T("Cybersecurity", "Ciberseguridad"),
     "text": T("Microsoft Defender XDR, Defender for Endpoint, Entra ID Protection, Security "
               "Copilot; incident detection, investigation and response.",
               "Microsoft Defender XDR, Defender for Endpoint, Entra ID Protection, Security "
               "Copilot; detección, investigación y respuesta ante incidentes.")},
]

LANGUAGES = [
    {"name": T("Spanish", "Español"), "level": T("Native", "Nativo")},
    {"name": T("English", "Inglés"),
     "level": T("B2 (TOEFL) + a full academic year and work experience in the US",
                "B2 (TOEFL) + un curso académico completo y experiencia laboral en EE. UU.")},
    {"name": T("French", "Francés"), "level": T("Basic", "Básico")},
]

COMPETENCIES = [
    T("Leadership", "Liderazgo"),
    T("Initiative", "Iniciativa"),
    T("Problem solving", "Resolución de problemas"),
    T("Communication & negotiation", "Comunicación y negociación"),
    T("Performance under pressure", "Rendimiento bajo presión"),
    T("International adaptability", "Adaptabilidad internacional"),
    T("Self-directed learning", "Aprendizaje autónomo"),
    T("Diverse teams", "Equipos diversos"),
]

INTERESTS = T(
    "Aviation, AI, cybersecurity, web and mobile development, fitness and music.",
    "Aviación, IA, ciberseguridad, desarrollo web y móvil, fitness y música.",
)

DOCUMENTS = [
    {"label": T("CV (English)", "CV (inglés)"), "file": "docs/JoseLuisLopez_CV_EN.pdf"},
    {"label": T("CV (Spanish)", "CV (español)"), "file": "docs/JoseLuisLopez_CV_ES.pdf"},
    {"label": T("Portfolio PDF (English)", "Portfolio PDF (inglés)"),
     "file": "docs/JoseLuisLopez_Portfolio_EN.pdf"},
]

# --------------------------------------------------------------------------
# Interface strings
# --------------------------------------------------------------------------

UI = {
    "nav_about": T("About", "Sobre mí"),
    "nav_work": T("Work", "Proyectos"),
    "label_status": T("Status", "Estado"),
    "label_stack": "Stack",
    "label_links": T("Links", "Enlaces"),
    "scroll": T("Scroll", "Desliza"),
    "case_study": T("View project", "Ver proyecto"),
    "role_line": T("Computer Engineering · University of Granada",
                   "Ingeniería Informática · Universidad de Granada"),
    "focus_line": T("applied AI · cybersecurity · backend", "IA aplicada · ciberseguridad · backend"),
    "email_me": T("Write me an email", "Escríbeme un email"),
    "elsewhere": T("Elsewhere", "En otros sitios"),
    "nav_projects": T("Projects", "Proyectos"),
    "nav_education": T("Education", "Formación"),
    "nav_experience": T("Experience", "Experiencia"),
    "nav_skills": T("Skills", "Habilidades"),
    "nav_contact": T("Contact", "Contacto"),
    "skip": T("Skip to content", "Saltar al contenido"),
    "theme": T("Toggle colour theme", "Cambiar tema de color"),
    "lang_switch": T("Leer en español", "Read in English"),
    "lang_switch_short": T("ES", "EN"),
    "menu": T("Menu", "Menú"),
    "cta_projects": T("See my projects", "Ver mis proyectos"),
    "cta_cv": T("Download CV", "Descargar CV"),
    "how_i_work": T("How I work", "Cómo trabajo"),
    "featured": T("Featured projects", "Proyectos destacados"),
    "featured_title": T("Things I've built", "Lo que he construido"),
    "other_projects": T("More work on GitHub", "Más trabajo en GitHub"),
    "tech_stack": T("Tech stack used in these projects", "Stack tecnológico de estos proyectos"),
    "details": T("Read more", "Ver detalles"),
    "repo": T("Repository", "Repositorio"),
    "visit_site": T("Visit site", "Visitar web"),
    "education_title": T("Academic background", "Trayectoria académica"),
    "training": T("Additional training", "Formación complementaria"),
    "experience_title": T("Launching projects and building teams",
                          "Poner proyectos en marcha y formar equipos"),
    "skills_title": T("Skills and competencies", "Habilidades y competencias"),
    "languages": T("Languages", "Idiomas"),
    "competencies": T("Competencies", "Competencias"),
    "interests": T("Interests", "Intereses"),
    "contact_title": T("Let's talk", "Hablemos"),
    "contact_text": T(
        "Open to internships, junior roles and interesting projects in backend, applied AI "
        "and cybersecurity. Email is the fastest way to reach me.",
        "Abierto a prácticas, puestos junior y proyectos interesantes de backend, IA aplicada "
        "y ciberseguridad. El email es la forma más rápida de contactar conmigo.",
    ),
    "documents": T("Documents", "Documentos"),
    "back": T("Back to projects", "Volver a proyectos"),
    "screenshots": T("Screenshots", "Capturas"),
    "results": T("Results", "Resultados"),
    "footer": T("Built with Django, rendered to static HTML and published with GitHub Actions. "
                "No cookies, no analytics, no third-party scripts.",
                "Hecho con Django, renderizado a HTML estático y publicado con GitHub Actions. "
                "Sin cookies, sin analítica, sin scripts de terceros."),
    "source": T("Source code", "Código fuente"),
    "not_found_title": T("Page not found", "Página no encontrada"),
    "not_found_text": T("This page doesn't exist or has moved.",
                        "Esta página no existe o se ha movido."),
    "go_home": T("Go to the home page", "Ir a la página de inicio"),
    "meta_description": T(
        "Portfolio of José Luis López López, Computer Engineering student at the University of "
        "Granada: applied AI, cybersecurity and backend systems.",
        "Portfolio de José Luis López López, estudiante de Ingeniería Informática en la "
        "Universidad de Granada: IA aplicada, ciberseguridad y sistemas backend.",
    ),
}


def project_slugs():
    return [p["slug"] for p in FEATURED_PROJECTS]


def get_context(lang):
    """Everything the templates need, already localized."""
    return localize(
        {
            "profile": PROFILE,
            "highlights": HIGHLIGHTS,
            "about": ABOUT,
            "featured_projects": FEATURED_PROJECTS,
            "other_projects": OTHER_PROJECTS,
            "tech_stack": TECH_STACK,
            "education": EDUCATION,
            "training": TRAINING,
            "experience_intro": EXPERIENCE_INTRO,
            "experience": EXPERIENCE,
            "skills": SKILLS,
            "languages": LANGUAGES,
            "competencies": COMPETENCIES,
            "interests": INTERESTS,
            "documents": DOCUMENTS,
            "ui": UI,
        },
        lang,
    )
