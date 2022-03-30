let colors = [
    "#DEB887FF",
    "#7EB973FF",
    "#B95A5AFF",
    "#AB4FC0FF"
];

function getRandomNumber() {
    return Math.floor(Math.random() * colors.length)
}

setInterval('document.body.style.backgroundColor = colors[getRandomNumber()]', 1000);
