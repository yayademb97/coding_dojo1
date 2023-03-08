const pokémon = Object.freeze([
    { "id": 1,   "name": "Bulbasaur",  "types": ["poison", "grass"] },
    { "id": 5,   "name": "Charmeleon", "types": ["fire"] },
    { "id": 9,   "name": "Blastoise",  "types": ["water"] },
    { "id": 12,  "name": "Butterfree", "types": ["bug", "flying"] },
    { "id": 16,  "name": "Pidgey",     "types": ["normal", "flying"] },
    { "id": 23,  "name": "Ekans",      "types": ["poison"] },
    { "id": 24,  "name": "Arbok",      "types": ["poison"] },
    { "id": 25,  "name": "Pikachu",    "types": ["electric"] },
    { "id": 37,  "name": "Vulpix",     "types": ["fire"] },
    { "id": 52,  "name": "Meowth",     "types": ["normal"] },
    { "id": 63,  "name": "Abra",       "types": ["psychic"] },
    { "id": 67,  "name": "Machamp",    "types": ["fighting"] },
    { "id": 72,  "name": "Tentacool",  "types": ["water", "poison"] },
    { "id": 74,  "name": "Geodude",    "types": ["rock", "ground"] },
    { "id": 87,  "name": "Dewgong",    "types": ["water", "ice"] },
    { "id": 98,  "name": "Krabby",     "types": ["water"] },
    { "id": 115, "name": "Kangaskhan", "types": ["normal"] },
    { "id": 122, "name": "Mr. Mime",   "types": ["psychic"] },
    { "id": 133, "name": "Eevee",      "types": ["normal"] },
    { "id": 144, "name": "Articuno",   "types": ["ice", "flying"] },
    { "id": 145, "name": "Zapdos",     "types": ["electric", "flying"] },
    { "id": 146, "name": "Moltres",    "types": ["fire", "flying"] },
    { "id": 148, "name": "Dragonair",  "types": ["dragon"] }
]);

const my_list_pokemon =pokémon.filter(p => p.id%3===0);
console.log(my_list_pokemon);
const fire_list_type=pokémon.filter(x => x.types=="fire");
console.log(fire_typefire_list_type);
const list_more_type=pokémon.filter(x => x.types.length>1);
console.log(list_more_type);

const my_pokemon_name = pokémon.map( p => p.name );
console.log(my_pokemon_name);

const my_pokemon_name_id=pokémon.filter(p => p.id>99).map(p => p.name);
console.log(my_pokemon_name_id);

const my_pokemon_name_type=pokémon.filter(p => p.types=="poison").map(p => p.name);
console.log(my_pokemon_name_type);

const list_of_two_types=pokémon.filter(x => x.types[1]==="flying").map(x => x.name);
console.log(list_of_two_types);

const normalPokemons = pokémon.filter(pokemon => pokemon.types.includes("normal"));
const normalCount = normalPokemons.length;
console.log(normalCount);