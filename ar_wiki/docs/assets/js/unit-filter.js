document.addEventListener("alpine:init", () => {
    console.log("Alpine Init: Registering unitFilterSystem..."); // Debug line
    Alpine.data("unitFilterSystem", () => ({
        search_term: "",
        selected_rarities: [],
        selected_elements: [],
        filter_open: false,

        rarities: ["Royalty", "Secret", "Mythic", "Legendary", "Epic", "Rare"],
        elements: ['Fire', 'Fighting', 'Psychic', 'Grass', 'Electric', 'Dark', 'Poison', 'Steel', 'Holy', 'Wind', 'Ice', 'Neutral', 'Ground', 'Water', 'Rock'],

        clear_filters() {
            this.search_term = "";
            this.selected_elements = [];
            this.selected_rarities = [];
        },

        toggle_rarity(val) {
            this.selected_rarities.includes(val)
                ? this.selected_rarities = this.selected_rarities.filter(i => i !== val)
                : this.selected_rarities.push(val)
            console.log("Selected Rarities:", JSON.parse(JSON.stringify(this.selected_rarities)));
        },

        toggle_element(val) {
            this.selected_elements.includes(val)
                ? this.selected_elements = this.selected_elements.filter(i => i !== val)
                : this.selected_elements.push(val)
            console.log("Selected Elements:", JSON.parse(JSON.stringify(this.selected_elements)));
        }
    }));
});