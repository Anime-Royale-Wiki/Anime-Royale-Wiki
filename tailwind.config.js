/** @type {import('tailwindcss').Config} */
module.exports = {
  important: '#tailwind-scope',
  corePlugins: {
    preflight: false,
  },
  content: [
    "./ar_wiki/docs/**/*.md", 
    "./ar_wiki/docs/Templates/**/*.html",
    "./ar_wiki/docs/**/*.js" 
  ],
  theme: { 
    extend: {} 
  },
  plugins: [],
}