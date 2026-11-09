// Baut WallShare-Investorenpraesentation.pptx aus content_full.json und art/slideNN.png
const fs = require("fs");
const pptxgen = require("pptxgenjs");
const SKILL = "/Users/bengerlach/.claude/skills/synced/d90fac65-63e9-445a-90c3-bd29bcc394d4_e4162e8e-2bd6-4b8d-9884-6e4b23bf72cc/pptx";
const { applyTheme } = require(SKILL + "/scripts/apply_theme.js");

const OUT = process.argv[2] || "WallShare-Investorenpraesentation.pptx";
const slides = JSON.parse(fs.readFileSync("content_full.json", "utf8"));

// Dunkles Theme: dk1 = Textfarbe (hell), lt1 = Hintergrund (dunkel), bewusst invertiert
const THEME = {
  name: "Quiet Voltage",
  headFontFace: "Arial",
  bodyFontFace: "Arial",
  colors: {
    dk1: "E9EEF9", lt1: "0A0F1E", dk2: "8FA0C6", lt2: "101830",
    accent1: "2DF2B6", accent2: "FFB347", accent3: "FF6B7A", accent4: "5B8CFF", accent5: "2A3A66", accent6: "5F6F96",
    hlink: "2DF2B6", folHlink: "8FA0C6",
  },
};

const pres = new pptxgen();
pres.layout = "LAYOUT_WIDE"; // 13.33 x 7.5 Zoll
pres.title = "WallShare: Investorenpräsentation (Entwurf)";
pres.author = "Gruppe Businessplan Wallbox-Sharing";
pres.subject = "Geschäftsmodell, Zielmarkt und SWOT/TOWS";
pres.theme = { headFontFace: "Arial", bodyFontFace: "Arial" };
const C = pres.SchemeColor;

const ph = (name, type, x, y, w, h, size, bold, color, extra = {}) => ({
  placeholder: { options: Object.assign({ name, type, x, y, w, h, fontFace: "Arial", fontSize: size, bold, color, margin: 0, valign: "top" }, extra), text: "" },
});

pres.defineSlideMaster({
  title: "ART",
  background: { color: C.background1 },
  objects: [
    ph("kicker", "body", 0.6, 0.72, 9.0, 0.3, 11, true, C.accent1, { charSpacing: 2 }),
    ph("title", "title", 0.6, 1.02, 12.13, 0.98, 28, true, C.text1),
    ph("sub", "body", 0.6, 2.0, 12.13, 0.4, 14, false, C.text2),
    ph("source", "body", 0.6, 6.93, 9.6, 0.42, 10, false, C.text2),
  ],
});
pres.defineSlideMaster({
  title: "TITELFOLIE",
  background: { color: C.background1 },
  objects: [
    ph("title", "title", 0.6, 1.0, 6.6, 1.2, 62, true, C.text1),
    ph("sub", "body", 0.6, 2.25, 6.2, 1.0, 24, false, C.text1),
    ph("meta", "body", 0.6, 3.25, 6.4, 0.35, 13, true, C.accent1),
    ph("source", "body", 0.6, 6.93, 9.6, 0.42, 10, false, C.text2),
  ],
});

let lastSection = null;
for (const s of slides) {
  if (s.section !== lastSection) { pres.addSection({ title: s.section }); lastSection = s.section; }
  const slide = pres.addSlide({ masterName: s.n === 1 ? "TITELFOLIE" : "ART", sectionTitle: s.section });
  const n2 = String(s.n).padStart(2, "0");
  slide.addImage({ path: `art/slide${n2}.png`, x: 0, y: 0, w: 13.333, h: 7.5, altText: s.alt, objectName: `Grafik ${n2}` });
  const byRole = {};
  for (const b of s.boxes) byRole[b.role] = b.text;
  if (s.n !== 1) slide.addText(byRole.kicker, { placeholder: "kicker", objectName: `Kicker ${n2}` });
  slide.addText(byRole.title, { placeholder: "title", objectName: `Titel ${n2}` });
  slide.addText(byRole.sub, { placeholder: "sub", objectName: `Untertitel ${n2}` });
  if (s.n === 1) slide.addText(byRole.meta, { placeholder: "meta", objectName: "Meta 01" });
  slide.addText(byRole.source, { placeholder: "source", objectName: `Quelle ${n2}` });
  slide.addNotes(s.notes);
}

(async () => {
  await pres.writeFile({ fileName: OUT });
  await applyTheme(OUT, THEME);
  console.log("geschrieben:", OUT);
})();
