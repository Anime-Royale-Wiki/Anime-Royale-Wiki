<div x-data="unitFilterSystem" class="db-container glow-default">
  <div class="db-title">Units</div>
  <div class="db-content">
    <div class="unit-menu">
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
          placeholder="Search units..."
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
            <h4 class="filter-category-title">Element</h4>
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

    <div class="unit-grid">
      
      <div
        class="unit-item Rare Fire"
        data-name="fire leg"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-rare">
            <a href="../units/sanji" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Fire Leg"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Fire Leg</span>
        </div>
      </div>
      
      <div
        class="unit-item Rare Fighting"
        data-name="goko"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-rare">
            <a href="../units/goku" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Goko"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Goko</span>
        </div>
      </div>
      
      <div
        class="unit-item Legendary Fighting"
        data-name="the juicebox"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-legendary">
            <a href="../units/kid trunks" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="The Juicebox"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">The Juicebox</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Psychic"
        data-name="okuno"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/okuyasu" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Okuno"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Okuno</span>
        </div>
      </div>
      
      <div
        class="unit-item Secret Grass"
        data-name="deer girl"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-secret">
            <a href="../units/nokotan" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Deer Girl"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Deer Girl</span>
        </div>
      </div>
      
      <div
        class="unit-item Legendary Electric"
        data-name="sosoke (kirin)"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-legendary">
            <a href="../units/sasuke[kirin]" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Sosoke (Kirin)"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Sosoke (Kirin)</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Dark"
        data-name="the evil cup"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/majinvegeta" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="The Evil Cup"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">The Evil Cup</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Psychic"
        data-name="freeze [final]"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/frieza" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Freeze [Final]"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Freeze [Final]</span>
        </div>
      </div>
      
      <div
        class="unit-item Epic Psychic"
        data-name="pickle"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-epic">
            <a href="../units/piccolo" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Pickle"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Pickle</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Psychic"
        data-name="gotho"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/gojo" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Gotho"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Gotho</span>
        </div>
      </div>
      
      <div
        class="unit-item Rare Electric"
        data-name="sosoke"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-rare">
            <a href="../units/sasuke" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Sosoke"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Sosoke</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Fire"
        data-name="game master"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/heathcliff" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Game Master"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Game Master</span>
        </div>
      </div>
      
      <div
        class="unit-item Secret Psychic"
        data-name="eyezen"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-secret">
            <a href="../units/aizen" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Eyezen"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Eyezen</span>
        </div>
      </div>
      
      <div
        class="unit-item Legendary Fire"
        data-name="jogoat"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-legendary">
            <a href="../units/jogo" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Jogoat"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Jogoat</span>
        </div>
      </div>
      
      <div
        class="unit-item Legendary Fighting"
        data-name="gio"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-legendary">
            <a href="../units/dio" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Gio"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Gio</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Poison"
        data-name="semi-perfect konchu"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/cellevo" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Semi-Perfect Konchu"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Semi-Perfect Konchu</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Steel"
        data-name="virtual swordmaster [ultimate]"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/kiritooaevo" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Virtual Swordmaster [Ultimate]"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Virtual Swordmaster [Ultimate]</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Fire"
        data-name="game master [serious]"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/heathcliff [serious]" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Game Master [Serious]"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Game Master [Serious]</span>
        </div>
      </div>
      
      <div
        class="unit-item Legendary Dark"
        data-name="zangu"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-legendary">
            <a href="../units/zangetsu" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Zangu"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Zangu</span>
        </div>
      </div>
      
      <div
        class="unit-item Secret Dark"
        data-name="almighty"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-secret">
            <a href="../units/yhwach" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Almighty"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Almighty</span>
        </div>
      </div>
      
      <div
        class="unit-item Legendary Psychic"
        data-name="freeze"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-legendary">
            <a href="../units/frieza 1st form" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Freeze"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Freeze</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Dark"
        data-name="mira [demon]"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/mirajane" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Mira [Demon]"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Mira [Demon]</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Holy"
        data-name="super boogtenks"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/buutenks" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Super Boogtenks"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Super Boogtenks</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Psychic"
        data-name="getho"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/geto" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Getho"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Getho</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Wind"
        data-name="leafy [fairy]"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/leafa [serious]" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Leafy [Fairy]"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Leafy [Fairy]</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Steel"
        data-name="stabs"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/shanks" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Stabs"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Stabs</span>
        </div>
      </div>
      
      <div
        class="unit-item Rare Wind"
        data-name="noroto"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-rare">
            <a href="../units/naruto" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Noroto"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Noroto</span>
        </div>
      </div>
      
      <div
        class="unit-item Legendary Ice"
        data-name="geo"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-legendary">
            <a href="../units/eugeo" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Geo"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Geo</span>
        </div>
      </div>
      
      <div
        class="unit-item Rare Grass"
        data-name="virtual swordgirl"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-rare">
            <a href="../units/asuna" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Virtual Swordgirl"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Virtual Swordgirl</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Fighting"
        data-name="gobanks"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/gotenks" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Gobanks"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Gobanks</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Holy"
        data-name="goko (end)"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/gokuzend" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Goko (End)"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Goko (End)</span>
        </div>
      </div>
      
      <div
        class="unit-item Rare Steel"
        data-name="ryko"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-rare">
            <a href="../units/ryuko" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Ryko"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Ryko</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Dark"
        data-name="ichiko [awakened]"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/ichigobankai" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Ichiko [Awakened]"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Ichiko [Awakened]</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Fighting"
        data-name="otakurun [venomous]"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/okarunbundle" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Otakurun [Venomous]"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Otakurun [Venomous]</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Fighting"
        data-name="jotero"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/jotaro" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Jotero"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Jotero</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Fighting"
        data-name="yeagar"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/eren" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Yeagar"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Yeagar</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Fighting"
        data-name="otakurun"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/okarun" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Otakurun"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Otakurun</span>
        </div>
      </div>
      
      <div
        class="unit-item Legendary Dark"
        data-name="goko dark"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-legendary">
            <a href="../units/goku black" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Goko Dark"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Goko Dark</span>
        </div>
      </div>
      
      <div
        class="unit-item Legendary Fighting"
        data-name="goden"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-legendary">
            <a href="../units/goten" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Goden"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Goden</span>
        </div>
      </div>
      
      <div
        class="unit-item Legendary Psychic"
        data-name="aya"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-legendary">
            <a href="../units/ayase" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Aya"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Aya</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Steel"
        data-name="misaka"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/mikasa" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Misaka"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Misaka</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Steel"
        data-name="the drink"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/futuretrunks" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="The Drink"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">The Drink</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Dark"
        data-name="nakuma"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/nazuna" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Nakuma"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Nakuma</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Holy"
        data-name="kid boog"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/kidbuu" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Kid Boog"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Kid Boog</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Dark"
        data-name="nightmare xiii"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/death13" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Nightmare XIII"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Nightmare XIII</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Fire"
        data-name="captain yama"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/yamamoto" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Captain Yama"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Captain Yama</span>
        </div>
      </div>
      
      <div
        class="unit-item Rare Neutral"
        data-name="nemo"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-rare">
            <a href="../units/nami" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Nemo"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Nemo</span>
        </div>
      </div>
      
      <div
        class="unit-item Legendary Steel"
        data-name="nobaro"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-legendary">
            <a href="../units/nobara" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Nobaro"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Nobaro</span>
        </div>
      </div>
      
      <div
        class="unit-item Epic Ground"
        data-name="aligator"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-epic">
            <a href="../units/crocodile" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Aligator"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Aligator</span>
        </div>
      </div>
      
      <div
        class="unit-item Legendary Steel"
        data-name="microw"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-legendary">
            <a href="../units/mihawk" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Microw"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Microw</span>
        </div>
      </div>
      
      <div
        class="unit-item Epic Ground"
        data-name="klai"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-epic">
            <a href="../units/klein" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Klai"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Klai</span>
        </div>
      </div>
      
      <div
        class="unit-item Legendary Dark"
        data-name="megu"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-legendary">
            <a href="../units/megumi" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Megu"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Megu</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Dark"
        data-name="manara"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/madara" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Manara"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Manara</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Holy"
        data-name="alize"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/alice" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Alize"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Alize</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Grass"
        data-name="sunny"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/shunsui" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Sunny"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Sunny</span>
        </div>
      </div>
      
      <div
        class="unit-item Secret Water"
        data-name="virtual sniper"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-secret">
            <a href="../units/shino" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Virtual Sniper"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Virtual Sniper</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Wind"
        data-name="leafy"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/leafa" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Leafy"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Leafy</span>
        </div>
      </div>
      
      <div
        class="unit-item Legendary Neutral"
        data-name="lawlight"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-legendary">
            <a href="../units/l lawliet" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Lawlight"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Lawlight</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Poison"
        data-name="perfect konchu"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/cellevo2" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Perfect Konchu"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Perfect Konchu</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Fighting"
        data-name="gun [pact]"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/gonevo" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Gun [Pact]"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Gun [Pact]</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Fighting"
        data-name="teen gokan (awakened)"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/gohanteenssj2" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Teen Gokan (Awakened)"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Teen Gokan (Awakened)</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Holy"
        data-name="super booghan"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/buuhan" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Super Booghan"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Super Booghan</span>
        </div>
      </div>
      
      <div
        class="unit-item Rare Steel"
        data-name="virtual swordman"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-rare">
            <a href="../units/kirito" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Virtual Swordman"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Virtual Swordman</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Ice"
        data-name="tochito"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/toshiro" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Tochito"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Tochito</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Dark"
        data-name="dracula"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/alucard" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Dracula"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Dracula</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Steel"
        data-name="moon demon"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/kokushibo" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Moon Demon"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Moon Demon</span>
        </div>
      </div>
      
      <div
        class="unit-item Legendary Poison"
        data-name="imperfect konchu"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-legendary">
            <a href="../units/cell" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Imperfect Konchu"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Imperfect Konchu</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Steel"
        data-name="virtual swordwoman"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/asunaoa" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Virtual Swordwoman"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Virtual Swordwoman</span>
        </div>
      </div>
      
      <div
        class="unit-item Secret Dark"
        data-name="shadow"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-secret">
            <a href="../units/cid" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Shadow"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Shadow</span>
        </div>
      </div>
      
      <div
        class="unit-item Epic Grass"
        data-name="inusuke"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-epic">
            <a href="../units/inosuke" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Inusuke"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Inusuke</span>
        </div>
      </div>
      
      <div
        class="unit-item Legendary Steel"
        data-name="kaito"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-legendary">
            <a href="../units/kite" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Kaito"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Kaito</span>
        </div>
      </div>
      
      <div
        class="unit-item Secret Psychic"
        data-name="friend"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-secret">
            <a href="../units/frieren" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Friend"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Friend</span>
        </div>
      </div>
      
      <div
        class="unit-item Legendary Wind"
        data-name="reaper child"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-legendary">
            <a href="../units/deathkid" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Reaper Child"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Reaper Child</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Psychic"
        data-name="gotho [honored]"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/gojoevo" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Gotho [Honored]"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Gotho [Honored]</span>
        </div>
      </div>
      
      <div
        class="unit-item Legendary Fire"
        data-name="netsu"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-legendary">
            <a href="../units/natsu" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Netsu"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Netsu</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Fighting"
        data-name="goko the 3rd"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/goku (ssj3)" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Goko The 3rd"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Goko The 3rd</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Fighting"
        data-name="keneki"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/kaneki" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Keneki"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Keneki</span>
        </div>
      </div>
      
      <div
        class="unit-item Epic Electric"
        data-name="kekeshi"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-epic">
            <a href="../units/kakashi" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Kekeshi"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Kekeshi</span>
        </div>
      </div>
      
      <div
        class="unit-item Legendary Dark"
        data-name="itchy"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-legendary">
            <a href="../units/itachi" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Itchy"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Itchy</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Holy"
        data-name="gogetable (angel)"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/gogeta" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Gogetable (Angel)"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Gogetable (Angel)</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Steel"
        data-name="vile"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/levi" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Vile"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Vile</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Dark"
        data-name="jamba"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/janemba" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Jamba"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Jamba</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Fighting"
        data-name="adult gokan"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/adultgohan" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Adult Gokan"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Adult Gokan</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Steel"
        data-name="virtual swordmaster [awakened]"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/kiritooa" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Virtual Swordmaster [Awakened]"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Virtual Swordmaster [Awakened]</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Psychic"
        data-name="getho [zero]"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/getoevo" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Getho [Zero]"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Getho [Zero]</span>
        </div>
      </div>
      
      <div
        class="unit-item Legendary Wind"
        data-name="ulquorio"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-legendary">
            <a href="../units/ulquiorra" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Ulquorio"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Ulquorio</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Fighting"
        data-name="goko [ssj]"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/goku [ssj]" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Goko [SSJ]"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Goko [SSJ]</span>
        </div>
      </div>
      
      <div
        class="unit-item Legendary Ice"
        data-name="lion"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-legendary">
            <a href="../units/lyon" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Lion"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Lion</span>
        </div>
      </div>
      
      <div
        class="unit-item Rare Psychic"
        data-name="vegetable"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-rare">
            <a href="../units/vegeta" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Vegetable"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Vegetable</span>
        </div>
      </div>
      
      <div
        class="unit-item Secret Fighting"
        data-name="uzi"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-secret">
            <a href="../units/tengen" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Uzi"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Uzi</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Dark"
        data-name="thukuna [king]"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/sukunaevo" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Thukuna [King]"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Thukuna [King]</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Fire"
        data-name="flame master [ablaze]"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/rengokuevo" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Flame Master [Ablaze]"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Flame Master [Ablaze]</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Water"
        data-name="bean"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/bang" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Bean"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Bean</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Steel"
        data-name="bonkstick"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/metalbat" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Bonkstick"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Bonkstick</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Ice"
        data-name="jolly eslife"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/esdeathbundle" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Jolly Eslife"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Jolly Eslife</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Psychic"
        data-name="boru [released]"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/borosevo" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Boru [Released]"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Boru [Released]</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Holy"
        data-name="super boog"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/superbuu" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Super Boog"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Super Boog</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Dark"
        data-name="dako"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/daki" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Dako"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Dako</span>
        </div>
      </div>
      
      <div
        class="unit-item Legendary Steel"
        data-name="kendo"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-legendary">
            <a href="../units/kenshin" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Kendo"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Kendo</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Water"
        data-name="gui"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/giyu" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Gui"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Gui</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Psychic"
        data-name="fubuu"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/fubuki" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Fubuu"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Fubuu</span>
        </div>
      </div>
      
      <div
        class="unit-item Epic Fighting"
        data-name="yamba"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-epic">
            <a href="../units/yamcha" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Yamba"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Yamba</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Electric"
        data-name="kill [angered]"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/killuaevo" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Kill [Angered]"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Kill [Angered]</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Ice"
        data-name="emily"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/emilia" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Emily"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Emily</span>
        </div>
      </div>
      
      <div
        class="unit-item Legendary Psychic"
        data-name="boru"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-legendary">
            <a href="../units/boros" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Boru"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Boru</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Dark"
        data-name="ulquioro (second)"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/ulquiorra (segunda)" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Ulquioro (Second)"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Ulquioro (Second)</span>
        </div>
      </div>
      
      <div
        class="unit-item Legendary Neutral"
        data-name="speedy sonic"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-legendary">
            <a href="../units/sonic" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Speedy Sonic"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Speedy Sonic</span>
        </div>
      </div>
      
      <div
        class="unit-item Legendary Electric"
        data-name="zonitsu"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-legendary">
            <a href="../units/zenitsu" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Zonitsu"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Zonitsu</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Ice"
        data-name="kuzo"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/kuzan" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Kuzo"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Kuzo</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Electric"
        data-name="killa"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/killua" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Killa"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Killa</span>
        </div>
      </div>
      
      <div
        class="unit-item Secret Dark"
        data-name="demon lord"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-secret">
            <a href="../units/muzan" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Demon Lord"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Demon Lord</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Neutral"
        data-name="card magician"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/hisoka" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Card Magician"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Card Magician</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Fighting"
        data-name="kaiju"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/kaiju" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Kaiju"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Kaiju</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Holy"
        data-name="vegitu"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/vegito" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Vegitu"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Vegitu</span>
        </div>
      </div>
      
      <div
        class="unit-item Secret Fighting"
        data-name="kaillou (serious)"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-secret">
            <a href="../units/saitamaevo" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Kaillou (Serious)"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Kaillou (Serious)</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Dark"
        data-name="thukuna"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/sukuna" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Thukuna"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Thukuna</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Steel"
        data-name="atomic warrior"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/atomicsamurai" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Atomic Warrior"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Atomic Warrior</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Dark"
        data-name="ichiko"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/ichigo" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Ichiko"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Ichiko</span>
        </div>
      </div>
      
      <div
        class="unit-item Secret Fighting"
        data-name="broccoli"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-secret">
            <a href="../units/zbroly" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Broccoli"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Broccoli</span>
        </div>
      </div>
      
      <div
        class="unit-item Epic Fighting"
        data-name="greg"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-epic">
            <a href="../units/gregor" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Greg"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Greg</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Electric"
        data-name="yoru"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/yoruichi" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Yoru"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Yoru</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Ice"
        data-name="eslife"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/esdeath" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Eslife"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Eslife</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Ice"
        data-name="akatou"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/akaza" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Akatou"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Akatou</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Fighting"
        data-name="gun"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/gon" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Gun"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Gun</span>
        </div>
      </div>
      
      <div
        class="unit-item Secret Steel"
        data-name="tochi"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-secret">
            <a href="../units/toji" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Tochi"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Tochi</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Psychic"
        data-name="boru [100% released]"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/borosdoubleevo" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Boru [100% Released]"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Boru [100% Released]</span>
        </div>
      </div>
      
      <div
        class="unit-item Legendary Neutral"
        data-name="kisu"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-legendary">
            <a href="../units/kisuke" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Kisu"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Kisu</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Dark"
        data-name="neko"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/neferpitou" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Neko"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Neko</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Electric"
        data-name="zonitsu [awakened]"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/eoszenitsu" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Zonitsu [Awakened]"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Zonitsu [Awakened]</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Dark"
        data-name="ichiko [gumetsu]"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/mugetsu" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Ichiko [Gumetsu]"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Ichiko [Gumetsu]</span>
        </div>
      </div>
      
      <div
        class="unit-item Rare Water"
        data-name="tojiro"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-rare">
            <a href="../units/tanjiro" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Tojiro"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Tojiro</span>
        </div>
      </div>
      
      <div
        class="unit-item Secret Fire"
        data-name="gen z"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-secret">
            <a href="../units/genos" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Gen Z"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Gen Z</span>
        </div>
      </div>
      
      <div
        class="unit-item Royale Fighting"
        data-name="testunitforvolo"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-royale">
            <a href="../units/testunitforvolo" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="TestUnitForVolo"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">TestUnitForVolo</span>
        </div>
      </div>
      
      <div
        class="unit-item Secret Psychic"
        data-name="yabo"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-secret">
            <a href="../units/yato" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Yabo"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Yabo</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Grass"
        data-name="sunny (release)"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/shunsuievo" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Sunny (Release)"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Sunny (Release)</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Holy"
        data-name="nezu"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/nezuko" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Nezu"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Nezu</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Psychic"
        data-name="yutha"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/yuta" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Yutha"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Yutha</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Steel"
        data-name="mitsu"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/mitsuri" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Mitsu"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Mitsu</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Rock"
        data-name="gomu"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/gyomei" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Gomu"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Gomu</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Dark"
        data-name="nezu [demon]"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/nezukoevo" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Nezu [Demon]"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Nezu [Demon]</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Dark"
        data-name="guitar"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/gyutaro" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Guitar"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Guitar</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Electric"
        data-name="yoru [raging raijin]"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/yoruichievo" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Yoru [Raging Raijin]"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Yoru [Raging Raijin]</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Fire"
        data-name="sun tojiro"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/suntanjiro" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Sun Tojiro"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Sun Tojiro</span>
        </div>
      </div>
      
      <div
        class="unit-item Rare Steel"
        data-name="roro"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-rare">
            <a href="../units/zoro" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Roro"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Roro</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Fire"
        data-name="flame master"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/rengoku" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Flame Master"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Flame Master</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Fire"
        data-name="hellborn"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/rin" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Hellborn"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Hellborn</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Fighting"
        data-name="teen gokan"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/teengohan" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Teen Gokan"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Teen Gokan</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Rock"
        data-name="xeke"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/zeke" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Xeke"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Xeke</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Fighting"
        data-name="motomoto"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/sakamoto" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Motomoto"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Motomoto</span>
        </div>
      </div>
      
      <div
        class="unit-item Epic Poison"
        data-name="bug queen"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-epic">
            <a href="../units/mosquitogirl" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Bug Queen"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Bug Queen</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Fighting"
        data-name="motomoto [thin]"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/sakamotoevo" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Motomoto [Thin]"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Motomoto [Thin]</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Fighting"
        data-name="donkey"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/madong" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Donkey"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Donkey</span>
        </div>
      </div>
      
      <div
        class="unit-item Legendary Holy"
        data-name="juno"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-legendary">
            <a href="../units/joohee" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Juno"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Juno</span>
        </div>
      </div>
      
      <div
        class="unit-item Secret Holy"
        data-name="nero"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-secret">
            <a href="../units/netero" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Nero"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Nero</span>
        </div>
      </div>
      
      <div
        class="unit-item Epic Fighting"
        data-name="kokoin"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-epic">
            <a href="../units/kakyoin" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Kokoin"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Kokoin</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Neutral"
        data-name="fanny"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/fran" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Fanny"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Fanny</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Fighting"
        data-name="chick"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/chika" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Chick"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Chick</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Fighting"
        data-name="kaillou"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/saitama" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Kaillou"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Kaillou</span>
        </div>
      </div>
      
      <div
        class="unit-item Secret Steel"
        data-name="aura farmer [purple]"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-secret">
            <a href="../units/igrisevo" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Aura Farmer [Purple]"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Aura Farmer [Purple]</span>
        </div>
      </div>
      
      <div
        class="unit-item Secret Grass"
        data-name="dreamer"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-secret">
            <a href="../units/giorno" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Dreamer"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Dreamer</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Holy"
        data-name="origiri"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/origami" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Origiri"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Origiri</span>
        </div>
      </div>
      
      <div
        class="unit-item Secret Dark"
        data-name="merem"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-secret">
            <a href="../units/meruem" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Merem"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Merem</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Steel"
        data-name="silver knight"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/polnareff" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Silver Knight"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Silver Knight</span>
        </div>
      </div>
      
      <div
        class="unit-item Legendary Ice"
        data-name="ruka"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-legendary">
            <a href="../units/rukia" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Ruka"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Ruka</span>
        </div>
      </div>
      
      <div
        class="unit-item Secret Dark"
        data-name="aura king [monarch]"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-secret">
            <a href="../units/sunjinwooevo2" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Aura King [Monarch]"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Aura King [Monarch]</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Psychic"
        data-name="rumika"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/riruka" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Rumika"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Rumika</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Holy"
        data-name="urwu (kwency)"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/uryuevo" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Urwu (Kwency)"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Urwu (Kwency)</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Dark"
        data-name="headless swordsman"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/goto" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Headless Swordsman"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Headless Swordsman</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Holy"
        data-name="urwu"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/uryu" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Urwu"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Urwu</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Holy"
        data-name="moon princess"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/sailormoon" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Moon Princess"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Moon Princess</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Dark"
        data-name="aura king [shadow]"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/sunjinwooevo" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Aura King [Shadow]"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Aura King [Shadow]</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Holy"
        data-name="mahoka"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/madoka" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Mahoka"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Mahoka</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Neutral"
        data-name="the weakest esper"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/touma" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="The Weakest Esper"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">The Weakest Esper</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Steel"
        data-name="aura farmer"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/igris" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Aura Farmer"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Aura Farmer</span>
        </div>
      </div>
      
      <div
        class="unit-item Royalty Dark"
        data-name="ichigoat [true]"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-royalty">
            <a href="../units/trueichigo" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Ichigoat [True]"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Ichigoat [True]</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Wind"
        data-name="weather"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/weatherreport" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Weather"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Weather</span>
        </div>
      </div>
      
      <div
        class="unit-item Secret Dark"
        data-name="the mastermind"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-secret">
            <a href="../units/lelouch" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="The Mastermind"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">The Mastermind</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Grass"
        data-name="mims"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/mimosa" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Mims"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Mims</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Neutral"
        data-name="orihamis"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/orihime" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Orihamis"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Orihamis</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Steel"
        data-name="kenny"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/kenpachi" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Kenny"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Kenny</span>
        </div>
      </div>
      
      <div
        class="unit-item Secret Holy"
        data-name="gio [over heaven]"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-secret">
            <a href="../units/dio[oh]" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Gio [Over Heaven]"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Gio [Over Heaven]</span>
        </div>
      </div>
      
      <div
        class="unit-item Legendary Grass"
        data-name="hana"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-legendary">
            <a href="../units/hanami" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Hana"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Hana</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Fighting"
        data-name="loop"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/lu" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Loop"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Loop</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Psychic"
        data-name="ria"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/rikka" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Ria"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Ria</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Dark"
        data-name="diablo"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/diavolo" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Diablo"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Diablo</span>
        </div>
      </div>
      
      <div
        class="unit-item Secret Fire"
        data-name="demon blade"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-secret">
            <a href="../units/akame" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Demon Blade"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Demon Blade</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Holy"
        data-name="maiko"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/bocchi" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Maiko"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Maiko</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Dark"
        data-name="toka"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/tohka" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Toka"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Toka</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Fire"
        data-name="gems master"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/rin tohsaka" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Gems Master"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Gems Master</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Fighting"
        data-name="beast hunter"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/baek" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Beast Hunter"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Beast Hunter</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Psychic"
        data-name="tatsu"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/tatsumaki" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Tatsu"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Tatsu</span>
        </div>
      </div>
      
      <div
        class="unit-item Secret Steel"
        data-name="nagu"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-secret">
            <a href="../units/nagumo" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Nagu"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Nagu</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Steel"
        data-name="greg [kurokumo]"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/gregorevo" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Greg [Kurokumo]"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Greg [Kurokumo]</span>
        </div>
      </div>
      
      <div
        class="unit-item Secret Psychic"
        data-name="shine"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-secret">
            <a href="../units/shin" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Shine"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Shine</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Wind"
        data-name="yuka"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/yukari" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Yuka"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Yuka</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Fighting"
        data-name="motomoto bunny [thin]"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/sakamotoevobundle" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Motomoto Bunny [Thin]"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Motomoto Bunny [Thin]</span>
        </div>
      </div>
      
      <div
        class="unit-item Legendary Steel"
        data-name="kuropi"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-legendary">
            <a href="../units/kurapika" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Kuropi"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Kuropi</span>
        </div>
      </div>
      
      <div
        class="unit-item Legendary Neutral"
        data-name="lollang"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-legendary">
            <a href="../units/roland" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Lollang"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Lollang</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Steel"
        data-name="haze"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/heisuke" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Haze"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Haze</span>
        </div>
      </div>
      
      <div
        class="unit-item Secret Fighting"
        data-name="valentine delight"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-secret">
            <a href="../units/funnyvalentine" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Valentine Delight"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Valentine Delight</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Ground"
        data-name="hashino"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/hashirama" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Hashino"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Hashino</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Fighting"
        data-name="motomoto bunny"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/sakamotobundle" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Motomoto Bunny"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Motomoto Bunny</span>
        </div>
      </div>
      
      <div
        class="unit-item Legendary Fighting"
        data-name="dungpoo"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-legendary">
            <a href="../units/dongsoo" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Dungpoo"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Dungpoo</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Steel"
        data-name="seven star hunter"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/liu" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Seven Star Hunter"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Seven Star Hunter</span>
        </div>
      </div>
      
      <div
        class="unit-item Legendary Water"
        data-name="himothy"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-legendary">
            <a href="../units/himmel" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Himothy"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Himothy</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Fire"
        data-name="s-rank bomber"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/choi" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="S-Rank Bomber"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">S-Rank Bomber</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Water"
        data-name="aura king"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/sunjinwoo" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Aura King"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Aura King</span>
        </div>
      </div>
      
      <div
        class="unit-item Secret Grass"
        data-name="ant general"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-secret">
            <a href="../units/beru" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Ant General"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Ant General</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Holy"
        data-name="light bearer [blessed]"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/chaeevo" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Light Bearer [Blessed]"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Light Bearer [Blessed]</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Fire"
        data-name="song"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/song" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Song"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Song</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Holy"
        data-name="light bearer"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/chae" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Light Bearer"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Light Bearer</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Neutral"
        data-name="beast hunter [wrath]"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/baekevo" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Beast Hunter [Wrath]"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Beast Hunter [Wrath]</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Dark"
        data-name="lollang (black silence)"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/rolandevo" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Lollang (Black Silence)"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Lollang (Black Silence)</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Wind"
        data-name="wind mage [spirit ascension]"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/yunoevo" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Wind Mage [Spirit Ascension]"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Wind Mage [Spirit Ascension]</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Wind"
        data-name="wind mage"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/yuno" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Wind Mage"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Wind Mage</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Fire"
        data-name="steamed"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/boiled" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Steamed"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Steamed</span>
        </div>
      </div>
      
      <div
        class="unit-item Legendary Fighting"
        data-name="mahi"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-legendary">
            <a href="../units/mahito" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Mahi"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Mahi</span>
        </div>
      </div>
      
      <div
        class="unit-item Mythic Fighting"
        data-name="thompson anderson"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-mythic">
            <a href="../units/thomas" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Thompson Anderson"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Thompson Anderson</span>
        </div>
      </div>
      
      <div
        class="unit-item Legendary Steel"
        data-name="rookie assassin"
      >
        <div class="unit-card">
          <div class="unit-img-container-face bg-legendary">
            <a href="../units/kang" class="unit-link-container">
              <img
                src="http://placehold.co/120x120"
                alt="Rookie Assassin"
                loading="lazy"
              />
            </a>
          </div>
          <span class="unit_name">Rookie Assassin</span>
        </div>
      </div>
      
    </div>
  </div>
</div>