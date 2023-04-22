"""
                                                     
     /\                                              
    /  \   _ __ ___  _ __   ___ _ __ __ _  __ _  ___ 
   / /\ \ | '_ ` _ \| '_ \ / _ \ '__/ _` |/ _` |/ _ \
  / ____ \| | | | | | |_) |  __/ | | (_| | (_| |  __/
 /_/    \_\_| |_| |_| .__/ \___|_|  \__,_|\__, |\___|
  _____           _ | |       _        _   __/ |     
 |_   _|         | ||_|      | |      (_) |___/      
   | |  _ __   __| |_   _ ___| |_ _ __ _  ___  ___   
   | | | '_ \ / _` | | | / __| __| '__| |/ _ \/ __|  
  _| |_| | | | (_| | |_| \__ \ |_| |  | |  __/\__ \  
 |_____|_| |_|\__,_|\__,_|___/\__|_|  |_|\___||___/                                  
                                                     
"""


from requests import get as yoink
import pandas as pd

def PKGRAB(DEX, PATH, ability, types, handw):

    # =============================================================================
    # requesting names list for each pokedex
    # =============================================================================
    # end of URL for each Pokedex ranges from 1 - 31
    # =============================================================================
    
    x = yoink(f'https://pokeapi.co/api/v2/pokedex/{DEX}').json()
    
    # Here is the initial list of Pokemon names from the current Pokedex
    
    names = []
    
    for z in x["pokemon_entries"]:
        names.append(z["pokemon_species"]["name"])
        
    # Name of Pokedex requested
    
    DexName = (x["name"].capitalize())
    
    # Now we need a list of URL's for each Pokemon's info
    
    URLlist = [f'https://pokeapi.co/api/v2/pokemon/{i}' for i in names]
    
    # Print Dex Name, testing purposes, makes me feel better. REMOVE LATER
    
    print(DexName)
    
    # =============================================================================
    # The list. not changing name, sorry
    # =============================================================================
    List2 = []
    
# =============================================================================
#     first line of list to turn into csv
# =============================================================================

    List2.append("Dex Number")
    List2.append("Name")
    if handw == "true":
        List2.append("Height")
        List2.append("Weight")
    else:
        pass
    if ability == "true":
        List2.append("Ability 1")
        List2.append("Ability 2")
        List2.append("Ability 3")
    else:
        pass
    if types == "true":
        List2.append("Type")
        List2.append("Secondary Type")
    else:
        pass
    List2.append("TestSprite1")
    List2.append("TestSprite2")
    
    test_df = pd.DataFrame(columns = List2) 
    test_df.to_csv(PATH, mode='w', header=True, index=False)
    
    
    
    # =============================================================================
    # The while loop that writes the list that will be turned into a .txt for Excel
    # =============================================================================

    b = 0
    
    while b < len(names):
    
    # abtest tests for abilities to populate Null entries
    
        abtest = []
        List = []
    
    # appends the Pokemon's name
        List.append(str(b+1))
        List.append(names[b])
        
    # =============================================================================
    # requests for Pokemon's specific json
    # 
    # add elif statements because the website is trying to fuck with this being
    # an easy task. My function cannot automatically create urls for these
    # fuckers so they must be hardcoded in.
    # most are covered but newer gens will have to be added in as they release
    #
    # Later I can add all the different forms somehow but thats very low priority
    #
    # Last update pas pokemon number 905
    # =============================================================================
    
    
        if names[b] == 'oricorio':
            a = yoink('https://pokeapi.co/api/v2/pokemon/oricorio-baile').json()
        elif names[b] == 'lycanroc':
            a = yoink('https://pokeapi.co/api/v2/pokemon/lycanroc-midday').json()
        elif names[b] == 'basculin':
            a = yoink('https://pokeapi.co/api/v2/pokemon/basculin-red-striped').json()
        elif names[b] == 'wishiwashi':
            a = yoink('https://pokeapi.co/api/v2/pokemon/wishiwashi-school').json()
        elif names[b] == 'zygarde':
            a = yoink('https://pokeapi.co/api/v2/pokemon/zygarde-50').json()
        elif names[b] == 'minior':
            a = yoink('https://pokeapi.co/api/v2/pokemon/minior-red').json()
        elif names[b] == 'mimikyu':
            a = yoink('https://pokeapi.co/api/v2/pokemon/mimikyu-busted').json()
        elif names[b] == 'deoxys':
            a = yoink('https://pokeapi.co/api/v2/pokemon/deoxys-attack/').json()
        elif names[b] == 'wormadam':
            a = yoink('https://pokeapi.co/api/v2/pokemon/wormadam-plant').json()
        elif names[b] == 'giratina':
            a = yoink('https://pokeapi.co/api/v2/pokemon/giratina-origin').json()
        elif names[b] == 'shaymin':
            a = yoink('https://pokeapi.co/api/v2/pokemon/shaymin-sky').json()
        elif names[b] == 'darmanitan':
            a = yoink('https://pokeapi.co/api/v2/pokemon/darmanitan-standard').json()
        elif names[b] == 'tornadus':
            a = yoink('https://pokeapi.co/api/v2/pokemon/tornadus-incarnate').json()
        elif names[b] == 'thundurus':
            a = yoink('https://pokeapi.co/api/v2/pokemon/thundurus-incarnate').json()
        elif names[b] == 'landorus':
            a = yoink('https://pokeapi.co/api/v2/pokemon/landorus-incarnate').json()    
        elif names[b] == 'keldeo':
            a = yoink('https://pokeapi.co/api/v2/pokemon/keldeo-resolute').json() 
        elif names[b] == 'meloetta':
            a = yoink('https://pokeapi.co/api/v2/pokemon/meloetta-pirouette').json()
        elif names[b] == 'meowstic':
            a = yoink('https://pokeapi.co/api/v2/pokemon/meowstic-female').json()
        elif names[b] == 'aegislash':
            a = yoink('https://pokeapi.co/api/v2/pokemon/aegislash-shield').json()
        elif names[b] == 'pumpkaboo':
            a = yoink('https://pokeapi.co/api/v2/pokemon/pumpkaboo-average').json()
        elif names[b] == 'gourgeist':
            a = yoink('https://pokeapi.co/api/v2/pokemon/gourgeist-average').json()
        elif names[b] == 'toxtricity':
            a = yoink('https://pokeapi.co/api/v2/pokemon/toxtricity-amped').json()
        elif names[b] == 'eiscue':
            a = yoink('https://pokeapi.co/api/v2/pokemon/eiscue-ice').json()
        elif names[b] == 'indeedee':
            a = yoink('https://pokeapi.co/api/v2/pokemon/indeedee-female').json()
        elif names[b] == 'morpeko':
            a = yoink('https://pokeapi.co/api/v2/pokemon/morpeko-full-belly').json()
        elif names[b] == 'urshifu':
            a = yoink('https://pokeapi.co/api/v2/pokemon/urshifu-rapid-strike').json()
        elif names[b] == 'basculegion':
            a = yoink('https://pokeapi.co/api/v2/pokemon/basculegion-male').json()
        elif names[b] == 'enamorus':
            a = yoink('https://pokeapi.co/api/v2/pokemon/enamorus-incarnate').json()
        else:
            a = yoink(URLlist[b]).json()
            
        
        
        if handw == "true":
            List.append(str(a["height"]))
            List.append(str(a["weight"]))
        else:
            pass
    
    
    # Adding abilities and populating NULL entries
        if ability == "true":
            for c in a["abilities"]:
                List.append(c["ability"]["name"])
                abtest.append(c["ability"]["name"])
            if len(abtest) == 3:
                pass
            elif len(abtest) == 2:
                List.append("NULL")
            elif len(abtest) == 1:
                List.append("NULL")
                List.append("NULL")
        else:
            pass
            

    
    # tytest, abtest for types
    
        tytest = []
        
    # printing types
        if types == "true":
            for d in a["types"]:
                List.append(d["type"]["name"])
                tytest.append(d["type"]["name"])
            if len(tytest) == 2:
                pass
            elif len(tytest) == 1:
                List.append("NULL")
        else:
            pass
            
    # printing sprites
    
        List.append('=IMAGE("' + a["sprites"]["front_default"] + '")')
        List.append('=IMAGE("' + a["sprites"]["front_shiny"] + '")')   
    
   
    
   # End Pokemon entry and repeat function
    
        new_df  = pd.DataFrame([List], columns = List2) 
        new_df.to_csv(PATH, mode='a', header=False, index=False)
        test_df = pd.concat([test_df, new_df], ignore_index=True)
        b = b + 1
        
    # =============================================================================
    #     Finish by writing
    # =============================================================================

 ## TODO

# sprite picker

# base stats picker + all button (idk)
