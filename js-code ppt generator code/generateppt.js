const pptxgen = require("pptxgenjs");

const pptx = new pptxgen();

// Presentation properties
pptx.author = "Saanvi Kulkarni";
pptx.title = "Agricultural Drone Presentation";
pptx.lang = "en-US";

// --------------------
// Slide 1: Title Slide
// --------------------
let slide1 = pptx.addSlide();

slide1.addText("Agricultural Drone", {
    x: 1,
    y: 1.5,
    w: 8,
    h: 0.8,
    fontSize: 24,
    bold: true,
    align: "center"
});

slide1.addText("Created by Saanvi Kulkarni", {
    x: 1,
    y: 2.5,
    w: 8,
    h: 0.5,
    fontSize: 16,
    align: "center"
});

// --------------------
// Slide 2: Content Slide
// --------------------
let slide2 = pptx.addSlide();

slide2.addText("Key Points", {
    x: 0.5,
    y: 0.5,
    w: 4,
    h: 0.5,
    fontSize: 20,
    bold: true
});

slide2.addText([
     { text: "Uses drones to monitor crop health and field conditions." },
    { text: "Captures aerial images for precision farming." },
    { text: "Detects pests, diseases, and irrigation issues early." },
    { text: "Reduces manual labor and increases efficiency." },
    { text: "Helps farmers improve crop yield and resource management." }
], {
    x: 0.8,
    y: 1.2,
    w: 8,
    h: 3,
    bullet: { indent: 18 },
    fontSize: 16
});

// Save presentation
pptx.writeFile({ fileName: "Project_Presentation.pptx" })
    .then(() => {
        console.log("Presentation created successfully!");
    });