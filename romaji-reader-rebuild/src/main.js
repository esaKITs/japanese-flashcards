// Adapted from Yomikomi's client OCR initialization approach (MIT).
// https://github.com/sieugene/yomikomi/blob/main/src/features/ocr-client/hooks/useOCRLoader.ts
// https://github.com/sieugene/yomikomi/blob/main/src/features/ocr-client/constants/ocr.engines.ts
import * as ocr from '@oovz/esearch-ocr';
import * as ort from 'onnxruntime-web';
import './style.css';
ort.env.wasm.numThreads = 1;
ort.env.webgpu.powerPreference = 'low-power';
const base = import.meta.env.BASE_URL;
let instance;
const status = document.getElementById('status');
const output = document.getElementById('output');
async function load() {
  if (instance) return instance;
  status.textContent = 'Loading OCR model…';
  const dict = await fetch(base + 'ocr/ppocrv5_dict.txt').then(r => {if(!r.ok)throw Error('Dictionary unavailable');return r.text()});
  instance = await ocr.init({
    ort,
    det: {input: base + 'ocr/ppocr_v5_mobile_det.onnx'},
    rec: {input: base + 'ocr/ppocr_v5_mobile_rec.onnx', decodeDic: dict, optimize:{space:false}},
    docCls: {input: base + 'ocr/doc_cls.onnx'}
  });
  return instance;
}
document.getElementById('go').onclick = async () => {
  const file = document.getElementById('photo').files[0];
  if(!file){status.textContent='Choose a photo first.';return;}
  const start = performance.now();
  try {
    const engine = await load();
    status.textContent = 'Recognizing…';
    // The OCR library accepts ImageData; this path is intentionally explicit.
    const bitmap = await createImageBitmap(file);
    const scale = Math.min(1, 1600 / Math.max(bitmap.width,bitmap.height));
    const canvas = document.createElement('canvas');
    canvas.width = Math.round(bitmap.width*scale);canvas.height=Math.round(bitmap.height*scale);
    const ctx = canvas.getContext('2d',{willReadFrequently:true});
    ctx.drawImage(bitmap,0,0,canvas.width,canvas.height);
    bitmap.close();
    const data = ctx.getImageData(0,0,canvas.width,canvas.height);
    const result = await engine.ocr(data);
    output.textContent = JSON.stringify(result,null,2);
    status.textContent = 'OCR completed in '+((performance.now()-start)/1000).toFixed(1)+' s (including model load).';
  } catch(e) {status.textContent = 'OCR error: '+String(e?.message||e);}
};