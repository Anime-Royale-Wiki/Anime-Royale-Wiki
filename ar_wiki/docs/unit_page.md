<div x-data="unitFilterSystem" class="db-container glow-units">
  <div class="db-title">Units</div>
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
              <template x-for="element in elements" :key="element">
                <li>
                  <button
                    type="button"
                    class="filter-chip"
                    :class="selected_elements.includes(element) ? 'is_active' : ''"
                    @click="toggle_element(element)"
                    x-text="element"
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
        class="data-item Royalty Dark"
        data-name="ichigoat [true]"
      >
        <div class="data-card">
          <div class="data-img-container bg-royalty">
            <a href="../units/trueichigo" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Ichigoat [True]"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Ichigoat [True]</span>
        </div>
      </div>
      
      <div
        class="data-item Secret Dark"
        data-name="almighty"
      >
        <div class="data-card">
          <div class="data-img-container bg-secret">
            <a href="../units/yhwach" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Almighty"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Almighty</span>
        </div>
      </div>
      
      <div
        class="data-item Secret Grass"
        data-name="ant general"
      >
        <div class="data-card">
          <div class="data-img-container bg-secret">
            <a href="../units/beru" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Ant General"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Ant General</span>
        </div>
      </div>
      
      <div
        class="data-item Secret Steel"
        data-name="aura farmer [purple]"
      >
        <div class="data-card">
          <div class="data-img-container bg-secret">
            <a href="../units/igrisevo" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Aura Farmer [Purple]"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Aura Farmer [Purple]</span>
        </div>
      </div>
      
      <div
        class="data-item Secret Dark"
        data-name="aura king [monarch]"
      >
        <div class="data-card">
          <div class="data-img-container bg-secret">
            <a href="../units/sunjinwooevo2" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Aura King [Monarch]"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Aura King [Monarch]</span>
        </div>
      </div>
      
      <div
        class="data-item Secret Fighting"
        data-name="broccoli"
      >
        <div class="data-card">
          <div class="data-img-container bg-secret">
            <a href="../units/zbroly" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Broccoli"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Broccoli</span>
        </div>
      </div>
      
      <div
        class="data-item Secret Grass"
        data-name="deer girl"
      >
        <div class="data-card">
          <div class="data-img-container bg-secret">
            <a href="../units/nokotan" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Deer Girl"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Deer Girl</span>
        </div>
      </div>
      
      <div
        class="data-item Secret Fire"
        data-name="demon blade"
      >
        <div class="data-card">
          <div class="data-img-container bg-secret">
            <a href="../units/akame" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Demon Blade"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Demon Blade</span>
        </div>
      </div>
      
      <div
        class="data-item Secret Dark"
        data-name="demon lord"
      >
        <div class="data-card">
          <div class="data-img-container bg-secret">
            <a href="../units/muzan" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Demon Lord"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Demon Lord</span>
        </div>
      </div>
      
      <div
        class="data-item Secret Grass"
        data-name="dreamer"
      >
        <div class="data-card">
          <div class="data-img-container bg-secret">
            <a href="../units/giorno" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Dreamer"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Dreamer</span>
        </div>
      </div>
      
      <div
        class="data-item Secret Psychic"
        data-name="eyezen"
      >
        <div class="data-card">
          <div class="data-img-container bg-secret">
            <a href="../units/aizen" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Eyezen"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Eyezen</span>
        </div>
      </div>
      
      <div
        class="data-item Secret Psychic"
        data-name="friend"
      >
        <div class="data-card">
          <div class="data-img-container bg-secret">
            <a href="../units/frieren" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Friend"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Friend</span>
        </div>
      </div>
      
      <div
        class="data-item Secret Fire"
        data-name="gen z"
      >
        <div class="data-card">
          <div class="data-img-container bg-secret">
            <a href="../units/genos" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Gen Z"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Gen Z</span>
        </div>
      </div>
      
      <div
        class="data-item Secret Holy"
        data-name="gio [over heaven]"
      >
        <div class="data-card">
          <div class="data-img-container bg-secret">
            <a href="../units/dio[oh]" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Gio [Over Heaven]"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Gio [Over Heaven]</span>
        </div>
      </div>
      
      <div
        class="data-item Secret Fighting"
        data-name="kaillou (serious)"
      >
        <div class="data-card">
          <div class="data-img-container bg-secret">
            <a href="../units/saitamaevo" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Kaillou (Serious)"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Kaillou (Serious)</span>
        </div>
      </div>
      
      <div
        class="data-item Secret Dark"
        data-name="merem"
      >
        <div class="data-card">
          <div class="data-img-container bg-secret">
            <a href="../units/meruem" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Merem"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Merem</span>
        </div>
      </div>
      
      <div
        class="data-item Secret Steel"
        data-name="nagu"
      >
        <div class="data-card">
          <div class="data-img-container bg-secret">
            <a href="../units/nagumo" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Nagu"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Nagu</span>
        </div>
      </div>
      
      <div
        class="data-item Secret Holy"
        data-name="nero"
      >
        <div class="data-card">
          <div class="data-img-container bg-secret">
            <a href="../units/netero" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Nero"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Nero</span>
        </div>
      </div>
      
      <div
        class="data-item Secret Dark"
        data-name="shadow"
      >
        <div class="data-card">
          <div class="data-img-container bg-secret">
            <a href="../units/cid" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Shadow"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Shadow</span>
        </div>
      </div>
      
      <div
        class="data-item Secret Psychic"
        data-name="shine"
      >
        <div class="data-card">
          <div class="data-img-container bg-secret">
            <a href="../units/shin" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Shine"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Shine</span>
        </div>
      </div>
      
      <div
        class="data-item Secret Dark"
        data-name="the mastermind"
      >
        <div class="data-card">
          <div class="data-img-container bg-secret">
            <a href="../units/lelouch" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="The Mastermind"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">The Mastermind</span>
        </div>
      </div>
      
      <div
        class="data-item Secret Steel"
        data-name="tochi"
      >
        <div class="data-card">
          <div class="data-img-container bg-secret">
            <a href="../units/toji" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Tochi"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Tochi</span>
        </div>
      </div>
      
      <div
        class="data-item Secret Fighting"
        data-name="uzi"
      >
        <div class="data-card">
          <div class="data-img-container bg-secret">
            <a href="../units/tengen" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Uzi"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Uzi</span>
        </div>
      </div>
      
      <div
        class="data-item Secret Fighting"
        data-name="valentine delight"
      >
        <div class="data-card">
          <div class="data-img-container bg-secret">
            <a href="../units/funnyvalentine" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Valentine Delight"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Valentine Delight</span>
        </div>
      </div>
      
      <div
        class="data-item Secret Water"
        data-name="virtual sniper"
      >
        <div class="data-card">
          <div class="data-img-container bg-secret">
            <a href="../units/shino" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Virtual Sniper"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Virtual Sniper</span>
        </div>
      </div>
      
      <div
        class="data-item Secret Psychic"
        data-name="yabo"
      >
        <div class="data-card">
          <div class="data-img-container bg-secret">
            <a href="../units/yato" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Yabo"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Yabo</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Fighting"
        data-name="adult gokan"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/adultgohan" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Adult Gokan"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Adult Gokan</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Ice"
        data-name="akatou"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/akaza" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Akatou"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Akatou</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Holy"
        data-name="alize"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/alice" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Alize"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Alize</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Steel"
        data-name="atomic warrior"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/atomicsamurai" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Atomic Warrior"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Atomic Warrior</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Steel"
        data-name="aura farmer"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/igris" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Aura Farmer"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Aura Farmer</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Water"
        data-name="aura king"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/sunjinwoo" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Aura King"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Aura King</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Dark"
        data-name="aura king [shadow]"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/sunjinwooevo" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Aura King [Shadow]"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Aura King [Shadow]</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Water"
        data-name="bean"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/bang" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Bean"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Bean</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Fighting"
        data-name="beast hunter"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/baek" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Beast Hunter"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Beast Hunter</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Neutral"
        data-name="beast hunter [wrath]"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/baekevo" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Beast Hunter [Wrath]"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Beast Hunter [Wrath]</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Steel"
        data-name="bonkstick"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/metalbat" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Bonkstick"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Bonkstick</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Psychic"
        data-name="boru [100% released]"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/borosdoubleevo" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Boru [100% Released]"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Boru [100% Released]</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Psychic"
        data-name="boru [released]"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/borosevo" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Boru [Released]"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Boru [Released]</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Fire"
        data-name="captain yama"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/yamamoto" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Captain Yama"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Captain Yama</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Neutral"
        data-name="card magician"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/hisoka" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Card Magician"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Card Magician</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Fighting"
        data-name="chick"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/chika" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Chick"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Chick</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Dark"
        data-name="dako"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/daki" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Dako"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Dako</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Dark"
        data-name="diablo"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/diavolo" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Diablo"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Diablo</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Fighting"
        data-name="donkey"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/madong" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Donkey"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Donkey</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Dark"
        data-name="dracula"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/alucard" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Dracula"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Dracula</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Ice"
        data-name="emily"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/emilia" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Emily"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Emily</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Ice"
        data-name="eslife"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/esdeath" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Eslife"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Eslife</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Neutral"
        data-name="fanny"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/fran" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Fanny"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Fanny</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Fire"
        data-name="flame master"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/rengoku" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Flame Master"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Flame Master</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Fire"
        data-name="flame master [ablaze]"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/rengokuevo" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Flame Master [Ablaze]"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Flame Master [Ablaze]</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Psychic"
        data-name="freeze [final]"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/frieza" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Freeze [Final]"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Freeze [Final]</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Psychic"
        data-name="fubuu"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/fubuki" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Fubuu"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Fubuu</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Fire"
        data-name="game master"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/heathcliff" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Game Master"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Game Master</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Fire"
        data-name="game master [serious]"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/heathcliff [serious]" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Game Master [Serious]"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Game Master [Serious]</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Fire"
        data-name="gems master"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/rin tohsaka" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Gems Master"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Gems Master</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Psychic"
        data-name="getho"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/geto" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Getho"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Getho</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Psychic"
        data-name="getho [zero]"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/getoevo" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Getho [Zero]"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Getho [Zero]</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Fighting"
        data-name="gobanks"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/gotenks" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Gobanks"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Gobanks</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Holy"
        data-name="gogetable (angel)"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/gogeta" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Gogetable (Angel)"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Gogetable (Angel)</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Holy"
        data-name="goko (end)"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/gokuzend" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Goko (End)"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Goko (End)</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Fighting"
        data-name="goko the 3rd"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/goku (ssj3)" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Goko The 3rd"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Goko The 3rd</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Fighting"
        data-name="goko [ssj]"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/goku [ssj]" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Goko [SSJ]"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Goko [SSJ]</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Rock"
        data-name="gomu"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/gyomei" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Gomu"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Gomu</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Psychic"
        data-name="gotho"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/gojo" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Gotho"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Gotho</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Psychic"
        data-name="gotho [honored]"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/gojoevo" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Gotho [Honored]"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Gotho [Honored]</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Steel"
        data-name="greg [kurokumo]"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/gregorevo" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Greg [Kurokumo]"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Greg [Kurokumo]</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Water"
        data-name="gui"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/giyu" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Gui"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Gui</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Dark"
        data-name="guitar"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/gyutaro" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Guitar"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Guitar</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Fighting"
        data-name="gun"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/gon" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Gun"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Gun</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Fighting"
        data-name="gun [pact]"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/gonevo" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Gun [Pact]"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Gun [Pact]</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Ground"
        data-name="hashino"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/hashirama" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Hashino"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Hashino</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Steel"
        data-name="haze"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/heisuke" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Haze"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Haze</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Dark"
        data-name="headless swordsman"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/goto" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Headless Swordsman"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Headless Swordsman</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Fire"
        data-name="hellborn"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/rin" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Hellborn"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Hellborn</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Dark"
        data-name="ichiko"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/ichigo" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Ichiko"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Ichiko</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Dark"
        data-name="ichiko [awakened]"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/ichigobankai" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Ichiko [Awakened]"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Ichiko [Awakened]</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Dark"
        data-name="ichiko [gumetsu]"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/mugetsu" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Ichiko [Gumetsu]"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Ichiko [Gumetsu]</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Dark"
        data-name="jamba"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/janemba" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Jamba"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Jamba</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Ice"
        data-name="jolly eslife"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/esdeathbundle" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Jolly Eslife"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Jolly Eslife</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Fighting"
        data-name="jotero"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/jotaro" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Jotero"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Jotero</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Fighting"
        data-name="kaiju"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/kaiju" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Kaiju"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Kaiju</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Fighting"
        data-name="kaillou"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/saitama" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Kaillou"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Kaillou</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Fighting"
        data-name="keneki"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/kaneki" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Keneki"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Keneki</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Steel"
        data-name="kenny"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/kenpachi" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Kenny"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Kenny</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Holy"
        data-name="kid boog"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/kidbuu" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Kid Boog"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Kid Boog</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Electric"
        data-name="kill [angered]"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/killuaevo" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Kill [Angered]"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Kill [Angered]</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Electric"
        data-name="killa"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/killua" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Killa"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Killa</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Ice"
        data-name="kuzo"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/kuzan" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Kuzo"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Kuzo</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Wind"
        data-name="leafy"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/leafa" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Leafy"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Leafy</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Wind"
        data-name="leafy [fairy]"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/leafa [serious]" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Leafy [Fairy]"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Leafy [Fairy]</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Holy"
        data-name="light bearer"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/chae" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Light Bearer"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Light Bearer</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Holy"
        data-name="light bearer [blessed]"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/chaeevo" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Light Bearer [Blessed]"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Light Bearer [Blessed]</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Dark"
        data-name="lollang (black silence)"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/rolandevo" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Lollang (Black Silence)"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Lollang (Black Silence)</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Fighting"
        data-name="loop"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/lu" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Loop"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Loop</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Holy"
        data-name="mahoka"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/madoka" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Mahoka"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Mahoka</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Holy"
        data-name="maiko"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/bocchi" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Maiko"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Maiko</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Dark"
        data-name="manara"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/madara" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Manara"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Manara</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Grass"
        data-name="mims"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/mimosa" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Mims"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Mims</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Dark"
        data-name="mira [demon]"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/mirajane" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Mira [Demon]"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Mira [Demon]</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Steel"
        data-name="misaka"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/mikasa" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Misaka"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Misaka</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Steel"
        data-name="mitsu"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/mitsuri" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Mitsu"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Mitsu</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Steel"
        data-name="moon demon"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/kokushibo" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Moon Demon"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Moon Demon</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Holy"
        data-name="moon princess"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/sailormoon" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Moon Princess"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Moon Princess</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Fighting"
        data-name="motomoto"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/sakamoto" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Motomoto"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Motomoto</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Fighting"
        data-name="motomoto bunny"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/sakamotobundle" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Motomoto Bunny"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Motomoto Bunny</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Fighting"
        data-name="motomoto bunny [thin]"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/sakamotoevobundle" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Motomoto Bunny [Thin]"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Motomoto Bunny [Thin]</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Fighting"
        data-name="motomoto [thin]"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/sakamotoevo" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Motomoto [Thin]"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Motomoto [Thin]</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Dark"
        data-name="nakuma"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/nazuna" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Nakuma"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Nakuma</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Dark"
        data-name="neko"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/neferpitou" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Neko"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Neko</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Holy"
        data-name="nezu"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/nezuko" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Nezu"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Nezu</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Dark"
        data-name="nezu [demon]"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/nezukoevo" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Nezu [Demon]"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Nezu [Demon]</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Dark"
        data-name="nightmare xiii"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/death13" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Nightmare XIII"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Nightmare XIII</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Psychic"
        data-name="okuno"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/okuyasu" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Okuno"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Okuno</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Holy"
        data-name="origiri"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/origami" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Origiri"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Origiri</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Neutral"
        data-name="orihamis"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/orihime" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Orihamis"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Orihamis</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Fighting"
        data-name="otakurun"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/okarun" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Otakurun"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Otakurun</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Fighting"
        data-name="otakurun [venomous]"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/okarunbundle" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Otakurun [Venomous]"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Otakurun [Venomous]</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Poison"
        data-name="perfect konchu"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/cellevo2" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Perfect Konchu"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Perfect Konchu</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Psychic"
        data-name="ria"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/rikka" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Ria"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Ria</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Psychic"
        data-name="rumika"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/riruka" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Rumika"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Rumika</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Fire"
        data-name="s-rank bomber"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/choi" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="S-Rank Bomber"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">S-Rank Bomber</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Poison"
        data-name="semi-perfect konchu"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/cellevo" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Semi-Perfect Konchu"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Semi-Perfect Konchu</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Steel"
        data-name="seven star hunter"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/liu" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Seven Star Hunter"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Seven Star Hunter</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Steel"
        data-name="silver knight"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/polnareff" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Silver Knight"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Silver Knight</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Fire"
        data-name="song"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/song" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Song"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Song</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Steel"
        data-name="stabs"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/shanks" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Stabs"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Stabs</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Fire"
        data-name="steamed"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/boiled" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Steamed"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Steamed</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Fire"
        data-name="sun tojiro"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/suntanjiro" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Sun Tojiro"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Sun Tojiro</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Grass"
        data-name="sunny"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/shunsui" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Sunny"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Sunny</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Grass"
        data-name="sunny (release)"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/shunsuievo" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Sunny (Release)"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Sunny (Release)</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Holy"
        data-name="super boog"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/superbuu" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Super Boog"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Super Boog</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Holy"
        data-name="super booghan"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/buuhan" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Super Booghan"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Super Booghan</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Holy"
        data-name="super boogtenks"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/buutenks" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Super Boogtenks"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Super Boogtenks</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Psychic"
        data-name="tatsu"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/tatsumaki" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Tatsu"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Tatsu</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Fighting"
        data-name="teen gokan"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/teengohan" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Teen Gokan"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Teen Gokan</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Fighting"
        data-name="teen gokan (awakened)"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/gohanteenssj2" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Teen Gokan (Awakened)"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Teen Gokan (Awakened)</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Steel"
        data-name="the drink"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/futuretrunks" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="The Drink"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">The Drink</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Dark"
        data-name="the evil cup"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/majinvegeta" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="The Evil Cup"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">The Evil Cup</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Neutral"
        data-name="the weakest esper"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/touma" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="The Weakest Esper"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">The Weakest Esper</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Fighting"
        data-name="thompson anderson"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/thomas" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Thompson Anderson"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Thompson Anderson</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Dark"
        data-name="thukuna"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/sukuna" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Thukuna"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Thukuna</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Dark"
        data-name="thukuna [king]"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/sukunaevo" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Thukuna [King]"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Thukuna [King]</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Ice"
        data-name="tochito"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/toshiro" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Tochito"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Tochito</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Dark"
        data-name="toka"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/tohka" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Toka"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Toka</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Dark"
        data-name="ulquioro (second)"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/ulquiorra (segunda)" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Ulquioro (Second)"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Ulquioro (Second)</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Holy"
        data-name="urwu"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/uryu" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Urwu"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Urwu</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Holy"
        data-name="urwu (kwency)"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/uryuevo" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Urwu (Kwency)"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Urwu (Kwency)</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Holy"
        data-name="vegitu"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/vegito" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Vegitu"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Vegitu</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Steel"
        data-name="vile"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/levi" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Vile"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Vile</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Steel"
        data-name="virtual swordmaster [awakened]"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/kiritooa" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Virtual Swordmaster [Awakened]"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Virtual Swordmaster [Awakened]</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Steel"
        data-name="virtual swordmaster [ultimate]"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/kiritooaevo" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Virtual Swordmaster [Ultimate]"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Virtual Swordmaster [Ultimate]</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Steel"
        data-name="virtual swordwoman"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/asunaoa" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Virtual Swordwoman"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Virtual Swordwoman</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Wind"
        data-name="weather"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/weatherreport" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Weather"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Weather</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Wind"
        data-name="wind mage"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/yuno" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Wind Mage"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Wind Mage</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Wind"
        data-name="wind mage [spirit ascension]"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/yunoevo" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Wind Mage [Spirit Ascension]"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Wind Mage [Spirit Ascension]</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Rock"
        data-name="xeke"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/zeke" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Xeke"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Xeke</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Fighting"
        data-name="yeagar"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/eren" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Yeagar"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Yeagar</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Electric"
        data-name="yoru"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/yoruichi" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Yoru"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Yoru</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Electric"
        data-name="yoru [raging raijin]"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/yoruichievo" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Yoru [Raging Raijin]"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Yoru [Raging Raijin]</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Wind"
        data-name="yuka"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/yukari" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Yuka"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Yuka</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Psychic"
        data-name="yutha"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/yuta" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Yutha"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Yutha</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Electric"
        data-name="zonitsu [awakened]"
      >
        <div class="data-card">
          <div class="data-img-container bg-mythic">
            <a href="../units/eoszenitsu" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Zonitsu [Awakened]"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Zonitsu [Awakened]</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Psychic"
        data-name="aya"
      >
        <div class="data-card">
          <div class="data-img-container bg-legendary">
            <a href="../units/ayase" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Aya"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Aya</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Psychic"
        data-name="boru"
      >
        <div class="data-card">
          <div class="data-img-container bg-legendary">
            <a href="../units/boros" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Boru"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Boru</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Fighting"
        data-name="dungpoo"
      >
        <div class="data-card">
          <div class="data-img-container bg-legendary">
            <a href="../units/dongsoo" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Dungpoo"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Dungpoo</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Psychic"
        data-name="freeze"
      >
        <div class="data-card">
          <div class="data-img-container bg-legendary">
            <a href="../units/frieza 1st form" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Freeze"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Freeze</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Ice"
        data-name="geo"
      >
        <div class="data-card">
          <div class="data-img-container bg-legendary">
            <a href="../units/eugeo" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Geo"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Geo</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Fighting"
        data-name="gio"
      >
        <div class="data-card">
          <div class="data-img-container bg-legendary">
            <a href="../units/dio" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Gio"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Gio</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Fighting"
        data-name="goden"
      >
        <div class="data-card">
          <div class="data-img-container bg-legendary">
            <a href="../units/goten" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Goden"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Goden</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Dark"
        data-name="goko dark"
      >
        <div class="data-card">
          <div class="data-img-container bg-legendary">
            <a href="../units/goku black" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Goko Dark"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Goko Dark</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Grass"
        data-name="hana"
      >
        <div class="data-card">
          <div class="data-img-container bg-legendary">
            <a href="../units/hanami" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Hana"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Hana</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Water"
        data-name="himothy"
      >
        <div class="data-card">
          <div class="data-img-container bg-legendary">
            <a href="../units/himmel" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Himothy"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Himothy</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Poison"
        data-name="imperfect konchu"
      >
        <div class="data-card">
          <div class="data-img-container bg-legendary">
            <a href="../units/cell" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Imperfect Konchu"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Imperfect Konchu</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Dark"
        data-name="itchy"
      >
        <div class="data-card">
          <div class="data-img-container bg-legendary">
            <a href="../units/itachi" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Itchy"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Itchy</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Fire"
        data-name="jogoat"
      >
        <div class="data-card">
          <div class="data-img-container bg-legendary">
            <a href="../units/jogo" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Jogoat"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Jogoat</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Holy"
        data-name="juno"
      >
        <div class="data-card">
          <div class="data-img-container bg-legendary">
            <a href="../units/joohee" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Juno"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Juno</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Steel"
        data-name="kaito"
      >
        <div class="data-card">
          <div class="data-img-container bg-legendary">
            <a href="../units/kite" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Kaito"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Kaito</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Steel"
        data-name="kendo"
      >
        <div class="data-card">
          <div class="data-img-container bg-legendary">
            <a href="../units/kenshin" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Kendo"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Kendo</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Neutral"
        data-name="kisu"
      >
        <div class="data-card">
          <div class="data-img-container bg-legendary">
            <a href="../units/kisuke" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Kisu"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Kisu</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Steel"
        data-name="kuropi"
      >
        <div class="data-card">
          <div class="data-img-container bg-legendary">
            <a href="../units/kurapika" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Kuropi"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Kuropi</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Neutral"
        data-name="lawlight"
      >
        <div class="data-card">
          <div class="data-img-container bg-legendary">
            <a href="../units/l lawliet" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Lawlight"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Lawlight</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Ice"
        data-name="lion"
      >
        <div class="data-card">
          <div class="data-img-container bg-legendary">
            <a href="../units/lyon" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Lion"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Lion</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Neutral"
        data-name="lollang"
      >
        <div class="data-card">
          <div class="data-img-container bg-legendary">
            <a href="../units/roland" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Lollang"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Lollang</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Fighting"
        data-name="mahi"
      >
        <div class="data-card">
          <div class="data-img-container bg-legendary">
            <a href="../units/mahito" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Mahi"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Mahi</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Dark"
        data-name="megu"
      >
        <div class="data-card">
          <div class="data-img-container bg-legendary">
            <a href="../units/megumi" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Megu"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Megu</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Steel"
        data-name="microw"
      >
        <div class="data-card">
          <div class="data-img-container bg-legendary">
            <a href="../units/mihawk" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Microw"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Microw</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Fire"
        data-name="netsu"
      >
        <div class="data-card">
          <div class="data-img-container bg-legendary">
            <a href="../units/natsu" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Netsu"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Netsu</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Steel"
        data-name="nobaro"
      >
        <div class="data-card">
          <div class="data-img-container bg-legendary">
            <a href="../units/nobara" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Nobaro"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Nobaro</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Wind"
        data-name="reaper child"
      >
        <div class="data-card">
          <div class="data-img-container bg-legendary">
            <a href="../units/deathkid" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Reaper Child"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Reaper Child</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Steel"
        data-name="rookie assassin"
      >
        <div class="data-card">
          <div class="data-img-container bg-legendary">
            <a href="../units/kang" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Rookie Assassin"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Rookie Assassin</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Ice"
        data-name="ruka"
      >
        <div class="data-card">
          <div class="data-img-container bg-legendary">
            <a href="../units/rukia" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Ruka"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Ruka</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Electric"
        data-name="sosoke (kirin)"
      >
        <div class="data-card">
          <div class="data-img-container bg-legendary">
            <a href="../units/sasuke[kirin]" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Sosoke (Kirin)"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Sosoke (Kirin)</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Neutral"
        data-name="speedy sonic"
      >
        <div class="data-card">
          <div class="data-img-container bg-legendary">
            <a href="../units/sonic" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Speedy Sonic"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Speedy Sonic</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Fighting"
        data-name="the juicebox"
      >
        <div class="data-card">
          <div class="data-img-container bg-legendary">
            <a href="../units/kid trunks" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="The Juicebox"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">The Juicebox</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Wind"
        data-name="ulquorio"
      >
        <div class="data-card">
          <div class="data-img-container bg-legendary">
            <a href="../units/ulquiorra" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Ulquorio"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Ulquorio</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Dark"
        data-name="zangu"
      >
        <div class="data-card">
          <div class="data-img-container bg-legendary">
            <a href="../units/zangetsu" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Zangu"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Zangu</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Electric"
        data-name="zonitsu"
      >
        <div class="data-card">
          <div class="data-img-container bg-legendary">
            <a href="../units/zenitsu" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Zonitsu"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Zonitsu</span>
        </div>
      </div>
      
      <div
        class="data-item Epic Ground"
        data-name="aligator"
      >
        <div class="data-card">
          <div class="data-img-container bg-epic">
            <a href="../units/crocodile" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Aligator"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Aligator</span>
        </div>
      </div>
      
      <div
        class="data-item Epic Poison"
        data-name="bug queen"
      >
        <div class="data-card">
          <div class="data-img-container bg-epic">
            <a href="../units/mosquitogirl" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Bug Queen"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Bug Queen</span>
        </div>
      </div>
      
      <div
        class="data-item Epic Fighting"
        data-name="greg"
      >
        <div class="data-card">
          <div class="data-img-container bg-epic">
            <a href="../units/gregor" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Greg"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Greg</span>
        </div>
      </div>
      
      <div
        class="data-item Epic Grass"
        data-name="inusuke"
      >
        <div class="data-card">
          <div class="data-img-container bg-epic">
            <a href="../units/inosuke" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Inusuke"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Inusuke</span>
        </div>
      </div>
      
      <div
        class="data-item Epic Electric"
        data-name="kekeshi"
      >
        <div class="data-card">
          <div class="data-img-container bg-epic">
            <a href="../units/kakashi" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Kekeshi"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Kekeshi</span>
        </div>
      </div>
      
      <div
        class="data-item Epic Ground"
        data-name="klai"
      >
        <div class="data-card">
          <div class="data-img-container bg-epic">
            <a href="../units/klein" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Klai"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Klai</span>
        </div>
      </div>
      
      <div
        class="data-item Epic Fighting"
        data-name="kokoin"
      >
        <div class="data-card">
          <div class="data-img-container bg-epic">
            <a href="../units/kakyoin" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Kokoin"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Kokoin</span>
        </div>
      </div>
      
      <div
        class="data-item Epic Psychic"
        data-name="pickle"
      >
        <div class="data-card">
          <div class="data-img-container bg-epic">
            <a href="../units/piccolo" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Pickle"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Pickle</span>
        </div>
      </div>
      
      <div
        class="data-item Epic Fighting"
        data-name="yamba"
      >
        <div class="data-card">
          <div class="data-img-container bg-epic">
            <a href="../units/yamcha" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Yamba"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Yamba</span>
        </div>
      </div>
      
      <div
        class="data-item Rare Fire"
        data-name="fire leg"
      >
        <div class="data-card">
          <div class="data-img-container bg-rare">
            <a href="../units/sanji" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Fire Leg"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Fire Leg</span>
        </div>
      </div>
      
      <div
        class="data-item Rare Fighting"
        data-name="goko"
      >
        <div class="data-card">
          <div class="data-img-container bg-rare">
            <a href="../units/goku" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Goko"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Goko</span>
        </div>
      </div>
      
      <div
        class="data-item Rare Neutral"
        data-name="nemo"
      >
        <div class="data-card">
          <div class="data-img-container bg-rare">
            <a href="../units/nami" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Nemo"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Nemo</span>
        </div>
      </div>
      
      <div
        class="data-item Rare Wind"
        data-name="noroto"
      >
        <div class="data-card">
          <div class="data-img-container bg-rare">
            <a href="../units/naruto" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Noroto"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Noroto</span>
        </div>
      </div>
      
      <div
        class="data-item Rare Steel"
        data-name="roro"
      >
        <div class="data-card">
          <div class="data-img-container bg-rare">
            <a href="../units/zoro" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Roro"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Roro</span>
        </div>
      </div>
      
      <div
        class="data-item Rare Steel"
        data-name="ryko"
      >
        <div class="data-card">
          <div class="data-img-container bg-rare">
            <a href="../units/ryuko" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Ryko"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Ryko</span>
        </div>
      </div>
      
      <div
        class="data-item Rare Electric"
        data-name="sosoke"
      >
        <div class="data-card">
          <div class="data-img-container bg-rare">
            <a href="../units/sasuke" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Sosoke"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Sosoke</span>
        </div>
      </div>
      
      <div
        class="data-item Rare Water"
        data-name="tojiro"
      >
        <div class="data-card">
          <div class="data-img-container bg-rare">
            <a href="../units/tanjiro" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Tojiro"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Tojiro</span>
        </div>
      </div>
      
      <div
        class="data-item Rare Psychic"
        data-name="vegetable"
      >
        <div class="data-card">
          <div class="data-img-container bg-rare">
            <a href="../units/vegeta" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Vegetable"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Vegetable</span>
        </div>
      </div>
      
      <div
        class="data-item Rare Grass"
        data-name="virtual swordgirl"
      >
        <div class="data-card">
          <div class="data-img-container bg-rare">
            <a href="../units/asuna" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Virtual Swordgirl"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Virtual Swordgirl</span>
        </div>
      </div>
      
      <div
        class="data-item Rare Steel"
        data-name="virtual swordman"
      >
        <div class="data-card">
          <div class="data-img-container bg-rare">
            <a href="../units/kirito" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="Virtual Swordman"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">Virtual Swordman</span>
        </div>
      </div>
      
      <div
        class="data-item Royale Fighting"
        data-name="testunitforvolo"
      >
        <div class="data-card">
          <div class="data-img-container bg-royale">
            <a href="../units/testunitforvolo" class="data-link">
              <img
                src="http://placehold.co/120x120"
                alt="TestUnitForVolo"
                loading="lazy"
              />
            </a>
          </div>
          <span class="data-name">TestUnitForVolo</span>
        </div>
      </div>
      
    </div>
  </div>
</div>