## **Technická Dokumentácia**

### **Popis tried**

#### **1. `Cell` Trieda**
Reprezentuje samotné políčko z celého pola.

**Hlavné Metódy**:
- `__init__(self, has_mine: bool, surrounding_mines_count: int, is_open: bool = False) -> None`: Inicializuje políčko.
- `open(self)`: Označí políčko ako otvorené.
- `unopened_non_mine(self) -> bool`: Overuje či je políčko neotvorené a nie je mína.
- `__str__(self) -> str`: Vracia reťazcovú reprezentáciu políčka.

#### **2. `Grid` Trieda**
Reprezentuje pole hry a obsahuje samotnú logiku hry.

**Hlavné Metódy**:
- `__init__(self, width: int, height: int, difficulty: int) -> None`: Inicializuje pole s rozmermi a obtiažnosťou od uživateľa.
- `has_unopened_non_mines(self) -> bool`: Overuje, či existujú neotvorené políčka bez mín.
- `print(self) -> None`: Vypíše v terminály aktuálny stav herného pola.
- `is_cell_open(self, row_index: int, column_index: int) -> bool`: Overuje, či je dané políčko otvorené.
- `has_mine(self, coordinate: Coordinate) -> bool`: Overuje, či daná súradnica obsahuje mínu v políčku.
- `hint(self)`: Vypíše nápovedu užívateľovi.
- `_create_empty_cells(self) -> List[List[Cell]]`: Vytvorí prázdne pole políčok.
- `_set_cell_mines_and_surrounding_counts(self) -> None`: Nastaví míny a vypočíta počet mín v okolí.
- `_generate_grid_coordinate_positions(self) -> List[Tuple[int, int]]`: Generuje súradnice celého pola.
- `_generate_mine_positions(self, coordinate_positions: List[Tuple[int, int]]) -> List[Tuple[int, int]]`: Náhodne vyberie pozície pre míny.
- `_identify_non_mine_positions(self, coordinate_positions: List[Tuple[int, int]], mine_positions: List[Tuple[int, int]]) -> set`: Identifikuje súradnice bez mín.
- `_place_mines(self, mine_positions: List[Tuple[int, int]]) -> List[List[Cell]]`: Vkladá míny do pola. 
- `_is_valid_position(self, row_index: int, column_index: int) -> bool`: Rozhoduje, či je pozícia v poli alebo mimo. 
- `_set_surrounding_mine_count(self, non_mine_positions: set[Tuple[int, int]]) -> None`: Nastavuje počet mín v okolí pre políčka bez mín.
- `_recursive_backtrack_search(self, row, col, visited)`: Rekurzívna pomocná metóda pre metódu s nápovedou. 

#### **3. `Minesweeper` Trieda**
Hlavná trieda pre organizovanie herného priebehu.

**Hlavné Métody**:
- `__init__(self, width: int, height: int, difficulty: int) -> None`: Inicializuje kompletnú hru.
- `_get_valid_coordinate(self, plane: str, max_index: int) -> int`: Berie vhodný input od uživateľa.
- `_get_user_guess(self) -> Coordinate`: Berie vhodný odhad od uživateľa.
- `_has_guessed_mine(self, user_coordinate_guess: Coordinate) -> bool`: Overuje, či uživateľ zadal súradnice s mínou.
- `request_hint(self)`: Sprostredkuje nápovedu pre uživateľa. 
- `play(self) -> None`: Hlavný 'loop' hry.

### **Algoritmy**
- **Mínové Umiestnenie**: Náhodne vyberie mínové pozície podľa určenej obtiažnosti.
- **Generovanie Nápovedy**: Využíva rekurzívny backtracking k nájdeniu voľného políčka. 

