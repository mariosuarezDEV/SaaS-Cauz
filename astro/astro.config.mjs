// @ts-check
import { defineConfig } from 'astro/config';

import tailwindcss from '@tailwindcss/vite';

// https://astro.build/config
export default defineConfig({
  server:{
      host: '0.0.0.0',
      port: 4003,
  },

  vite: {
    plugins: [tailwindcss()]
  },
});