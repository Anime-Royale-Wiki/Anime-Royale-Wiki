if (!window.unitFilterRegistered) {
    document.addEventListener("alpine:init", () => {
        Alpine.data("unitFilterSystem", () => ({
            search_term: "",
            selected_rarities: [],
            selected_elements: [],
            filter_open: false,
            iso: null,
            rarities: ["Royalty", "Secret", "Mythic", "Legendary", "Epic", "Rare"],
            elements: ['Fire', 'Fighting', 'Psychic', 'Grass', 'Electric', 'Dark', 'Poison', 'Steel', 'Holy', 'Wind', 'Ice', 'Neutral', 'Ground', 'Water', 'Rock'],

            init() {
                this.$nextTick(() => {
                    if (window.Isotope) {
                        this.iso = new Isotope(".data-grid", {
                            itemSelector: ".data-item",
                            layoutMode: "fitRows",
                            percentPosition: true
                        });

                        if (window.imagesLoaded) {
                            imagesLoaded(".data-grid", () => this.iso.layout());
                        }
                    }
                });

                this.$watch("search_term", () => this.applyFilters());
                this.$watch("selected_rarities", () => this.applyFilters());
                this.$watch("selected_elements", () => this.applyFilters());
            },

            applyFilters() {
                if (!this.iso) return;
                this.iso.arrange({
                    filter: (el) => {
                        const name = el.getAttribute("data-name") || "";
                        const sMatch = name.includes(this.search_term.toLowerCase());
                        const rMatch = this.selected_rarities.length === 0 || 
                                       this.selected_rarities.some(r => el.classList.contains(r));
                        const eMatch = this.selected_elements.length === 0 || 
                                       this.selected_elements.some(e => el.classList.contains(e));
                        return sMatch && rMatch && eMatch;
                    }
                });
            },

            toggle_rarity(val) {
                this.selected_rarities = this.selected_rarities.includes(val)
                    ? this.selected_rarities.filter(i => i !== val)
                    : [...this.selected_rarities, val];
            },

            toggle_element(val) {
                this.selected_elements = this.selected_elements.includes(val)
                    ? this.selected_elements.filter(i => i !== val)
                    : [...this.selected_elements, val];
            },

            clear_filters() {
                this.search_term = "";
                this.selected_elements = [];
                this.selected_rarities = [];
            }
        }));
    });

    window.unitFilterRegistered = true;
    console.log("Unit Filter System Registered.");
}