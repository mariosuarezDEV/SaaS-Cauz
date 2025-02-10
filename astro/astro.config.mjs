// @ts-check
import { defineConfig } from 'astro/config';

import tailwindcss from '@tailwindcss/vite';

// https://astro.build/config
export default defineConfig({
  server:{
      port: 4003,
      host: '0.0.0.0'
  },

  vite: {
    plugins: [tailwindcss()]
  }
});