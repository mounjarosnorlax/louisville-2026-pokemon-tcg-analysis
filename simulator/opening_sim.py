#!/usr/bin/env python3
"""Opening/prize simulator only. It does not model full games or match win rates."""
from __future__ import annotations
import argparse, json, random
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def expanded(counts):
    return [name for name, count in counts.items() for _ in range(count)]

STARMIE_BASE = {
 "Staryu":4,"Snorunt":4,"Mega Starmie ex":3,"Mega Froslass ex":3,
 "Water Energy":10,"Legacy Energy":1,"Ignition Energy":1,"Salvatore":4,
 "Lillie's Determination":4,"Wally's Compassion":3,"Boss's Orders":2,"Hilda":2,
 "Black Belt's Training":1,"Buddy-Buddy Poffin":4,"Switch":2,"Mega Signal":2,
 "Pokegear 3.0":3,"Energy Search":4,"Night Stretcher":1,"Gravity Mountain":2,
}
KANG_BASE = {
 "Joltik":2,"Dwebble":2,"Crustle":2,"Mega Kangaskhan ex":2,"Psyduck":1,
 "Munkidori":1,"Bouffalant":3,"Latias ex":1,"Lightning Energy":4,"Grass Energy":4,
 "Darkness Energy":2,"Growing Grass Energy":1,"Mist Energy":1,"Boss's Orders":3,
 "Brock's Scouting":1,"Ciphermaniac's Codebreaking":1,"Lillie's Determination":4,
 "Team Rocket's Petrel":4,"Xerosic's Machinations":1,"Buddy-Buddy Poffin":2,
 "Jumbo Ice Cream":4,"Night Stretcher":1,"Poke Pad":1,"Pokegear 3.0":3,
 "Special Red Card":1,"Switch":1,"Ultra Ball":1,"Precious Trolley":1,
 "Team Rocket's Factory":1,"Battle Cage":1,"Backtrack Badge":1,"Hilda":1,"Crispin":1,
}

def mulligan_to_basic(cards, basics, rng):
    mulligans = 0
    while True:
        rng.shuffle(cards)
        hand = cards[:7]
        if any(c in basics for c in hand):
            return hand, cards[7:], mulligans
        mulligans += 1

def gear_for_salvatore(hand, deck, rng):
    if "Salvatore" in hand: return True
    gears = hand.count("Pokegear 3.0")
    for _ in range(gears):
        top = deck[:7]
        if "Salvatore" in top:
            deck.remove("Salvatore"); hand.append("Salvatore"); rng.shuffle(deck); return True
        rng.shuffle(deck)
    return False

def energy_live(hand, deck):
    if "Water Energy" in hand or "Legacy Energy" in hand: return True
    return "Energy Search" in hand and "Water Energy" in deck

def starmie_trial(counts, rng, opp):
    cards=expanded(counts); basics={"Staryu","Snorunt"}
    hand, rem, mulls=mulligan_to_basic(cards,basics,rng)
    # Active is declared before prizes. Prefer Staryu because Jetting Blow is hand-size independent.
    active="Staryu" if "Staryu" in hand else "Snorunt"
    prizes=rem[:6]; deck=rem[6:]
    if deck: hand.append(deck.pop(0)) # first turn draw going second
    direct_sal="Salvatore" in hand
    sal=gear_for_salvatore(hand,deck,rng)
    e_live=energy_live(hand,deck)
    evo={"Staryu":"Mega Starmie ex","Snorunt":"Mega Froslass ex"}
    chosen=active if deck.count(evo[active]) else None
    # If the active line is fully prized/held, Poffin plus Switch can create the other line.
    other="Snorunt" if active=="Staryu" else "Staryu"
    alternate_basic = other in hand or ("Buddy-Buddy Poffin" in hand and other in deck)
    if chosen is None and alternate_basic and "Switch" in hand and evo[other] in deck:
        chosen=other
    attack=bool(sal and e_live and chosen)
    damage=0
    if attack:
        damage=120 if chosen=="Staryu" else 50*opp["post_setup_hand_size"]
    hp_roll=rng.random(); cumulative=0; hp=999
    for value,prob in opp["active_hp_distribution"].items():
        cumulative+=prob
        if hp_roll<=cumulative: hp=int(value); break
    ko=attack and damage>=hp
    single=rng.random()<opp["single_basic_probability"]
    bench=rng.random()<opp["bench_present_probability"]
    meaningful=attack and (damage>=120 or (chosen=="Staryu" and bench))
    high_pressure=attack and (ko or damage>=200 or (chosen=="Staryu" and bench))
    return {"mulligans":mulls,"direct_salvatore":direct_sal,"salvatore_access":sal,
            "energy_access":e_live,"evolution_target_in_deck":bool(chosen),"t1_attack":attack,
            "t1_meaningful":meaningful,"t1_high_pressure":high_pressure,"ko":ko,
            "donk":ko and single,"starmie_attack":attack and chosen=="Staryu",
            "froslass_attack":attack and chosen=="Snorunt"}

def kang_trial(counts,rng):
    basics={"Joltik","Dwebble","Mega Kangaskhan ex","Psyduck","Munkidori","Bouffalant","Latias ex"}
    hand,rem,mulls=mulligan_to_basic(expanded(counts),basics,rng); prizes=rem[:6]; deck=rem[6:]
    hand2=hand+[deck.pop(0)]
    supporter=set(["Boss's Orders","Brock's Scouting","Ciphermaniac's Codebreaking","Lillie's Determination","Team Rocket's Petrel","Xerosic's Machinations","Hilda","Crispin"])
    natural=any(c in supporter for c in hand2)
    gear=False
    for _ in range(hand2.count("Pokegear 3.0")):
        top=deck[:7]
        if any(c in supporter for c in top): gear=True; break
        rng.shuffle(deck)
    energy=any(c.endswith("Energy") for c in hand2)
    joltik="Joltik" in hand2 or ("Buddy-Buddy Poffin" in hand2 and "Joltik" in deck) or ("Poke Pad" in hand2 and "Joltik" in deck) or "Precious Trolley" in hand2
    dwebble="Dwebble" in hand2 or ("Buddy-Buddy Poffin" in hand2 and "Dwebble" in deck) or ("Poke Pad" in hand2 and "Dwebble" in deck) or "Precious Trolley" in hand2
    return {"mulligans":mulls,"energy_access":energy,"supporter_access":natural or gear,
            "pokegear_effective_access":gear and not natural,"poffin_access":"Buddy-Buddy Poffin" in hand2,
            "trolley_access":"Precious Trolley" in hand2,"lillie_access":"Lillie's Determination" in hand2,
            "joltik_access":joltik,"dwebble_access":dwebble,"setup_pair":joltik and dwebble and energy and (natural or gear)}

def summarize(trials):
    n=len(trials); keys=set().union(*(t.keys() for t in trials)); out={"iterations":n}
    out["mulligan_rate_per_opening_attempt_pct"]=round(100*sum(t["mulligans"] for t in trials)/(n+sum(t["mulligans"] for t in trials)),3)
    out["mean_mulligans_before_valid_hand"]=round(sum(t["mulligans"] for t in trials)/n,4)
    for k in sorted(keys-{"mulligans"}): out[k+"_pct"]=round(100*sum(bool(t[k]) for t in trials)/n,3)
    return out

def run_counts(base, changes):
    c=base.copy()
    for name,value in changes.items(): c[name]=value
    delta=60-sum(c.values()); c["Blank flex slot"]=c.get("Blank flex slot",0)+delta
    assert sum(c.values())==60
    return c

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--iterations',type=int); ap.add_argument('--seed',type=int); args=ap.parse_args()
    cfg=json.loads((Path(__file__).parent/'config.json').read_text()); n=args.iterations or cfg['iterations']; seed=args.seed or cfg['seed']
    results={"seed":seed,"iterations_per_configuration":n,"scope":"opening and prize simulation only","starmie":{},"kang":{}}
    variants={"baseline":{},**{f"salvatore_{x}":{"Salvatore":x} for x in [3,2,1,0]},
              **{f"energy_search_{x}":{"Energy Search":x} for x in [3,2]},
              "energy_11":{"Water Energy":9},"energy_10":{"Water Energy":8},
              "froslass_2":{"Mega Froslass ex":2},"starmie_2":{"Mega Starmie ex":2},
              "wally_2":{"Wally's Compassion":2},"hilda_1":{"Hilda":1},
              "pokegear_2":{"Pokegear 3.0":2},"mega_signal_1":{"Mega Signal":1},
              "switch_1":{"Switch":1},"gravity_1":{"Gravity Mountain":1}}
    for i,(name,changes) in enumerate(variants.items()):
        rng=random.Random(seed+i*1009); counts=run_counts(STARMIE_BASE,changes)
        results['starmie'][name]={"changes":changes,"metrics":summarize([starmie_trial(counts,rng,cfg['opponent_assumptions']) for _ in range(n)])}
    rng=random.Random(seed+99991); results['kang']['baseline']=summarize([kang_trial(KANG_BASE,rng) for _ in range(n)])
    out=ROOT/'results'/'opening_simulation.json'; out.write_text(json.dumps(results,indent=2)+"\n"); print(out)
if __name__=='__main__': main()
