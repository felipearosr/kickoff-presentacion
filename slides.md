---
theme: default
title: Reunión de Inicio de Proyecto
info: |
  Presentación de kickoff para el proyecto.
  Template corporativo.
class: text-center
drawings:
  persist: false
transition: slide-left
mdc: true
---

<div class="absolute inset-0">
  <img src="/hero-cover.jpg" class="w-full h-full object-cover" />
  <div class="absolute inset-0 bg-gradient-to-r from-stone-950/95 via-stone-950/85 to-stone-900/60"></div>
</div>

<div class="relative z-10 flex flex-col justify-center h-full text-left px-16">
  <div class="mb-6">
    <span class="px-3 py-1 rounded-full bg-rose-600 text-white text-xs font-semibold uppercase tracking-widest">Kickoff del Proyecto</span>
  </div>
  <div class="text-5xl font-black text-white leading-tight mb-4" style="text-shadow: 0 2px 20px rgba(0,0,0,0.5);">Reunión de Inicio<br/>de Proyecto</div>
  <p class="text-lg text-white max-w-xl leading-relaxed font-medium" style="text-shadow: 0 1px 10px rgba(0,0,0,0.5);">Sistema de Configuración de Prendas On-Demand y Gestión Interna de Negocio Independiente de Confección</p>
  <div class="mt-10 flex items-center gap-6">
    <span class="text-sm text-white font-medium">01 / Abril / 2026</span>
    <span class="w-12 h-px bg-white/40"></span>
  </div>
</div>

<style>
.slidev-layout { padding: 0 !important; }
</style>

---
transition: fade-out
layout: default
---

# Agenda

<div class="grid grid-cols-2 gap-6 mt-20">

<v-click>
<div class="p-4 rounded-2xl bg-stone-50 border border-stone-200 space-y-3">
  <div class="flex items-center gap-3">
    <span class="w-8 h-8 rounded-lg bg-rose-600 text-white font-bold text-sm flex items-center justify-center shrink-0">1</span>
    <span class="text-sm font-semibold text-stone-700">Contexto de la iniciativa</span>
  </div>
  <div class="flex items-center gap-3">
    <span class="w-8 h-8 rounded-lg bg-rose-600 text-white font-bold text-sm flex items-center justify-center shrink-0">2</span>
    <span class="text-sm font-semibold text-stone-700">Situación futura</span>
  </div>
  <div class="flex items-center gap-3">
    <span class="w-8 h-8 rounded-lg bg-rose-600 text-white font-bold text-sm flex items-center justify-center shrink-0">3</span>
    <div><span class="text-sm font-semibold text-stone-700">Objetivos del proyecto</span><br/><span class="text-xs text-stone-500">General y Específicos</span></div>
  </div>
  <div class="flex items-center gap-3">
    <span class="w-8 h-8 rounded-lg bg-rose-600 text-white font-bold text-sm flex items-center justify-center shrink-0">4</span>
    <span class="text-sm font-semibold text-stone-700">Justificación y beneficios</span>
  </div>
</div>
</v-click>

<v-click>
<div class="p-4 rounded-2xl bg-stone-50 border border-stone-200 space-y-3">
  <div class="flex items-center gap-3">
    <span class="w-8 h-8 rounded-lg bg-stone-700 text-white font-bold text-sm flex items-center justify-center shrink-0">5</span>
    <span class="text-sm font-semibold text-stone-700">Alcance del proyecto</span>
  </div>
  <div class="flex items-center gap-3">
    <span class="w-8 h-8 rounded-lg bg-stone-700 text-white font-bold text-sm flex items-center justify-center shrink-0">6</span>
    <span class="text-sm font-semibold text-stone-700">Arquitectura de la solución</span>
  </div>
  <div class="flex items-center gap-3">
    <span class="w-8 h-8 rounded-lg bg-stone-700 text-white font-bold text-sm flex items-center justify-center shrink-0">7</span>
    <div><span class="text-sm font-semibold text-stone-700">Estrategia de implementación</span><br/><span class="text-xs text-stone-500">Plan, cronograma, riesgos y equipo</span></div>
  </div>
</div>
</v-click>

</div>

<SlideNum num="02" />

---
transition: slide-left
layout: default
---

# Contexto de la Iniciativa

<div class="grid grid-cols-7 gap-x-6 gap-y-3 mt-10">

<v-click>
<div class="col-span-5 p-3 rounded-xl bg-stone-50 border border-stone-200">
  <span class="text-rose-600 font-bold">01</span> <span class="text-stone-700">— El sector de confección independiente sufre de alta desorganización logística y falta de límites laborales</span>
</div>
<div class="col-span-2 relative overflow-hidden rounded-xl border border-stone-200">
  <img src="/contexto-01.jpg" class="absolute inset-0 w-full h-full object-cover" alt="Desorganización" />
</div>
</v-click>

<v-click>
<div class="col-span-5 p-3 rounded-xl bg-stone-50 border border-stone-200">
  <span class="text-rose-600 font-bold">02</span> <span class="text-stone-700">— Dependencia de WhatsApp genera invasión a la privacidad y alta carga mental en el emprendedor</span>
</div>
<div class="col-span-2 relative overflow-hidden rounded-xl border border-stone-200">
  <img src="/contexto-02.jpg" class="absolute inset-0 w-full h-full object-cover" style="object-position: center 60%;" alt="WhatsApp" />
</div>
</v-click>

<v-click>
<div class="col-span-5 p-3 rounded-xl bg-stone-50 border border-stone-200">
  <span class="text-rose-600 font-bold">03</span> <span class="text-stone-700">— Gestión manual de ventas, catálogos, citas e inventario genera ineficiencias operativas</span>
</div>
<div class="col-span-2 relative overflow-hidden rounded-xl border border-stone-200">
  <img src="/contexto-03.jpg" class="absolute inset-0 w-full h-full object-cover" alt="Gestión manual" />
</div>
</v-click>

<v-click>
<div class="col-span-5 p-3 rounded-xl bg-stone-50 border border-stone-200">
  <span class="text-rose-600 font-bold">04</span> <span class="text-stone-700">— Necesidad de profesionalizar el servicio y optimizar el uso de recursos del negocio</span>
</div>
<div class="col-span-2 relative overflow-hidden rounded-xl border border-stone-200">
  <img src="/contexto-04.jpg" class="absolute inset-0 w-full h-full object-cover" style="object-position: center 80%;" alt="Profesionalización" />
</div>
</v-click>

</div>

<SlideNum num="03" />

---
transition: fade-out
layout: default
---

# Situación Futura

<div class="mt-20 p-8 rounded-2xl bg-stone-50 border border-stone-200">

<v-click>

<p class="text-lg leading-relaxed text-stone-700">
  Digitalizar y automatizar el flujo operativo del negocio de confección, centralizando ventas, catálogos, agendamiento de citas y comunicación en una sola plataforma tecnológica, eliminando la carga mental y las ineficiencias de la gestión manual.
</p>

</v-click>

<v-click>

<div class="mt-6 flex gap-4">
  <div class="flex-1 p-4 rounded-xl bg-white border border-stone-200 text-center">
    <div class="text-rose-600 font-bold text-lg mb-1">Plataforma web</div>
    <div class="text-sm text-stone-500">centralizada</div>
  </div>
  <div class="flex-1 p-4 rounded-xl bg-white border border-stone-200 text-center">
    <div class="text-rose-600 font-bold text-lg mb-1">80% migración</div>
    <div class="text-sm text-stone-500">desde WhatsApp</div>
  </div>
  <div class="flex-1 p-4 rounded-xl bg-white border border-stone-200 text-center">
    <div class="text-rose-600 font-bold text-lg mb-1">Automatización</div>
    <div class="text-sm text-stone-500">operativa</div>
  </div>
</div>

</v-click>

</div>

<SlideNum num="04" />

---
transition: slide-left
layout: default
---

# Objetivos del Proyecto

<div class="grid grid-cols-5 gap-6 mt-16">

<v-click>
<div class="col-span-3 p-5 rounded-2xl bg-stone-50 border border-stone-200">
  <h3 class="text-rose-600 font-bold mb-3">Objetivo General</h3>
  <p class="text-stone-700 leading-relaxed">
    Implementar un ecosistema digital (página web) de gestión para negocios de confección bajo demanda, que centralice la configuración de prendas, reserva de citas y la administración operativa para maximizar la eficiencia del servicio.
  </p>
</div>
</v-click>

<v-click>
<div class="col-span-2 grid grid-rows-4 gap-3">
  <div class="p-3 rounded-xl bg-stone-50 border border-stone-200 flex items-center gap-3">
    <span class="w-8 h-8 rounded-lg bg-rose-600 text-white font-bold flex items-center justify-center shrink-0">1</span>
    <span class="text-sm text-stone-700">Interfaz web para configuración de prendas y catálogos dinámicos</span>
  </div>
  <div class="p-3 rounded-xl bg-stone-50 border border-stone-200 flex items-center gap-3">
    <span class="w-8 h-8 rounded-lg bg-rose-500 text-white font-bold flex items-center justify-center shrink-0">2</span>
    <span class="text-sm text-stone-700">Módulo de agendamiento automatizado para toma de medidas y pruebas</span>
  </div>
  <div class="p-3 rounded-xl bg-stone-50 border border-stone-200 flex items-center gap-3">
    <span class="w-8 h-8 rounded-lg bg-rose-400 text-white font-bold flex items-center justify-center shrink-0">3</span>
    <span class="text-sm text-stone-700">Sistema de notificaciones inteligentes vía correo y mensajería</span>
  </div>
  <div class="p-3 rounded-xl bg-stone-50 border border-stone-200 flex items-center gap-3">
    <span class="w-8 h-8 rounded-lg bg-rose-300 text-white font-bold flex items-center justify-center shrink-0">4</span>
    <span class="text-sm text-stone-700">Dashboard administrativo para gestión de inventario de insumos</span>
  </div>
</div>
</v-click>

</div>

<v-click>
<div class="text-center text-xs text-stone-400 mt-4">Objetivos Específicos alineados al objetivo general del proyecto</div>
</v-click>

<SlideNum num="05" />

---
transition: fade-out
layout: default
---

# Justificación y Beneficios

<div class="grid grid-cols-3 gap-6 mt-20">

<v-click>
<div class="p-6 rounded-2xl bg-stone-50 border border-stone-200">
  <h3 class="text-rose-600 font-bold mb-3">Eficiencia</h3>
  <ul class="text-sm space-y-2 text-stone-600">
    <li>Automatización de tareas repetitivas y consultas frecuentes</li>
    <li>Optimización del uso de recursos</li>
    <li>Eliminación de gestión manual</li>
  </ul>
</div>
</v-click>

<v-click>
<div class="p-6 rounded-2xl bg-stone-50 border border-stone-200">
  <h3 class="text-rose-600 font-bold mb-3">Calidad de Vida</h3>
  <ul class="text-sm space-y-2 text-stone-600">
    <li>Reducción de la carga mental del emprendedor</li>
    <li>Separación vida personal/laboral</li>
    <li>Fin de la dependencia de WhatsApp</li>
  </ul>
</div>
</v-click>

<v-click>
<div class="p-6 rounded-2xl bg-stone-50 border border-stone-200">
  <h3 class="text-rose-600 font-bold mb-3">Profesionalización</h3>
  <ul class="text-sm space-y-2 text-stone-600">
    <li>100% trazabilidad de transacciones y citas</li>
    <li>Control preciso de stock de insumos</li>
    <li>Imagen profesional ante el cliente</li>
  </ul>
</div>
</v-click>

</div>

<SlideNum num="06" />

---
transition: slide-left
layout: default
---

# Alcance del Proyecto

<div class="mt-16">

<v-click>
<div class="p-6 rounded-2xl bg-stone-50 border border-stone-200 mb-4">
  <h3 class="text-rose-600 font-bold mb-2">Dentro del Alcance</h3>
  <ul class="text-sm space-y-1 text-stone-600">
    <li><strong class="text-stone-700">Módulo Principal</strong> — Catálogo digital interactivo, configurador de prendas on-demand y sistema de reserva de citas</li>
    <li><strong class="text-stone-700">Módulo de Administración</strong> — Gestión de inventario de materiales (telas, hilos, etc.), historial de clientes y panel de control de ventas</li>
    <li><strong class="text-stone-700">Notificaciones</strong> — Sistema de notificaciones inteligentes vía correo y mensajería</li>
  </ul>
</div>
</v-click>

<v-click>
<div class="p-6 rounded-2xl bg-stone-50 border border-stone-200">
  <h3 class="text-stone-400 font-bold mb-2">Condicional</h3>
  <ul class="text-sm space-y-1 text-stone-500">
    <li><strong class="text-stone-600">Comunicación</strong> — Chatbot para preguntas frecuentes y recordatorios automáticos de entregas (sujeto a acuerdo)</li>
  </ul>
</div>
</v-click>

</div>

<SlideNum num="07" />

---
transition: fade-out
layout: default
---

# Arquitectura Global de la Solución

<div class="grid grid-cols-11 gap-3 mt-16 items-center">

<v-click>
<div class="col-span-3 space-y-3">
  <div class="text-xs font-bold text-rose-600 uppercase tracking-wider mb-2 text-center">Plataforma Web</div>
  <div class="p-3 rounded-xl bg-rose-50 border border-rose-200 text-center">
    <div class="text-sm font-semibold text-stone-700">Catálogo Digital</div>
    <div class="text-xs text-stone-500">& Configurador</div>
  </div>
  <div class="p-3 rounded-xl bg-rose-50 border border-rose-200 text-center">
    <div class="text-sm font-semibold text-stone-700">Agendamiento</div>
    <div class="text-xs text-stone-500">de Citas</div>
  </div>
  <div class="p-3 rounded-xl bg-rose-50 border border-rose-200 text-center">
    <div class="text-sm font-semibold text-stone-700">Dashboard</div>
    <div class="text-xs text-stone-500">Administrativo</div>
  </div>
</div>
</v-click>

<v-click>
<div class="col-span-1 flex items-center justify-center">
  <div class="text-2xl text-stone-500 font-light">&rarr;</div>
</div>
</v-click>

<v-click>
<div class="col-span-3 space-y-3">
  <div class="text-xs font-bold text-stone-500 uppercase tracking-wider mb-2 text-center">Servicios</div>
  <div class="p-4 rounded-xl bg-stone-800 text-center">
    <div class="text-sm font-semibold text-white">API Central</div>
    <div class="text-xs text-stone-300">Lógica de negocio</div>
  </div>
  <div class="p-3 rounded-xl bg-stone-50 border border-stone-200 text-center">
    <div class="text-sm font-semibold text-stone-700">Notificaciones</div>
    <div class="text-xs text-stone-500">Correo & Mensajería</div>
  </div>
</div>
</v-click>

<v-click>
<div class="col-span-1 flex items-center justify-center">
  <div class="text-2xl text-stone-500 font-light">&rarr;</div>
</div>
</v-click>

<v-click>
<div class="col-span-3 space-y-3">
  <div class="text-xs font-bold text-stone-500 uppercase tracking-wider mb-2 text-center">Datos</div>
  <div class="p-4 rounded-xl bg-stone-50 border border-stone-200 text-center">
    <div class="w-10 h-10 mx-auto mb-2 rounded-full bg-stone-200 flex items-center justify-center">
      <div class="w-5 h-3 rounded-sm bg-stone-400"></div>
    </div>
    <div class="text-sm font-semibold text-stone-700">Base de Datos</div>
  </div>
  <div class="p-4 rounded-xl bg-stone-50 border border-stone-200 text-center">
    <div class="w-10 h-10 mx-auto mb-2 rounded-full bg-stone-200 flex items-center justify-center">
      <div class="w-5 h-3 rounded-sm bg-stone-400"></div>
    </div>
    <div class="text-sm font-semibold text-stone-700">Inventario</div>
    <div class="text-xs text-stone-500">Materiales</div>
  </div>
</div>
</v-click>

</div>

<v-click>
<div class="mt-4 text-center text-sm text-stone-500">
  Diagrama simplificado — arquitectura sujeta a definición en Fase de Diseño (Semanas 7-10)
</div>
</v-click>

<SlideNum num="08" />

---
transition: slide-left
layout: default
---

# Estrategia de Implementación
## Plan de Alto Nivel

<div class="mt-20">

<!-- Timeline bar -->
<div class="relative">
  <div class="absolute top-5 left-0 right-0 h-1 bg-stone-200 rounded-full"></div>
  <div class="grid grid-cols-4 gap-4 relative">

<v-click>
  <div class="text-center">
    <div class="w-10 h-10 mx-auto rounded-full bg-rose-600 text-white font-bold text-sm flex items-center justify-center relative z-10">1</div>
    <div class="mt-4 p-4 rounded-2xl bg-rose-50 border border-rose-200 h-32 flex flex-col justify-center">
      <div class="font-bold text-stone-800 text-sm">Kickoff & Requerimientos</div>
      <div class="text-xs text-stone-400 mt-1">Semanas 1–2</div>
      <div class="mt-3 text-xs text-rose-600 font-semibold">Marzo</div>
      <div class="text-xs text-stone-400">2 semanas</div>
    </div>
  </div>
</v-click>

<v-click>
  <div class="text-center">
    <div class="w-10 h-10 mx-auto rounded-full bg-rose-500 text-white font-bold text-sm flex items-center justify-center relative z-10">2</div>
    <div class="mt-4 p-4 rounded-2xl bg-rose-50 border border-rose-200 h-32 flex flex-col justify-center">
      <div class="font-bold text-stone-800 text-sm">Sprints de Desarrollo</div>
      <div class="text-xs text-stone-400 mt-1">Semanas 3–6</div>
      <div class="mt-3 text-xs text-rose-600 font-semibold">Abril</div>
      <div class="text-xs text-stone-400">4 semanas</div>
    </div>
  </div>
</v-click>

<v-click>
  <div class="text-center">
    <div class="w-10 h-10 mx-auto rounded-full bg-rose-400 text-white font-bold text-sm flex items-center justify-center relative z-10">3</div>
    <div class="mt-4 p-4 rounded-2xl bg-stone-50 border border-stone-200 h-32 flex flex-col justify-center">
      <div class="font-bold text-stone-800 text-sm">Arquitectura, UI/UX & BD</div>
      <div class="text-xs text-stone-400 mt-1">Semanas 7–10</div>
      <div class="mt-3 text-xs text-rose-600 font-semibold">Mayo</div>
      <div class="text-xs text-stone-400">4 semanas</div>
    </div>
  </div>
</v-click>

<v-click>
  <div class="text-center">
    <div class="w-10 h-10 mx-auto rounded-full bg-rose-300 text-white font-bold text-sm flex items-center justify-center relative z-10">4</div>
    <div class="mt-4 p-4 rounded-2xl bg-stone-50 border border-stone-200 h-32 flex flex-col justify-center">
      <div class="font-bold text-stone-800 text-sm">QA, Pruebas & Entrega</div>
      <div class="text-xs text-stone-400 mt-1">Semanas 11–12</div>
      <div class="mt-3 text-xs text-rose-600 font-semibold">Junio</div>
      <div class="text-xs text-stone-400">2 semanas</div>
    </div>
  </div>
</v-click>

  </div>
</div>

</div>

<v-click>
<div class="mt-6 text-center text-sm text-stone-400">12 semanas de ejecución — Marzo a Junio 2026</div>
</v-click>

<SlideNum num="09" />

---
transition: fade-out
layout: default
---

# Estrategia de Implementación
## Cronograma de Trabajo

<div class="mt-8 space-y-1.5">
<div class="grid grid-cols-12 gap-0 ml-32 mr-2">
  <div class="text-center text-xs text-stone-500 font-medium">S1</div>
  <div class="text-center text-xs text-stone-500 font-medium">S2</div>
  <div class="text-center text-xs text-stone-500 font-medium">S3</div>
  <div class="text-center text-xs text-stone-500 font-medium">S4</div>
  <div class="text-center text-xs text-stone-500 font-medium">S5</div>
  <div class="text-center text-xs text-stone-500 font-medium">S6</div>
  <div class="text-center text-xs text-stone-500 font-medium">S7</div>
  <div class="text-center text-xs text-stone-500 font-medium">S8</div>
  <div class="text-center text-xs text-stone-500 font-medium">S9</div>
  <div class="text-center text-xs text-stone-500 font-medium">S10</div>
  <div class="text-center text-xs text-stone-500 font-medium">S11</div>
  <div class="text-center text-xs text-stone-500 font-medium">S12</div>
</div>
<div class="flex items-start gap-3">
  <div class="w-28 shrink-0 pt-1"><div class="text-sm font-bold text-stone-700">Fase 1</div><div class="text-xs text-stone-500">Marzo</div></div>
  <div class="flex-1 grid grid-cols-12 gap-0.5">
    <div class="col-span-2 rounded bg-rose-600 h-5 flex items-center justify-center text-[11px] text-white font-medium">Kickoff & Req.</div>
    <div class="col-span-10"></div>
  </div>
</div>
<div class="flex items-start gap-3">
  <div class="w-28 shrink-0 pt-1"><div class="text-sm font-bold text-stone-700">Fase 2</div><div class="text-xs text-stone-500">Abril</div></div>
  <div class="flex-1 space-y-0.5">
    <div class="grid grid-cols-12 gap-0.5">
      <div class="col-span-2"></div>
      <div class="col-span-2 rounded bg-rose-600 h-5 flex items-center justify-center text-[11px] text-white font-medium">Configurador</div>
      <div class="col-span-8"></div>
    </div>
    <div class="grid grid-cols-12 gap-0.5">
      <div class="col-span-2"></div>
      <div class="col-span-3 rounded bg-rose-600 h-5 flex items-center justify-center text-[11px] text-white">Catálogo</div>
      <div class="col-span-7"></div>
    </div>
    <div class="grid grid-cols-12 gap-0.5">
      <div class="col-span-4"></div>
      <div class="col-span-3 rounded bg-rose-600 h-5 flex items-center justify-center text-[11px] text-white">Agendamiento</div>
      <div class="col-span-5"></div>
    </div>
    <div class="grid grid-cols-12 gap-0.5">
      <div class="col-span-4"></div>
      <div class="col-span-2 rounded bg-stone-600 h-5 flex items-center justify-center text-[11px] text-white">Feedback</div>
      <div class="col-span-6"></div>
    </div>
  </div>
</div>
<div class="flex items-start gap-3">
  <div class="w-28 shrink-0 pt-1"><div class="text-sm font-bold text-stone-700">Fase 3</div><div class="text-xs text-stone-500">Mayo</div></div>
  <div class="flex-1 space-y-0.5">
    <div class="grid grid-cols-12 gap-0.5">
      <div class="col-span-6"></div>
      <div class="col-span-2 rounded bg-rose-600 h-5 flex items-center justify-center text-[11px] text-white font-medium">Arquitectura</div>
      <div class="col-span-4"></div>
    </div>
    <div class="grid grid-cols-12 gap-0.5">
      <div class="col-span-6"></div>
      <div class="col-span-3 rounded bg-rose-600 h-5 flex items-center justify-center text-[11px] text-white">UI/UX</div>
      <div class="col-span-3"></div>
    </div>
    <div class="grid grid-cols-12 gap-0.5">
      <div class="col-span-8"></div>
      <div class="col-span-2 rounded bg-rose-600 h-5 flex items-center justify-center text-[11px] text-white">Inventario</div>
      <div class="col-span-2"></div>
    </div>
    <div class="grid grid-cols-12 gap-0.5">
      <div class="col-span-8"></div>
      <div class="col-span-2 rounded bg-stone-600 h-5 flex items-center justify-center text-[11px] text-white">Feedback</div>
      <div class="col-span-2"></div>
    </div>
  </div>
</div>
<div class="flex items-start gap-3">
  <div class="w-28 shrink-0 pt-1"><div class="text-sm font-bold text-stone-700">Fase 4</div><div class="text-xs text-stone-500">Junio</div></div>
  <div class="flex-1 space-y-0.5">
    <div class="grid grid-cols-12 gap-0.5">
      <div class="col-span-10"></div>
      <div class="col-span-2 rounded bg-rose-600 h-5 flex items-center justify-center text-[11px] text-white font-medium">QA & Pruebas</div>
    </div>
    <div class="grid grid-cols-12 gap-0.5">
      <div class="col-span-11"></div>
      <div class="col-span-1 rounded bg-stone-600 h-5 flex items-center justify-center text-[11px] text-white">Cap.</div>
    </div>
  </div>
</div>
</div>

<SlideNum num="10" />

---
transition: slide-left
layout: default
---

# Estrategia de Implementación
## Principales Riesgos

<div class="mt-14">

<div class="grid grid-cols-2 gap-6">

<v-click>
<div class="p-5 rounded-2xl bg-stone-50 border border-stone-200">
  <h3 class="text-rose-600 font-bold mb-3">Gestión y Documentación</h3>
  <ul class="text-sm space-y-3 text-stone-600">
    <li><strong class="text-stone-700">Desfase cronológico:</strong> Cualquier retraso en diseño afecta desarrollo. <em class="text-stone-400">Mitigación: Scrum y priorización de MVP</em></li>
    <li><strong class="text-stone-700">Pérdida de datos:</strong> Inconsistencia en documentación técnica. <em class="text-stone-400">Mitigación: GitHub y respaldos en la nube</em></li>
    <li><strong class="text-stone-700">Brechas de comunicación:</strong> Desincronía Backend/Frontend. <em class="text-stone-400">Mitigación: Reuniones semanales de coordinación</em></li>
  </ul>
</div>
</v-click>

<v-click>
<div class="p-5 rounded-2xl bg-stone-50 border border-stone-200">
  <h3 class="text-rose-600 font-bold mb-3">Operativos y Desarrollo</h3>
  <ul class="text-sm space-y-3 text-stone-600">
    <li><strong class="text-stone-700">Resistencia al cambio:</strong> Preferencia por WhatsApp. <em class="text-stone-400">Mitigación: UX extremadamente sencilla e intuitiva</em></li>
    <li><strong class="text-stone-700">Desviación del alcance:</strong> Priorizar funcionalidades secundarias. <em class="text-stone-400">Mitigación: Control estricto del Product Backlog</em></li>
    <li><strong class="text-stone-700">Bugs críticos:</strong> Errores en inventario o citas. <em class="text-stone-400">Mitigación: Testing exhaustivo y pruebas unitarias</em></li>
  </ul>
</div>
</v-click>

</div>

</div>

<SlideNum num="11" />

---
transition: fade-out
layout: default
---

# Estrategia de Implementación
## Equipo de Trabajo

<div class="grid grid-cols-2 gap-8 mt-14">

<div>
<h3 class="text-rose-600 font-bold mb-4">Equipo del Proyecto</h3>

<v-clicks>

<div class="flex items-center gap-3 p-3 rounded-lg bg-stone-50 border border-stone-200 mb-2">
  <div class="w-10 h-10 rounded-full bg-rose-600 flex items-center justify-center text-sm font-bold text-white">BM</div>
  <div><div class="font-medium text-stone-800">Benjamín Morales</div><div class="text-xs text-stone-400">UI/UX, Product Owner & Gerente del Proyecto</div></div>
</div>

<div class="flex items-center gap-3 p-3 rounded-lg bg-stone-50 border border-stone-200 mb-2">
  <div class="w-10 h-10 rounded-full bg-rose-500 flex items-center justify-center text-sm font-bold text-white">FA</div>
  <div><div class="font-medium text-stone-800">Felipe Aros</div><div class="text-xs text-stone-400">Desarrollador Backend — lógica de negocios y requerimientos</div></div>
</div>

<div class="flex items-center gap-3 p-3 rounded-lg bg-stone-50 border border-stone-200 mb-2">
  <div class="w-10 h-10 rounded-full bg-rose-400 flex items-center justify-center text-sm font-bold text-white">PM</div>
  <div><div class="font-medium text-stone-800">Philip Magna</div><div class="text-xs text-stone-400">Desarrollador Frontend — vistas, calendario y paneles</div></div>
</div>

</v-clicks>

</div>

<div>
<h3 class="text-stone-500 font-bold mb-4">Stakeholders</h3>

<v-clicks>

<div class="flex items-center gap-3 p-3 rounded-lg bg-stone-50 border border-stone-200 mb-2">
  <div class="w-10 h-10 rounded-full bg-stone-500 flex items-center justify-center text-sm font-bold text-white">CL</div>
  <div><div class="font-medium text-stone-800">Cliente Independiente de Confección</div><div class="text-xs text-stone-400">Patrocinador — requerimientos y validación</div></div>
</div>

<div class="flex items-center gap-3 p-3 rounded-lg bg-stone-50 border border-stone-200 mb-2">
  <div class="w-10 h-10 rounded-full bg-stone-400 flex items-center justify-center text-sm font-bold text-white">CO</div>
  <div><div class="font-medium text-stone-800">Cristian Osorio</div><div class="text-xs text-stone-400">Profesor — Proyecto en TICs II</div></div>
</div>

</v-clicks>

</div>
</div>

<SlideNum num="12" />

---
layout: center
class: text-center
transition: fade-out
---

<div class="text-6xl font-bold mb-8 text-stone-800" style="font-family: 'Adamina', serif !important;">
  ¿Preguntas?
</div>

<div class="text-lg text-stone-400">
  Gracias por su atención
</div>

<SlideNum num="13" />

