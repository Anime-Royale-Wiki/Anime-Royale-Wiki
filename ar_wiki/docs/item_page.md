<div x-data="itemFilterSystem" class="db-container glow-items">
  <script>
    window.itemData = {"Apple": {"Class": "Food", "Description": "Used to give exp to units.", "Name": "Apple", "Obtainment": ["1", "2", "3", "4", "5", "6", "Corp City Act 1-6", "Fairy Town Act 1-6", "Ghoul City Act 1-6", "Green Planet Act 1-6", "Green Planet Rift", "Hidden Village Act 1-6", "Test Act 1-6"], "Rarity": "Rare"}, "Apron": {"Class": "Evo", "Description": "Used to evo Shin.", "Name": "Apron", "Obtainment": ["Not currently dropped"], "Rarity": "Rare"}, "Assassin\u0027s Double Daggers": {"Class": "Evo", "Description": "Used to evolve some units.", "Name": "Assassin\u0027s Double Daggers", "Obtainment": ["Not currently dropped"], "Rarity": "Legendary"}, "Aura Sword": {"Class": "Evo", "Description": "Used to evolve some units.", "Name": "Aura Sword", "Obtainment": ["Aura Room"], "Rarity": "Secret"}, "Aura Sword [Purple]": {"Class": "Evo", "Description": "Used to evolve some units.", "Name": "Aura Sword [Purple]", "Obtainment": ["Not currently dropped"], "Rarity": "Secret"}, "Bankai Sword": {"Class": "Evo", "Description": "Used to evolve some units.", "Name": "Bankai Sword", "Obtainment": ["Not currently dropped"], "Rarity": "Secret"}, "Baruka\u0027s Dagger": {"Class": "Evo", "Description": "Used to evolve some units.", "Name": "Baruka\u0027s Dagger", "Obtainment": ["Not currently dropped"], "Rarity": "Legendary"}, "Bean": {"Class": "Food", "Description": "Used to give exp to units.", "Name": "Bean", "Obtainment": ["Corp City Act 1-6", "Green Planet Act 1-6", "Green Planet Destroyed"], "Rarity": "Rare"}, "Beast Belt": {"Class": "Evo", "Description": "Used to evolve some units.", "Name": "Beast Belt", "Obtainment": ["Not currently dropped"], "Rarity": "Mythic"}, "Beast Claws": {"Class": "Evo", "Description": "Used to evolve some units.", "Name": "Beast Claws", "Obtainment": ["God Statue"], "Rarity": "Mythic"}, "Black Sword": {"Class": "Evo", "Description": "Used to evolve Virtual Swordman [Awakened].", "Name": "Black Sword", "Obtainment": ["Red Palace"], "Rarity": "Legendary"}, "Blindfold": {"Class": "Evo", "Description": "Used to evolve Gotho.", "Name": "Blindfold", "Obtainment": ["Sorcery Academy"], "Rarity": "Legendary"}, "Boru Torso": {"Class": "Evo", "Description": "Used to evolve some units.", "Name": "Boru Torso", "Obtainment": ["Boru\u0027s Room"], "Rarity": "Mythic"}, "Burger": {"Class": "Food", "Description": "Used to give exp to units.", "Name": "Burger", "Obtainment": ["Ghoul City Act 1-6", "Test Act 1-6"], "Rarity": "Epic"}, "Candy": {"Class": "Food", "Description": "Used to give exp to units.", "Name": "Candy", "Obtainment": ["Not currently dropped"], "Rarity": "Mythic"}, "Candy Cane": {"Class": "Food", "Description": "Used to give exp to units.", "Name": "Candy Cane", "Obtainment": ["Not currently dropped"], "Rarity": "Mythic"}, "Cape": {"Class": "Evo", "Description": "Used to evolve some units.", "Name": "Cape", "Obtainment": ["Strongest\u0027s City Act 1-6"], "Rarity": "Mythic"}, "Christmas Capsule": {"Class": "Capsule", "Description": "Unlock festive units!", "Name": "Christmas Capsule", "Obtainment": ["Not currently dropped"], "Rarity": "Secret"}, "Cloud Cloak": {"Class": "Evo", "Description": "The cloak of the tsuki members.", "Name": "Cloud Cloak", "Obtainment": ["Not currently dropped"], "Rarity": "Legendary"}, "Cracked Power Core": {"Class": "Evo", "Description": "Used to evolve some units.", "Name": "Cracked Power Core", "Obtainment": ["Boru\u0027s Room"], "Rarity": "Mythic"}, "Crystal Ball 1": {"Class": "Misc", "Description": "Used to wish to the dragon (requires all the crystal balls)", "Name": "Crystal Ball 1", "Obtainment": ["Green Planet Act 6"], "Rarity": "Mythic"}, "Crystal Ball 2": {"Class": "Misc", "Description": "Used to wish to the dragon (requires all the crystal balls)", "Name": "Crystal Ball 2", "Obtainment": ["Fairy Town Act 6"], "Rarity": "Mythic"}, "Crystal Ball 3": {"Class": "Misc", "Description": "Used to wish to the dragon (requires all the crystal balls)", "Name": "Crystal Ball 3", "Obtainment": ["Corp City Act 6"], "Rarity": "Mythic"}, "Crystal Ball 4": {"Class": "Misc", "Description": "Used to wish to the dragon (requires all the crystal balls)", "Name": "Crystal Ball 4", "Obtainment": ["Green Planet Destroyed", "Green Planet Rift"], "Rarity": "Mythic"}, "Crystal Ball 5": {"Class": "Misc", "Description": "Used to wish to the dragon (requires all the crystal balls)", "Name": "Crystal Ball 5", "Obtainment": ["Ghoul City Rift", "Hidden Village Rift", "Red Palace"], "Rarity": "Mythic"}, "Crystal Ball 6": {"Class": "Misc", "Description": "Used to wish to the dragon (requires all the crystal balls)", "Name": "Crystal Ball 6", "Obtainment": ["Fairy Town Rift", "Lookout", "Sharkman Island Rift"], "Rarity": "Mythic"}, "Crystal Ball 7": {"Class": "Misc", "Description": "Used to wish to the dragon (requires all the crystal balls)", "Name": "Crystal Ball 7", "Obtainment": ["Hell"], "Rarity": "Mythic"}, "CupNoodle": {"Class": "Food", "Description": "Used to give exp to Units.", "Name": "CupNoodle", "Obtainment": ["Candy Park"], "Rarity": "Epic"}, "Cupcake": {"Class": "Food", "Description": "Used to give exp to units.", "Name": "Cupcake", "Obtainment": ["Ant Island", "Fairy Town Rift", "Ghoul City Rift", "God Statue", "Green Planet Rift", "Hidden Village Rift", "Lookout", "Orc Dungeon", "Sharkman Island Rift", "Slayers District", "The Underground Tomb"], "Rarity": "Mythic"}, "Cursed Energy": {"Class": "Evo", "Description": "Used to evolve some units.", "Name": "Cursed Energy", "Obtainment": ["Cursed Town Act 1-6"], "Rarity": "Legendary"}, "Cursed Finger": {"Class": "Stats", "Description": "Used to give a curse to your units.", "Name": "Cursed Finger", "Obtainment": ["Cursed Town Act 1-6", "Fairy Town Rift", "Ghoul City Rift", "Green Planet Rift", "Hidden Village Rift", "Sharkman Island Rift", "Sorcery Academy"], "Rarity": "Mythic"}, "Cursed Head Band": {"Class": "Evo", "Description": "Head Band of the hidden village traitors.", "Name": "Cursed Head Band", "Obtainment": ["Not currently dropped"], "Rarity": "Epic"}, "Cursed Orb": {"Class": "Evo", "Description": "Used to evolve Getho.", "Name": "Cursed Orb", "Obtainment": ["Cursed Town Act 1-6"], "Rarity": "Legendary"}, "Cyan Sword": {"Class": "Evo", "Description": "Used to evolve Virtual Swordman [Awakened].", "Name": "Cyan Sword", "Obtainment": ["Red Palace"], "Rarity": "Legendary"}, "Dark Elixir": {"Class": "Misc", "Description": "Used for smithing.", "Name": "Dark Elixir", "Obtainment": ["Not currently dropped"], "Rarity": "Mythic"}, "Deafbone": {"Class": "Card", "Description": "+24% Damage, -12% Range", "Name": "Deafbone", "Obtainment": ["Not currently dropped"], "Rarity": "Legendary"}, "Deaffone": {"Class": "Card", "Description": "+16% Damage, -8% Range", "Name": "Deaffone", "Obtainment": ["Not currently dropped"], "Rarity": "Epic"}, "Deafone": {"Class": "Card", "Description": "+8% Damage, -4% Range", "Name": "Deafone", "Obtainment": ["Not currently dropped"], "Rarity": "Rare"}, "Deaftone": {"Class": "Card", "Description": "+40% Damage, -20% Range", "Name": "Deaftone", "Obtainment": ["Not currently dropped"], "Rarity": "Mythic"}, "Deer": {"Class": "Evo", "Description": "DEEEEEEER.", "Name": "Deer", "Obtainment": ["Not currently dropped"], "Rarity": "Secret"}, "Demon Horn": {"Class": "Evo", "Description": "Used to evolve some units.", "Name": "Demon Horn", "Obtainment": ["Slayers District"], "Rarity": "Legendary"}, "Demon King Sword": {"Class": "Evo", "Description": "Used to evolve some units.", "Name": "Demon King Sword", "Obtainment": ["Not currently dropped"], "Rarity": "Legendary"}, "Demon Monarch Earings": {"Class": "Evo", "Description": "Used to evolve some units.", "Name": "Demon Monarch Earings", "Obtainment": ["Not currently dropped"], "Rarity": "Rare"}, "Demon Monarch\u0027s Necklace": {"Class": "Evo", "Description": "Used to evolve some units.", "Name": "Demon Monarch\u0027s Necklace", "Obtainment": ["Not currently dropped"], "Rarity": "Legendary"}, "Dice": {"Class": "Evo", "Description": "Used to evolve Nagumo.", "Name": "Dice", "Obtainment": ["Not currently dropped"], "Rarity": "Mythic"}, "Divine Earing": {"Class": "Misc", "Description": "Used to fuse Vegetable (Evil) and Goko (End).", "Name": "Divine Earing", "Obtainment": ["Hell"], "Rarity": "Mythic"}, "Divine Stone": {"Class": "Evo", "Description": "Evolution Material for some units.", "Name": "Divine Stone", "Obtainment": ["Fairy Town Act 1-6"], "Rarity": "Legendary"}, "Dominator\u0027s Rune (Purple)": {"Class": "Evo", "Description": "Used to evolve some units.", "Name": "Dominator\u0027s Rune (Purple)", "Obtainment": ["Not currently dropped"], "Rarity": "Legendary"}, "Dominator\u0027s Rune (Red)": {"Class": "Evo", "Description": "Used to evolve some units.", "Name": "Dominator\u0027s Rune (Red)", "Obtainment": ["Aura Room"], "Rarity": "Legendary"}, "Drawnup": {"Class": "Card", "Description": "For every unit not recieving a damage buff in this unit\u0027s range, this unit gains +50% Damage.", "Name": "Drawnup", "Obtainment": ["Not currently dropped"], "Rarity": "Rare"}, "Dummy Hair": {"Class": "Evo", "Description": "Used to evolve some units.", "Name": "Dummy Hair", "Obtainment": ["The Underground Tomb"], "Rarity": "Legendary"}, "Dummy Hat": {"Class": "Evo", "Description": "Used to evolve some units.", "Name": "Dummy Hat", "Obtainment": ["The Underground Tomb"], "Rarity": "Legendary"}, "Ecoist": {"Class": "Card", "Description": "-2% Cost", "Name": "Ecoist", "Obtainment": ["Not currently dropped"], "Rarity": "Rare"}, "Ecolist": {"Class": "Card", "Description": "-3% Cost", "Name": "Ecolist", "Obtainment": ["Not currently dropped"], "Rarity": "Epic"}, "Ecolo": {"Class": "Card", "Description": "-5% Cost", "Name": "Ecolo", "Obtainment": ["Not currently dropped"], "Rarity": "Legendary"}, "Ecoro": {"Class": "Card", "Description": "-6% Cost", "Name": "Ecoro", "Obtainment": ["Not currently dropped"], "Rarity": "Mythic"}, "Elixir Of Life": {"Class": "Misc", "Description": "Used for smithing.", "Name": "Elixir Of Life", "Obtainment": ["Not currently dropped"], "Rarity": "Mythic"}, "Ember": {"Class": "Card", "Description": "-12% SPA, +4% Cost", "Name": "Ember", "Obtainment": ["Not currently dropped"], "Rarity": "Mythic"}, "Embrew": {"Class": "Card", "Description": "-3% SPA, +2% Cost", "Name": "Embrew", "Obtainment": ["Not currently dropped"], "Rarity": "Epic"}, "Emburish": {"Class": "Card", "Description": "-1% SPA, +1% Cost", "Name": "Emburish", "Obtainment": ["Not currently dropped"], "Rarity": "Rare"}, "Emtan": {"Class": "Card", "Description": "-6% SPA, +3% Cost", "Name": "Emtan", "Obtainment": ["Not currently dropped"], "Rarity": "Legendary"}, "Evil Orb": {"Class": "Evo", "Description": "Used to evolve Boo.", "Name": "Evil Orb", "Obtainment": ["Lookout"], "Rarity": "Mythic"}, "Exchange Ring": {"Class": "Evo", "Description": "Used to evolve some units.", "Name": "Exchange Ring", "Obtainment": ["Ant Island"], "Rarity": "Legendary"}, "Eye Patch": {"Class": "Evo", "Description": "Used to evolve some units.", "Name": "Eye Patch", "Obtainment": ["Soul World Act 2"], "Rarity": "Legendary"}, "Fairy Sword": {"Class": "Evo", "Description": "Used to evolve Leafy.", "Name": "Fairy Sword", "Obtainment": ["Red Palace"], "Rarity": "Legendary"}, "Fairy Wings": {"Class": "Evo", "Description": "Used to evolve Leafy.", "Name": "Fairy Wings", "Obtainment": ["Red Palace"], "Rarity": "Legendary"}, "Fire Haori": {"Class": "Evo", "Description": "Used to evolve some units.", "Name": "Fire Haori", "Obtainment": ["Slayers District"], "Rarity": "Mythic"}, "Fire Katana": {"Class": "Evo", "Description": "Used to evolve some units.", "Name": "Fire Katana", "Obtainment": ["Slayers District"], "Rarity": "Mythic"}, "Fish": {"Class": "Food", "Description": "Used to give exp to units.", "Name": "Fish", "Obtainment": ["1", "2", "3", "4", "5", "6"], "Rarity": "Epic"}, "Flask": {"Class": "Food", "Description": "Used to give exp to Units.", "Name": "Flask", "Obtainment": ["Not currently dropped"], "Rarity": "Legendary"}, "Flip Book": {"Class": "Evo", "Description": "Used to evolve some units.", "Name": "Flip Book", "Obtainment": ["Soul World Act 1"], "Rarity": "Legendary"}, "Four Leaf Grimoire": {"Class": "Evo", "Description": "You can hear its power, like winds in a forest.", "Name": "Four Leaf Grimoire", "Obtainment": ["Not currently dropped"], "Rarity": "Mythic"}, "Game Shield": {"Class": "Evo", "Description": "Used to evolve Game Master.", "Name": "Game Shield", "Obtainment": ["Red Palace"], "Rarity": "Legendary"}, "Game Sword": {"Class": "Evo", "Description": "Used to evolve Game Master.", "Name": "Game Sword", "Obtainment": ["Red Palace"], "Rarity": "Legendary"}, "Gen Z Core": {"Class": "Evo", "Description": "Used to evolve some units.", "Name": "Gen Z Core", "Obtainment": ["Strongest\u0027s City Act 1-6"], "Rarity": "Secret"}, "Getho Outfit": {"Class": "Evo", "Description": "Used to evolve Getho.", "Name": "Getho Outfit", "Obtainment": ["Cursed Town Act 1-6"], "Rarity": "Mythic"}, "Glass Bow": {"Class": "Evo", "Description": "Used to evolve some units.", "Name": "Glass Bow", "Obtainment": ["Soul World Act 1-6"], "Rarity": "Mythic"}, "Glass Sword": {"Class": "Evo", "Description": "Used to evolve some units.", "Name": "Glass Sword", "Obtainment": ["Soul World Act 1-6"], "Rarity": "Mythic"}, "Glasses": {"Class": "Evo", "Description": "Used to evolve some units.", "Name": "Glasses", "Obtainment": ["Soul World Act 1-6"], "Rarity": "Mythic"}, "Gobanks Jacket": {"Class": "Misc", "Description": "Used to fuse Goden and The Juicebox.", "Name": "Gobanks Jacket", "Obtainment": ["Hell"], "Rarity": "Mythic"}, "Gogetable Jacket": {"Class": "Misc", "Description": "Used to fuse Goko (End) and Vegetable (Evil).", "Name": "Gogetable Jacket", "Obtainment": ["Hell"], "Rarity": "Mythic"}, "Goko Outfit": {"Class": "Evo", "Description": "Used to evolve Goko SSJ.", "Name": "Goko Outfit", "Obtainment": ["Lookout"], "Rarity": "Mythic"}, "Gokon": {"Class": "Evo", "Description": "Used to evolve some units.", "Name": "Gokon", "Obtainment": ["Soul World Act 1-6"], "Rarity": "Legendary"}, "Grocery Bag": {"Class": "Evo", "Description": "Used to evolve some units.", "Name": "Grocery Bag", "Obtainment": ["Strongest\u0027s City Act 1-6"], "Rarity": "Mythic"}, "Gun": {"Class": "Evo", "Description": "Used to evolve Nagumo and Shin.", "Name": "Gun", "Obtainment": ["Not currently dropped"], "Rarity": "Legendary"}, "Gun\u0027s Top": {"Class": "Evo", "Description": "Used to evolve some units.", "Name": "Gun\u0027s Top", "Obtainment": ["The Underground Tomb"], "Rarity": "Legendary"}, "Hair Gel": {"Class": "Evo", "Description": "Used to evolve some units.", "Name": "Hair Gel", "Obtainment": ["The Underground Tomb"], "Rarity": "Mythic"}, "Halloween Capsule": {"Class": "Capsule", "Description": "Unlock spooky units!", "Name": "Halloween Capsule", "Obtainment": ["Not currently dropped"], "Rarity": "Secret"}, "Hollow Leader Mask": {"Class": "Evo", "Description": "Used to evolve Ulquiorro.", "Name": "Hollow Leader Mask", "Obtainment": ["Hollow Desert"], "Rarity": "Epic"}, "Hollow Spear": {"Class": "Evo", "Description": "Used to evolve Ulquiorro.", "Name": "Hollow Spear", "Obtainment": ["Hollow Desert"], "Rarity": "Legendary"}, "Hollow Warrior Mask": {"Class": "Evo", "Description": "Used to evolve Ulquiorro.", "Name": "Hollow Warrior Mask", "Obtainment": ["Hollow Desert"], "Rarity": "Rare"}, "Holy Cross": {"Class": "Food", "Description": "Used to give exp to units.", "Name": "Holy Cross", "Obtainment": ["Not currently dropped"], "Rarity": "Mythic"}, "Juice": {"Class": "Evo", "Description": "Used to evolve Nagumo.", "Name": "Juice", "Obtainment": ["Candy Park"], "Rarity": "Mythic"}, "Kill\u0027s Shirt": {"Class": "Evo", "Description": "Used to evolve some units.", "Name": "Kill\u0027s Shirt", "Obtainment": ["The Underground Tomb"], "Rarity": "Legendary"}, "Kill\u0027s Shoe": {"Class": "Evo", "Description": "Used to evolve some units.", "Name": "Kill\u0027s Shoe", "Obtainment": ["The Underground Tomb"], "Rarity": "Legendary"}, "Kill\u0027s Shorts": {"Class": "Evo", "Description": "Used to evolve some units.", "Name": "Kill\u0027s Shorts", "Obtainment": ["The Underground Tomb"], "Rarity": "Legendary"}, "Kisu Hat": {"Class": "Evo", "Description": "Used to evolve some units.", "Name": "Kisu Hat", "Obtainment": ["Soul World Act 3"], "Rarity": "Legendary"}, "Knight Killer": {"Class": "Evo", "Description": "Used to evolve some units.", "Name": "Knight Killer", "Obtainment": ["Not currently dropped"], "Rarity": "Mythic"}, "Light Crown": {"Class": "Evo", "Description": "Used to evolve some units.", "Name": "Light Crown", "Obtainment": ["Ant Island"], "Rarity": "Mythic"}, "Light Pickaxe": {"Class": "Evo", "Description": "Used to evolve some units.", "Name": "Light Pickaxe", "Obtainment": ["Orc Dungeon"], "Rarity": "Mythic"}, "Light Sword": {"Class": "Evo", "Description": "Used to evolve some units.", "Name": "Light Sword", "Obtainment": ["Not currently dropped"], "Rarity": "Mythic"}, "Love Cake": {"Class": "Food", "Description": "Used to give exp to units.", "Name": "Love Cake", "Obtainment": ["Not currently dropped"], "Rarity": "Mythic"}, "LuHat": {"Class": "Evo", "Description": "Used to evolve Sakamoto.", "Name": "LuHat", "Obtainment": ["Not currently dropped"], "Rarity": "Legendary"}, "LuKey": {"Class": "Evo", "Description": "Used to evolve Sakamoto.", "Name": "LuKey", "Obtainment": ["Candy Park"], "Rarity": "Mythic"}, "LuStaff": {"Class": "Evo", "Description": "Used to evolve some Unit.", "Name": "LuStaff", "Obtainment": ["Candy Park"], "Rarity": "Mythic"}, "Lucky": {"Class": "Misc", "Description": "Gives 2x Luck for 1 hour in the summon banner.", "Name": "Lucky", "Obtainment": ["Fairy Town Rift", "Ghoul City Rift", "Green Planet Rift", "Hidden Village Rift", "Sharkman Island Rift"], "Rarity": "Legendary"}, "Mana Crystal": {"Class": "Evo", "Description": "Used to evolve some units.", "Name": "Mana Crystal", "Obtainment": ["Ant Island", "God Statue", "Orc Dungeon"], "Rarity": "Legendary"}, "Multiweapon": {"Class": "Evo", "Description": "Used to evolve Nagumo.", "Name": "Multiweapon", "Obtainment": ["Not currently dropped"], "Rarity": "Epic"}, "Nezu Bamboo": {"Class": "Evo", "Description": "Used to evolve some units.", "Name": "Nezu Bamboo", "Obtainment": ["Slayers District"], "Rarity": "Mythic"}, "Nezu Box": {"Class": "Evo", "Description": "Used to evolve some units.", "Name": "Nezu Box", "Obtainment": ["Slayers District"], "Rarity": "Mythic"}, "Nezu Outfit": {"Class": "Evo", "Description": "Used to evolve some units.", "Name": "Nezu Outfit", "Obtainment": ["Slayers District"], "Rarity": "Mythic"}, "Overit": {"Class": "Card", "Description": "Every 10 attacks, this unit gains +25% Damage for 15 seconds.", "Name": "Overit", "Obtainment": ["Not currently dropped"], "Rarity": "Epic"}, "Overme": {"Class": "Card", "Description": "Every 10 attacks, this unit gains +55% Damage for 15 seconds.", "Name": "Overme", "Obtainment": ["Not currently dropped"], "Rarity": "Mythic"}, "Overnow": {"Class": "Card", "Description": "Every 10 attacks, this unit gains +20% Damage for 15 seconds.", "Name": "Overnow", "Obtainment": ["Not currently dropped"], "Rarity": "Rare"}, "Oversized Shins": {"Class": "Evo", "Description": "Used to evolve some units.", "Name": "Oversized Shins", "Obtainment": ["Ant Island"], "Rarity": "Mythic"}, "Overyou": {"Class": "Card", "Description": "Every 10 attacks, this unit gains +35% Damage for 15 seconds.", "Name": "Overyou", "Obtainment": ["Not currently dropped"], "Rarity": "Legendary"}, "Pickle Cape": {"Class": "Misc", "Description": "Used to evolve Teen Gokan.", "Name": "Pickle Cape", "Obtainment": ["Lookout"], "Rarity": "Mythic"}, "Pink Kimono": {"Class": "Evo", "Description": "Used to evolve some units.", "Name": "Pink Kimono", "Obtainment": ["Hollow Desert"], "Rarity": "Mythic"}, "Power Core": {"Class": "Evo", "Description": "Used to evolve some units.", "Name": "Power Core", "Obtainment": ["Boru\u0027s Room"], "Rarity": "Mythic"}, "Purification Powder": {"Class": "Misc", "Description": "Used to remove curse of an unit.", "Name": "Purification Powder", "Obtainment": ["Not currently dropped"], "Rarity": "Mythic"}, "Quincy Cross": {"Class": "Evo", "Description": "Used to evolve some units.", "Name": "Quincy Cross", "Obtainment": ["Soul World Act 1-6"], "Rarity": "Mythic"}, "Radar": {"Class": "Evo", "Description": "Used to evolve Freeze.", "Name": "Radar", "Obtainment": ["Corp City Act 1-6", "Green Planet Act 1-6", "Green Planet Destroyed"], "Rarity": "Epic"}, "Raid Ticket": {"Class": "Misc", "Description": "Used to enter Raids.", "Name": "Raid Ticket", "Obtainment": ["Not currently dropped"], "Rarity": "Mythic"}, "Ramen": {"Class": "Food", "Description": "Used to give exp to units.", "Name": "Ramen", "Obtainment": ["Hidden Village Act 1-6"], "Rarity": "Legendary"}, "Reaper Badge": {"Class": "Evo", "Description": "Used to evolve some units.", "Name": "Reaper Badge", "Obtainment": ["Soul World Act 1-6"], "Rarity": "Legendary"}, "Red Knight\u0027s Helmet": {"Class": "Evo", "Description": "Used to evolve some units.", "Name": "Red Knight\u0027s Helmet", "Obtainment": ["Aura Room"], "Rarity": "Mythic"}, "Rerolls": {"Class": "Misc", "Description": "Used to reroll the trait of your units.", "Name": "Rerolls", "Obtainment": ["1", "2", "3", "4", "5", "6", "Ant Island", "Aura Room", "Boru\u0027s Room", "Candy Park", "Corp City Act 1-6", "Cursed Town Act 1-6", "Fairy Town Act 1-6", "Fairy Town Rift", "Ghoul City Act 1-6", "Ghoul City Rift", "God Statue", "Green Planet Act 1-6", "Green Planet Destroyed", "Green Planet Rift", "Hidden Village Act 1-6", "Hidden Village Rift", "Hollow Desert", "Lookout", "Orc Dungeon", "Red Palace", "Sharkman Island Rift", "Slayers District", "Sorcery Academy", "The Underground Tomb", "Valentine Castle"], "Rarity": "Mythic"}, "Ripped Bandages": {"Class": "Evo", "Description": "Used to evolve some units.", "Name": "Ripped Bandages", "Obtainment": ["Not currently dropped"], "Rarity": "Mythic"}, "Ruby": {"Class": "Evo", "Description": "A gem used for evolutions.", "Name": "Ruby", "Obtainment": ["Ant Island", "Corp City Act 1-6", "Fairy Town Act 1-6", "Ghoul City Act 1-6", "Ghoul City Rift", "God Statue", "Hidden Village Act 1-6", "Hollow Desert", "Midas", "Orc Dungeon", "Slayers District", "Sorcery Academy", "Strongest\u0027s City Act 1-6"], "Rarity": "Legendary"}, "Sandwich": {"Class": "Food", "Description": "Used to give exp to units.", "Name": "Sandwich", "Obtainment": ["Not currently dropped"], "Rarity": "Mythic"}, "Sapphire": {"Class": "Evo", "Description": "A gem used for evolutions.", "Name": "Sapphire", "Obtainment": ["1", "2", "3", "4", "5", "6", "Ant Island", "Fairy Town Rift", "Ghoul City Act 1-6", "God Statue", "Orc Dungeon", "Sharkman Island Rift", "Sorcery Academy", "The Underground Tomb"], "Rarity": "Legendary"}, "Scouter": {"Class": "Evo", "Description": "Used to evolve Freeze.", "Name": "Scouter", "Obtainment": ["Corp City Act 1-6", "Green Planet Act 1-6", "Green Planet Destroyed"], "Rarity": "Rare"}, "Sheathe": {"Class": "Evo", "Description": "Used to evolve some units.", "Name": "Sheathe", "Obtainment": ["Not currently dropped"], "Rarity": "Mythic"}, "Shintin": {"Class": "Evo", "Description": "Used to evolve some units.", "Name": "Shintin", "Obtainment": ["Soul World Act 1-6"], "Rarity": "Mythic"}, "Shiny Stone": {"Class": "Evo", "Description": "Can be used to turn an Unit into its Shiny version. (Doesn\u0027t work on Secret and above Units)", "Name": "Shiny Stone", "Obtainment": ["Not currently dropped"], "Rarity": "Secret"}, "Six Eyes": {"Class": "Evo", "Description": "Used to evolve Gotho.", "Name": "Six Eyes", "Obtainment": ["Sorcery Academy"], "Rarity": "Mythic"}, "Soul Candy": {"Class": "Evo", "Description": "Used to evolve some units.", "Name": "Soul Candy", "Obtainment": ["Hollow Desert", "Soul World Act 1-6"], "Rarity": "Epic"}, "Soul Cutter": {"Class": "Food", "Description": "Used to give exp to units.", "Name": "Soul Cutter", "Obtainment": ["Not currently dropped"], "Rarity": "Mythic"}, "Spring Capsule": {"Class": "Capsule", "Description": "Unlock festive units!", "Name": "Spring Capsule", "Obtainment": ["Not currently dropped"], "Rarity": "Secret"}, "Starheart": {"Class": "Card", "Description": "+10% Range", "Name": "Starheart", "Obtainment": ["Not currently dropped"], "Rarity": "Epic"}, "Starkindle": {"Class": "Card", "Description": "+15% Range", "Name": "Starkindle", "Obtainment": ["Not currently dropped"], "Rarity": "Legendary"}, "Starlight": {"Class": "Card", "Description": "+4% Range", "Name": "Starlight", "Obtainment": ["Not currently dropped"], "Rarity": "Rare"}, "Starpath": {"Class": "Card", "Description": "+25% Range", "Name": "Starpath", "Obtainment": ["Not currently dropped"], "Rarity": "Mythic"}, "Stat Crystal": {"Class": "Stat", "Description": "Used to reroll all stats of your unit.", "Name": "Stat Crystal", "Obtainment": ["Sorcery Academy"], "Rarity": "Mythic"}, "Stat Shard": {"Class": "Stat", "Description": "Used to reroll a stat of your unit.", "Name": "Stat Shard", "Obtainment": ["Sorcery Academy"], "Rarity": "Mythic"}, "Straw Hat": {"Class": "Evo", "Description": "Used to evolve some units.", "Name": "Straw Hat", "Obtainment": ["Soul World Act 2"], "Rarity": "Legendary"}, "Strawberry Cake": {"Class": "Food", "Description": "Used to give exp to units.", "Name": "Strawberry Cake", "Obtainment": ["Fairy Town Act 1-6"], "Rarity": "Legendary"}, "Super Lucky": {"Class": "Misc", "Description": "Gives 3x Luck for 1 hour in the summon banner.", "Name": "Super Lucky", "Obtainment": ["Fairy Town Rift", "Ghoul City Rift", "Hidden Village Rift", "Sharkman Island Rift"], "Rarity": "Mythic"}, "Taser": {"Class": "Evo", "Description": "Used to evolve Sakamoto.", "Name": "Taser", "Obtainment": ["Candy Park"], "Rarity": "Legendary"}, "Teleportation Stone": {"Class": "Evo", "Description": "Used to evolve some units.", "Name": "Teleportation Stone", "Obtainment": ["Orc Dungeon"], "Rarity": "Legendary"}, "TestCard": {"Class": "Card", "Description": "+5% Damage, +3% Range", "Name": "TestCard", "Obtainment": ["Not currently dropped"], "Rarity": "Rare"}, "Thukuna Outfit": {"Class": "Evo", "Description": "Used to evolve Thukuna.", "Name": "Thukuna Outfit", "Obtainment": ["Sorcery Academy"], "Rarity": "Mythic"}, "Thunder Haori": {"Class": "Evo", "Description": "Used to evolve some units.", "Name": "Thunder Haori", "Obtainment": ["Slayers District"], "Rarity": "Mythic"}, "Thunder Katana": {"Class": "Evo", "Description": "Used to evolve some units.", "Name": "Thunder Katana", "Obtainment": ["Slayers District"], "Rarity": "Mythic"}, "Topaz": {"Class": "Evo", "Description": "A gem used for evolutions.", "Name": "Topaz", "Obtainment": ["1", "2", "3", "4", "5", "6", "Ant Island", "Cursed Town Act 1-6", "God Statue", "Green Planet Act 1-6", "Green Planet Destroyed", "Green Planet Rift", "Hidden Village Act 1-6", "Hidden Village Rift", "Lookout", "Midas", "Orc Dungeon", "Strongest\u0027s City Act 1-6"], "Rarity": "Legendary"}, "Toy Windmill": {"Class": "Evo", "Description": "Used to evolve some units.", "Name": "Toy Windmill", "Obtainment": ["Soul World Act 3"], "Rarity": "Legendary"}, "Transformation Paper": {"Class": "Evo", "Description": "Used to evolve some units.", "Name": "Transformation Paper", "Obtainment": ["Hollow Desert"], "Rarity": "Mythic"}, "Video Game": {"Class": "Evo", "Description": "Used to evolve some units.", "Name": "Video Game", "Obtainment": ["Strongest\u0027s City Act 1-6"], "Rarity": "Mythic"}, "Virtual Food": {"Class": "Evo", "Description": "Used to evolve some units.", "Name": "Virtual Food", "Obtainment": ["Red Palace"], "Rarity": "Epic"}, "Wind Spirit Crown": {"Class": "Evo", "Description": "You can hear wispers from it... Sylph.", "Name": "Wind Spirit Crown", "Obtainment": ["Not currently dropped"], "Rarity": "Mythic"}, "Wish Ball": {"Class": "Evo", "Description": "Used to evolve some units.", "Name": "Wish Ball", "Obtainment": ["Green Planet Destroyed"], "Rarity": "Legendary"}, "Yoyo": {"Class": "Evo", "Description": "Used to evolve some units.", "Name": "Yoyo", "Obtainment": ["The Underground Tomb"], "Rarity": "Mythic"}};
  </script>

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
        data-id="Aura Sword"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-secret">
            <img
              src="http://placehold.co/120x120"
              alt="Aura Sword"
            />
          </div>
          <span class="data-name">Aura Sword</span>
        </div>
      </div>
      
      <div
        class="data-item Secret Evo"
        data-name="aura sword [purple]"
        data-id="Aura Sword [Purple]"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-secret">
            <img
              src="http://placehold.co/120x120"
              alt="Aura Sword [Purple]"
            />
          </div>
          <span class="data-name">Aura Sword [Purple]</span>
        </div>
      </div>
      
      <div
        class="data-item Secret Evo"
        data-name="bankai sword"
        data-id="Bankai Sword"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-secret">
            <img
              src="http://placehold.co/120x120"
              alt="Bankai Sword"
            />
          </div>
          <span class="data-name">Bankai Sword</span>
        </div>
      </div>
      
      <div
        class="data-item Secret Capsule"
        data-name="christmas capsule"
        data-id="Christmas Capsule"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-secret">
            <img
              src="http://placehold.co/120x120"
              alt="Christmas Capsule"
            />
          </div>
          <span class="data-name">Christmas Capsule</span>
        </div>
      </div>
      
      <div
        class="data-item Secret Evo"
        data-name="deer"
        data-id="Deer"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-secret">
            <img
              src="http://placehold.co/120x120"
              alt="Deer"
            />
          </div>
          <span class="data-name">Deer</span>
        </div>
      </div>
      
      <div
        class="data-item Secret Evo"
        data-name="gen z core"
        data-id="Gen Z Core"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-secret">
            <img
              src="http://placehold.co/120x120"
              alt="Gen Z Core"
            />
          </div>
          <span class="data-name">Gen Z Core</span>
        </div>
      </div>
      
      <div
        class="data-item Secret Capsule"
        data-name="halloween capsule"
        data-id="Halloween Capsule"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-secret">
            <img
              src="http://placehold.co/120x120"
              alt="Halloween Capsule"
            />
          </div>
          <span class="data-name">Halloween Capsule</span>
        </div>
      </div>
      
      <div
        class="data-item Secret Evo"
        data-name="shiny stone"
        data-id="Shiny Stone"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-secret">
            <img
              src="http://placehold.co/120x120"
              alt="Shiny Stone"
            />
          </div>
          <span class="data-name">Shiny Stone</span>
        </div>
      </div>
      
      <div
        class="data-item Secret Capsule"
        data-name="spring capsule"
        data-id="Spring Capsule"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-secret">
            <img
              src="http://placehold.co/120x120"
              alt="Spring Capsule"
            />
          </div>
          <span class="data-name">Spring Capsule</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Evo"
        data-name="beast belt"
        data-id="Beast Belt"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Beast Belt"
            />
          </div>
          <span class="data-name">Beast Belt</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Evo"
        data-name="beast claws"
        data-id="Beast Claws"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Beast Claws"
            />
          </div>
          <span class="data-name">Beast Claws</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Evo"
        data-name="boru torso"
        data-id="Boru Torso"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Boru Torso"
            />
          </div>
          <span class="data-name">Boru Torso</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Food"
        data-name="candy"
        data-id="Candy"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Candy"
            />
          </div>
          <span class="data-name">Candy</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Food"
        data-name="candy cane"
        data-id="Candy Cane"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Candy Cane"
            />
          </div>
          <span class="data-name">Candy Cane</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Evo"
        data-name="cape"
        data-id="Cape"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Cape"
            />
          </div>
          <span class="data-name">Cape</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Evo"
        data-name="cracked power core"
        data-id="Cracked Power Core"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Cracked Power Core"
            />
          </div>
          <span class="data-name">Cracked Power Core</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Misc"
        data-name="crystal ball 1"
        data-id="Crystal Ball 1"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Crystal Ball 1"
            />
          </div>
          <span class="data-name">Crystal Ball 1</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Misc"
        data-name="crystal ball 2"
        data-id="Crystal Ball 2"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Crystal Ball 2"
            />
          </div>
          <span class="data-name">Crystal Ball 2</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Misc"
        data-name="crystal ball 3"
        data-id="Crystal Ball 3"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Crystal Ball 3"
            />
          </div>
          <span class="data-name">Crystal Ball 3</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Misc"
        data-name="crystal ball 4"
        data-id="Crystal Ball 4"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Crystal Ball 4"
            />
          </div>
          <span class="data-name">Crystal Ball 4</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Misc"
        data-name="crystal ball 5"
        data-id="Crystal Ball 5"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Crystal Ball 5"
            />
          </div>
          <span class="data-name">Crystal Ball 5</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Misc"
        data-name="crystal ball 6"
        data-id="Crystal Ball 6"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Crystal Ball 6"
            />
          </div>
          <span class="data-name">Crystal Ball 6</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Misc"
        data-name="crystal ball 7"
        data-id="Crystal Ball 7"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Crystal Ball 7"
            />
          </div>
          <span class="data-name">Crystal Ball 7</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Food"
        data-name="cupcake"
        data-id="Cupcake"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Cupcake"
            />
          </div>
          <span class="data-name">Cupcake</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Stats"
        data-name="cursed finger"
        data-id="Cursed Finger"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Cursed Finger"
            />
          </div>
          <span class="data-name">Cursed Finger</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Misc"
        data-name="dark elixir"
        data-id="Dark Elixir"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Dark Elixir"
            />
          </div>
          <span class="data-name">Dark Elixir</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Card"
        data-name="deaftone"
        data-id="Deaftone"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Deaftone"
            />
          </div>
          <span class="data-name">Deaftone</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Evo"
        data-name="dice"
        data-id="Dice"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Dice"
            />
          </div>
          <span class="data-name">Dice</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Misc"
        data-name="divine earing"
        data-id="Divine Earing"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Divine Earing"
            />
          </div>
          <span class="data-name">Divine Earing</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Card"
        data-name="ecoro"
        data-id="Ecoro"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Ecoro"
            />
          </div>
          <span class="data-name">Ecoro</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Misc"
        data-name="elixir of life"
        data-id="Elixir Of Life"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Elixir Of Life"
            />
          </div>
          <span class="data-name">Elixir Of Life</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Card"
        data-name="ember"
        data-id="Ember"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Ember"
            />
          </div>
          <span class="data-name">Ember</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Evo"
        data-name="evil orb"
        data-id="Evil Orb"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Evil Orb"
            />
          </div>
          <span class="data-name">Evil Orb</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Evo"
        data-name="fire haori"
        data-id="Fire Haori"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Fire Haori"
            />
          </div>
          <span class="data-name">Fire Haori</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Evo"
        data-name="fire katana"
        data-id="Fire Katana"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Fire Katana"
            />
          </div>
          <span class="data-name">Fire Katana</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Evo"
        data-name="four leaf grimoire"
        data-id="Four Leaf Grimoire"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Four Leaf Grimoire"
            />
          </div>
          <span class="data-name">Four Leaf Grimoire</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Evo"
        data-name="getho outfit"
        data-id="Getho Outfit"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Getho Outfit"
            />
          </div>
          <span class="data-name">Getho Outfit</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Evo"
        data-name="glass bow"
        data-id="Glass Bow"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Glass Bow"
            />
          </div>
          <span class="data-name">Glass Bow</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Evo"
        data-name="glass sword"
        data-id="Glass Sword"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Glass Sword"
            />
          </div>
          <span class="data-name">Glass Sword</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Evo"
        data-name="glasses"
        data-id="Glasses"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Glasses"
            />
          </div>
          <span class="data-name">Glasses</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Misc"
        data-name="gobanks jacket"
        data-id="Gobanks Jacket"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Gobanks Jacket"
            />
          </div>
          <span class="data-name">Gobanks Jacket</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Misc"
        data-name="gogetable jacket"
        data-id="Gogetable Jacket"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Gogetable Jacket"
            />
          </div>
          <span class="data-name">Gogetable Jacket</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Evo"
        data-name="goko outfit"
        data-id="Goko Outfit"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Goko Outfit"
            />
          </div>
          <span class="data-name">Goko Outfit</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Evo"
        data-name="grocery bag"
        data-id="Grocery Bag"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Grocery Bag"
            />
          </div>
          <span class="data-name">Grocery Bag</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Evo"
        data-name="hair gel"
        data-id="Hair Gel"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Hair Gel"
            />
          </div>
          <span class="data-name">Hair Gel</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Food"
        data-name="holy cross"
        data-id="Holy Cross"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Holy Cross"
            />
          </div>
          <span class="data-name">Holy Cross</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Evo"
        data-name="juice"
        data-id="Juice"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Juice"
            />
          </div>
          <span class="data-name">Juice</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Evo"
        data-name="knight killer"
        data-id="Knight Killer"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Knight Killer"
            />
          </div>
          <span class="data-name">Knight Killer</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Evo"
        data-name="light crown"
        data-id="Light Crown"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Light Crown"
            />
          </div>
          <span class="data-name">Light Crown</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Evo"
        data-name="light pickaxe"
        data-id="Light Pickaxe"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Light Pickaxe"
            />
          </div>
          <span class="data-name">Light Pickaxe</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Evo"
        data-name="light sword"
        data-id="Light Sword"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Light Sword"
            />
          </div>
          <span class="data-name">Light Sword</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Food"
        data-name="love cake"
        data-id="Love Cake"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Love Cake"
            />
          </div>
          <span class="data-name">Love Cake</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Evo"
        data-name="lukey"
        data-id="LuKey"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="LuKey"
            />
          </div>
          <span class="data-name">LuKey</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Evo"
        data-name="lustaff"
        data-id="LuStaff"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="LuStaff"
            />
          </div>
          <span class="data-name">LuStaff</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Evo"
        data-name="nezu bamboo"
        data-id="Nezu Bamboo"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Nezu Bamboo"
            />
          </div>
          <span class="data-name">Nezu Bamboo</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Evo"
        data-name="nezu box"
        data-id="Nezu Box"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Nezu Box"
            />
          </div>
          <span class="data-name">Nezu Box</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Evo"
        data-name="nezu outfit"
        data-id="Nezu Outfit"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Nezu Outfit"
            />
          </div>
          <span class="data-name">Nezu Outfit</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Card"
        data-name="overme"
        data-id="Overme"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Overme"
            />
          </div>
          <span class="data-name">Overme</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Evo"
        data-name="oversized shins"
        data-id="Oversized Shins"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Oversized Shins"
            />
          </div>
          <span class="data-name">Oversized Shins</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Misc"
        data-name="pickle cape"
        data-id="Pickle Cape"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Pickle Cape"
            />
          </div>
          <span class="data-name">Pickle Cape</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Evo"
        data-name="pink kimono"
        data-id="Pink Kimono"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Pink Kimono"
            />
          </div>
          <span class="data-name">Pink Kimono</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Evo"
        data-name="power core"
        data-id="Power Core"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Power Core"
            />
          </div>
          <span class="data-name">Power Core</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Misc"
        data-name="purification powder"
        data-id="Purification Powder"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Purification Powder"
            />
          </div>
          <span class="data-name">Purification Powder</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Evo"
        data-name="quincy cross"
        data-id="Quincy Cross"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Quincy Cross"
            />
          </div>
          <span class="data-name">Quincy Cross</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Misc"
        data-name="raid ticket"
        data-id="Raid Ticket"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Raid Ticket"
            />
          </div>
          <span class="data-name">Raid Ticket</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Evo"
        data-name="red knight's helmet"
        data-id="Red Knight's Helmet"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Red Knight's Helmet"
            />
          </div>
          <span class="data-name">Red Knight's Helmet</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Misc"
        data-name="rerolls"
        data-id="Rerolls"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Rerolls"
            />
          </div>
          <span class="data-name">Rerolls</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Evo"
        data-name="ripped bandages"
        data-id="Ripped Bandages"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Ripped Bandages"
            />
          </div>
          <span class="data-name">Ripped Bandages</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Food"
        data-name="sandwich"
        data-id="Sandwich"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Sandwich"
            />
          </div>
          <span class="data-name">Sandwich</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Evo"
        data-name="sheathe"
        data-id="Sheathe"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Sheathe"
            />
          </div>
          <span class="data-name">Sheathe</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Evo"
        data-name="shintin"
        data-id="Shintin"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Shintin"
            />
          </div>
          <span class="data-name">Shintin</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Evo"
        data-name="six eyes"
        data-id="Six Eyes"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Six Eyes"
            />
          </div>
          <span class="data-name">Six Eyes</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Food"
        data-name="soul cutter"
        data-id="Soul Cutter"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Soul Cutter"
            />
          </div>
          <span class="data-name">Soul Cutter</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Card"
        data-name="starpath"
        data-id="Starpath"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Starpath"
            />
          </div>
          <span class="data-name">Starpath</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Stat"
        data-name="stat crystal"
        data-id="Stat Crystal"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Stat Crystal"
            />
          </div>
          <span class="data-name">Stat Crystal</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Stat"
        data-name="stat shard"
        data-id="Stat Shard"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Stat Shard"
            />
          </div>
          <span class="data-name">Stat Shard</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Misc"
        data-name="super lucky"
        data-id="Super Lucky"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Super Lucky"
            />
          </div>
          <span class="data-name">Super Lucky</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Evo"
        data-name="thukuna outfit"
        data-id="Thukuna Outfit"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Thukuna Outfit"
            />
          </div>
          <span class="data-name">Thukuna Outfit</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Evo"
        data-name="thunder haori"
        data-id="Thunder Haori"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Thunder Haori"
            />
          </div>
          <span class="data-name">Thunder Haori</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Evo"
        data-name="thunder katana"
        data-id="Thunder Katana"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Thunder Katana"
            />
          </div>
          <span class="data-name">Thunder Katana</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Evo"
        data-name="transformation paper"
        data-id="Transformation Paper"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Transformation Paper"
            />
          </div>
          <span class="data-name">Transformation Paper</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Evo"
        data-name="video game"
        data-id="Video Game"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Video Game"
            />
          </div>
          <span class="data-name">Video Game</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Evo"
        data-name="wind spirit crown"
        data-id="Wind Spirit Crown"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Wind Spirit Crown"
            />
          </div>
          <span class="data-name">Wind Spirit Crown</span>
        </div>
      </div>
      
      <div
        class="data-item Mythic Evo"
        data-name="yoyo"
        data-id="Yoyo"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-mythic">
            <img
              src="http://placehold.co/120x120"
              alt="Yoyo"
            />
          </div>
          <span class="data-name">Yoyo</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Evo"
        data-name="assassin's double daggers"
        data-id="Assassin's Double Daggers"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-legendary">
            <img
              src="http://placehold.co/120x120"
              alt="Assassin's Double Daggers"
            />
          </div>
          <span class="data-name">Assassin's Double Daggers</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Evo"
        data-name="baruka's dagger"
        data-id="Baruka's Dagger"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-legendary">
            <img
              src="http://placehold.co/120x120"
              alt="Baruka's Dagger"
            />
          </div>
          <span class="data-name">Baruka's Dagger</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Evo"
        data-name="black sword"
        data-id="Black Sword"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-legendary">
            <img
              src="http://placehold.co/120x120"
              alt="Black Sword"
            />
          </div>
          <span class="data-name">Black Sword</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Evo"
        data-name="blindfold"
        data-id="Blindfold"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-legendary">
            <img
              src="http://placehold.co/120x120"
              alt="Blindfold"
            />
          </div>
          <span class="data-name">Blindfold</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Evo"
        data-name="cloud cloak"
        data-id="Cloud Cloak"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-legendary">
            <img
              src="http://placehold.co/120x120"
              alt="Cloud Cloak"
            />
          </div>
          <span class="data-name">Cloud Cloak</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Evo"
        data-name="cursed energy"
        data-id="Cursed Energy"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-legendary">
            <img
              src="http://placehold.co/120x120"
              alt="Cursed Energy"
            />
          </div>
          <span class="data-name">Cursed Energy</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Evo"
        data-name="cursed orb"
        data-id="Cursed Orb"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-legendary">
            <img
              src="http://placehold.co/120x120"
              alt="Cursed Orb"
            />
          </div>
          <span class="data-name">Cursed Orb</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Evo"
        data-name="cyan sword"
        data-id="Cyan Sword"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-legendary">
            <img
              src="http://placehold.co/120x120"
              alt="Cyan Sword"
            />
          </div>
          <span class="data-name">Cyan Sword</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Card"
        data-name="deafbone"
        data-id="Deafbone"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-legendary">
            <img
              src="http://placehold.co/120x120"
              alt="Deafbone"
            />
          </div>
          <span class="data-name">Deafbone</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Evo"
        data-name="demon horn"
        data-id="Demon Horn"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-legendary">
            <img
              src="http://placehold.co/120x120"
              alt="Demon Horn"
            />
          </div>
          <span class="data-name">Demon Horn</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Evo"
        data-name="demon king sword"
        data-id="Demon King Sword"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-legendary">
            <img
              src="http://placehold.co/120x120"
              alt="Demon King Sword"
            />
          </div>
          <span class="data-name">Demon King Sword</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Evo"
        data-name="demon monarch's necklace"
        data-id="Demon Monarch's Necklace"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-legendary">
            <img
              src="http://placehold.co/120x120"
              alt="Demon Monarch's Necklace"
            />
          </div>
          <span class="data-name">Demon Monarch's Necklace</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Evo"
        data-name="divine stone"
        data-id="Divine Stone"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-legendary">
            <img
              src="http://placehold.co/120x120"
              alt="Divine Stone"
            />
          </div>
          <span class="data-name">Divine Stone</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Evo"
        data-name="dominator's rune (purple)"
        data-id="Dominator's Rune (Purple)"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-legendary">
            <img
              src="http://placehold.co/120x120"
              alt="Dominator's Rune (Purple)"
            />
          </div>
          <span class="data-name">Dominator's Rune (Purple)</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Evo"
        data-name="dominator's rune (red)"
        data-id="Dominator's Rune (Red)"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-legendary">
            <img
              src="http://placehold.co/120x120"
              alt="Dominator's Rune (Red)"
            />
          </div>
          <span class="data-name">Dominator's Rune (Red)</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Evo"
        data-name="dummy hair"
        data-id="Dummy Hair"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-legendary">
            <img
              src="http://placehold.co/120x120"
              alt="Dummy Hair"
            />
          </div>
          <span class="data-name">Dummy Hair</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Evo"
        data-name="dummy hat"
        data-id="Dummy Hat"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-legendary">
            <img
              src="http://placehold.co/120x120"
              alt="Dummy Hat"
            />
          </div>
          <span class="data-name">Dummy Hat</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Card"
        data-name="ecolo"
        data-id="Ecolo"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-legendary">
            <img
              src="http://placehold.co/120x120"
              alt="Ecolo"
            />
          </div>
          <span class="data-name">Ecolo</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Card"
        data-name="emtan"
        data-id="Emtan"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-legendary">
            <img
              src="http://placehold.co/120x120"
              alt="Emtan"
            />
          </div>
          <span class="data-name">Emtan</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Evo"
        data-name="exchange ring"
        data-id="Exchange Ring"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-legendary">
            <img
              src="http://placehold.co/120x120"
              alt="Exchange Ring"
            />
          </div>
          <span class="data-name">Exchange Ring</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Evo"
        data-name="eye patch"
        data-id="Eye Patch"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-legendary">
            <img
              src="http://placehold.co/120x120"
              alt="Eye Patch"
            />
          </div>
          <span class="data-name">Eye Patch</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Evo"
        data-name="fairy sword"
        data-id="Fairy Sword"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-legendary">
            <img
              src="http://placehold.co/120x120"
              alt="Fairy Sword"
            />
          </div>
          <span class="data-name">Fairy Sword</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Evo"
        data-name="fairy wings"
        data-id="Fairy Wings"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-legendary">
            <img
              src="http://placehold.co/120x120"
              alt="Fairy Wings"
            />
          </div>
          <span class="data-name">Fairy Wings</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Food"
        data-name="flask"
        data-id="Flask"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-legendary">
            <img
              src="http://placehold.co/120x120"
              alt="Flask"
            />
          </div>
          <span class="data-name">Flask</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Evo"
        data-name="flip book"
        data-id="Flip Book"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-legendary">
            <img
              src="http://placehold.co/120x120"
              alt="Flip Book"
            />
          </div>
          <span class="data-name">Flip Book</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Evo"
        data-name="game shield"
        data-id="Game Shield"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-legendary">
            <img
              src="http://placehold.co/120x120"
              alt="Game Shield"
            />
          </div>
          <span class="data-name">Game Shield</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Evo"
        data-name="game sword"
        data-id="Game Sword"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-legendary">
            <img
              src="http://placehold.co/120x120"
              alt="Game Sword"
            />
          </div>
          <span class="data-name">Game Sword</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Evo"
        data-name="gokon"
        data-id="Gokon"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-legendary">
            <img
              src="http://placehold.co/120x120"
              alt="Gokon"
            />
          </div>
          <span class="data-name">Gokon</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Evo"
        data-name="gun"
        data-id="Gun"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-legendary">
            <img
              src="http://placehold.co/120x120"
              alt="Gun"
            />
          </div>
          <span class="data-name">Gun</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Evo"
        data-name="gun's top"
        data-id="Gun's Top"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-legendary">
            <img
              src="http://placehold.co/120x120"
              alt="Gun's Top"
            />
          </div>
          <span class="data-name">Gun's Top</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Evo"
        data-name="hollow spear"
        data-id="Hollow Spear"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-legendary">
            <img
              src="http://placehold.co/120x120"
              alt="Hollow Spear"
            />
          </div>
          <span class="data-name">Hollow Spear</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Evo"
        data-name="kill's shirt"
        data-id="Kill's Shirt"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-legendary">
            <img
              src="http://placehold.co/120x120"
              alt="Kill's Shirt"
            />
          </div>
          <span class="data-name">Kill's Shirt</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Evo"
        data-name="kill's shoe"
        data-id="Kill's Shoe"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-legendary">
            <img
              src="http://placehold.co/120x120"
              alt="Kill's Shoe"
            />
          </div>
          <span class="data-name">Kill's Shoe</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Evo"
        data-name="kill's shorts"
        data-id="Kill's Shorts"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-legendary">
            <img
              src="http://placehold.co/120x120"
              alt="Kill's Shorts"
            />
          </div>
          <span class="data-name">Kill's Shorts</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Evo"
        data-name="kisu hat"
        data-id="Kisu Hat"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-legendary">
            <img
              src="http://placehold.co/120x120"
              alt="Kisu Hat"
            />
          </div>
          <span class="data-name">Kisu Hat</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Evo"
        data-name="luhat"
        data-id="LuHat"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-legendary">
            <img
              src="http://placehold.co/120x120"
              alt="LuHat"
            />
          </div>
          <span class="data-name">LuHat</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Misc"
        data-name="lucky"
        data-id="Lucky"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-legendary">
            <img
              src="http://placehold.co/120x120"
              alt="Lucky"
            />
          </div>
          <span class="data-name">Lucky</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Evo"
        data-name="mana crystal"
        data-id="Mana Crystal"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-legendary">
            <img
              src="http://placehold.co/120x120"
              alt="Mana Crystal"
            />
          </div>
          <span class="data-name">Mana Crystal</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Card"
        data-name="overyou"
        data-id="Overyou"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-legendary">
            <img
              src="http://placehold.co/120x120"
              alt="Overyou"
            />
          </div>
          <span class="data-name">Overyou</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Food"
        data-name="ramen"
        data-id="Ramen"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-legendary">
            <img
              src="http://placehold.co/120x120"
              alt="Ramen"
            />
          </div>
          <span class="data-name">Ramen</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Evo"
        data-name="reaper badge"
        data-id="Reaper Badge"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-legendary">
            <img
              src="http://placehold.co/120x120"
              alt="Reaper Badge"
            />
          </div>
          <span class="data-name">Reaper Badge</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Evo"
        data-name="ruby"
        data-id="Ruby"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-legendary">
            <img
              src="http://placehold.co/120x120"
              alt="Ruby"
            />
          </div>
          <span class="data-name">Ruby</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Evo"
        data-name="sapphire"
        data-id="Sapphire"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-legendary">
            <img
              src="http://placehold.co/120x120"
              alt="Sapphire"
            />
          </div>
          <span class="data-name">Sapphire</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Card"
        data-name="starkindle"
        data-id="Starkindle"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-legendary">
            <img
              src="http://placehold.co/120x120"
              alt="Starkindle"
            />
          </div>
          <span class="data-name">Starkindle</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Evo"
        data-name="straw hat"
        data-id="Straw Hat"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-legendary">
            <img
              src="http://placehold.co/120x120"
              alt="Straw Hat"
            />
          </div>
          <span class="data-name">Straw Hat</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Food"
        data-name="strawberry cake"
        data-id="Strawberry Cake"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-legendary">
            <img
              src="http://placehold.co/120x120"
              alt="Strawberry Cake"
            />
          </div>
          <span class="data-name">Strawberry Cake</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Evo"
        data-name="taser"
        data-id="Taser"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-legendary">
            <img
              src="http://placehold.co/120x120"
              alt="Taser"
            />
          </div>
          <span class="data-name">Taser</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Evo"
        data-name="teleportation stone"
        data-id="Teleportation Stone"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-legendary">
            <img
              src="http://placehold.co/120x120"
              alt="Teleportation Stone"
            />
          </div>
          <span class="data-name">Teleportation Stone</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Evo"
        data-name="topaz"
        data-id="Topaz"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-legendary">
            <img
              src="http://placehold.co/120x120"
              alt="Topaz"
            />
          </div>
          <span class="data-name">Topaz</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Evo"
        data-name="toy windmill"
        data-id="Toy Windmill"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-legendary">
            <img
              src="http://placehold.co/120x120"
              alt="Toy Windmill"
            />
          </div>
          <span class="data-name">Toy Windmill</span>
        </div>
      </div>
      
      <div
        class="data-item Legendary Evo"
        data-name="wish ball"
        data-id="Wish Ball"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-legendary">
            <img
              src="http://placehold.co/120x120"
              alt="Wish Ball"
            />
          </div>
          <span class="data-name">Wish Ball</span>
        </div>
      </div>
      
      <div
        class="data-item Epic Food"
        data-name="burger"
        data-id="Burger"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-epic">
            <img
              src="http://placehold.co/120x120"
              alt="Burger"
            />
          </div>
          <span class="data-name">Burger</span>
        </div>
      </div>
      
      <div
        class="data-item Epic Food"
        data-name="cupnoodle"
        data-id="CupNoodle"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-epic">
            <img
              src="http://placehold.co/120x120"
              alt="CupNoodle"
            />
          </div>
          <span class="data-name">CupNoodle</span>
        </div>
      </div>
      
      <div
        class="data-item Epic Evo"
        data-name="cursed head band"
        data-id="Cursed Head Band"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-epic">
            <img
              src="http://placehold.co/120x120"
              alt="Cursed Head Band"
            />
          </div>
          <span class="data-name">Cursed Head Band</span>
        </div>
      </div>
      
      <div
        class="data-item Epic Card"
        data-name="deaffone"
        data-id="Deaffone"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-epic">
            <img
              src="http://placehold.co/120x120"
              alt="Deaffone"
            />
          </div>
          <span class="data-name">Deaffone</span>
        </div>
      </div>
      
      <div
        class="data-item Epic Card"
        data-name="ecolist"
        data-id="Ecolist"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-epic">
            <img
              src="http://placehold.co/120x120"
              alt="Ecolist"
            />
          </div>
          <span class="data-name">Ecolist</span>
        </div>
      </div>
      
      <div
        class="data-item Epic Card"
        data-name="embrew"
        data-id="Embrew"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-epic">
            <img
              src="http://placehold.co/120x120"
              alt="Embrew"
            />
          </div>
          <span class="data-name">Embrew</span>
        </div>
      </div>
      
      <div
        class="data-item Epic Food"
        data-name="fish"
        data-id="Fish"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-epic">
            <img
              src="http://placehold.co/120x120"
              alt="Fish"
            />
          </div>
          <span class="data-name">Fish</span>
        </div>
      </div>
      
      <div
        class="data-item Epic Evo"
        data-name="hollow leader mask"
        data-id="Hollow Leader Mask"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-epic">
            <img
              src="http://placehold.co/120x120"
              alt="Hollow Leader Mask"
            />
          </div>
          <span class="data-name">Hollow Leader Mask</span>
        </div>
      </div>
      
      <div
        class="data-item Epic Evo"
        data-name="multiweapon"
        data-id="Multiweapon"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-epic">
            <img
              src="http://placehold.co/120x120"
              alt="Multiweapon"
            />
          </div>
          <span class="data-name">Multiweapon</span>
        </div>
      </div>
      
      <div
        class="data-item Epic Card"
        data-name="overit"
        data-id="Overit"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-epic">
            <img
              src="http://placehold.co/120x120"
              alt="Overit"
            />
          </div>
          <span class="data-name">Overit</span>
        </div>
      </div>
      
      <div
        class="data-item Epic Evo"
        data-name="radar"
        data-id="Radar"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-epic">
            <img
              src="http://placehold.co/120x120"
              alt="Radar"
            />
          </div>
          <span class="data-name">Radar</span>
        </div>
      </div>
      
      <div
        class="data-item Epic Evo"
        data-name="soul candy"
        data-id="Soul Candy"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-epic">
            <img
              src="http://placehold.co/120x120"
              alt="Soul Candy"
            />
          </div>
          <span class="data-name">Soul Candy</span>
        </div>
      </div>
      
      <div
        class="data-item Epic Card"
        data-name="starheart"
        data-id="Starheart"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-epic">
            <img
              src="http://placehold.co/120x120"
              alt="Starheart"
            />
          </div>
          <span class="data-name">Starheart</span>
        </div>
      </div>
      
      <div
        class="data-item Epic Evo"
        data-name="virtual food"
        data-id="Virtual Food"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-epic">
            <img
              src="http://placehold.co/120x120"
              alt="Virtual Food"
            />
          </div>
          <span class="data-name">Virtual Food</span>
        </div>
      </div>
      
      <div
        class="data-item Rare Food"
        data-name="apple"
        data-id="Apple"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-rare">
            <img
              src="http://placehold.co/120x120"
              alt="Apple"
            />
          </div>
          <span class="data-name">Apple</span>
        </div>
      </div>
      
      <div
        class="data-item Rare Evo"
        data-name="apron"
        data-id="Apron"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-rare">
            <img
              src="http://placehold.co/120x120"
              alt="Apron"
            />
          </div>
          <span class="data-name">Apron</span>
        </div>
      </div>
      
      <div
        class="data-item Rare Food"
        data-name="bean"
        data-id="Bean"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-rare">
            <img
              src="http://placehold.co/120x120"
              alt="Bean"
            />
          </div>
          <span class="data-name">Bean</span>
        </div>
      </div>
      
      <div
        class="data-item Rare Card"
        data-name="deafone"
        data-id="Deafone"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-rare">
            <img
              src="http://placehold.co/120x120"
              alt="Deafone"
            />
          </div>
          <span class="data-name">Deafone</span>
        </div>
      </div>
      
      <div
        class="data-item Rare Evo"
        data-name="demon monarch earings"
        data-id="Demon Monarch Earings"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-rare">
            <img
              src="http://placehold.co/120x120"
              alt="Demon Monarch Earings"
            />
          </div>
          <span class="data-name">Demon Monarch Earings</span>
        </div>
      </div>
      
      <div
        class="data-item Rare Card"
        data-name="drawnup"
        data-id="Drawnup"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-rare">
            <img
              src="http://placehold.co/120x120"
              alt="Drawnup"
            />
          </div>
          <span class="data-name">Drawnup</span>
        </div>
      </div>
      
      <div
        class="data-item Rare Card"
        data-name="ecoist"
        data-id="Ecoist"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-rare">
            <img
              src="http://placehold.co/120x120"
              alt="Ecoist"
            />
          </div>
          <span class="data-name">Ecoist</span>
        </div>
      </div>
      
      <div
        class="data-item Rare Card"
        data-name="emburish"
        data-id="Emburish"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-rare">
            <img
              src="http://placehold.co/120x120"
              alt="Emburish"
            />
          </div>
          <span class="data-name">Emburish</span>
        </div>
      </div>
      
      <div
        class="data-item Rare Evo"
        data-name="hollow warrior mask"
        data-id="Hollow Warrior Mask"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-rare">
            <img
              src="http://placehold.co/120x120"
              alt="Hollow Warrior Mask"
            />
          </div>
          <span class="data-name">Hollow Warrior Mask</span>
        </div>
      </div>
      
      <div
        class="data-item Rare Card"
        data-name="overnow"
        data-id="Overnow"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-rare">
            <img
              src="http://placehold.co/120x120"
              alt="Overnow"
            />
          </div>
          <span class="data-name">Overnow</span>
        </div>
      </div>
      
      <div
        class="data-item Rare Evo"
        data-name="scouter"
        data-id="Scouter"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-rare">
            <img
              src="http://placehold.co/120x120"
              alt="Scouter"
            />
          </div>
          <span class="data-name">Scouter</span>
        </div>
      </div>
      
      <div
        class="data-item Rare Card"
        data-name="starlight"
        data-id="Starlight"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-rare">
            <img
              src="http://placehold.co/120x120"
              alt="Starlight"
            />
          </div>
          <span class="data-name">Starlight</span>
        </div>
      </div>
      
      <div
        class="data-item Rare Card"
        data-name="testcard"
        data-id="TestCard"
        @click="openItem(window.itemData[$el.dataset.id])"
      >
        <div class="data-card cursor-pointer">
          <div class="data-img-container bg-rare">
            <img
              src="http://placehold.co/120x120"
              alt="TestCard"
            />
          </div>
          <span class="data-name">TestCard</span>
        </div>
      </div>
      
    </div>
  </div>

  <div
    class="item-modal-overlay"
    x-show="selected_item"
    x-transition.opacity
    x-cloak
    @click.self="closeItem()"
  >
    <div
      class="item-modal-container"
      :class="'glow-' + selected_item?.Rarity?.toLowerCase()"
      x-show="selected_item"
      x-transition.scale
    >
      <div class="item-modal-header">
        <div class="item-modal-img-wrapper">
          <img
            :src="selected_item?.Image"
            :alt="selected_item?.Name"
            class="item-modal-img"
          />
        </div>
        <h2
          class="item-modal-title"
          :class="'text-' + selected_item?.Rarity?.toLowerCase()"
          x-text="selected_item?.Name"
        ></h2>
        <span
          class="item-modal-rarity-label text-white"
          x-text="selected_item?.Rarity"
        ></span>
      </div>

      <div class="item-modal-body">
        <div>
          <h4 class="item-modal-section-title">Description</h4>
          <p
            class="item-modal-description"
            x-text="selected_item?.Description"
          ></p>
        </div>
        <div>
          <h4 class="item-modal-section-title">Obtainment Locations</h4>
          <div class="item-modal-obtainment-grid">
            <template x-for="loc in selected_item?.Obtainment" :key="loc">
              <span class="item-modal-tag" x-text="loc"></span>
            </template>
          </div>
        </div>
        <button @click="closeItem()" class="item-modal-close-btn">Close</button>
      </div>
    </div>
  </div>
</div>