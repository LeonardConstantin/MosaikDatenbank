# MosaikDatenbank
Dieses Programm ist eine "Inventarsoftware" meiner Mosaik-Abrafaxe Comics. Die Intention hinter diesem Programm, war es sich mit SQL auseinander zu setzen. Deswegen werden die Daten auch aus der csv Datei überhaupt erst in die Datenbank eingetragen. 
Der Datensatz beträgt nur 31 Stück weil ich nicht die Zeit habe alle zum jetzigen Zeitpunkt zu archivieren. Auch fehlen die Bilder, weswegen momentan ein Platzhalter herhalten muss. Auch hier fehlt mir die Zeit von jedem Comic ein Bild zu machen. 
Als Datenbank wird sqlite3 verwendet, weil diese in Python bereits vorinstalliert ist.

Es gibt folgende Suchoptionen:
1.  Suche per ID: In der Suchleiste wird eine Seriennummer des Comics eingegeben und der Suchenknopf betätigt. 
2.  Suche per Filter: Der rechte Teil des Frames spiegelt den Filter wieder. Man kann nach Monaten, Jahren und der Serie des Comics suchen. **Diese Suchoption funktioniert nur wenn die Sucheneingabe leer ist!** Anfänglich ist alles ausgewählt, kann aber durch die Checkboxen abgewählt werden. 
3. In naher Zukunft sollen die Comics auch nach ihrem Titel gesucht werden können. 

Syntax der Jahrescomponent:
Über dem Eingabefeld wird der aktuelle Jahreszeitraum ausgegeben. Standartmäßig 1966-2022. Es gibt folgende lösch und hinzufüge optionen:
1. Hinzufügen/ Löschen **eines** Jahres: Hierfür einfach das Jahr im Format yyyy eingeben. Bsp. 1999
2. Hinzufügen/ Löschen **meherer Jahre**: Hierfür das Intervall durch ein "-" getrennt eingeben. Bsp. 1999-2004.
**Wichtig** Momentan kann es noch zu Fehlern kommen, falls ein Jahr isoliert werden sollte. Bsp. 1960-1999; 2001; 2002-2022.

**Generell muss man davon ausgehen, dass das Programm regelmäßig in Error läuft, welche nicht abgefangen werden. In Zukunft sollen diese Abgefangen werden, aber auf die schnelle ist das nicht gelungen.**
