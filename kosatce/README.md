
## Kosatce
Tučně jsou názvy bloků
### Postup
Import (source) - STATISTIC FILE (read labels as data, zakliknu usefield format info)\
TYPE (field ops) - nastavím target jako spiecices\
FEATURE SELECTION (models - supervised) - vyhodnocuje důležitost velké sady prediktorů (model nemodel, škrtne zbytečné sloupce)\
PARTITION (field ops) - rozdělím data na trénovací a testovací (vždy u učení s učitelem)\
AUTO CLASSIFIER (models - all) - zkouší různé algoritmy\
DISCRIMINANT (models - supervised) - vyšel nejlépe tak ho uděláme zvlášť\
ANALYSIS (output) - Detailnější výsledky\
USER INPUT (musím udělat sám) - kliknu pravým na vstup, generate user input, a zpět (zpátky připojí původní ale UI zůstane), odstraním si klasifikaci\
zkopíruju si můj nejlepší model, a odpojím ho (pravým remove link)\
připojím TABLE(output) a uvidím, jak ho klasifikoval i s jakou jistotout (pravděpodovností)

### Kosatce s expertem
DERIVE(field ops) - vytvorim sepal area a petal area (naklikám v pravo (width * length))\
FILTER (field ops) - odstraníme nepotřebné proměné, nebo můžu v typu zrušit význam
### Poznámky
DATA AUDIT |(output) se používá pro více grafů\
FEATURE SELECTION (models - supervised) - vyhodnocuje důležitost velké sady prediktorů\
Po kliknutí na run se vytvoří model, pokud ho odpojíme od např FUTURE SELECTION tak se nebude aktualizovat.\
Učení s učitelem - mám sadu dat i s targetem (tj znám výsledek)/Učení bez učitele\
Při učení s učitelem - rozdělíme sadu na trénovací a testovací množinu, aby se algoritmus nenaučil data nazpamět (nepřeučil se)\
Pokud chci porovnat výsledky, tak modely zapojím sériově za sebou.