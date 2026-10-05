# Validierung von Künstlicher Intelligenz zur Erkennung von Hasskommentaren im Netz
# zum Clonen
Für das Klonen des Repositories wird Git LFS (Large File Storage) benötigt, da die KI-Modelle aufgrund ihrer Größe darüber verwaltet werden.E
Es kann unter diesem Link herunterladen:

https://git-lfs.com/ 

oder über die git bash:
```bash
git lfs install

git clone <https://github.com/MariaFuhrhop/KIs_Validierung_Hasskommentar.git>

cd <Repository-Ordner>

git lfs pull
```

Ordner strukturen:

Im Ordner KI befinden sich  unter Modelle die gespeicherten Modelle, unter Code der COde des Modelltrainings, das Datenset sowie die Textdateien mit den Wahrscheinlichkeiten aus der Validierung.

Im Ordner untitled befindet sich das aktuelle KI-Modell welches im Prototypen integriert ist, sowie seine FastAPI (main.py).

Im Ordner API befindet sich die Springboot API unter API/src/main/java/org/example/api die Maindatei ist PredictController.java.

Im Ordner Frontend befindet sich unter frontend-app/src/app/eingabe das Frontend.


# Prototypen starten
Modell starten: im Terminal im untitled Ordner "uvicorn main:app --host 127.0.0.1 --port 8000" 
<img width="873" height="388" alt="grafik" src="https://github.com/user-attachments/assets/315002d1-9432-40c0-b664-06d7807f2433" />
/ oder in IntelliJ oder andere Entwicklerumgebungen auch Run main.py (oder Current File) 
<img width="495" height="77" alt="grafik" src="https://github.com/user-attachments/assets/6a95b96a-7752-4f41-95d5-44195df97718" />

API starten: im Terminal im API Ordner ".\mvnw.cmd spring-boot:run" 
<img width="696" height="199" alt="grafik" src="https://github.com/user-attachments/assets/3a0d2a2a-7523-4dee-9ebd-685f419f2260" />
/ oder in IntelliJ oder andere Entwicklerumgebungen auch Run Api Application klicken
<img width="2300" height="386" alt="grafik" src="https://github.com/user-attachments/assets/e0a39805-cc92-41f8-93bc-398fe875a7c3" />


Fronted starten: im Terminal im Frontend/frontend-app Ornder "ng serve"
<img width="426" height="67" alt="grafik" src="https://github.com/user-attachments/assets/89657e6c-f280-4ac3-83b1-2293bb827ee7" />

