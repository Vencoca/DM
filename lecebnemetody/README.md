
# Lecebne metody
Tučně jsou názvy bloků
## Postup
### Import
- Import (source) - VAR FILE 
- TYPE (field ops) - nastavím target jako drug

### Porozumění datům
 - DATA AUDIT(output )(jestli je vyvážené muž/žena, jaké je věkové rozložení...) 
 - PLOT(graph) závislosti sodíku(x) a draslíku(y) na léku(color)
 - WEB (graph) - vztah mezi krevním tlakem a lékem, vyhodím pacienty s lékem Y pomocí bloku SELECT(record ops) 
    - s vysokým tlakem A/B, s nízkým X/C a s normálním tlakem X
 - Vytvoříme novou proměnou - poměr sodíku a draslíku DERIVE(field ops) a nezapomeneme na TYPE
    - Zobrazíme HISTOGRAMem a zjistíme že pro poměr větší než 15 je vhodný lék Y
    - můžeme zahodit sloupce Na K FILTRem(field ops) (můžu ho použít pro přejmenování proměné)

### Modelování
 - Použijme CHAID a C5.0 (models - supervised)
    - model CHAID -> záložka view a vidím DENDROGRAM

### Testování
 - zkopíruju diamanty
 - import -> type -> diamanty -> ANALYST(output)
 - zapojím tabulku za CHAID a vidím že se mi přidal řádek 
 - userinput z diamantu (pravým a generate user input), musí být napojený na data
    - nastavím si vlastní hodnoty, smažu nepotřebné