# OCR rebuild — source only, not deployed

This is a work-in-progress migration of Yomikomi's browser PaddleOCR approach to a standalone Vite app. No OCR models have yet been copied into this repository. This is **not runnable as deployed** until dependencies are installed, OCR assets are placed under public/ocr, and a production build is made and tested. The OCR API invocation and model compatibility remain unverified.

## Required assets
Yomikomi currently uses public/ocr/ppocr_v5_mobile_det.onnx, ppocr_v5_mobile_rec.onnx, doc_cls.onnx, and ppocrv5_dict.txt. Model redistribution licenses must be verified before copying.

## Attribution
Yomikomi: https://github.com/sieugene/yomikomi (MIT, retain its original LICENSE). OCR package: @oovz/esearch-ocr, plus onnxruntime-web; check their licenses and model licenses independently.

## Release gate
No main-branch or public-site change until build, model licensing, iPhone cold/warm speed, and ruby/romaji output are verified. No paid services.
