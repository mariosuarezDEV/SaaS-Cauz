<script setup>
import { RouterLink } from 'vue-router'
</script>
<template>
  <div class="navbar bg-base-100 shadow-lg">
    <div className="navbar-start">
      <div className="dropdown">
        <div tabIndex="{0}" role="button" className="btn btn-ghost btn-circle">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            className="h-5 w-5"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
          >
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth="2"
              d="M4 6h16M4 12h16M4 18h7"
            />
          </svg>
        </div>
        <ul
          tabIndex="{0}"
          class="menu menu-sm dropdown-content bg-base-100 rounded-box z-1 mt-3 w-52 p-2 shadow"
        >
          <li><RouterLink to="/" class="btn btn-outline m-2 text-base">Inicio</RouterLink></li>
          <li><button class="btn btn-outline m-2 text-base">Eventos</button></li>
          <!-- Usar router link -->
          <li>
            <RouterLink to="/solicitud" class="btn btn-outline m-2 text-base"
              >Quiero presentarme</RouterLink
            >
          </li>
        </ul>
      </div>
    </div>
    <div className="navbar-center">
      <p className="text-2xl font-bold">Cauz | Foro & Libreria</p>
    </div>
    <div className="navbar-end"></div>
  </div>
</template>
