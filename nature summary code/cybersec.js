/**
 * nature_abstract.js
 * -------------------
 * Generates a .docx file formatted in Nature journal's
 * "summary paragraph" abstract style.
 *
 * Usage:
 *   node nature_abstract.js
 *   node nature_abstract.js --title "Your Title" --output my_abstract.docx
 *
 * Dependencies:
 *   npm install docx
 */

const {
  Document,
  Packer,
  Paragraph,
  TextRun,
  AlignmentType,
  BorderStyle,
} = require("docx");
const fs = require("fs");
const path = require("path");

// ── CLI argument parsing ──────────────────────────────────────────────────────
const args = process.argv.slice(2);
const getArg = (flag, fallback) => {
  const i = args.indexOf(flag);
  return i !== -1 && args[i + 1] ? args[i + 1] : fallback;
};

const TITLE  = getArg("--title",  "CYBERSECURITY");
const OUTPUT = getArg("--output", "nature_abstract.docx");

// ── Abstract text (edit these five sentences to match your work) ──────────────
//
// Nature summary paragraphs follow a strict five-sentence arc:
//   [1] BROAD CONTEXT  – one sentence placing the work in its field
//   [2] SPECIFIC GAP   – one sentence on what is unknown / unsolved
//   [3] APPROACH       – one sentence on what you did / how
//   [4] KEY RESULT     – one sentence on your main finding
//   [5] SIGNIFICANCE   – one sentence on what this means / broader impact
//
// Replace the placeholder text below with your own content.
// ─────────────────────────────────────────────────────────────────────────────
const BROAD_CONTEXT =
  "Cybersecurity has become a fundamental requirement in modern society as digital technologies increasingly influence communication, commerce, healthcare, education, transportation, and government operations. The widespread adoption of internet-connected devices and cloud-based services has created unprecedented opportunities for innovation and economic growth, but it has also expanded the potential attack surface for cybercriminals and malicious actors. As a result, organizations and individuals face growing threats from cyberattacks, including malware infections, ransomware campaigns, phishing schemes, data breaches, and denial-of-service attacks.";

const SPECIFIC_GAP ="The consequences of cybersecurity failures extend beyond financial losses and can affect national security, public safety, and personal privacy. Critical infrastructure systems such as power grids, transportation networks, healthcare facilities, and banking services are increasingly dependent on digital technologies, making them attractive targets for cyber threats. Protecting these systems requires a comprehensive approach that combines technological solutions, organizational policies, and user awareness. Common security measures include encryption, multi-factor authentication, firewalls, intrusion detection systems, vulnerability assessments, and regular software updates.";


const APPROACH =
  "Recent advancements in artificial intelligence, machine learning, and automation have transformed the cybersecurity landscape. These technologies enable faster threat detection and response but can also be exploited by attackers to develop more sophisticated attack methods. Consequently, cybersecurity has become a continuous process rather than a one-time implementation. Effective defence strategies must adapt to emerging threats, evolving technologies, and changing user behaviours.";

const KEY_RESULT =
  "As digital transformation accelerates worldwide, cybersecurity plays a crucial role in maintaining trust, ensuring data confidentiality, preserving system integrity, and guaranteeing service availability. Continued investment in cybersecurity research, workforce development, and international collaboration will be essential for addressing future challenges and building resilient digital ecosystems capable of supporting the needs of an increasingly connected world.";

const SIGNIFICANCE =
  "Cybersecurity is of great significance in the modern world because it protects sensitive information, digital assets, and critical systems from cyber threats and unauthorized access. As individuals and organizations increasingly depend on digital technologies for communication, banking, healthcare, education, business operations, and government services, the need for strong cybersecurity measures has become more important than ever. Effective cybersecurity helps prevent financial losses, data breaches, identity theft, and disruptions to essential services. It also safeguards the privacy of users and ensures the secure exchange of information across networks. In addition, cybersecurity plays a vital role in protecting critical infrastructure such as power grids, transportation systems, healthcare facilities, and financial institutions, whose failure could have serious economic and social consequences. With the rapid growth of technologies such as cloud computing, artificial intelligence, and the Internet of Things (IoT), the cybersecurity landscape continues to evolve, requiring continuous improvement in security practices and technologies. By maintaining the confidentiality, integrity, and availability of information, cybersecurity promotes trust in digital systems, supports business continuity, enhances national security, and contributes to the development of a safe and resilient digital society. Therefore, cybersecurity is not only a technical necessity but also a fundamental requirement for the secure functioning of modern life and future technological advancement.";

// Combine into one flowing paragraph (Nature style: no line breaks inside the abstract)
const ABSTRACT_TEXT = [
  BROAD_CONTEXT,
  SPECIFIC_GAP,
  APPROACH,
  KEY_RESULT,
  SIGNIFICANCE,
].join("  ");

// ── Document construction ─────────────────────────────────────────────────────
const doc = new Document({
  // ── Global styles ──
  styles: {
    default: {
      document: {
        run: { font: "Times New Roman", size: 24 }, // 12 pt body
      },
    },
    paragraphStyles: [
      {
        id: "NatureTitle",
        name: "Nature Title",
        basedOn: "Normal",
        run: { font: "Arial", size: 32, bold: true, color: "000000" },
        paragraph: { spacing: { before: 0, after: 240 } },
      },
      {
        id: "SectionLabel",
        name: "Section Label",
        basedOn: "Normal",
        run: {
          font: "Arial",
          size: 22,
          bold: true,
          color: "444444",
          allCaps: true,
        },
        paragraph: { spacing: { before: 360, after: 120 } },
      },
      {
        id: "AbstractBody",
        name: "Abstract Body",
        basedOn: "Normal",
        run: { font: "Times New Roman", size: 24, color: "000000" },
        paragraph: {
          alignment: AlignmentType.JUSTIFIED,
          spacing: { line: 276, before: 0, after: 0 }, // ~1.15× line spacing
        },
      },
    ],
  },

  // ── Page layout ──
  sections: [
    {
      properties: {
        page: {
          size: { width: 12240, height: 15840 }, // US Letter
          margin: { top: 1440, right: 1440, bottom: 1440, left: 1440 }, // 1 in
        },
      },
      children: [
        // ── Article title ──────────────────────────────────────────────────
        new Paragraph({
          style: "NatureTitle",
          children: [new TextRun(TITLE)],
        }),

        // ── Thin rule below title ──────────────────────────────────────────
        new Paragraph({
          border: {
            bottom: { style: BorderStyle.SINGLE, size: 6, color: "AAAAAA", space: 1 },
          },
          children: [],
        }),

        // ── "Abstract" label ───────────────────────────────────────────────
        new Paragraph({
          style: "SectionLabel",
          children: [new TextRun("Abstract")],
        }),

        // ── Abstract body (five-sentence Nature summary paragraph) ─────────
        new Paragraph({
          style: "AbstractBody",
          children: [
            // Sentence 1 – broad context
            new TextRun({
              text: BROAD_CONTEXT + "  ",
            }),
            // Sentence 2 – specific gap
            new TextRun({
              text: SPECIFIC_GAP + "  ",
            }),
            // Sentence 3 – approach (bold lead-in is a Nature convention)
            new TextRun({
              text: "Here we show",
              bold: true,
            }),
            new TextRun({
              text:
                APPROACH.replace(/^Here we show/, "").replace(/^\,\s*/, ", ") +
                "  ",
            }),
            // Sentence 4 – key result
            new TextRun({
              text: KEY_RESULT + "  ",
            }),
            // Sentence 5 – significance
            new TextRun({
              text: SIGNIFICANCE,
            }),
          ],
        }),

        // ── Sentence-by-sentence annotation (for editing / review) ─────────
        new Paragraph({
          style: "SectionLabel",
          spacing: { before: 480 },
          children: [new TextRun("Sentence-by-sentence breakdown")],
        }),

        // Helper: render an annotated row
        ...buildAnnotationRows([
          { role: "1 · Broad context",  text: BROAD_CONTEXT },
          { role: "2 · Specific gap",   text: SPECIFIC_GAP  },
          { role: "3 · Approach",       text: APPROACH      },
          { role: "4 · Key result",     text: KEY_RESULT    },
          { role: "5 · Significance",   text: SIGNIFICANCE  },
        ]),

        // ── Notes for the author ───────────────────────────────────────────
        new Paragraph({
          style: "SectionLabel",
          spacing: { before: 480 },
          children: [new TextRun("Formatting notes (delete before submission)")],
        }),
        ...buildNoteRows([
          "Nature summary paragraphs are a single, unbroken paragraph of ≤200 words.",
          "Do NOT use subheadings, bullet points, or abbreviations inside the abstract.",
          'The lead-in \u201cHere we show\u201d (or \u201cHere, using X, we show\u201d) is a Nature house style.',
          "Font: Times New Roman 12 pt, justified, ~1.15× line spacing.",
          "Remove this section and the breakdown table before submission.",
        ]),
      ],
    },
  ],
});

// ── Helper functions ──────────────────────────────────────────────────────────
function buildAnnotationRows(rows) {
  return rows.flatMap(({ role, text }) => [
    new Paragraph({
      spacing: { before: 180, after: 60 },
      children: [
        new TextRun({ text: role, bold: true, font: "Arial", size: 22, color: "1F5C99" }),
      ],
    }),
    new Paragraph({
      alignment: AlignmentType.JUSTIFIED,
      spacing: { before: 0, after: 120 },
      indent: { left: 360 },
      children: [new TextRun({ text, font: "Times New Roman", size: 22, italics: true })],
    }),
  ]);
}

function buildNoteRows(notes) {
  return notes.map(
    (note) =>
      new Paragraph({
        spacing: { before: 60, after: 60 },
        indent: { left: 360 },
        children: [
          new TextRun({ text: "• ", font: "Arial", size: 22, color: "888888" }),
          new TextRun({ text: note, font: "Arial", size: 22, color: "555555" }),
        ],
      })
  );
}

// ── Write to disk ─────────────────────────────────────────────────────────────
Packer.toBuffer(doc).then((buffer) => {
  const outPath = path.resolve(OUTPUT);
  fs.writeFileSync(outPath, buffer);
  console.log(`✅  Written → ${outPath}`);
});
