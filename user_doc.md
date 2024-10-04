# **Uživateľská Dokumentácia**

## **Úvod**
Táto verzia hry 'Minesweeper' je textová verzia hry. Cieľom je vyčistiť pole otvorením všetkých políčok, ktoré neobsahujú míny, bez spustenia skrytých mín. Môžete tiež požiadať o nápovedu, ktorá vám pomôže nájsť bezpečné políčka.

## **Nastavenia Hry**
1. **Rozmery Plochy**:
   - Uživateľ zadá rozmery hracej plochy (šírka a výška). Plocha musí mať aspoň 2x2.
   
2. **Obtiažnosť**:
   - Po určení rozmerov plochy, uživateľ vyberie level obtiažnosti:
     - **Easy (1)**: 10% plochy bude obsahovať míny.
     - **Medium (2)**: 15% plochy bude obsahovať míny.
     - **Hard (3)**: 20% plochy bude obsahovať míny.

## **Gameplay**
1. **Cieľ hry**:
   - Otvoriť všetky políčka, ktoré nemajú míny.
   - Hra končí, keď sa otvorí políčko s mínou.

2. **Reprezentácia plochy**:
   - Plocha je zobrazená s políčkami, ktoré sú reprezentované nasledovne:
     - `" "`:  Neotvorené políčko.
     - `"0"`: Otvorené políčko bez okolitých mín.
     - Číslo (`"1"`, `"2"`, atď.): Indikuje počet mín, ktoré sú okolo otvoreného políčka.

3. **Kroky**:
   - **Play**: Uživateľ zadá tip, na základe ktorého sa odhalí políčko
   - **Hint**: Hra vypíše nápovedu so súradnicami, ktoré určite neobsahujú míny.
   - Keď uživateľ zadá možnosť `play` , vyberie políčko zadaním jeho súradnic.



## **Hints**
- You can request a hint by typing `hint` when prompted. The game will guide you to a safe cell.
