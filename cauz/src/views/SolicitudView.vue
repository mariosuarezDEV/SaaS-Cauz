<script setup>
import NavBar from '@/components/NavBar.vue'
import { reactive } from 'vue'
import axios from 'axios'

const postulante = reactive({
  nombre: '',
  apellido_paterno: '',
  apellido_materno: '',
  correo: '',
  telefono: '',
})

const enviarSolicitud = async () => {
  try {
    const response = await axios.post(
      'http://192.168.1.228:4000/postulantes/api/postulantes/',
      postulante,
    )
    console.log(response)
  } catch (error) {
    console.error(error)
  }
}
</script>

<template>
  <NavBar />
  <div class="container mx-auto mt-10">
    <!-- Inicio de presentacion -->
    <div>
      <h1 class="text-4xl font-bold text-center">Quiero presentarme</h1>
      <p class="text-center text-lg mt-3">
        ¡Estamos emocionados de que quieras compartir tu talento con nosotros! Por favor, llena el
        siguiente formulario para que podamos conocerte mejor.
      </p>
    </div>
    <!-- Formulario de presentacion -->
    <div class="card bg-base-100 shadow-xl mt-6">
      <form class="card-body" @submit.prevent="enviarSolicitud">
        <h2 class="card-title text-2xl mb-2">Cuentanos sobre ti.</h2>
        <!-- Información de postulante -->
        <div class="grid grid-cols-2 justify-items-center gap-3">
          <label class="input input-bordered gap-2 col-span-2 w-full">
            Nombre(s)<span class="text-red-700">*</span>:
            <input type="text" class="grow" placeholder="Daisy" v-model="postulante.nombre" />
          </label>
          <label class="input input-bordered gap-2 col-span-1 w-full">
            Apellidos Paterno:
            <input
              type="text"
              class="grow"
              placeholder="Daisy"
              v-model="postulante.apellido_paterno"
            />
          </label>
          <label class="input input-bordered gap-2 col-span-1 w-full">
            Apellidos Materno<span class="text-red-700">*</span>:
            <input
              type="text"
              class="grow"
              placeholder="Daisy"
              v-model="postulante.apellido_materno"
            />
          </label>
          <label class="input input-bordered gap-2 col-span-1 w-full">
            Correo<span class="text-red-700">*</span>:
            <input type="email" class="grow" placeholder="Daisy" v-model="postulante.correo" />
          </label>
          <label class="input input-bordered gap-2 col-span-1 w-full">
            Número de teléfono<span class="text-red-700">*</span>:
            <input type="text" class="grow" placeholder="Daisy" v-model="postulante.telefono" />
          </label>
        </div>
        <p>
          {{ postulante.nombre }} {{ postulante.apellido_paterno }}
          {{ postulante.apellido_materno }} {{ postulante.correo_electronico }}
          {{ postulante.telefono }}
        </p>
        <!-- Informacion de solicitud -->
        <h2 class="card-title text-2xl mb-2 mt-6">¿Qué tipo de presentación te gustaría hacer?</h2>
        <button class="btn btn-primary">Enviar datos</button>
      </form>
    </div>
  </div>
</template>
