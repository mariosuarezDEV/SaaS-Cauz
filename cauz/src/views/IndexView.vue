<script setup>
import { RouterLink, RouterView } from 'vue-router'
import NavBar from '@/components/NavBar.vue'
</script>
<template>
  <div class="hero bg-base-200 min-h-screen">
    <div class="hero-content text-center">
      <div class="max-w-md">
        <h1 class="text-6xl font-bold">Cauz</h1>
        <h1 class="text-5xl font-bold">Foro & Libreria</h1>

        <p class="py-6">
          Aquí, cada presentación es una experiencia única, cada historia encuentra su voz y cada
          expresión artística conecta con quienes buscan inspiración.
        </p>
        <div class="flex justify-center space-x-4">
          <button class="btn btn-primary">¡Ver eventos!</button>
          <RouterLink to="/solicitud" class="btn btn-neutral">Quiero presentarme</RouterLink>
        </div>
      </div>
    </div>
  </div>
</template>
