if (!window.itemFilterRegistered) {
  document.addEventListener("alpine:init", () => {
    Alpine.data("itemFilterSystem", () => ({
      search_term: "",
      selected_rarities: [],
      selected_categories: [],
      filter_open: false,
      iso: null,
      selected_item: null,
      rarities: ["Secret", "Mythic", "Legendary", "Epic", "Rare"],
      categories: ["Evo", "Card", "Misc", "Food", "Capsule", "Stat", "Stats"],

      init() {
        this.$nextTick(() => {
          if (window.Isotope) {
            this.iso = new Isotope(".data-grid", {
              itemSelector: ".data-item",
              layoutMode: "fitRows",
              percentPosition: true,
            });

            if (window.imagesLoaded) {
              imagesLoaded(".data-grid", () => {
                this.iso.layout();
              });
            }
          }
        });

        this.$watch("search_term", () => this.applyFilters());
        this.$watch("selected_rarities", () => this.applyFilters());
        this.$watch("selected_categories", () => this.applyFilters());
      },

      applyFilters() {
        if (!this.iso) return;
        this.iso.arrange({
          filter: (el) => {
            const name = el.getAttribute("data-name") || "";
            const sMatch = name.includes(this.search_term.toLowerCase());
            const rMatch =
              this.selected_rarities.length === 0 ||
              this.selected_rarities.some((r) => el.classList.contains(r));
            const cMatch =
              this.selected_categories.length === 0 ||
              this.selected_categories.some((c) => el.classList.contains(c));
            return sMatch && rMatch && cMatch;
          },
        });
      },

      toggle_rarity(val) {
        this.selected_rarities = this.selected_rarities.includes(val)
          ? this.selected_rarities.filter((i) => i !== val)
          : [...this.selected_rarities, val];
      },

      toggle_category(val) {
        this.selected_categories = this.selected_categories.includes(val)
          ? this.selected_categories.filter((i) => i !== val)
          : [...this.selected_categories, val];
      },

      clear_filters() {
        this.search_term = "";
        this.selected_rarities = [];
        this.selected_categories = [];
      },

      openItem(itemData) {
        this.selected_item = itemData;
        document.body.style.overflow = "hidden";
      },

      closeItem() {
        this.selected_item = null;
        document.body.style.overflow = "auto";
      },
    }));
  });
  window.itemFilterRegistered = true;
}
