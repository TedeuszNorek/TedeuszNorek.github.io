# Vortex University Lab, publiczny demonstrator

To repozytorium publikuje wyłącznie statyczny podgląd demonstratora pod adresem:

`https://tedeusznorek.github.io/vortex-university-lab/`

Źródłem prawdy aplikacji pozostaje osobne repo `simulationsUW`, katalog `apps/decision-lab-showcase`. Plików w `site/vortex-university-lab/` nie należy poprawiać ręcznie, ponieważ kolejny build je zastąpi.

## Aktualizacja

1. Zbuduj i sprawdź aplikację w repo źródłowym.
2. Uruchom `python3 scripts/sync_showcase.py /pełna/ścieżka/do/wygenerowanego/pakietu`.
3. Sprawdź zmiany poleceniem `git diff --check`.
4. Zatwierdź zmiany i wypchnij je do gałęzi `main`. Publikacja GitHub Pages uruchomi się automatycznie.

Skrypt kopiuje wyłącznie trzy dokumenty HTML i trzy schematy wyniku. Automatycznie zachowuje też znacznik `noindex,nofollow` w publicznych dokumentach.

Publiczny panel prowadzącego zawiera materiał referencyjny. Nadaje się do recenzji i pokazu dla kadry, ale nie jest zabezpieczonym środowiskiem zaliczeniowym.
