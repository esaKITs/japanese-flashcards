# Romaji Reader — OCR rebuild (experimental)

Do not merge or publish this branch until all checks pass.

## Sources under review
- Yomikomi: https://github.com/sieugene/yomikomi (MIT; copyright (c) 2026 sieugene). Client-side PaddleOCR/ONNX implementation in src/features/ocr-client and assets in public/ocr; evaluate actual dependencies, model weights and licenses before reuse.
- nihongo-mono: https://github.com/stndaru/nihongo-mono. Evaluate mobile image capture/cropping and license of each component and data file.

## Non-negotiable requirements
- 0 JPY development, hosting and use; no billing, paid API, ads or login.
- Horizontal Japanese print, camera/photo upload; entirely client-side processing; no image upload to server.
- Japanese OCR including furigana where feasible; ruby reading must override base-text reading when reliable.
- Hepburn romaji with macrons for long vowels; output romaji only, no translations/dictionary/grammar UI.
- English/icon UI; iPhone Safari first; existing hiragana and other projects untouched.

## Validation gates before release
1. Verify complete license and third-party model/data attribution and permissions.
2. Build self-contained static GitHub Pages bundle; inspect network requests and ensure no image upload.
3. Measure cold-start and warm-start timings separately on iPhone Safari.
4. Test kana, kanji, furigana, long vowels, punctuation, mixed text and low-quality photographs.
5. Only then update the public romaji-reader/ path on main. Existing public prototype is not validated.
