# Uppgift 4 Bibliotek
Skriv tester med BDD för ett biblioteksystem, där man kan:
* söka efter böcker baserat på titel 
* söka efter böcker baserat på författare
* låna en bok
* lämna tillbaka en bok
* kontrollera om en viss bok är utlånad eller inte


## Projektstruktur
* features/library.feature beskriver beteendet med Given, When, Then
* features/steps/library_steps.py – innehåller stegdefinitioner i Python
* src/books.py och Library.py – innehåller funktionerna för Bibliotekets funktioner

## Tester (BDD)
Testerna är skrivna enligt BDD och består av två delar:

### Feature-fil
Beteendet beskrivs i en .feature-fil med Gherkin-syntax:
* Given – startvärde
* When – handling (omvandling)
* Then – förväntat resultat

## Installation
* installerar beroenden:
```
pip install -r requirements.txt
```
## Kör tester
```
behave
```

## Konfigurationsfiler
* requirements.txt
* .gitignore