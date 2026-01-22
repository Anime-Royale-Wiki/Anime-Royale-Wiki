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
    extend: {
      colors: {
        'rarity-royalty': '#fac415',
        'rarity-secret': '#f43f5e',
        'rarity-mythic': '#a855f7',
        'rarity-legendary': '#eab308',
        'rarity-epic': '',
        'rarity-rare': ''
      }
    } 
  },
  plugins: [],
}