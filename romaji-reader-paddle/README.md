# Official PaddleOCR.js experiment

Separate development-only experiment; **not deployed or validated**. It does not change the public Romaji Reader.

Uses official `@paddleocr/paddleocr-js` (Apache-2.0) for on-device OCR, and Kuroshiro (MIT) for Japanese-to-romaji conversion. The first scan downloads OCR models; timing separates initialization from inference. The OCR result is visible immediately and conversion is a separate step to isolate performance.

Build: `npm install && npm run build`. Requires internet to fetch packages and model resources. Check Japanese language identifier and model download compatibility in an actual browser before deployment. No assertion of working iPhone support until tested. Hepburn macrons, furigana layout and speed are not yet validated.

Reference: https://www.paddleocr.ai/latest/en/version3.x/inference_deployment/cross_platform/browser.html
