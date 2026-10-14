# License review — BLOCKED (2026-10-14)

Inspection of the GitHub repository metadata for https://github.com/sieugene/yomikomi returned `license: null`. The conventional root `LICENSE` path returned 404. This does **not** establish permission to copy Yomikomi source or model weights. Earlier assumptions that the entire project was MIT-licensed were not verified and must not be relied upon.

The current experimental `src/main.js` was independently written using public API usage patterns and does not contain a verbatim copy of the Yomikomi implementation. Do not copy model binaries or code from Yomikomi until the copyright holders' permissions and third-party model licenses are verified.

Identified runtime dependency: `@oovz/esearch-ocr@8.4.4`, `onnxruntime-web@1.19.2`. Identified upstream model names: `ppocr_v5_mobile_det.onnx`, `ppocr_v5_mobile_rec.onnx`, `doc_cls.onnx`, and `ppocrv5_dict.txt`. These are NOT yet incorporated.

Next steps: verify upstream license through authoritative repository/package documentation, select appropriately licensed model artifacts from their original distributors, inspect API compatibility, build/test offline before public deployment.
