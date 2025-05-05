import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  build: {
    outDir: 'dist', // Ensure the output directory is 'dist'
    target: 'esnext', // Set the target to 'esnext' for modern browsers
    minify: true, // Minify the output
    emptyOutDir: true, // Clear the output directory before building
  },
});
