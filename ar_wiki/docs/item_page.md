<div x-data="itemFilterSystem" class="db-container glow-items">
  <div class="db-title">Items</div>
  <div class="db-content">
    <div class="data-menu">
      <div class="search-container">
        <svg
          class="w-4 h-4 text-white/20 mr-2"
          fill="none"
          stroke="currentColor"
          viewBox="0 0 24 24"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"
          ></path>
        </svg>
        <input
          type="text"
          class="search-input"
          placeholder="Search..."
          x-model.debounce.200ms="search_term"
        />
        <button
          class="search-clear-btn"
          x-show="search_term != ''"
          @click="search_term=''"
        >
          ✕
        </button>
      </div>

      <div class="filter-container">
        <button
          type="button"
          class="filter-toggle-btn"
          @click="filter_open = !filter_open"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="16"
            height="16"
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round"
            class="text-[#e63946]"
          >
            <polygon
              points="22 3 2 3 10 12.46 10 19 14 21 14 12.46 22 3"
            ></polygon>
          </svg>
          Filter
        </button>

        <div
          class="filter-content"
          x-show="filter_open"
          @click.away="filter_open = false"
          x-cloak
        >
          <div class="filter-category">
            <h4 class="filter-category-title">Rarity</h4>
            <ul class="filter-category-list">
              <template x-for="rarity in rarities" :key="rarity">
                <li>
                  <button
                    type="button"
                    class="filter-chip"
                    :class="selected_rarities.includes(rarity) ? 'is_active' : ''"
                    @click="toggle_rarity(rarity)"
                    x-text="rarity"
                  ></button>
                </li>
              </template>
            </ul>
          </div>
          <div class="filter-category">
            <h4 class="filter-category-title">Type</h4>
            <ul class="filter-category-list grid-style">
              <template x-for="category in categories" :key="category">
                <li>
                  <button
                    type="button"
                    class="filter-chip"
                    :class="selected_categories.includes(category) ? 'is_active' : ''"
                    @click="toggle_category(category)"
                    x-text="category"
                  ></button>
                </li>
              </template>
            </ul>

            <button
              type="button"
              @click="clear_filters()"
              class="clear-filters-btn"
            >
              Clear All Filters
            </button>
          </div>
        </div>
      </div>
    </div>

    <div class="data-grid">
      
      <div
        class="data-item Secret Evo"
        data-name="aura sword"
      >
        <div class="data-card">
          <div class="data-img-container bg-secret">
            <img
              src="http://placehold.co/120x120"
              alt="Aura Sword"
              loading="lazy"
            />
          </div>
          <span class="data-name">Aura Sword</span>
        </div>
      </div>
      
      <div
        class="data-item Secret Evo"
        data-name="aura sword [purple]"
      >
        <div class="data-card">
          <div class="data-img-container bg-secret">
            <img
              src="http://placehold.co/120x120"
              alt="Aura Sword [Purple]"
              loading="lazy"
            />
          </div>
          <span class="data-name">Aura Sword [Purple]</span>
        </div>
      </div>
      
      <div
        class="data-item Secret Evo"
        data-name="bankai sword"
      >
        <div class="data-card">
          <div class="data-img-container bg-secret">
            <img
              src="http://placehold.co/120x120"
              alt="Bankai Sword"
              loading="lazy"
            />
          </div>
          <span class="data-name">Bankai Sword</span>
        </div>
      </div>
      
      <div
        class="data-item Secret Capsule"
        data-name="christmas capsule"
      >
        <div class="data-card">
          <div class="data-img-container bg-secret">
            <img
              src="http://placehold.co/120x120"
              alt="Christmas Capsule"
              loading="lazy"
            />
          </div>
          <span class="data-name">Christmas Capsule</span>
        </div>
      </div>
      
      <div
        class="data-item Secret Evo"
        data-name="deer"
      >
        <div class="data-card">
          <div class="data-img-container bg-secret">
            <img
              src="http://placehold.co/120x120"
              alt="Deer"
              loading="lazy"
            />
          </div>
          <span class="data-name">Deer</span>
        </div>
      </div>
      
      <div
        class="data-item Secret Evo"
        data-name="gen z core"
      >
        <div class="data-card">
          <div class="data-img-container bg-secret">
            <img
              src="http://placehold.co/120x120"
              alt="Gen Z Core"
              loading="lazy"
            />
          </div>
          <span class="data-name">Gen Z Core</span>
        </div>
      </div>
      
      <div
        class="data-item Secret Capsule"
        data-name="halloween capsule"
      >
        <div class="data-card">
          <div class="data-img-container bg-secret">
            <img
              src="http://placehold.co/120x120"
              alt="Halloween Capsule"
              loading="lazy"
            />
          </div>
          <span class="data-name">Halloween Capsule</span>
        </div>
      </div>
      
      <div
        class="data-item Secret Evo"
        data-name="shiny stone"
      >
        <div class="data-card">
          <div class="data-img-container bg-secret">
            <img
              src="http://placehold.co/120x120"
              alt="Shiny Stone"
              loading="lazy"
            />
          </div>
          <span class="data-name">Shiny Stone</span>
        </div>
      </div>
      
      <div
        class="data-item Secret Capsule"
        data-name="spring capsule"
      >
        <div class="data-card">
          <div class="data-img-container bg-secret">
            <img
              src="http://placehold.co/120x120"
              alt="Spring Capsule"
              loading="lazy"
            />
          </div>
          <span class="data-name">Spring Capsule</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Evo"
        data-name="beast belt"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Beast Belt"
              loading="lazy"
            />
          </div>
          <span class="data-name">Beast Belt</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Evo"
        data-name="beast claws"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Beast Claws"
              loading="lazy"
            />
          </div>
          <span class="data-name">Beast Claws</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Evo"
        data-name="boru torso"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Boru Torso"
              loading="lazy"
            />
          </div>
          <span class="data-name">Boru Torso</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Food"
        data-name="candy"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Candy"
              loading="lazy"
            />
          </div>
          <span class="data-name">Candy</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Food"
        data-name="candy cane"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Candy Cane"
              loading="lazy"
            />
          </div>
          <span class="data-name">Candy Cane</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Evo"
        data-name="cape"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Cape"
              loading="lazy"
            />
          </div>
          <span class="data-name">Cape</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Evo"
        data-name="cracked power core"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Cracked Power Core"
              loading="lazy"
            />
          </div>
          <span class="data-name">Cracked Power Core</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Misc"
        data-name="crystal ball 1"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Crystal Ball 1"
              loading="lazy"
            />
          </div>
          <span class="data-name">Crystal Ball 1</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Misc"
        data-name="crystal ball 2"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Crystal Ball 2"
              loading="lazy"
            />
          </div>
          <span class="data-name">Crystal Ball 2</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Misc"
        data-name="crystal ball 3"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Crystal Ball 3"
              loading="lazy"
            />
          </div>
          <span class="data-name">Crystal Ball 3</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Misc"
        data-name="crystal ball 4"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Crystal Ball 4"
              loading="lazy"
            />
          </div>
          <span class="data-name">Crystal Ball 4</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Misc"
        data-name="crystal ball 5"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Crystal Ball 5"
              loading="lazy"
            />
          </div>
          <span class="data-name">Crystal Ball 5</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Misc"
        data-name="crystal ball 6"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Crystal Ball 6"
              loading="lazy"
            />
          </div>
          <span class="data-name">Crystal Ball 6</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Misc"
        data-name="crystal ball 7"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Crystal Ball 7"
              loading="lazy"
            />
          </div>
          <span class="data-name">Crystal Ball 7</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Food"
        data-name="cupcake"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Cupcake"
              loading="lazy"
            />
          </div>
          <span class="data-name">Cupcake</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Stats"
        data-name="cursed finger"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Cursed Finger"
              loading="lazy"
            />
          </div>
          <span class="data-name">Cursed Finger</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Misc"
        data-name="dark elixir"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Dark Elixir"
              loading="lazy"
            />
          </div>
          <span class="data-name">Dark Elixir</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Card"
        data-name="deaftone"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Deaftone"
              loading="lazy"
            />
          </div>
          <span class="data-name">Deaftone</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Evo"
        data-name="dice"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Dice"
              loading="lazy"
            />
          </div>
          <span class="data-name">Dice</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Misc"
        data-name="divine earing"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Divine Earing"
              loading="lazy"
            />
          </div>
          <span class="data-name">Divine Earing</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Card"
        data-name="ecoro"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Ecoro"
              loading="lazy"
            />
          </div>
          <span class="data-name">Ecoro</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Misc"
        data-name="elixir of life"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Elixir Of Life"
              loading="lazy"
            />
          </div>
          <span class="data-name">Elixir Of Life</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Card"
        data-name="ember"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Ember"
              loading="lazy"
            />
          </div>
          <span class="data-name">Ember</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Evo"
        data-name="evil orb"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Evil Orb"
              loading="lazy"
            />
          </div>
          <span class="data-name">Evil Orb</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Evo"
        data-name="fire haori"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Fire Haori"
              loading="lazy"
            />
          </div>
          <span class="data-name">Fire Haori</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Evo"
        data-name="fire katana"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Fire Katana"
              loading="lazy"
            />
          </div>
          <span class="data-name">Fire Katana</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Evo"
        data-name="four leaf grimoire"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Four Leaf Grimoire"
              loading="lazy"
            />
          </div>
          <span class="data-name">Four Leaf Grimoire</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Evo"
        data-name="getho outfit"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Getho Outfit"
              loading="lazy"
            />
          </div>
          <span class="data-name">Getho Outfit</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Evo"
        data-name="glass bow"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Glass Bow"
              loading="lazy"
            />
          </div>
          <span class="data-name">Glass Bow</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Evo"
        data-name="glass sword"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Glass Sword"
              loading="lazy"
            />
          </div>
          <span class="data-name">Glass Sword</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Evo"
        data-name="glasses"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Glasses"
              loading="lazy"
            />
          </div>
          <span class="data-name">Glasses</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Misc"
        data-name="gobanks jacket"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Gobanks Jacket"
              loading="lazy"
            />
          </div>
          <span class="data-name">Gobanks Jacket</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Misc"
        data-name="gogetable jacket"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Gogetable Jacket"
              loading="lazy"
            />
          </div>
          <span class="data-name">Gogetable Jacket</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Evo"
        data-name="goko outfit"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Goko Outfit"
              loading="lazy"
            />
          </div>
          <span class="data-name">Goko Outfit</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Evo"
        data-name="grocery bag"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Grocery Bag"
              loading="lazy"
            />
          </div>
          <span class="data-name">Grocery Bag</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Evo"
        data-name="hair gel"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Hair Gel"
              loading="lazy"
            />
          </div>
          <span class="data-name">Hair Gel</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Food"
        data-name="holy cross"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Holy Cross"
              loading="lazy"
            />
          </div>
          <span class="data-name">Holy Cross</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Evo"
        data-name="juice"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Juice"
              loading="lazy"
            />
          </div>
          <span class="data-name">Juice</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Evo"
        data-name="knight killer"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Knight Killer"
              loading="lazy"
            />
          </div>
          <span class="data-name">Knight Killer</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Evo"
        data-name="light crown"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Light Crown"
              loading="lazy"
            />
          </div>
          <span class="data-name">Light Crown</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Evo"
        data-name="light pickaxe"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Light Pickaxe"
              loading="lazy"
            />
          </div>
          <span class="data-name">Light Pickaxe</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Evo"
        data-name="light sword"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Light Sword"
              loading="lazy"
            />
          </div>
          <span class="data-name">Light Sword</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Food"
        data-name="love cake"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Love Cake"
              loading="lazy"
            />
          </div>
          <span class="data-name">Love Cake</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Evo"
        data-name="lukey"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="LuKey"
              loading="lazy"
            />
          </div>
          <span class="data-name">LuKey</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Evo"
        data-name="lustaff"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="LuStaff"
              loading="lazy"
            />
          </div>
          <span class="data-name">LuStaff</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Evo"
        data-name="nezu bamboo"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Nezu Bamboo"
              loading="lazy"
            />
          </div>
          <span class="data-name">Nezu Bamboo</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Evo"
        data-name="nezu box"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Nezu Box"
              loading="lazy"
            />
          </div>
          <span class="data-name">Nezu Box</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Evo"
        data-name="nezu outfit"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Nezu Outfit"
              loading="lazy"
            />
          </div>
          <span class="data-name">Nezu Outfit</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Card"
        data-name="overme"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Overme"
              loading="lazy"
            />
          </div>
          <span class="data-name">Overme</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Evo"
        data-name="oversized shins"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Oversized Shins"
              loading="lazy"
            />
          </div>
          <span class="data-name">Oversized Shins</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Misc"
        data-name="pickle cape"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Pickle Cape"
              loading="lazy"
            />
          </div>
          <span class="data-name">Pickle Cape</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Evo"
        data-name="pink kimono"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Pink Kimono"
              loading="lazy"
            />
          </div>
          <span class="data-name">Pink Kimono</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Evo"
        data-name="power core"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Power Core"
              loading="lazy"
            />
          </div>
          <span class="data-name">Power Core</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Misc"
        data-name="purification powder"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Purification Powder"
              loading="lazy"
            />
          </div>
          <span class="data-name">Purification Powder</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Evo"
        data-name="quincy cross"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Quincy Cross"
              loading="lazy"
            />
          </div>
          <span class="data-name">Quincy Cross</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Misc"
        data-name="raid ticket"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Raid Ticket"
              loading="lazy"
            />
          </div>
          <span class="data-name">Raid Ticket</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Evo"
        data-name="red knight's helmet"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Red Knight's Helmet"
              loading="lazy"
            />
          </div>
          <span class="data-name">Red Knight's Helmet</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Misc"
        data-name="rerolls"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Rerolls"
              loading="lazy"
            />
          </div>
          <span class="data-name">Rerolls</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Evo"
        data-name="ripped bandages"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Ripped Bandages"
              loading="lazy"
            />
          </div>
          <span class="data-name">Ripped Bandages</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Food"
        data-name="sandwich"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Sandwich"
              loading="lazy"
            />
          </div>
          <span class="data-name">Sandwich</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Evo"
        data-name="sheathe"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Sheathe"
              loading="lazy"
            />
          </div>
          <span class="data-name">Sheathe</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Evo"
        data-name="shintin"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Shintin"
              loading="lazy"
            />
          </div>
          <span class="data-name">Shintin</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Evo"
        data-name="six eyes"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Six Eyes"
              loading="lazy"
            />
          </div>
          <span class="data-name">Six Eyes</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Food"
        data-name="soul cutter"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Soul Cutter"
              loading="lazy"
            />
          </div>
          <span class="data-name">Soul Cutter</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Card"
        data-name="starpath"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Starpath"
              loading="lazy"
            />
          </div>
          <span class="data-name">Starpath</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Stat"
        data-name="stat crystal"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Stat Crystal"
              loading="lazy"
            />
          </div>
          <span class="data-name">Stat Crystal</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Stat"
        data-name="stat shard"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Stat Shard"
              loading="lazy"
            />
          </div>
          <span class="data-name">Stat Shard</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Misc"
        data-name="super lucky"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Super Lucky"
              loading="lazy"
            />
          </div>
          <span class="data-name">Super Lucky</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Evo"
        data-name="thukuna outfit"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Thukuna Outfit"
              loading="lazy"
            />
          </div>
          <span class="data-name">Thukuna Outfit</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Evo"
        data-name="thunder haori"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Thunder Haori"
              loading="lazy"
            />
          </div>
          <span class="data-name">Thunder Haori</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Evo"
        data-name="thunder katana"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Thunder Katana"
              loading="lazy"
            />
          </div>
          <span class="data-name">Thunder Katana</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Evo"
        data-name="transformation paper"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Transformation Paper"
              loading="lazy"
            />
          </div>
          <span class="data-name">Transformation Paper</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Evo"
        data-name="video game"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Video Game"
              loading="lazy"
            />
          </div>
          <span class="data-name">Video Game</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Evo"
        data-name="wind spirit crown"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Wind Spirit Crown"
              loading="lazy"
            />
          </div>
          <span class="data-name">Wind Spirit Crown</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Evo"
        data-name="yoyo"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Yoyo"
              loading="lazy"
            />
          </div>
          <span class="data-name">Yoyo</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Evo"
        data-name="assassin's double daggers"
      >
        <div class="data-card">
          <div class="data-img-container bg-legendary">
            <img
              src="http://placehold.co/120x120"
              alt="Assassin's Double Daggers"
              loading="lazy"
            />
          </div>
          <span class="data-name">Assassin's Double Daggers</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Evo"
        data-name="baruka's dagger"
      >
        <div class="data-card">
          <div class="data-img-container bg-legendary">
            <img
              src="http://placehold.co/120x120"
              alt="Baruka's Dagger"
              loading="lazy"
            />
          </div>
          <span class="data-name">Baruka's Dagger</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Evo"
        data-name="black sword"
      >
        <div class="data-card">
          <div class="data-img-container bg-legendary">
            <img
              src="http://placehold.co/120x120"
              alt="Black Sword"
              loading="lazy"
            />
          </div>
          <span class="data-name">Black Sword</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Evo"
        data-name="blindfold"
      >
        <div class="data-card">
          <div class="data-img-container bg-legendary">
            <img
              src="http://placehold.co/120x120"
              alt="Blindfold"
              loading="lazy"
            />
          </div>
          <span class="data-name">Blindfold</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Evo"
        data-name="cloud cloak"
      >
        <div class="data-card">
          <div class="data-img-container bg-legendary">
            <img
              src="http://placehold.co/120x120"
              alt="Cloud Cloak"
              loading="lazy"
            />
          </div>
          <span class="data-name">Cloud Cloak</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Evo"
        data-name="cursed energy"
      >
        <div class="data-card">
          <div class="data-img-container bg-legendary">
            <img
              src="http://placehold.co/120x120"
              alt="Cursed Energy"
              loading="lazy"
            />
          </div>
          <span class="data-name">Cursed Energy</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Evo"
        data-name="cursed orb"
      >
        <div class="data-card">
          <div class="data-img-container bg-legendary">
            <img
              src="http://placehold.co/120x120"
              alt="Cursed Orb"
              loading="lazy"
            />
          </div>
          <span class="data-name">Cursed Orb</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Evo"
        data-name="cyan sword"
      >
        <div class="data-card">
          <div class="data-img-container bg-legendary">
            <img
              src="http://placehold.co/120x120"
              alt="Cyan Sword"
              loading="lazy"
            />
          </div>
          <span class="data-name">Cyan Sword</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Card"
        data-name="deafbone"
      >
        <div class="data-card">
          <div class="data-img-container bg-legendary">
            <img
              src="http://placehold.co/120x120"
              alt="Deafbone"
              loading="lazy"
            />
          </div>
          <span class="data-name">Deafbone</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Evo"
        data-name="demon horn"
      >
        <div class="data-card">
          <div class="data-img-container bg-legendary">
            <img
              src="http://placehold.co/120x120"
              alt="Demon Horn"
              loading="lazy"
            />
          </div>
          <span class="data-name">Demon Horn</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Evo"
        data-name="demon king sword"
      >
        <div class="data-card">
          <div class="data-img-container bg-legendary">
            <img
              src="http://placehold.co/120x120"
              alt="Demon King Sword"
              loading="lazy"
            />
          </div>
          <span class="data-name">Demon King Sword</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Evo"
        data-name="demon monarch's necklace"
      >
        <div class="data-card">
          <div class="data-img-container bg-legendary">
            <img
              src="http://placehold.co/120x120"
              alt="Demon Monarch's Necklace"
              loading="lazy"
            />
          </div>
          <span class="data-name">Demon Monarch's Necklace</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Evo"
        data-name="divine stone"
      >
        <div class="data-card">
          <div class="data-img-container bg-legendary">
            <img
              src="http://placehold.co/120x120"
              alt="Divine Stone"
              loading="lazy"
            />
          </div>
          <span class="data-name">Divine Stone</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Evo"
        data-name="dominator's rune (purple)"
      >
        <div class="data-card">
          <div class="data-img-container bg-legendary">
            <img
              src="http://placehold.co/120x120"
              alt="Dominator's Rune (Purple)"
              loading="lazy"
            />
          </div>
          <span class="data-name">Dominator's Rune (Purple)</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Evo"
        data-name="dominator's rune (red)"
      >
        <div class="data-card">
          <div class="data-img-container bg-legendary">
            <img
              src="http://placehold.co/120x120"
              alt="Dominator's Rune (Red)"
              loading="lazy"
            />
          </div>
          <span class="data-name">Dominator's Rune (Red)</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Evo"
        data-name="dummy hair"
      >
        <div class="data-card">
          <div class="data-img-container bg-legendary">
            <img
              src="http://placehold.co/120x120"
              alt="Dummy Hair"
              loading="lazy"
            />
          </div>
          <span class="data-name">Dummy Hair</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Evo"
        data-name="dummy hat"
      >
        <div class="data-card">
          <div class="data-img-container bg-legendary">
            <img
              src="http://placehold.co/120x120"
              alt="Dummy Hat"
              loading="lazy"
            />
          </div>
          <span class="data-name">Dummy Hat</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Card"
        data-name="ecolo"
      >
        <div class="data-card">
          <div class="data-img-container bg-legendary">
            <img
              src="http://placehold.co/120x120"
              alt="Ecolo"
              loading="lazy"
            />
          </div>
          <span class="data-name">Ecolo</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Card"
        data-name="emtan"
      >
        <div class="data-card">
          <div class="data-img-container bg-legendary">
            <img
              src="http://placehold.co/120x120"
              alt="Emtan"
              loading="lazy"
            />
          </div>
          <span class="data-name">Emtan</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Evo"
        data-name="exchange ring"
      >
        <div class="data-card">
          <div class="data-img-container bg-legendary">
            <img
              src="http://placehold.co/120x120"
              alt="Exchange Ring"
              loading="lazy"
            />
          </div>
          <span class="data-name">Exchange Ring</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Evo"
        data-name="eye patch"
      >
        <div class="data-card">
          <div class="data-img-container bg-legendary">
            <img
              src="http://placehold.co/120x120"
              alt="Eye Patch"
              loading="lazy"
            />
          </div>
          <span class="data-name">Eye Patch</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Evo"
        data-name="fairy sword"
      >
        <div class="data-card">
          <div class="data-img-container bg-legendary">
            <img
              src="http://placehold.co/120x120"
              alt="Fairy Sword"
              loading="lazy"
            />
          </div>
          <span class="data-name">Fairy Sword</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Evo"
        data-name="fairy wings"
      >
        <div class="data-card">
          <div class="data-img-container bg-legendary">
            <img
              src="http://placehold.co/120x120"
              alt="Fairy Wings"
              loading="lazy"
            />
          </div>
          <span class="data-name">Fairy Wings</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Food"
        data-name="flask"
      >
        <div class="data-card">
          <div class="data-img-container bg-legendary">
            <img
              src="http://placehold.co/120x120"
              alt="Flask"
              loading="lazy"
            />
          </div>
          <span class="data-name">Flask</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Evo"
        data-name="flip book"
      >
        <div class="data-card">
          <div class="data-img-container bg-legendary">
            <img
              src="http://placehold.co/120x120"
              alt="Flip Book"
              loading="lazy"
            />
          </div>
          <span class="data-name">Flip Book</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Evo"
        data-name="game shield"
      >
        <div class="data-card">
          <div class="data-img-container bg-legendary">
            <img
              src="http://placehold.co/120x120"
              alt="Game Shield"
              loading="lazy"
            />
          </div>
          <span class="data-name">Game Shield</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Evo"
        data-name="game sword"
      >
        <div class="data-card">
          <div class="data-img-container bg-legendary">
            <img
              src="http://placehold.co/120x120"
              alt="Game Sword"
              loading="lazy"
            />
          </div>
          <span class="data-name">Game Sword</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Evo"
        data-name="gokon"
      >
        <div class="data-card">
          <div class="data-img-container bg-legendary">
            <img
              src="http://placehold.co/120x120"
              alt="Gokon"
              loading="lazy"
            />
          </div>
          <span class="data-name">Gokon</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Evo"
        data-name="gun"
      >
        <div class="data-card">
          <div class="data-img-container bg-legendary">
            <img
              src="http://placehold.co/120x120"
              alt="Gun"
              loading="lazy"
            />
          </div>
          <span class="data-name">Gun</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Evo"
        data-name="gun's top"
      >
        <div class="data-card">
          <div class="data-img-container bg-legendary">
            <img
              src="http://placehold.co/120x120"
              alt="Gun's Top"
              loading="lazy"
            />
          </div>
          <span class="data-name">Gun's Top</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Evo"
        data-name="hollow spear"
      >
        <div class="data-card">
          <div class="data-img-container bg-legendary">
            <img
              src="http://placehold.co/120x120"
              alt="Hollow Spear"
              loading="lazy"
            />
          </div>
          <span class="data-name">Hollow Spear</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Evo"
        data-name="kill's shirt"
      >
        <div class="data-card">
          <div class="data-img-container bg-legendary">
            <img
              src="http://placehold.co/120x120"
              alt="Kill's Shirt"
              loading="lazy"
            />
          </div>
          <span class="data-name">Kill's Shirt</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Evo"
        data-name="kill's shoe"
      >
        <div class="data-card">
          <div class="data-img-container bg-legendary">
            <img
              src="http://placehold.co/120x120"
              alt="Kill's Shoe"
              loading="lazy"
            />
          </div>
          <span class="data-name">Kill's Shoe</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Evo"
        data-name="kill's shorts"
      >
        <div class="data-card">
          <div class="data-img-container bg-legendary">
            <img
              src="http://placehold.co/120x120"
              alt="Kill's Shorts"
              loading="lazy"
            />
          </div>
          <span class="data-name">Kill's Shorts</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Evo"
        data-name="kisu hat"
      >
        <div class="data-card">
          <div class="data-img-container bg-legendary">
            <img
              src="http://placehold.co/120x120"
              alt="Kisu Hat"
              loading="lazy"
            />
          </div>
          <span class="data-name">Kisu Hat</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Evo"
        data-name="luhat"
      >
        <div class="data-card">
          <div class="data-img-container bg-legendary">
            <img
              src="http://placehold.co/120x120"
              alt="LuHat"
              loading="lazy"
            />
          </div>
          <span class="data-name">LuHat</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Misc"
        data-name="lucky"
      >
        <div class="data-card">
          <div class="data-img-container bg-legendary">
            <img
              src="http://placehold.co/120x120"
              alt="Lucky"
              loading="lazy"
            />
          </div>
          <span class="data-name">Lucky</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Evo"
        data-name="mana crystal"
      >
        <div class="data-card">
          <div class="data-img-container bg-legendary">
            <img
              src="http://placehold.co/120x120"
              alt="Mana Crystal"
              loading="lazy"
            />
          </div>
          <span class="data-name">Mana Crystal</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Card"
        data-name="overyou"
      >
        <div class="data-card">
          <div class="data-img-container bg-legendary">
            <img
              src="http://placehold.co/120x120"
              alt="Overyou"
              loading="lazy"
            />
          </div>
          <span class="data-name">Overyou</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Food"
        data-name="ramen"
      >
        <div class="data-card">
          <div class="data-img-container bg-legendary">
            <img
              src="http://placehold.co/120x120"
              alt="Ramen"
              loading="lazy"
            />
          </div>
          <span class="data-name">Ramen</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Evo"
        data-name="reaper badge"
      >
        <div class="data-card">
          <div class="data-img-container bg-legendary">
            <img
              src="http://placehold.co/120x120"
              alt="Reaper Badge"
              loading="lazy"
            />
          </div>
          <span class="data-name">Reaper Badge</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Evo"
        data-name="ruby"
      >
        <div class="data-card">
          <div class="data-img-container bg-legendary">
            <img
              src="http://placehold.co/120x120"
              alt="Ruby"
              loading="lazy"
            />
          </div>
          <span class="data-name">Ruby</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Evo"
        data-name="sapphire"
      >
        <div class="data-card">
          <div class="data-img-container bg-legendary">
            <img
              src="http://placehold.co/120x120"
              alt="Sapphire"
              loading="lazy"
            />
          </div>
          <span class="data-name">Sapphire</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Card"
        data-name="starkindle"
      >
        <div class="data-card">
          <div class="data-img-container bg-legendary">
            <img
              src="http://placehold.co/120x120"
              alt="Starkindle"
              loading="lazy"
            />
          </div>
          <span class="data-name">Starkindle</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Evo"
        data-name="straw hat"
      >
        <div class="data-card">
          <div class="data-img-container bg-legendary">
            <img
              src="http://placehold.co/120x120"
              alt="Straw Hat"
              loading="lazy"
            />
          </div>
          <span class="data-name">Straw Hat</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Food"
        data-name="strawberry cake"
      >
        <div class="data-card">
          <div class="data-img-container bg-legendary">
            <img
              src="http://placehold.co/120x120"
              alt="Strawberry Cake"
              loading="lazy"
            />
          </div>
          <span class="data-name">Strawberry Cake</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Evo"
        data-name="taser"
      >
        <div class="data-card">
          <div class="data-img-container bg-legendary">
            <img
              src="http://placehold.co/120x120"
              alt="Taser"
              loading="lazy"
            />
          </div>
          <span class="data-name">Taser</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Evo"
        data-name="teleportation stone"
      >
        <div class="data-card">
          <div class="data-img-container bg-legendary">
            <img
              src="http://placehold.co/120x120"
              alt="Teleportation Stone"
              loading="lazy"
            />
          </div>
          <span class="data-name">Teleportation Stone</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Evo"
        data-name="topaz"
      >
        <div class="data-card">
          <div class="data-img-container bg-legendary">
            <img
              src="http://placehold.co/120x120"
              alt="Topaz"
              loading="lazy"
            />
          </div>
          <span class="data-name">Topaz</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Evo"
        data-name="toy windmill"
      >
        <div class="data-card">
          <div class="data-img-container bg-legendary">
            <img
              src="http://placehold.co/120x120"
              alt="Toy Windmill"
              loading="lazy"
            />
          </div>
          <span class="data-name">Toy Windmill</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Evo"
        data-name="wish ball"
      >
        <div class="data-card">
          <div class="data-img-container bg-legendary">
            <img
              src="http://placehold.co/120x120"
              alt="Wish Ball"
              loading="lazy"
            />
          </div>
          <span class="data-name">Wish Ball</span>
        </div>
      </div>
      
      <div
        class="data-item Epic Food"
        data-name="burger"
      >
        <div class="data-card">
          <div class="data-img-container bg-epic">
            <img
              src="http://placehold.co/120x120"
              alt="Burger"
              loading="lazy"
            />
          </div>
          <span class="data-name">Burger</span>
        </div>
      </div>
      
      <div
        class="data-item Epic Food"
        data-name="cupnoodle"
      >
        <div class="data-card">
          <div class="data-img-container bg-epic">
            <img
              src="http://placehold.co/120x120"
              alt="CupNoodle"
              loading="lazy"
            />
          </div>
          <span class="data-name">CupNoodle</span>
        </div>
      </div>
      
      <div
        class="data-item Epic Evo"
        data-name="cursed head band"
      >
        <div class="data-card">
          <div class="data-img-container bg-epic">
            <img
              src="http://placehold.co/120x120"
              alt="Cursed Head Band"
              loading="lazy"
            />
          </div>
          <span class="data-name">Cursed Head Band</span>
        </div>
      </div>
      
      <div
        class="data-item Epic Card"
        data-name="deaffone"
      >
        <div class="data-card">
          <div class="data-img-container bg-epic">
            <img
              src="http://placehold.co/120x120"
              alt="Deaffone"
              loading="lazy"
            />
          </div>
          <span class="data-name">Deaffone</span>
        </div>
      </div>
      
      <div
        class="data-item Epic Card"
        data-name="ecolist"
      >
        <div class="data-card">
          <div class="data-img-container bg-epic">
            <img
              src="http://placehold.co/120x120"
              alt="Ecolist"
              loading="lazy"
            />
          </div>
          <span class="data-name">Ecolist</span>
        </div>
      </div>
      
      <div
        class="data-item Epic Card"
        data-name="embrew"
      >
        <div class="data-card">
          <div class="data-img-container bg-epic">
            <img
              src="http://placehold.co/120x120"
              alt="Embrew"
              loading="lazy"
            />
          </div>
          <span class="data-name">Embrew</span>
        </div>
      </div>
      
      <div
        class="data-item Epic Food"
        data-name="fish"
      >
        <div class="data-card">
          <div class="data-img-container bg-epic">
            <img
              src="http://placehold.co/120x120"
              alt="Fish"
              loading="lazy"
            />
          </div>
          <span class="data-name">Fish</span>
        </div>
      </div>
      
      <div
        class="data-item Epic Evo"
        data-name="hollow leader mask"
      >
        <div class="data-card">
          <div class="data-img-container bg-epic">
            <img
              src="http://placehold.co/120x120"
              alt="Hollow Leader Mask"
              loading="lazy"
            />
          </div>
          <span class="data-name">Hollow Leader Mask</span>
        </div>
      </div>
      
      <div
        class="data-item Epic Evo"
        data-name="multiweapon"
      >
        <div class="data-card">
          <div class="data-img-container bg-epic">
            <img
              src="http://placehold.co/120x120"
              alt="Multiweapon"
              loading="lazy"
            />
          </div>
          <span class="data-name">Multiweapon</span>
        </div>
      </div>
      
      <div
        class="data-item Epic Card"
        data-name="overit"
      >
        <div class="data-card">
          <div class="data-img-container bg-epic">
            <img
              src="http://placehold.co/120x120"
              alt="Overit"
              loading="lazy"
            />
          </div>
          <span class="data-name">Overit</span>
        </div>
      </div>
      
      <div
        class="data-item Epic Evo"
        data-name="radar"
      >
        <div class="data-card">
          <div class="data-img-container bg-epic">
            <img
              src="http://placehold.co/120x120"
              alt="Radar"
              loading="lazy"
            />
          </div>
          <span class="data-name">Radar</span>
        </div>
      </div>
      
      <div
        class="data-item Epic Evo"
        data-name="soul candy"
      >
        <div class="data-card">
          <div class="data-img-container bg-epic">
            <img
              src="http://placehold.co/120x120"
              alt="Soul Candy"
              loading="lazy"
            />
          </div>
          <span class="data-name">Soul Candy</span>
        </div>
      </div>
      
      <div
        class="data-item Epic Card"
        data-name="starheart"
      >
        <div class="data-card">
          <div class="data-img-container bg-epic">
            <img
              src="http://placehold.co/120x120"
              alt="Starheart"
              loading="lazy"
            />
          </div>
          <span class="data-name">Starheart</span>
        </div>
      </div>
      
      <div
        class="data-item Epic Evo"
        data-name="virtual food"
      >
        <div class="data-card">
          <div class="data-img-container bg-epic">
            <img
              src="http://placehold.co/120x120"
              alt="Virtual Food"
              loading="lazy"
            />
          </div>
          <span class="data-name">Virtual Food</span>
        </div>
      </div>
      
      <div
        class="data-item Rare Food"
        data-name="apple"
      >
        <div class="data-card">
          <div class="data-img-container bg-rare">
            <img
              src="http://placehold.co/120x120"
              alt="Apple"
              loading="lazy"
            />
          </div>
          <span class="data-name">Apple</span>
        </div>
      </div>
      
      <div
        class="data-item Rare Evo"
        data-name="apron"
      >
        <div class="data-card">
          <div class="data-img-container bg-rare">
            <img
              src="http://placehold.co/120x120"
              alt="Apron"
              loading="lazy"
            />
          </div>
          <span class="data-name">Apron</span>
        </div>
      </div>
      
      <div
        class="data-item Rare Food"
        data-name="bean"
      >
        <div class="data-card">
          <div class="data-img-container bg-rare">
            <img
              src="http://placehold.co/120x120"
              alt="Bean"
              loading="lazy"
            />
          </div>
          <span class="data-name">Bean</span>
        </div>
      </div>
      
      <div
        class="data-item Rare Card"
        data-name="deafone"
      >
        <div class="data-card">
          <div class="data-img-container bg-rare">
            <img
              src="http://placehold.co/120x120"
              alt="Deafone"
              loading="lazy"
            />
          </div>
          <span class="data-name">Deafone</span>
        </div>
      </div>
      
      <div
        class="data-item Rare Evo"
        data-name="demon monarch earings"
      >
        <div class="data-card">
          <div class="data-img-container bg-rare">
            <img
              src="http://placehold.co/120x120"
              alt="Demon Monarch Earings"
              loading="lazy"
            />
          </div>
          <span class="data-name">Demon Monarch Earings</span>
        </div>
      </div>
      
      <div
        class="data-item Rare Card"
        data-name="drawnup"
      >
        <div class="data-card">
          <div class="data-img-container bg-rare">
            <img
              src="http://placehold.co/120x120"
              alt="Drawnup"
              loading="lazy"
            />
          </div>
          <span class="data-name">Drawnup</span>
        </div>
      </div>
      
      <div
        class="data-item Rare Card"
        data-name="ecoist"
      >
        <div class="data-card">
          <div class="data-img-container bg-rare">
            <img
              src="http://placehold.co/120x120"
              alt="Ecoist"
              loading="lazy"
            />
          </div>
          <span class="data-name">Ecoist</span>
        </div>
      </div>
      
      <div
        class="data-item Rare Card"
        data-name="emburish"
      >
        <div class="data-card">
          <div class="data-img-container bg-rare">
            <img
              src="http://placehold.co/120x120"
              alt="Emburish"
              loading="lazy"
            />
          </div>
          <span class="data-name">Emburish</span>
        </div>
      </div>
      
      <div
        class="data-item Rare Evo"
        data-name="hollow warrior mask"
      >
        <div class="data-card">
          <div class="data-img-container bg-rare">
            <img
              src="http://placehold.co/120x120"
              alt="Hollow Warrior Mask"
              loading="lazy"
            />
          </div>
          <span class="data-name">Hollow Warrior Mask</span>
        </div>
      </div>
      
      <div
        class="data-item Rare Card"
        data-name="overnow"
      >
        <div class="data-card">
          <div class="data-img-container bg-rare">
            <img
              src="http://placehold.co/120x120"
              alt="Overnow"
              loading="lazy"
            />
          </div>
          <span class="data-name">Overnow</span>
        </div>
      </div>
      
      <div
        class="data-item Rare Evo"
        data-name="scouter"
      >
        <div class="data-card">
          <div class="data-img-container bg-rare">
            <img
              src="http://placehold.co/120x120"
              alt="Scouter"
              loading="lazy"
            />
          </div>
          <span class="data-name">Scouter</span>
        </div>
      </div>
      
      <div
        class="data-item Rare Card"
        data-name="starlight"
      >
        <div class="data-card">
          <div class="data-img-container bg-rare">
            <img
              src="http://placehold.co/120x120"
              alt="Starlight"
              loading="lazy"
            />
          </div>
          <span class="data-name">Starlight</span>
        </div>
      </div>
      
      <div
        class="data-item Rare Card"
        data-name="testcard"
      >
        <div class="data-card">
          <div class="data-img-container bg-rare">
            <img
              src="http://placehold.co/120x120"
              alt="TestCard"
              loading="lazy"
            />
          </div>
          <span class="data-name">TestCard</span>
        </div>
      </div>
      
    </div>
  </div>
</div>