# Louisville 2026 deck decision report

Checked October 3, 2026. Tournament play begins October 10; the RK9 event itself runs October 9–11.

## 1. Executive answer

The decision is not “proven deck versus meme deck.” It is **higher-floor, matchup-polarized control/tank** versus **lower-evidence, higher-tempo aggression**.

- **VERIFIED FACT:** Your Kang/Crustle list is 60. Your Starmie/Froslass list is 60. Each has one ACE SPEC.
- **VERIFIED FACT:** Salvatore can evolve a Pokémon placed during setup or that turn. Both Mega evolutions have no Ability, so a player going second may use Salvatore on turn one, attach Water, and attack. Mega Evolution adds a three-Prize knockout rule; it does not end the turn on evolution.
- **SIMULATION RESULT:** With your exact Starmie 60, 100,000 seeded openings produced a **45.4% T1 attack rate going second**. The 95% Monte Carlo sampling error is about ±0.31 points. Model uncertainty is much larger.
- **DATA-BASED INFERENCE:** Louisville should still be Dragapult-led, but the combined family fell from 30.5% at Baltimore to 26.5% Frankfurt and 23.7% Brisbane. A sensible Louisville center is roughly 26–29%, not “Baltimore repeats exactly.”
- **STRATEGIC JUDGMENT:** The key choice is whether Kang’s excellent straight-Dragapult and Zoroark evidence outweighs severe exposure to Slowking, Festival Lead, Honchkrow and some Excadrill constructions, versus whether your Salvatore edge and physical testing can overcome Starmie’s weak Baltimore evidence.

## 2. Format, legality and rules

Louisville is listed as Standard on October 10, 2026. The applicable regulation-mark pool is H/I/J plus legal reprints and Basic Energy. Both submitted lists use legal card names/printings as cross-checked against current tournament lists and live card pages.

The local validator snapshot was generated July 25 and incorrectly failed to resolve four later/alternate entries in Kang: Psyduck MEP 7, Poké Pad, Pokégear 3.0 and Backtrack Badge. Live card pages and September Regional lists show these are Standard legal. This is a tooling freshness defect, not a deck illegality. It is preserved in `results/kang_validation.json` instead of silently erased.

Salvatore’s exact constraint is “a card that has no Abilities and evolves from 1 of your Pokémon.” It can evolve a Pokémon placed during setup or that turn. It is still your one Supporter for the turn. A legal first-turn-going-second line is:

1. Start Staryu or Snorunt. All eight Basics in your list qualify for Poffin.
2. Find Salvatore directly or with Pokégear before shuffling the deck with another search.
3. Confirm the matching Mega remains in deck, then evolve with Salvatore.
4. Attach Water or Legacy Energy. Ignition Energy alone cannot pay the printed Water cost.
5. Attack with Jetting Blow or Resentful Refrain.

## 3. Louisville field models

Archetype labels combine Dragapult, Dragapult/Dusknoir and Dragapult/Blaziken as “Dragapult combined,” and both Alakazam families as “Alakazam combined.” Starmie combines pure, Froslass and Dusknoir variants only for field share, not for matchup claims.

| Family | Model A broad | Model B best estimate | Model C adaptation-heavy |
|---|---:|---:|---:|
| Dragapult combined | 25–31% | 27.5% | 23–27% |
| Zoroark | 6–8% | 7.0% | 6–7% |
| Basic Box | 5–8% | 6.5% | 7–9% |
| Slowking | 5–7% | 6.0% | 6–8% |
| Alakazam combined | 6–8% | 6.8% | 7–9% |
| Mega Excadrill | 4–7% | 5.3% | 6–8% |
| Crustle | 3–5% | 3.7% | 2.5–4% |
| Festival Lead | 2.5–5% | 3.6% | 4–6% |
| Dhelmise | 3–4.5% | 3.4% | 3–5% |
| Hydrapple | 2–4% | 3.0% | 3–5% |
| Starmie combined | 0.5–2% | 1.1% | 1–2.5% |
| Grimmsnarl/Froslass | 0.7–1.6% | 1.2% | 0.8–1.5% |
| Other | balance | 24.9% | balance |

These are planning ranges, not population estimates with statistical confidence intervals. Recife was live on October 3 and is not mixed into the model before final results exist. Yokohama confirms innovation and Starmie relevance, but its Japanese format/structure is not pooled with the three Western Regionals.

## 4. Kang/Crustle audit

Your list is a hybrid, not generic Crustle. Joltik creates the attachment surplus; Kang draws and can bridge attacks; Crustle changes which opposing attacks count; Bouffalant reduces damage to Basic Colorless Pokémon; Latias makes Basics mobile; Psyduck disables self-KO Abilities; Munkidori converts damage counters into healing/pressure.

Opening priority is Joltik plus the attacker branch the matchup actually rewards. Going first, attach to Joltik and establish Dwebble/Kang without spending the Supporter. Going second, use Petrel/Lillie to complete the board and charge only if the four Basic Energy mix remains in deck. Trolley is not “fill every Bench”: search fewer Pokémon in wall matchups.

Card roles:

| Role | Cards |
|---|---|
| Core | Joltik, Dwebble/Crustle, Kang, Petrel, Lillie, Poffin, Ice Cream, 12 Energy |
| High-value tech | Psyduck, Munkidori, Latias, Battle Cage, Mist, Switch |
| Meta-dependent | Xerosic, Special Red Card, Backtrack Badge, Factory, Growing Grass |
| Consistency | Brock, Ciphermaniac, Hilda, Crispin, Gear, Pad, Ultra Ball, Trolley |
| Questionable/flex | the *second* setup Supporter among Brock/Cipher, third Gear, Badge when Kang attacks rarely |

Important interactions: Crustle blocks damage from attacks by opposing Pokémon ex, not counters, Ability damage, or a non-ex attacker. Bouffalant reduces damage, not counters. Latias frees retreat only for Basics, not Crustle. Battle Cage blocks counters placed on Benched Pokémon by Abilities, but not ordinary attack damage. Backtrack Badge restarts the complete coin sequence; it does not keep early heads.

Recent aggregate Crustle evidence is real but does not equal your hybrid: Baltimore 138 players, 500-435-181 overall; Frankfurt 88 players, 322-305-110. Baltimore reported matchup samples include straight Dragapult 237 at 68.21%, Zoroark 91 at 64.47%, Basic Box 67 at 51.74%, Slowking 54 at 35.19%, Excadrill 52 at 13.46%, and Festival 27 at 28.40%. Frankfurt repeats the shape: Dragapult 130 at 68.46%, Zoroark 56 at 58.93%, Basic Box 43 at 53.49%, Slowking 48 at 19.44%, Excadrill 25 at 38.67%, Festival 41 at 17.07%. These are Limitless reported rates, not reconstructed W/L/T counts.

Candidate exact 60s:

- **Consistency:** `kang_consistency.txt`. ADD 1 Dwebble, 1 Night Stretcher, 1 Ultra Ball, 1 Energy Switch. CUT Brock, Ciphermaniac, one Gear, Badge. Gains redundant setup/recovery and makes moving Joltik’s surplus less theoretical; loses tailored hand construction and coin ceiling.
- **Louisville meta:** `kang_louisville_meta.txt`. ADD Night Stretcher and Energy Switch. CUT Brock and one Gear. Keeps Badge/Cipher while improving attacker reconstruction. This is the least identity-disruptive candidate.

## 5. Aggro Starmie audit and Salvatore study

Your baseline is unusually clean: eight 70-HP evolving Basics, six Mega targets, four Salvatore, three Gear, 11 Water-providing attachments, four Energy Search. Starmie’s Jetting Blow is 120 Active plus 50 Bench for one Water. Froslass’s Resentful Refrain is 50 per card in the opponent’s hand for one Water. Gravity Mountain affects Stage 2 HP only. Ignition supplies three Colorless to an Evolution but discards itself at end of turn; it cannot fund the one-Water opening attack. Legacy pays Water and can reduce prizes once per game when its holder is KO’d by attack damage.

Seed 20261003, 100,000 valid opening hands per configuration, mulligans and six prizes modeled:

| Configuration | Salvatore access | Energy access | T1 attack | modeled donk* |
|---|---:|---:|---:|---:|
| 4 Salvatore baseline | 52.0% | 90.1% | 45.4% | 3.30% |
| 3 Salvatore | 42.2% | 90.0% | 36.7% | 2.62% |
| 2 Salvatore | 30.7% | 90.1% | 26.6% | 1.94% |
| 1 Salvatore | 16.8% | 90.0% | 14.4% | 1.03% |
| 0 Salvatore | 0% | 89.8% | 0% | 0% |

Four to three loses 8.7 T1-attack points. Three to two loses 10.1. Two to one loses 12.2. One to zero loses 14.4. Because Salvatore itself searches the evolution, Mega Signal does not improve the T1 line.

Other isolated results: four to three Energy Search reduced T1 attack from 45.4% to 43.8%; to two reduced it to 42.6%. Reducing total Energy from 12 to 11 produced 44.2%; to 10 produced 42.7%. Cutting one Froslass produced 44.6%; cutting one Starmie produced 43.9%. Cutting Gear from three to two produced 42.3%. Counts of Wally, Hilda, Mega Signal, Switch and Gravity barely move this opening metric because they are follow-up cards, not opening-line pieces.

*The 3.30% donk number is **not a Louisville fact**. It uses editable assumptions: 8% of opponents finish setup with one Basic and the listed active-HP distribution. Conditional on the assumed HP mix, the baseline generated a KO in 41.8% of all games and an attack in 45.4%. The theoretical maximum donk rate, if every opponent had one lone Basic with that HP mix, is 41.8%. Realistic donk rate equals the full-line/KO probability multiplied by the actual lone-Basic frequency, which must be logged in physical tests. This distinction is why the simulator exposes the assumptions.

Candidate exact 60s:

- **Refined Aggro:** ADD 4 Ultra Ball. CUT 1 Wally, 1 Hilda, 1 Energy Search, 1 Gravity Mountain. This preserves four Salvatore and almost all T1 rate while fixing the glaring lack of unconditional evolution search after turn one.
- **Louisville Aggro:** ADD 2 non-ex Froslass, 1 Psyduck, 3 Ultra Ball. CUT 1 Mega Froslass, 2 Wally, 2 Energy Search, 1 Gravity Mountain. It gives a one-Prize line and Dusknoir protection; modeled T1 attack should land near 41–42% because the two isolated cuts cost roughly 3–4 points. Test it rather than accepting that estimate additively.

## 6. Matchup dashboard

No full-game win-rate simulation is reported. A credible engine would need opponent-specific search policies, counters, wall bypass, prize mapping, clock and conceding. The evidence below is therefore empirical plus strategic.

| Matchup | Kang/Crustle | Aggro Starmie | Confidence / deciding test |
|---|---|---|---|
| Straight Dragapult | Strong aggregate Crustle evidence; narrow Crustle board | Baltimore Starmie was 4/16 by reported match count/rate | High direction; test Pult/Dusk separately |
| Dragapult/Dusknoir | Near even aggregate; Psyduck important | High pressure can strand Dreepy, but three-Prize Megas invite counter maps | Medium; 4 physical games |
| Basic Box | Roughly even aggregate; identify non-ex wall breaker | Baltimore Starmie sample 7, reported 4.76% | Medium for Kang, low for your Starmie |
| Zoroark | Favorable aggregate for Crustle, but copied Shred bypasses effects | Baltimore sample only 2, both losses | Medium/very low |
| Slowking | Consistently bad aggregate; copied non-Rule-Box attacks matter | Small sample 5 at 40% | Medium/low; must test |
| Alakazam | Surprisingly favorable aggregate, but counters bypass wall; Mist/Xerosic sequencing | Small sample 4 at 33.3%; early spread can pressure Abra | Medium/low |
| Mega Excadrill | Bad and volatile across events; Grass resistance and alternate attacks | Sample 2, zero wins | Low; must test |
| Festival Lead | Very bad aggregate; non-ex double attacks invalidate wall | Sample 3, 44.4% | Medium/very low |
| Crustle mirror | About even aggregate; your Crustle attack bypasses effects | Jetting Blow does not bypass Crustle; Nebula Beam does, but needs three Colorless | Medium strategic |
| Starmie | Tiny data; attack the three-Prize evolution line | Aggro mirror rewards first pressure and Legacy mapping | Very low |

Kang sequencing: against ex-heavy boards, preserve Grass and a replacement Dwebble, then force the opponent to show the non-ex/bypass answer. Petrel is strongest before setup or when it finds the one Item that completes a branch. Xerosic/Red Card are tempo plays after draw engines or Prize state make the reduced hand matter, not automatic turn plays. Boss development pieces only when the KO changes their next attack.

Starmie sequencing: going second, pursue Salvatore only when it yields a legal attack and does not consume the only recovery route. Choose Starmie for fixed 120+50 and Froslass when the opponent’s hand makes the active KO meaningful. Going first, build two attackers and use Lillie/Hilda rather than holding dead Salvatore hopes. Save Switch when the opening Basic is not the desired attacker. Gravity Mountain is a threshold tool versus Stage 2 decks, not setup.

## 7. Decision framework and pilot edge

Use the physical test record, not an invented weighted win rate. The public evidence is apples-to-oranges: generic Crustle has hundreds of matches; the exact hybrid does not. Baltimore Starmie/Froslass had 25 wins, 49 losses and 13 ties across 14 players, but pure Mega Starmie also produced a 23rd-place finish. Your exact four-Salvatore build is not represented by that aggregate.

Pilot-edge sensitivity is simple: if one deck’s credible meta expectation is `d` percentage points lower, it needs more than `d` points of pilot advantage to reverse the order. Evaluate the dashboard at -5, -2.5, 0, +2.5 and +5. If your 26-game test produces no stable matchup gap larger than 5 points, familiarity, clock management and error rate can dominate the choice. Do not estimate pilot edge from raw game record alone; use misplays, missed lines and time.

Decision rule on October 8:

1. Eliminate a deck if it has more than two unforced sequencing errors per ten logged games or repeatedly approaches time.
2. Eliminate a build if its defining plan fails: Kang cannot establish/rebuild the correct wall, or Starmie’s meaningful T1 pressure is under 8 of 18 going-second trials.
3. Compare the five most likely families only: Dragapult, Zoroark, Basic Box, Slowking, Alakazam.
4. Apply your observed pilot edge in the ±5-point grid.
5. If still tied, choose by variance preference: Kang accepts matchup polarization; Starmie accepts opening/follow-up volatility.

## 8. Physical testing plan, October 3–8

Twenty-six games, chosen for information gain:

| Block | Your deck | Opponent | Games | First/second | Question |
|---|---|---|---:|---|---|
| 1 | Kang Louisville | Slowking | 4 | 2/2 | Can the hybrid escape its clearest evidence-based bad matchup? |
| 2 | Kang Louisville | Excadrill | 4 | 2/2 | Which attacker and Energy line survives resistance/non-ex outs? |
| 3 | Starmie Refined | Dragapult/Dusknoir | 4 | 0/4 | Does T1 pressure convert before the three-Prize counter map? |
| 4 | Starmie Refined | Basic Box | 4 | 0/4 | Is Baltimore’s awful small sample structural or list/pilot noise? |
| 5 | Starmie Louisville | Crustle | 4 | 2/2 | Are Nebula Beam and non-ex Froslass sufficient, and on what clock? |
| 6 | Both, alternating | Zoroark | 4 | 2 each | Which plan handles Shred and recovery with fewer decision errors? |
| 7 | Both, alternating | Alakazam | 2 | one each | Validate Mist/counter sequencing and early-KO pressure. |

Interpretation: 26 games cannot estimate true matchup percentages. A 3–1 block is a reason to inspect the games, not declare 75%. Use the sheet to count setup achieved, meaningful-attack turn, missed winning lines, unforced errors and time. Change a list only when the same failure mechanism appears at least three times or card access repeatedly decides the game.

## 9. Unresolved items

- Louisville’s final Masters attendance and exact Swiss/Day 2 threshold are not posted on the cited RK9 page as of October 3. No Day 1 path simulation is labeled “actual Louisville structure.”
- Exact opponent lone-Basic rates and post-setup hand sizes are unmeasured. Therefore donk is a sensitivity output, not a prediction.
- No credible full-game simulator exists in this project. Match win rates are intentionally not manufactured.
- Recife results may materially alter Model C once complete.
- The local legality generator did not successfully replace its July 25 metadata despite a live API refresh attempt; live card/event pages were used to resolve the affected cards.
