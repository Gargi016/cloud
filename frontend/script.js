const slider = document.getElementById("slider");
const img = document.getElementById("img");
const label = document.getElementById("label");
const graph = document.getElementById("graph");

const BACKEND = "http://127.0.0.1:5000";

slider.oninput = () => {
  img.src = `${BACKEND}/api/image/${slider.value}`;
  label.innerText = `T${slider.value}`;
};

fetch(`${BACKEND}/api/graph`)
  .then(res => res.json())
  .then(data => {
    graph.innerText = JSON.stringify(data, null, 2);
  });
